import React from 'react';
import './Home.css';

function Home() {
  return (
    <main className="home">
      <div className="hero-section">
        <div className="hero-content">
          <h1>Welcome to EduLearn</h1>
          <p>Your Gateway to Knowledge and Professional Growth</p>
          <p className="tagline">Learn at your own pace. Master new skills. Achieve your goals.</p>
          <button className="cta-button">Explore Courses</button>
        </div>
        <div className="hero-image">
          <div className="illustration">📖</div>
        </div>
      </div>

      <section className="features">
        <h2>Why Choose EduLearn?</h2>
        <div className="features-grid">
          <div className="feature-card">
            <div className="feature-icon">⚡</div>
            <h3>Fast Learning</h3>
            <p>Complete courses at your own pace with flexible scheduling.</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">👨‍🏫</div>
            <h3>Expert Instructors</h3>
            <p>Learn from industry experts with years of experience.</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">🎓</div>
            <h3>Certification</h3>
            <p>Earn recognized certificates upon course completion.</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">🌍</div>
            <h3>Global Community</h3>
            <p>Join thousands of learners from around the world.</p>
          </div>
        </div>
      </section>

      <section className="stats">
        <h2>Our Impact</h2>
        <div className="stats-grid">
          <div className="stat">
            <h3>50K+</h3>
            <p>Active Students</p>
          </div>
          <div className="stat">
            <h3>200+</h3>
            <p>Online Courses</p>
          </div>
          <div className="stat">
            <h3>95%</h3>
            <p>Success Rate</p>
          </div>
          <div className="stat">
            <h3>150+</h3>
            <p>Expert Tutors</p>
          </div>
        </div>
      </section>
    </main>
  );
}

export default Home;
