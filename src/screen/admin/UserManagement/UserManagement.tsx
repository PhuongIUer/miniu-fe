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
  const [allUsers, setAllUsers] = useState<User[]>([]); // Stores all 500 users
  const [displayedUsers, setDisplayedUsers] = useState<User[]>([]); // Users to display on current page
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

  const fetchAllUsers = async () => {
    setIsLoading(true);
    try {
      // Fetch 500 users at once
      const response = await userApi.getUsers(1, 500);
      const data = response.data;
      
      setAllUsers(data.items);
      setDisplayedUsers(data.items.slice(0, pagination.limit)); // Show first 10 initially
      setPagination(prev => ({
        ...prev,
        totalItems: data.items.length, // Use the actual count of fetched users
        totalPages: Math.ceil(data.items.length / prev.limit)
      }));
    } catch (error) {
      console.error('Error fetching users:', error);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchAllUsers();
  }, []);

  // Filter users and update pagination
  useEffect(() => {
    let result = allUsers;
    
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
    
    // Update pagination
    const totalPages = Math.ceil(result.length / pagination.limit);
    setPagination(prev => ({
      ...prev,
      totalItems: result.length,
      totalPages: totalPages
    }));
    
    // Update displayed users
    const startIndex = (pagination.page - 1) * pagination.limit;
    const endIndex = startIndex + pagination.limit;
    setDisplayedUsers(result.slice(startIndex, endIndex));
  }, [searchTerm, selectedMajor, allUsers, pagination.page, pagination.limit]);


async function urlToFile(proxyUrl: string, filename?: string): Promise<File> {
  const response = await fetch(proxyUrl);
  if (!response.ok) throw new Error("Proxy fetch failed");

  const blob = await response.blob();
  const name = filename || "image.jpg";
  return new File([blob], name, { type: blob.type });
}
function proxyUrl(url: string): string {
  const proxyUrl = `https://localhost:3001/proxy-image?url=${encodeURIComponent(url)}`;
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
    await fetchAllUsers();
    alert('Batch user processing completed!');
    
  } catch (error) {
    console.error('Error in createListUser:', error);
    alert('An error occurred during batch user processing');
  }
};
  const changeMajor = async (major: string) => {
    setSelectedMajor(major);
    setPagination(prev => ({ ...prev, page: 1 })); 
  };
  const handleCreateUser = async () => {
    try {
      fetchAllUsers();
      setShowCreateModal(false);
    } catch (error) {
      console.error('Error creating user:', error);
    }
  };

  const handleUpdateUser = async () => {
    fetchAllUsers();
  };

  const handleDeleteUser = async (userId: number) => {
    if (window.confirm('Are you sure you want to delete this user?')) {
      try {
        await userApi.deleteUser(userId);
      } catch (error) {
        console.error('Error deleting user:', error);
      } finally {
        fetchAllUsers();
      }
    }
  };

  const handlePageChange = (newPage: number) => {
    setPagination(prev => ({ ...prev, page: newPage }));
  };

  // Get unique majors (giữ nguyên)
  const uniqueMajors = [
    'all',
    ...Array.from(new Set(allUsers.map(user => user.major).filter(Boolean))) as string[],
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
                onChange={(e) => changeMajor(e.target.value)}
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
                {displayedUsers.length > 0 ? (
                  displayedUsers.map(user => (
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


    {/* Improved Pagination controls */}
          {pagination.totalPages > 1 && (
            <div className="user-pagination">
              <button
                className={`pagination-button ${pagination.page === 1 ? 'disabled' : ''}`}
                disabled={pagination.page === 1}
                onClick={() => handlePageChange(pagination.page - 1)}
              >
                &laquo; Previous
              </button>
              
              {Array.from({ length: Math.min(5, pagination.totalPages) }, (_, i) => {
                // Show only 5 page buttons at a time
                let pageNum;
                if (pagination.totalPages <= 5) {
                  pageNum = i + 1;
                } else if (pagination.page <= 3) {
                  pageNum = i + 1;
                } else if (pagination.page >= pagination.totalPages - 2) {
                  pageNum = pagination.totalPages - 4 + i;
                } else {
                  pageNum = pagination.page - 2 + i;
                }
                
                return (
                  <button
                    key={pageNum}
                    className={`pagination-button ${pagination.page === pageNum ? 'active' : ''}`}
                    onClick={() => handlePageChange(pageNum)}
                  >
                    {pageNum}
                  </button>
                );
              })}
              
              <button
                className={`pagination-button ${pagination.page === pagination.totalPages ? 'disabled' : ''}`}
                disabled={pagination.page === pagination.totalPages}
                onClick={() => handlePageChange(pagination.page + 1)}
              >
                Next &raquo;
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