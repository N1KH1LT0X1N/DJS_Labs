# 🛒 MERN Stack Application - Lab 7

A complete full-stack web application built with **MongoDB**, **Express**, **React**, and **Node.js** (MERN Stack).

---

## 📋 Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Usage Examples](#usage-examples)
- [Future Enhancements](#future-enhancements)

---

## ✨ Features

### Backend Features
- ✅ RESTful API with Express.js
- ✅ MongoDB database integration
- ✅ Data validation and error handling
- ✅ CORS support for cross-origin requests
- ✅ Clean separation of concerns (routes, models, controllers)
- ✅ Environment configuration

### Frontend Features
- ✅ Modern React application with hooks
- ✅ React Router for navigation
- ✅ Responsive design (mobile-friendly)
- ✅ Axios for API calls
- ✅ Form handling with validation
- ✅ Alert notifications
- ✅ Category filtering for products
- ✅ CRUD operations (Create, Read, Update, Delete)

---

## 🏗️ Architecture

### Client-Server Model
```
┌─────────────────┐
│   React Client  │
│   (Port 3000)   │
└────────┬────────┘
         │ HTTP/REST
         │
┌────────▼────────┐
│  Express Server │
│   (Port 5000)   │
└────────┬────────┘
         │ Mongoose
         │
┌────────▼────────┐
│   MongoDB       │
│ (Port 27017)    │
└─────────────────┘
```

---

## 💻 Tech Stack

### Backend
- **Runtime**: Node.js
- **Framework**: Express.js 4.18.2
- **Database**: MongoDB with Mongoose 7.0.0
- **Middleware**: CORS, Body Parser
- **Environment**: dotenv

### Frontend
- **Library**: React 18.2.0
- **Router**: React Router DOM 6.8.0
- **HTTP Client**: Axios 1.3.0
- **Build Tool**: Create React App
- **Styling**: CSS3 with Flexbox and Grid

---

## 📦 Prerequisites

Ensure you have installed:
- Node.js (v14 or higher)
- npm (v6 or higher)
- MongoDB (local or cloud - MongoDB Atlas)

Check versions:
```bash
node --version
npm --version
```

---

## 🚀 Installation

### 1. Clone or Download the Project
```bash
cd Web/lab7
```

### 2. Install Backend Dependencies
```bash
npm install
```

### 3. Install Frontend Dependencies
```bash
cd client
npm install
cd ..
```

---

## ⚙️ Configuration

### 1. Create Environment File
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

### 2. Update `.env` File
```env
# MongoDB Connection
MONGODB_URI=mongodb://localhost:27017/mern-app

# Server Port
PORT=5000

# Environment
NODE_ENV=development
```

### 3. MongoDB Setup

#### Option A: Local MongoDB
```bash
# Start MongoDB service
mongod
```

#### Option B: MongoDB Atlas (Cloud)
```env
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/mern-app
```

---

## 🎯 Running the Application

### Option 1: Run Both Frontend and Backend Together

#### Terminal 1 - Start Backend Server
```bash
npm run dev
```
Server runs on: `http://localhost:5000`

#### Terminal 2 - Start Frontend Development Server
```bash
cd client
npm start
```
App runs on: `http://localhost:3000`

### Option 2: Run Backend Only (For API Testing)
```bash
npm start
```

### Option 3: Production Build
```bash
cd client
npm run build
```

---

## 📁 Project Structure

```
Web/lab7/
├── server.js                 # Express server entry point
├── package.json              # Backend dependencies
├── .env.example              # Environment template
│
├── models/
│   ├── User.js              # User schema and model
│   └── Product.js           # Product schema and model
│
├── routes/
│   ├── userRoutes.js        # User API endpoints
│   └── productRoutes.js     # Product API endpoints
│
└── client/                   # React Frontend
    ├── public/
    │   └── index.html       # HTML entry point
    │
    ├── src/
    │   ├── index.js         # React DOM render
    │   ├── App.js           # Main app component
    │   ├── App.css          # Global styles
    │   │
    │   ├── components/
    │   │   ├── Navigation.js    # Navigation bar
    │   │   └── Navigation.css   # Navigation styles
    │   │
    │   ├── pages/
    │   │   ├── Home.js          # Home page
    │   │   ├── Home.css         # Home styles
    │   │   ├── Users.js         # Users list and form
    │   │   ├── Users.css        # Users styles
    │   │   ├── Products.js      # Products list and form
    │   │   ├── Products.css     # Products styles
    │   │   ├── UserDetail.js    # User detail page
    │   │   └── ProductDetail.js # Product detail page
    │   │
    │   └── package.json     # Frontend dependencies
```

---

## 🔌 API Endpoints

### Health Check
```
GET /api/health
Response: Server status and uptime
```

### Users API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/users` | Get all users |
| GET | `/api/users/:id` | Get specific user |
| POST | `/api/users` | Create new user |
| PUT | `/api/users/:id` | Update user |
| DELETE | `/api/users/:id` | Delete user |
| GET | `/api/users/search/:email` | Search by email |

### Products API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/products` | Get all products |
| GET | `/api/products?category=Electronics` | Filter by category |
| GET | `/api/products?minPrice=10&maxPrice=100` | Filter by price |
| GET | `/api/products/:id` | Get specific product |
| POST | `/api/products` | Create new product |
| PUT | `/api/products/:id` | Update product |
| DELETE | `/api/products/:id` | Delete product |
| GET | `/api/products/category/:category` | Get by category |
| POST | `/api/products/:id/review` | Add review |

---

## 💾 Database Schema

### User Schema
```javascript
{
  name: String,              // Required, max 100 chars
  email: String,             // Required, unique, validated
  phone: String,             // Required
  address: String,           // Optional, max 200 chars
  city: String,              // Optional, max 50 chars
  country: String,           // Optional, max 50 chars
  isActive: Boolean,         // Default: true
  role: String,              // 'user' or 'admin' (default: 'user')
  createdAt: Date,           // Auto-generated
  updatedAt: Date            // Auto-generated
}
```

### Product Schema
```javascript
{
  name: String,              // Required, max 100 chars
  description: String,       // Optional, max 1000 chars
  price: Number,             // Required, min: 0
  quantity: Number,          // Required, min: 0
  category: String,          // Enum: ['Electronics', 'Clothing', 'Books', 'Food', 'Other']
  image: String,             // Optional
  rating: Number,            // 0-5, default: 0
  reviews: Array,            // Array of review objects
  inStock: Boolean,          // Default: true
  createdAt: Date,           // Auto-generated
  updatedAt: Date            // Auto-generated
}
```

---

## 📝 Usage Examples

### Creating a User (API)
```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "9876543210",
    "address": "123 Main St",
    "city": "New York",
    "country": "USA"
  }'
```

### Creating a Product (API)
```bash
curl -X POST http://localhost:5000/api/products \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laptop",
    "description": "High-performance laptop",
    "price": 999.99,
    "quantity": 10,
    "category": "Electronics"
  }'
```

### Getting All Products with Filters (API)
```bash
# Get all products
curl http://localhost:5000/api/products

# Filter by category
curl http://localhost:5000/api/products?category=Electronics

# Filter by price range
curl http://localhost:5000/api/products?minPrice=100&maxPrice=1000
```

---

## 🔒 Error Handling

The API returns structured error responses:
```json
{
  "success": false,
  "error": "Error message here",
  "message": "Detailed error message"
}
```

---

## 📊 Common Workflow

### 1. Start Application
```bash
# Terminal 1 - Backend
npm run dev

# Terminal 2 - Frontend
cd client && npm start
```

### 2. Access Application
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:5000`
- API Health: `http://localhost:5000/api/health`

### 3. Create Data
- Navigate to Users page → Click "Add New User" → Fill form → Submit
- Navigate to Products page → Click "Add New Product" → Fill form → Submit

### 4. Browse Data
- View users in Users table
- Filter products by category
- Delete items with Delete button

---

## 🚀 Future Enhancements

- [ ] User authentication and authorization
- [ ] JWT token-based login system
- [ ] Product image upload functionality
- [ ] Shopping cart system
- [ ] Order management
- [ ] Payment integration (Stripe/PayPal)
- [ ] User reviews and ratings system
- [ ] Search functionality with elasticsearch
- [ ] Admin dashboard
- [ ] Email notifications
- [ ] Input sanitization and CSRF protection
- [ ] API rate limiting
- [ ] Unit and integration tests
- [ ] Docker containerization
- [ ] CI/CD pipeline

---

## 📚 Learning Resources

### Backend
- [Express.js Documentation](https://expressjs.com/)
- [Mongoose Docs](https://mongoosejs.com/)
- [RESTful API Design](https://restfulapi.net/)

### Frontend
- [React Documentation](https://react.dev/)
- [React Router Docs](https://reactrouter.com/)
- [Axios Documentation](https://axios-http.com/)

### Database
- [MongoDB Documentation](https://docs.mongodb.com/)
- [MongoDB Atlas Docs](https://www.mongodb.com/docs/atlas/)

---

## 🐛 Troubleshooting

### MongoDB Connection Error
**Error**: `connect ECONNREFUSED 127.0.0.1:27017`
**Solution**: Ensure MongoDB is running (`mongod` command)

### CORS Error
**Error**: `Access to XMLHttpRequest blocked by CORS policy`
**Solution**: CORS is already configured in server.js

### Port Already in Use
**Error**: `EADDRINUSE: address already in use :::5000`
**Solution**: Change PORT in .env or kill process using the port

### Module Not Found
**Error**: `Cannot find module 'express'`
**Solution**: Run `npm install` in root directory

---

## 📄 License

MIT License - Feel free to use this project for educational purposes.

---

## 👨‍💻 Author

MERN Stack Lab Assignment - Web Development

---

## ✅ Completion Checklist

- ✓ Backend server with Express.js
- ✓ MongoDB integration with Mongoose
- ✓ User and Product models with validation
- ✓ Complete CRUD API endpoints
- ✓ React frontend with React Router
- ✓ User management interface
- ✓ Product catalog with filtering
- ✓ Form handling and validation
- ✓ Error handling and notifications
- ✓ Responsive design
- ✓ Comprehensive documentation

---

**Happy Coding! 🎉**
