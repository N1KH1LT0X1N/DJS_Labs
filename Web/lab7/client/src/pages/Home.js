import React from 'react';
import './Home.css';

function Home() {
  return (
    <div className="home">
      <div className="hero">
        <h1>Welcome to MERN Stack Application</h1>
        <p>A modern full-stack web application using MongoDB, Express, React, and Node.js</p>
        <div className="hero-buttons">
          <a href="/users" className="btn btn-primary">
            Manage Users
          </a>
          <a href="/products" className="btn btn-primary">
            Browse Products
          </a>
        </div>
      </div>

      <section className="features">
        <h2>Features</h2>
        <div className="features-grid">
          <div className="feature-card">
            <div className="feature-icon">📦</div>
            <h3>MongoDB</h3>
            <p>NoSQL database for flexible data storage and management</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">⚙️</div>
            <h3>Express.js</h3>
            <p>Lightweight web framework for building RESTful APIs</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">⚛️</div>
            <h3>React</h3>
            <p>JavaScript library for building interactive user interfaces</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">🚀</div>
            <h3>Node.js</h3>
            <p>JavaScript runtime for server-side development</p>
          </div>
        </div>
      </section>

      <section className="api-endpoints">
        <h2>API Endpoints</h2>
        <div className="endpoints-grid">
          <div className="endpoint-card">
            <h4>Users</h4>
            <ul>
              <li>GET /api/users - Get all users</li>
              <li>GET /api/users/:id - Get user by ID</li>
              <li>POST /api/users - Create user</li>
              <li>PUT /api/users/:id - Update user</li>
              <li>DELETE /api/users/:id - Delete user</li>
            </ul>
          </div>
          <div className="endpoint-card">
            <h4>Products</h4>
            <ul>
              <li>GET /api/products - Get all products</li>
              <li>GET /api/products/:id - Get product by ID</li>
              <li>POST /api/products - Create product</li>
              <li>PUT /api/products/:id - Update product</li>
              <li>DELETE /api/products/:id - Delete product</li>
            </ul>
          </div>
        </div>
      </section>

      <section className="tech-stack">
        <h2>Technology Stack</h2>
        <div className="stack-list">
          <div className="stack-item">
            <strong>Backend:</strong> Node.js, Express.js, MongoDB, Mongoose
          </div>
          <div className="stack-item">
            <strong>Frontend:</strong> React, React Router, Axios
          </div>
          <div className="stack-item">
            <strong>Database:</strong> MongoDB with Mongoose ODM
          </div>
          <div className="stack-item">
            <strong>Architecture:</strong> RESTful API with separated backend and frontend
          </div>
        </div>
      </section>
    </div>
  );
}

export default Home;
