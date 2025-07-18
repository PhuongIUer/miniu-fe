import React, { useState, useEffect } from 'react';
import { FaEdit, FaTrash, FaPlus, FaChevronDown, FaChevronRight, FaSave, FaBook } from 'react-icons/fa';
import './CurriculumManagement.css';
import type { Major, Curriculum } from '../../../types/curriculum';
import { curriApi } from '../../../api/api';
import mockData from './mockdata.json'

const CurriculumManagement: React.FC = () => {
  const [currentCurriculum, setCurrentCurriculum] = useState<Curriculum | null>(null);
  const [mockCurriculum] = useState<Curriculum | null>(mockData);
  const [draftCurriculum, setDraftCurriculum] = useState<Major[]>([]);
  const [expanded, setExpanded] = useState<Record<string, boolean>>({});
  const [editingItem, setEditingItem] = useState<{
    type: 'major' | 'concentration' | 'semester' | 'subject';
    majorIndex: number;
    concentrationIndex?: number;
    semesterIndex?: number;
    subjectIndex?: number;
  } | null>(null);
  const [editForm, setEditForm] = useState({ name: '', credits: 0 });
  const [isLoading, setIsLoading] = useState(true);

  const loadLatestCurriculum = async () => {
    try {
      const response = await curriApi.getLastedCurri();
      setCurrentCurriculum(response.data);
      setDraftCurriculum(response.data.majors || []);
    } catch (error) {
      console.error('Failed to load curriculum:', error);
      // Initialize with empty curriculum if API fails
      setDraftCurriculum([]);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    loadLatestCurriculum();
  }, []);

  const toggleExpand = (key: string) => {
    setExpanded(prev => ({ ...prev, [key]: !prev[key] }));
  };

  const handleEdit = (
    type: 'major' | 'concentration' | 'semester' | 'subject',
    majorIndex: number,
    concentrationIndex?: number,
    semesterIndex?: number,
    subjectIndex?: number
  ) => {
    let item;
    if (type === 'major') {
      item = { name: draftCurriculum[majorIndex].name };
    } else if (type === 'concentration' && concentrationIndex !== undefined) {
      item = { name: draftCurriculum[majorIndex].concentrations[concentrationIndex].name };
    } else if (type === 'semester' && concentrationIndex !== undefined && semesterIndex !== undefined) {
      item = { name: draftCurriculum[majorIndex].concentrations[concentrationIndex].semesters[semesterIndex].name };
    } else if (type === 'subject' && concentrationIndex !== undefined && semesterIndex !== undefined && subjectIndex !== undefined) {
      item = draftCurriculum[majorIndex].concentrations[concentrationIndex].semesters[semesterIndex].subjects[subjectIndex];
    }

    setEditingItem({ type, majorIndex, concentrationIndex, semesterIndex, subjectIndex });
    setEditForm(item && 'credits' in item ? item : { name: item?.name || '', credits: 0 });
  };

  const handleSaveEdit = () => {
    if (!editingItem) return;

    setDraftCurriculum(prev => {
      const newCurriculum = [...prev];
      const { type, majorIndex, concentrationIndex, semesterIndex, subjectIndex } = editingItem;

      if (type === 'major') {
        newCurriculum[majorIndex] = { ...newCurriculum[majorIndex], name: editForm.name };
      } else if (type === 'concentration' && concentrationIndex !== undefined) {
        newCurriculum[majorIndex].concentrations[concentrationIndex] = {
          ...newCurriculum[majorIndex].concentrations[concentrationIndex],
          name: editForm.name
        };
      } else if (type === 'semester' && concentrationIndex !== undefined && semesterIndex !== undefined) {
        newCurriculum[majorIndex].concentrations[concentrationIndex].semesters[semesterIndex] = {
          ...newCurriculum[majorIndex].concentrations[concentrationIndex].semesters[semesterIndex],
          name: editForm.name
        };
      } else if (type === 'subject' && concentrationIndex !== undefined && semesterIndex !== undefined && subjectIndex !== undefined) {
        newCurriculum[majorIndex].concentrations[concentrationIndex].semesters[semesterIndex].subjects[subjectIndex] = {
          name: editForm.name,
          credits: editForm.credits
        };
      }

      return newCurriculum;
    });

    setEditingItem(null);
  };

  const handleAdd = (
    type: 'major' | 'concentration' | 'semester' | 'subject',
    majorIndex?: number,
    concentrationIndex?: number,
    semesterIndex?: number
  ) => {
    const newItem = type === 'subject' ? { name: 'New Subject', credits: 0 } : { name: `New ${type.charAt(0).toUpperCase() + type.slice(1)}` };

    setDraftCurriculum(prev => {
      const newCurriculum = JSON.parse(JSON.stringify(prev));
      if (type === 'major') {
        newCurriculum.push({ name: newItem.name, concentrations: [] });
      } else if (type === 'concentration' && majorIndex !== undefined) {
        newCurriculum[majorIndex].concentrations.push({ name: newItem.name, semesters: [] });
        setExpanded(prev => ({ ...prev, [`major-${majorIndex}`]: true }));
      } else if (type === 'semester' && majorIndex !== undefined && concentrationIndex !== undefined) {
        setExpanded(prev => ({ ...prev, [`concentration-${majorIndex}-${concentrationIndex}`]: true }));
        newCurriculum[majorIndex].concentrations[concentrationIndex].semesters.push({ name: newItem.name, subjects: [] });
      } else if (type === 'subject' && majorIndex !== undefined && concentrationIndex !== undefined && semesterIndex !== undefined) {
        newCurriculum[majorIndex].concentrations[concentrationIndex].semesters[semesterIndex].subjects.push(newItem);
        setExpanded(prev => ({ ...prev, [`semester-${majorIndex}-${concentrationIndex}-${semesterIndex}`]: true }));
      }
      
      return newCurriculum;
    });
  };

  const handleDelete = (
    type: 'major' | 'concentration' | 'semester' | 'subject',
    majorIndex: number,
    concentrationIndex?: number,
    semesterIndex?: number,
    subjectIndex?: number
  ) => {
    if (!window.confirm(`Are you sure you want to delete this ${type}?`)) return;

    setDraftCurriculum(prev => {
      const newCurriculum = [...prev];
      
      if (type === 'major') {
        newCurriculum.splice(majorIndex, 1);
      } else if (type === 'concentration' && concentrationIndex !== undefined) {
        newCurriculum[majorIndex].concentrations.splice(concentrationIndex, 1);
      } else if (type === 'semester' && concentrationIndex !== undefined && semesterIndex !== undefined) {
        newCurriculum[majorIndex].concentrations[concentrationIndex].semesters.splice(semesterIndex, 1);
      } else if (type === 'subject' && concentrationIndex !== undefined && semesterIndex !== undefined && subjectIndex !== undefined) {
        newCurriculum[majorIndex].concentrations[concentrationIndex].semesters[semesterIndex].subjects.splice(subjectIndex, 1);
      }

      return newCurriculum;
    });
  };
  const loadingMockData = async () => {
    if(!window.confirm('Are you sure you want to update all data?\nThis will overwrite existing data. Please know what you are doing!'))
      return;
    try {
      setIsLoading(true);
      
      const mockCurriculumName = mockCurriculum?.name || `New Curriculum`;
      const { data: newCurriculum } = await curriApi.createCurri(mockCurriculumName);
      
      if (!mockCurriculum || !mockCurriculum.majors) {
        console.error('Mock curriculum data is not available or invalid');
        return;
      }
      for (const major of mockCurriculum.majors) {
        const { data: newMajor } = await curriApi.createMajor(major.name, newCurriculum.id);
        
        if (!major.concentrations) continue;
        for (const concentration of major.concentrations || []) {
          const { data: newConcentration } = await curriApi.createConcen(concentration.name, newMajor.id);
          
          if (!concentration.semesters) continue;
          for (const semester of concentration.semesters || []) {
            const { data: newSemester } = await curriApi.createSems(semester.name, newConcentration.id);
            
            if (!semester.subjects) continue;
            for (const subject of semester.subjects || []) {
              await curriApi.createSub(subject, newSemester.id);
            }
          }
        }
      }
      
      const { data: updatedCurriculum } = await curriApi.getLastedCurri();
      setCurrentCurriculum(updatedCurriculum);
      setDraftCurriculum(updatedCurriculum.majors || []);
      
      alert('Curriculum saved successfully!');
    } catch (error) {
      console.error('Failed to save curriculum:', error);
      alert('Failed to save curriculum. Please try again.');
    } finally {
      setIsLoading(false);
    }
  }
  const saveCurriculum = async () => {
    if(!window.confirm('Are you sure you want to update all data?\nThis will overwrite existing data. Please know what you are doing!'))
      return;
    try {
      setIsLoading(true);
      
      const curriculumName = currentCurriculum?.name || `New Curriculum ${new Date().toLocaleDateString()}`;
      const { data: newCurriculum } = await curriApi.createCurri(curriculumName);
      
      if (!currentCurriculum || !currentCurriculum.majors) {
        console.error('Mock curriculum data is not available or invalid');
        return;
      }
      for (const major of currentCurriculum.majors) {
        const { data: newMajor } = await curriApi.createMajor(major.name, newCurriculum.id);
        
        if (!major.concentrations) continue;
        for (const concentration of major.concentrations || []) {
          const { data: newConcentration } = await curriApi.createConcen(concentration.name, newMajor.id);
          
          if (!concentration.semesters) continue;
          for (const semester of concentration.semesters || []) {
            const { data: newSemester } = await curriApi.createSems(semester.name, newConcentration.id);
            
            if (!semester.subjects) continue;
            for (const subject of semester.subjects || []) {
              await curriApi.createSub(subject, newSemester.id);
            }
          }
        }
      }
      
      const { data: updatedCurriculum } = await curriApi.getLastedCurri();
      setCurrentCurriculum(updatedCurriculum);
      setDraftCurriculum(updatedCurriculum.majors || []);
      
      alert('Curriculum saved successfully!');
    } catch (error) {
      console.error('Failed to save curriculum:', error);
      alert('Failed to save curriculum. Please try again.');
    } finally {
      loadLatestCurriculum();
      setIsLoading(false);
    }
  };

  if (isLoading) {
    return <div className="loading">Loading curriculum...</div>;
  }

  return (
    <div className="curriculum-management">
      <div className="header">
        <h1 className='title'> <FaBook/> Curriculum Management</h1>
        <div className="actions-btn">
          <button className="add-btn" onClick={() => handleAdd('major')}>
            <FaPlus /> Add Major
          </button>
          <button className="save-btn" onClick={saveCurriculum} disabled={isLoading}>
            <FaSave /> {isLoading ? 'Saving...' : 'Save Curriculum'}
          </button>
                    <button className="save-btn" onClick={loadingMockData} disabled={isLoading}>
            <FaSave /> {isLoading ? 'Saving...' : 'Loading Data from Json'}
          </button>
        </div> 
      </div>

      {editingItem && (
        <div className="edit-modal">
          <div className="edit-form">
            <h3>Edit {editingItem.type}</h3>
            <div className="form-group">
              <label>Name:</label>
              <input
                type="text"
                value={editForm.name}
                onChange={(e) => setEditForm({ ...editForm, name: e.target.value })}
              />
            </div>
            {editingItem.type === 'subject' && (
              <div className="form-group">
                <label>Credits:</label>
                <input
                  type="number"
                  value={editForm.credits}
                  onChange={(e) => setEditForm({ ...editForm, credits: parseInt(e.target.value) || 0 })}
                />
              </div>
            )}
            <div className="form-actions">
              <button className="cancel-btn" onClick={() => setEditingItem(null)}>
                Cancel
              </button>
              <button className="save-btn" onClick={handleSaveEdit}>
                Save
              </button>
            </div>
          </div>
        </div>
      )}

      <div className="curriculum-list">
        {draftCurriculum.map((major, majorIndex) => (
          <div key={`major-${majorIndex}`} className="major-item">
            <div className="item-header">
              <button
                className="expand-btn"
                onClick={() => toggleExpand(`major-${majorIndex}`)}
              >
                {expanded[`major-${majorIndex}`] ? <FaChevronDown /> : <FaChevronRight />}
              </button>
              <span className="item-name">{major.name}</span>
              <div className="item-actions">
                <button className="edit-btn" onClick={() => handleEdit('major', majorIndex)}>
                  <FaEdit />
                </button>
                <button className="delete-btn" onClick={() => handleDelete('major', majorIndex)}>
                  <FaTrash />
                </button>
                <button className="add-btn" onClick={() => handleAdd('concentration', majorIndex)}>
                  <FaPlus />
                </button>
              </div>
            </div>

            {expanded[`major-${majorIndex}`] && major.concentrations?.length > 0 && (
              <div className="nested-list">
                {major.concentrations.map((concentration, concentrationIndex) => (
                  <div key={`concentration-${majorIndex}-${concentrationIndex}`} className="concentration-item">
                    <div className="item-header">
                      <button
                        className="expand-btn"
                        onClick={() => toggleExpand(`concentration-${majorIndex}-${concentrationIndex}`)}
                      >
                        {expanded[`concentration-${majorIndex}-${concentrationIndex}`] ? <FaChevronDown /> : <FaChevronRight />}
                      </button>
                      <span className="item-name">{concentration.name}</span>
                      <div className="item-actions">
                        <button className="edit-btn" onClick={() => handleEdit('concentration', majorIndex, concentrationIndex)}>
                          <FaEdit />
                        </button>
                        <button className="delete-btn" onClick={() => handleDelete('concentration', majorIndex, concentrationIndex)}>
                          <FaTrash />
                        </button>
                        <button className="add-btn" onClick={() => handleAdd('semester', majorIndex, concentrationIndex)}>
                          <FaPlus />
                        </button>
                      </div>
                    </div>

                    {expanded[`concentration-${majorIndex}-${concentrationIndex}`] && concentration.semesters?.length > 0 && (
                      <div className="nested-list">
                        {concentration.semesters.map((semester, semesterIndex) => (
                          <div key={`semester-${majorIndex}-${concentrationIndex}-${semesterIndex}`} className="semester-item">
                            <div className="item-header">
                              <button
                                className="expand-btn"
                                onClick={() => toggleExpand(`semester-${majorIndex}-${concentrationIndex}-${semesterIndex}`)}
                              >
                                {expanded[`semester-${majorIndex}-${concentrationIndex}-${semesterIndex}`] ? <FaChevronDown /> : <FaChevronRight />}
                              </button>
                              <span className="item-name">{semester.name}</span>
                              <div className="item-actions">
                                <button className="edit-btn" onClick={() => handleEdit('semester', majorIndex, concentrationIndex, semesterIndex)}>
                                  <FaEdit />
                                </button>
                                <button className="delete-btn" onClick={() => handleDelete('semester', majorIndex, concentrationIndex, semesterIndex)}>
                                  <FaTrash />
                                </button>
                                <button className="add-btn" onClick={() => handleAdd('subject', majorIndex, concentrationIndex, semesterIndex)}>
                                  <FaPlus />
                                </button>
                              </div>
                            </div>

                            {expanded[`semester-${majorIndex}-${concentrationIndex}-${semesterIndex}`] && semester.subjects?.length > 0 && (
                              <div className="nested-list">
                                {semester.subjects.map((subject, subjectIndex) => (
                                  <div key={`subject-${majorIndex}-${concentrationIndex}-${semesterIndex}-${subjectIndex}`} className="subject-item">
                                    <div className="item-header">
                                      <div className='item-subject'>
                                        <span className="subject-name">{subject.name} </span> 
                                        <span className="credits">({subject.credits} credits)</span>
                                      </div>                          
                                      <div className="item-actions">
                                        <button className="edit-btn" onClick={() => handleEdit('subject', majorIndex, concentrationIndex, semesterIndex, subjectIndex)}>
                                          <FaEdit />
                                        </button>
                                        <button className="delete-btn" onClick={() => handleDelete('subject', majorIndex, concentrationIndex, semesterIndex, subjectIndex)}>
                                          <FaTrash />
                                        </button>
                                      </div>
                                    </div>
                                  </div>
                                ))}
                              </div>
                            )}
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                ))}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default CurriculumManagement;