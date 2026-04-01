import React, { useState } from 'react';
import './Courses.css';

function Courses() {
  const [courses, setCourses] = useState([
    {
      id: 1,
      title: 'Web Development Basics',
      category: 'Web Development',
      level: 'Beginner',
      duration: '4 weeks',
      students: 1250,
      rating: 4.8,
      image: '🌐',
      description: 'Learn HTML, CSS, and JavaScript fundamentals.'
    },
    {
      id: 2,
      title: 'React Advanced',
      category: 'Web Development',
      level: 'Advanced',
      duration: '6 weeks',
      students: 890,
      rating: 4.9,
      image: '⚛️',
      description: 'Master React with hooks, context, and state management.'
    },
    {
      id: 3,
      title: 'Python for Data Science',
      category: 'Data Science',
      level: 'Intermediate',
      duration: '8 weeks',
      students: 2100,
      rating: 4.7,
      image: '🐍',
      description: 'Learn Python pandas, NumPy, and data visualization.'
    },
    {
      id: 4,
      title: 'Machine Learning 101',
      category: 'AI/ML',
      level: 'Beginner',
      duration: '6 weeks',
      students: 1650,
      rating: 4.8,
      image: '🤖',
      description: 'Introduction to machine learning algorithms and models.'
    },
    {
      id: 5,
      title: 'UI/UX Design',
      category: 'Design',
      level: 'Beginner',
      duration: '5 weeks',
      students: 945,
      rating: 4.6,
      image: '🎨',
      description: 'Create beautiful user interfaces and experiences.'
    },
    {
      id: 6,
      title: 'Full Stack Development',
      category: 'Web Development',
      level: 'Advanced',
      duration: '10 weeks',
      students: 756,
      rating: 4.9,
      image: '🚀',
      description: 'Build complete web applications from frontend to backend.'
    }
  ]);

  const [selectedCategory, setSelectedCategory] = useState('All');
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  const categories = ['All', 'Web Development', 'Data Science', 'AI/ML', 'Design'];

  const filteredCourses = selectedCategory === 'All'
    ? courses
    : courses.filter(course => course.category === selectedCategory);

  const handleEnroll = (courseId) => {
    if (!enrolledCourses.includes(courseId)) {
      setEnrolledCourses([...enrolledCourses, courseId]);
    }
  };

  const handleUnenroll = (courseId) => {
    setEnrolledCourses(enrolledCourses.filter(id => id !== courseId));
  };

  return (
    <main className="courses">
      <h1>Explore Our Courses</h1>
      <p className="subtitle">Choose from our diverse range of courses taught by industry experts</p>

      <div className="filter-section">
        <h2>Filter by Category:</h2>
        <div className="category-buttons">
          {categories.map(category => (
            <button
              key={category}
              className={`category-btn ${selectedCategory === category ? 'active' : ''}`}
              onClick={() => setSelectedCategory(category)}
            >
              {category}
            </button>
          ))}
        </div>
      </div>

      <div className="courses-grid">
        {filteredCourses.map(course => (
          <div key={course.id} className="course-card">
            <div className="course-image">{course.image}</div>
            <div className="course-content">
              <h3>{course.title}</h3>
              <p className="course-description">{course.description}</p>
              <div className="course-meta">
                <span className="badge level">{course.level}</span>
                <span className="badge duration">{course.duration}</span>
              </div>
              <div className="course-stats">
                <span>👥 {course.students} students</span>
                <span>⭐ {course.rating}/5</span>
              </div>
              <button
                className={`enroll-btn ${enrolledCourses.includes(course.id) ? 'enrolled' : ''}`}
                onClick={() => {
                  if (enrolledCourses.includes(course.id)) {
                    handleUnenroll(course.id);
                  } else {
                    handleEnroll(course.id);
                  }
                }}
              >
                {enrolledCourses.includes(course.id) ? '✓ Enrolled' : 'Enroll Now'}
              </button>
            </div>
          </div>
        ))}
      </div>

      {enrolledCourses.length > 0 && (
        <div className="enrollment-summary">
          <h2>My Enrollments ({enrolledCourses.length})</h2>
          <div className="enrolled-courses">
            {courses
              .filter(course => enrolledCourses.includes(course.id))
              .map(course => (
                <div key={course.id} className="enrolled-item">
                  <span>{course.image} {course.title}</span>
                  <button
                    className="remove-btn"
                    onClick={() => handleUnenroll(course.id)}
                  >
                    Remove
                  </button>
                </div>
              ))}
          </div>
        </div>
      )}
    </main>
  );
}

export default Courses;
