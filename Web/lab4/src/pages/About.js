import React from 'react';
import './About.css';

function About() {
  const team = [
    {
      id: 1,
      name: 'Sarah Chen',
      role: 'Founder & CEO',
      bio: 'Education enthusiast with 15+ years of experience',
      icon: '👩‍💼'
    },
    {
      id: 2,
      name: 'John Smith',
      role: 'Head of Curriculum',
      bio: 'Former Stanford professor specializing in tech education',
      icon: '👨‍🏫'
    },
    {
      id: 3,
      name: 'Emma Rodriguez',
      role: 'Lead Developer',
      bio: 'Full-stack engineer passionate about edtech',
      icon: '👩‍💻'
    },
    {
      id: 4,
      name: 'Michael Park',
      role: 'Community Manager',
      bio: 'Building thriving learning communities worldwide',
      icon: '👨‍💼'
    }
  ];

  const milestones = [
    { year: '2020', milestone: 'EduLearn Founded' },
    { year: '2021', milestone: 'Reached 10,000+ Students' },
    { year: '2022', milestone: 'Expanded to 50+ Courses' },
    { year: '2023', milestone: 'Reached 50,000+ Active Learners' },
    { year: '2024', milestone: 'Global Expansion to 25 Countries' },
    { year: '2025', milestone: 'Certified by International Education Bodies' }
  ];

  return (
    <main className="about">
      <div className="about-hero">
        <h1>About EduLearn</h1>
        <p>Transforming Education for Everyone, Everywhere</p>
      </div>

      <section className="mission-section">
        <h2>Our Mission</h2>
        <p>
          At EduLearn, we believe that education is the key to unlocking human potential.
          Our mission is to make quality education accessible and affordable to everyone,
          regardless of their background or location. We're committed to creating engaging,
          practical, and transformative learning experiences that empower individuals to
          achieve their goals and make a positive impact in the world.
        </p>
      </section>

      <section className="values-section">
        <h2>Our Core Values</h2>
        <div className="values-grid">
          <div className="value-card">
            <h3>🎯 Excellence</h3>
            <p>We strive for the highest quality in everything we do.</p>
          </div>
          <div className="value-card">
            <h3>🌍 Accessibility</h3>
            <p>Education should be accessible to learners worldwide.</p>
          </div>
          <div className="value-card">
            <h3>💡 Innovation</h3>
            <p>We continuously innovate to improve the learning experience.</p>
          </div>
          <div className="value-card">
            <h3>🤝 Community</h3>
            <p>We foster a supportive community of learners and educators.</p>
          </div>
        </div>
      </section>

      <section className="timeline-section">
        <h2>Our Journey</h2>
        <div className="timeline">
          {milestones.map((item, index) => (
            <div key={index} className="timeline-item">
              <div className="timeline-dot"></div>
              <div className="timeline-content">
                <h3>{item.year}</h3>
                <p>{item.milestone}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      <section className="team-section">
        <h2>Meet Our Team</h2>
        <p className="team-intro">Led by passionate educators and technologists</p>
        <div className="team-grid">
          {team.map(member => (
            <div key={member.id} className="team-card">
              <div className="team-icon">{member.icon}</div>
              <h3>{member.name}</h3>
              <p className="role">{member.role}</p>
              <p className="bio">{member.bio}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="why-choose-section">
        <h2>Why Choose EduLearn?</h2>
        <div className="reasons-grid">
          <div className="reason">
            <span className="reason-icon">✓</span>
            <h3>Expert-Led Courses</h3>
            <p>All courses are created and taught by industry professionals.</p>
          </div>
          <div className="reason">
            <span className="reason-icon">✓</span>
            <h3>Flexible Learning</h3>
            <p>Learn at your own pace, on your own schedule.</p>
          </div>
          <div className="reason">
            <span className="reason-icon">✓</span>
            <h3>Hands-On Projects</h3>
            <p>Build real-world projects to strengthen your portfolio.</p>
          </div>
          <div className="reason">
            <span className="reason-icon">✓</span>
            <h3>Lifetime Access</h3>
            <p>Continue learning with lifetime access to course materials.</p>
          </div>
          <div className="reason">
            <span className="reason-icon">✓</span>
            <h3>Career Support</h3>
            <p>Get guidance on career development and job placement.</p>
          </div>
          <div className="reason">
            <span className="reason-icon">✓</span>
            <h3>Certification</h3>
            <p>Earn recognized certifications to boost your career.</p>
          </div>
        </div>
      </section>
    </main>
  );
}

export default About;
