import React, { useState, useEffect } from 'react';
import { FaUsers, FaSearch, FaFilter, FaPlus, FaEdit, FaTrash, FaUser } from 'react-icons/fa';
import NewUserModal from './NewUserModal';
import EditUserModal from './EditUserModal';
import { userApi } from '../../../api/api';
import type { User } from '../../../types/user'
import './UserManagement.css';
import type { MajorLecturerList, } from '../../../types/lecturer'
import mockData from './mockdata.json'

const UserManagement: React.FC = () => {
  const [loadingMockData] = useState<MajorLecturerList>(mockData);
  const [users, setUsers] = useState<User[]>([]);
  const [filteredUsers, setFilteredUsers] = useState<User[]>([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedMajor, setSelectedMajor] = useState<string>('all');
  const [isLoading, setIsLoading] = useState(true);
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [editingUser, setEditingUser] = useState<User | null>(null);
  const [pagination, setPagination] = useState({
    page: 1,
    limit: 10,
    totalItems: 0,
    totalPages: 1
  });
  const passwordDefault = "111111"

      const fetchUsers = async () => {
      setIsLoading(true);
      try {
        const response = await userApi.getUsers(pagination.page, pagination.limit);
        const data = response.data;
        
        setUsers(data.items);
        setFilteredUsers(data.items);
        setPagination(prev => ({
          ...prev,
          totalItems: data.meta.totalItems,
          totalPages: data.meta.totalPages
        }));
      } catch (error) {
        console.error('Error fetching users:', error);
        // Xử lý lỗi (hiển thị thông báo, v.v.)
      } finally {
        setIsLoading(false);
      }
    };
  // Fetch users from API
  useEffect(() => {
    fetchUsers();
  }, [pagination.page, pagination.limit]);

  // Filter users (giữ nguyên)
  useEffect(() => {
    let result = users;
    
    if (searchTerm) {
      result = result.filter(user => 
        user.userName.toLowerCase().includes(searchTerm.toLowerCase()) ||
        user.email.toLowerCase().includes(searchTerm.toLowerCase())
      );
    }
    
    if (selectedMajor !== 'all' && selectedMajor !== 'null') {
      result = result.filter(user => user.major === selectedMajor);
    } else if (selectedMajor === 'null') {
      result = result.filter(user => user.major === null);
    }
    
    setFilteredUsers(result);
  }, [searchTerm, selectedMajor, users]);

async function urlToFile(proxyUrl: string, filename?: string): Promise<File> {
  const response = await fetch(proxyUrl);
  if (!response.ok) throw new Error("Proxy fetch failed");

  const blob = await response.blob();
  const name = filename || "image.jpg";
  return new File([blob], name, { type: blob.type });
}
function proxyUrl(url: string): string {
  const proxyUrl = `http://localhost:3001/proxy-image?url=${encodeURIComponent(url)}`;
  return proxyUrl;
}
function encodeEmail(email: string): string {
  return encodeURIComponent(email);
}

const createListUser = async (data: MajorLecturerList) => {
  try {
    // Process all majors and lecturers sequentially
    
    for (const majorData of data.majorLecturers) {
      for (const lecturer of majorData.lecturers) {
        try {
          // 1. Prepare profile data
          const profileData = new FormData();
          profileData.append('userName', lecturer.name);
          profileData.append('major', majorData.majorName);
          profileData.append('position', lecturer.position);
          profileData.append('office', lecturer.office);
          
          // Convert avatar if URL exists
          if (lecturer.imageUrl) {
            try {
              const avatarFile = await urlToFile(proxyUrl(lecturer.imageUrl));
              profileData.append('avatar', avatarFile);
            } catch (error) {
              console.error(`Failed to convert avatar for ${lecturer.email}:`, error);
            }
          }

          let userId: number;
          
          // 2. Try to create user first
          try {
            const registration = await userApi.createUser({
              email: lecturer.email,
              password: passwordDefault,
              userName: lecturer.name
            });
            
            if (!registration.data?.id) {
              throw new Error(`No user ID returned for ${lecturer.email}`);
            }
            
            userId = registration.data.id;
            console.log(`Created new user ${lecturer.email}`);
          } catch (createError: any) {
            // 3. If user already exists, find and update
            if (createError.response?.data?.message === "Email already exists") {
              console.log(`User ${lecturer.email} exists, finding user to update...`);
              
              try {
                // Try to get user by email
                const response = await userApi.getUserbyEmail(encodeEmail(lecturer.email));
                if (!response?.data.id) {
                  throw new Error(`User ${lecturer.email} not found`);
                }
                
                userId = response.data.id;
                console.log(`Found existing user ${lecturer.email}, ID: ${userId}`);
              } catch (findError) {
                console.error(`Error finding user ${lecturer.email}:`, findError);
                continue; // Skip to next lecturer if we can't find the user
              }
            } else {
              console.error(`Error creating user ${lecturer.email}:`, createError);
              continue; // Skip to next lecturer for other errors
            }
          }

          // 4. Update user profile (for both new and existing users)
          try {
            await userApi.updateUser(userId, profileData);
            console.log(`Successfully updated profile for ${lecturer.email}`);
          } catch (updateError) {
            console.error(`Error updating profile for ${lecturer.email}:`, updateError);
          }
          
          // Small delay to avoid rate limiting
          await new Promise(resolve => setTimeout(resolve, 500));
          
        } catch (error) {
          console.error(`Error processing lecturer ${lecturer.email}:`, error);
        }
      }
    }
    
    // Refresh the user list after all operations
    await fetchUsers();
    alert('Batch user processing completed!');
    
  } catch (error) {
    console.error('Error in createListUser:', error);
    alert('An error occurred during batch user processing');
  }
};

  const handleCreateUser = async () => {
    try {
      fetchUsers();
      setShowCreateModal(false);
    } catch (error) {
      console.error('Error creating user:', error);
    }
  };

  const handleUpdateUser = async () => {
    fetchUsers();
  };

  const handleDeleteUser = async (userId: number) => {
    if (window.confirm('Are you sure you want to delete this user?')) {
      try {
        await userApi.deleteUser(userId);
        setUsers(prev => prev.filter(user => user.id !== userId));
      } catch (error) {
        console.error('Error deleting user:', error);
      }
    }
  };

  const handlePageChange = (newPage: number) => {
    setPagination(prev => ({ ...prev, page: newPage }));
  };

  // Get unique majors (giữ nguyên)
  const uniqueMajors = [
    'all',
    ...Array.from(new Set(users.map(user => user.major).filter(Boolean))) as string[],
    'null'
  ];

  return (
    <div className="user-management-container">
      <div className="user-management-header">
        <h1 className="user-management-title"><FaUsers /> User Management</h1>
        <div className="user-management-controls">
          <div className="search-filter-container">
            <div className="user-search-box">
              <FaSearch className="search-icon" />
              <input
                type="text"
                placeholder="Search users..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </div>
            <div className="user-filter-dropdown">
              <FaFilter className="filter-icon" />
              <select
                value={selectedMajor}
                onChange={(e) => setSelectedMajor(e.target.value)}
              >
                {uniqueMajors.map(major => (
                  <option key={major} value={major}>
                    {major === 'all' ? 'All Majors' : 
                     major === 'null' ? 'No Major' : major}
                  </option>
                ))}
              </select>
            </div>
          </div>
          <button 
            className="user-add-button"
            onClick={() => setShowCreateModal(true)}
          >
            <FaPlus /> Create User
          </button>
          <button 
            className="user-add-button"
            onClick={() => createListUser(loadingMockData)}
          >
            <FaPlus /> Create List User
          </button>
        </div>
      </div>

      {isLoading ? (
        <div className="user-loading-state">
          <div className="user-loading-spinner">
            <FaUsers />
          </div>
          Loading users...
        </div>
      ) : (
        <>
          <div className="user-table-container">
            <table className="user-table">
              <thead>
                <tr>
                  <th>Avatar</th>
                  <th>Username</th>
                  <th>Email</th>
                  <th>Major</th>
                  <th>Position</th>
                  <th>Office</th>
                  <th>Role</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {filteredUsers.length > 0 ? (
                  filteredUsers.map(user => (
                    <tr key={user.id}>
                      <td className='user-box'>
                        <div className="user-avatar">
                          {user.avatar ? (
                            <img src={user.avatar} alt="User Avatar" className='img-avatar'/>
                          ) : (
                            <div className="user-avatar-placeholder">
                              <FaUser />
                            </div>
                          )}
                        </div>
                      </td>
                      <td>{user.userName}</td>
                      <td>{user.email}</td>
                      <td>{user.major || '-'}</td>
                      <td>{user.position || '-'}</td>
                      <td>{user.office || '-'}</td>
                      <td>
                        <span className={`user-status-badge ${
                          user.role.name === 'admin' ? 'badge-admin' : 'badge-user'
                        }`}>
                          {user.role.name}
                        </span>
                      </td>
                      <td>
                        <div className="user-actions-container">
                          <button 
                            className="user-action-btn user-edit-btn"
                            onClick={() => setEditingUser(user)}
                          >
                            <FaEdit />
                          </button>
                          <button 
                            className="user-action-btn user-delete-btn"
                            onClick={() => handleDeleteUser(user.id)}
                          >
                            <FaTrash />
                          </button>
                        </div>                      
                      </td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan={8} className="user-empty-state">
                      <div className="user-empty-icon">
                        <FaUsers />
                      </div>
                      No users found matching your criteria
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>

          {/* Pagination controls */}
          {pagination.totalPages > 1 && (
            <div className="user-pagination">
              <button
                disabled={pagination.page === 1}
                onClick={() => handlePageChange(pagination.page - 1)}
              >
                Previous
              </button>
              
              {Array.from({ length: pagination.totalPages }, (_, i) => i + 1).map(page => (
                <button
                  key={page}
                  className={pagination.page === page ? 'active' : ''}
                  onClick={() => handlePageChange(page)}
                >
                  {page}
                </button>
              ))}
              
              <button
                disabled={pagination.page === pagination.totalPages}
                onClick={() => handlePageChange(pagination.page + 1)}
              >
                Next
              </button>
            </div>
          )}
        </>
      )}

      {/* Modals */}
      {showCreateModal && (
        <NewUserModal
          onClose={() => setShowCreateModal(false)}
          onCreate={handleCreateUser}
        />
      )}

      {editingUser && (
        <EditUserModal
          user={editingUser}
          onClose={() => setEditingUser(null)}
          onSave={handleUpdateUser}
        />
      )}
    </div>
  );
};

export default UserManagement;