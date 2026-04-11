import React from 'react';
import { useParams, Link } from 'react-router-dom';

function UserDetail() {
  const { id } = useParams();

  return (
    <div className="detail-page">
      <Link to="/users" className="back-link">
        ← Back to Users
      </Link>
      <div className="detail-content">
        <h1>User Detail</h1>
        <p>User ID: {id}</p>
        <p>This page would display detailed information for a specific user.</p>
        <p>Feature to be implemented: Fetch user data from API and display it.</p>
      </div>
    </div>
  );
}

export default UserDetail;
