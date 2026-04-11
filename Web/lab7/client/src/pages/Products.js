import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Products.css';

function Products() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [filterCategory, setFilterCategory] = useState('All');
  const [successMessage, setSuccessMessage] = useState('');
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    price: '',
    quantity: '',
    category: 'Electronics',
  });

  useEffect(() => {
    fetchProducts();
  }, [filterCategory]);

  const fetchProducts = async () => {
    try {
      setLoading(true);
      const url =
        filterCategory === 'All'
          ? '/api/products'
          : `/api/products?category=${filterCategory}`;
      const response = await axios.get(url);
      setProducts(response.data.data || []);
      setError(null);
    } catch (err) {
      setError('Failed to fetch products: ' + (err.response?.data?.error || err.message));
      setProducts([]);
    } finally {
      setLoading(false);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: name === 'price' || name === 'quantity' ? parseFloat(value) : value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('/api/products', formData);
      setSuccessMessage('Product created successfully!');
      setFormData({
        name: '',
        description: '',
        price: '',
        quantity: '',
        category: 'Electronics',
      });
      setShowForm(false);
      fetchProducts();
      setTimeout(() => setSuccessMessage(''), 3000);
    } catch (err) {
      setError('Failed to create product: ' + (err.response?.data?.error || err.message));
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this product?')) {
      try {
        await axios.delete(`/api/products/${id}`);
        setSuccessMessage('Product deleted successfully!');
        fetchProducts();
        setTimeout(() => setSuccessMessage(''), 3000);
      } catch (err) {
        setError('Failed to delete product: ' + (err.response?.data?.error || err.message));
      }
    }
  };

  if (loading) {
    return <div className="loading">Loading products...</div>;
  }

  return (
    <div className="products-page">
      <h1>Products Catalog</h1>

      {error && <div className="alert alert-danger">{error}</div>}
      {successMessage && <div className="alert alert-success">{successMessage}</div>}

      <div className="button-group">
        <button
          className="btn btn-success"
          onClick={() => setShowForm(!showForm)}
        >
          {showForm ? 'Cancel' : 'Add New Product'}
        </button>
      </div>

      {showForm && (
        <form onSubmit={handleSubmit} className="product-form">
          <h2>Create New Product</h2>
          <div className="form-group">
            <label htmlFor="name">Product Name *</label>
            <input
              type="text"
              id="name"
              name="name"
              value={formData.name}
              onChange={handleInputChange}
              required
              placeholder="Enter product name"
            />
          </div>
          <div className="form-group">
            <label htmlFor="description">Description</label>
            <textarea
              id="description"
              name="description"
              value={formData.description}
              onChange={handleInputChange}
              placeholder="Enter product description"
              rows="3"
            ></textarea>
          </div>
          <div className="form-row">
            <div className="form-group">
              <label htmlFor="price">Price *</label>
              <input
                type="number"
                id="price"
                name="price"
                value={formData.price}
                onChange={handleInputChange}
                required
                placeholder="Enter price"
                step="0.01"
                min="0"
              />
            </div>
            <div className="form-group">
              <label htmlFor="quantity">Quantity *</label>
              <input
                type="number"
                id="quantity"
                name="quantity"
                value={formData.quantity}
                onChange={handleInputChange}
                required
                placeholder="Enter quantity"
                min="0"
              />
            </div>
          </div>
          <div className="form-group">
            <label htmlFor="category">Category *</label>
            <select
              id="category"
              name="category"
              value={formData.category}
              onChange={handleInputChange}
              required
            >
              <option>Electronics</option>
              <option>Clothing</option>
              <option>Books</option>
              <option>Food</option>
              <option>Other</option>
            </select>
          </div>
          <button type="submit" className="btn btn-primary">
            Create Product
          </button>
        </form>
      )}

      <div className="filter-section">
        <h3>Filter by Category</h3>
        <div className="category-buttons">
          {['All', 'Electronics', 'Clothing', 'Books', 'Food', 'Other'].map(
            (category) => (
              <button
                key={category}
                className={`category-btn ${filterCategory === category ? 'active' : ''}`}
                onClick={() => setFilterCategory(category)}
              >
                {category}
              </button>
            )
          )}
        </div>
      </div>

      <div className="products-grid">
        <h2>Products ({products.length})</h2>
        {products.length === 0 ? (
          <p className="no-data">No products found in this category.</p>
        ) : (
          <div className="grid">
            {products.map((product) => (
              <div key={product._id} className="product-card">
                <h3>{product.name}</h3>
                <p className="category">{product.category}</p>
                <p className="description">{product.description || 'No description'}</p>
                <div className="product-info">
                  <span className="price">${product.price.toFixed(2)}</span>
                  <span className={`stock ${product.inStock ? 'in-stock' : 'out-of-stock'}`}>
                    {product.inStock ? '✓ In Stock' : '✗ Out of Stock'}
                  </span>
                </div>
                <p className="quantity">Stock: {product.quantity}</p>
                <button
                  className="btn btn-danger"
                  onClick={() => handleDelete(product._id)}
                >
                  Delete
                </button>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default Products;
