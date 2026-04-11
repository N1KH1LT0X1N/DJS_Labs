# ⚡ Quick Start Guide - LAB 7 MERN Stack

## 30-Second Setup

### Prerequisites Check
```bash
node --version    # Should be v14+
npm --version     # Should be v6+
mongod --version  # MongoDB installed
```

### 1️⃣ Start MongoDB
```bash
mongod
```

### 2️⃣ Install Backend Dependencies
```bash
npm install
```

### 3️⃣ Install Frontend Dependencies
```bash
cd client
npm install
cd ..
```

### 4️⃣ Start Backend Server
```bash
npm run dev
```
✅ Server runs on `http://localhost:5000`

### 5️⃣ Start Frontend (New Terminal)
```bash
cd client
npm start
```
✅ App opens on `http://localhost:3000`

---

## What's Included? 📦

### Backend ✅
- ⚙️ Express.js server with middleware
- 🗄️ MongoDB + Mongoose ODM
- 📡 RESTful API with error handling
- ✔️ Data validation and sanitization
- 📋 Two complete schemas (User, Product)

### Frontend ✅
- ⚛️ React with React Router
- 🎨 Responsive CSS styling
- 🔄 Axios for API calls
- 📝 Form handling with validation
- 🔍 Filtering and search functionality

---

## Test It Out! 🧪

### Using the Web Interface
1. Go to **`http://localhost:3000`**
2. Click on **"Users"** → Add a user
3. Click on **"Products"** → Add a product
4. Filter products by category
5. View data in tables and cards

### Using Postman/cURL

**Get all users:**
```bash
curl http://localhost:5000/api/users
```

**Create a user:**
```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"John","email":"john@test.com","phone":"123456"}'
```

**Get all products:**
```bash
curl http://localhost:5000/api/products
```

---

## File Structure Overview 📁

```
Web/lab7/
├── server.js                 ← Backend entry point
├── models/User.js            ← User schema
├── models/Product.js         ← Product schema
├── routes/userRoutes.js      ← User endpoints
├── routes/productRoutes.js   ← Product endpoints
└── client/                   ← React app
    ├── src/App.js           ← Main component
    └── src/pages/
        ├── Users.js         ← User management
        └── Products.js      ← Product management
```

---

## Common Commands 🔧

| Command | Purpose |
|---------|---------|
| `npm run dev` | Run backend in watch mode |
| `npm start` | Run backend in production |
| `cd client && npm start` | Run React frontend |
| `cd client && npm run build` | Build for production |

---

## Troubleshooting 🆘

| Issue | Solution |
|-------|----------|
| MongoDB not found | Install MongoDB or use MongoDB Atlas |
| Port 5000 in use | Change PORT in .env file |
| CORS error | Already configured in server.js |
| Module not found | Run `npm install` in both root and client/ |

---

## Features to Explore 🚀

✅ **Users Management**
- Add new users
- View user list
- Delete users
- Input validation

✅ **Products Management**
- Add products
- View catalog
- Filter by category
- Filter by price
- Check stock status

✅ **API Features**
- RESTful endpoints
- Error handling
- Data validation
- Async/await

✅ **UI Features**
- Responsive design
- Mobile-friendly
- Smooth animations
- Alert notifications

---

## Next Steps 📚

1. **Explore the code:**
   - Read `README.md` for detailed documentation
   - Check API endpoints in `routes/` folder
   - Review schemas in `models/` folder

2. **Enhance the app:**
   - Add authentication
   - Implement user reviews
   - Add sorting/pagination
   - Create admin dashboard

3. **Learn more:**
   - Study async/await patterns
   - Understand MongoDB queries
   - Master React hooks
   - Learn HTTP protocols

---

## API Documentation 📖

**Base URL**: `http://localhost:5000/api`

### Users
- `GET /users` - Get all users
- `POST /users` - Create user
- `GET /users/:id` - Get user
- `PUT /users/:id` - Update user
- `DELETE /users/:id` - Delete user

### Products
- `GET /products` - Get all products
- `POST /products` - Create product
- `GET /products/:id` - Get product
- `PUT /products/:id` - Update product
- `DELETE /products/:id` - Delete product
- `GET /products?category=Electronics` - Filter

---

**🎉 You're all set! Happy coding!**
