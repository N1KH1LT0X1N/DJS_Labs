import React from 'react';
import { useParams, Link } from 'react-router-dom';

function ProductDetail() {
  const { id } = useParams();

  return (
    <div className="detail-page">
      <Link to="/products" className="back-link">
        ← Back to Products
      </Link>
      <div className="detail-content">
        <h1>Product Detail</h1>
        <p>Product ID: {id}</p>
        <p>This page would display detailed information for a specific product.</p>
        <p>Feature to be implemented: Fetch product data from API and display it with reviews.</p>
      </div>
    </div>
  );
}

export default ProductDetail;
