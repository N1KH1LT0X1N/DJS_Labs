# Lab 4 - Code Snippets & Examples

## 1. React Hooks - useState Examples

### Example 1: Navigation Mobile Menu Toggle

```javascript
// Navigation.js
import React, { useState } from 'react';

function Navigation() {
  // useState Hook: Manages mobile menu open/close state
  const [isOpen, setIsOpen] = useState(false);

  // Toggle function that updates state
  const toggleMenu = () => {
    setIsOpen(!isOpen);  // Change false to true or true to false
  };

  return (
    <nav className="navbar">
      <div className="hamburger" onClick={toggleMenu}>
        {/* Conditional class based on state */}
        <span className={isOpen ? 'bar open' : 'bar'}></span>
        <span className={isOpen ? 'bar open' : 'bar'}></span>
        <span className={isOpen ? 'bar open' : 'bar'}></span>
      </div>
      
      {/* Conditional rendering based on state */}
      <ul className={isOpen ? 'nav-menu active' : 'nav-menu'}>
        <li className="nav-item">
          <Link to="/" onClick={() => setIsOpen(false)}>Home</Link>
        </li>
      </ul>
    </nav>
  );
}
```

### Example 2: Course Filtering with Multiple useState Hooks

```javascript
// Courses.js
import React, { useState } from 'react';

function Courses() {
  // State 1: Manage courses list
  const [courses, setCourses] = useState([
    { id: 1, title: 'Web Development', category: 'Web Development' },
    { id: 2, title: 'React Advanced', category: 'Web Development' },
    // ... more courses
  ]);

  // State 2: Track selected category filter
  const [selectedCategory, setSelectedCategory] = useState('All');

  // State 3: Track enrolled courses
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  // Filter courses based on category
  const filteredCourses = selectedCategory === 'All'
    ? courses
    : courses.filter(course => course.category === selectedCategory);

  // Enroll in a course
  const handleEnroll = (courseId) => {
    if (!enrolledCourses.includes(courseId)) {
      setEnrolledCourses([...enrolledCourses, courseId]);
    }
  };

  return (
    <div>
      {/* Filter buttons that update state */}
      {['All', 'Web Development', 'Data Science'].map(category => (
        <button
          key={category}
          onClick={() => setSelectedCategory(category)}
          className={selectedCategory === category ? 'active' : ''}
        >
          {category}
        </button>
      ))}

      {/* Display filtered courses */}
      {filteredCourses.map(course => (
        <div key={course.id}>
          <h3>{course.title}</h3>
          <button onClick={() => handleEnroll(course.id)}>
            {enrolledCourses.includes(course.id) ? '✓ Enrolled' : 'Enroll'}
          </button>
        </div>
      ))}
    </div>
  );
}
```

### Example 3: Form Validation with useState

```javascript
// Contact.js
import React, { useState } from 'react';

function Contact() {
  // State 1: Form data (object with multiple fields)
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: ''
  });

  // State 2: Track submission success
  const [submitted, setSubmitted] = useState(false);

  // State 3: Store validation errors
  const [errors, setErrors] = useState({});

  // Handle input changes - update formData state
  const handleChange = (e) => {
    const { name, value } = e.target;
    
    // Spread operator to preserve other fields, update one field
    setFormData(prevState => ({
      ...prevState,
      [name]: value  // Update only the changed field
    }));

    // Clear error for this field when user starts typing
    if (errors[name]) {
      setErrors(prevErrors => ({
        ...prevErrors,
        [name]: ''
      }));
    }
  };

  // Validate form
  const validateForm = () => {
    const newErrors = {};
    
    if (!formData.name.trim()) {
      newErrors.name = 'Name is required';
    }
    
    if (!formData.email.trim()) {
      newErrors.email = 'Email is required';
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      newErrors.email = 'Email is invalid';
    }
    
    if (!formData.message.trim()) {
      newErrors.message = 'Message is required';
    }
    
    return newErrors;
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    
    const newErrors = validateForm();
    
    if (Object.keys(newErrors).length === 0) {
      // No errors - set submitted state
      setSubmitted(true);
      
      // Clear form
      setFormData({
        name: '',
        email: '',
        subject: '',
        message: ''
      });
      
      // Hide success message after 5 seconds
      setTimeout(() => setSubmitted(false), 5000);
    } else {
      // Set errors state to display validation messages
      setErrors(newErrors);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Success message - conditional rendering based on submitte state */}
      {submitted && <div className="success-message">✓ Message sent!</div>}

      {/* Form input with error handling */}
      <div className="form-group">
        <label htmlFor="name">Name</label>
        <input
          type="text"
          id="name"
          name="name"
          value={formData.name}
          onChange={handleChange}
          className={errors.name ? 'error' : ''}
        />
        {errors.name && <span className="error-message">{errors.name}</span>}
      </div>

      <button type="submit">Send</button>
    </form>
  );
}
```

---

## 2. CSS Examples

### CSS Grid for Responsive Cards

```css
/* Courses.css - Course grid layout */
.courses-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 4rem;
}

/* Auto-fit creates responsive columns:
   - 4 columns on 1400px+ screens
   - 3 columns on 1000px+ screens
   - 2 columns on 700px+ screens
   - 1 column on mobile
*/
```

### Mobile-First Responsive Design with Media Queries

```css
/* Base: Mobile first! */
.container {
  width: 100%;
  padding: 1rem;
}

.grid {
  display: grid;
  grid-template-columns: 1fr;  /* Single column on mobile */
  gap: 1rem;
}

/* Tablet and up */
@media screen and (min-width: 768px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);  /* Two columns on tablet */
  }
}

/* Desktop and up */
@media screen and (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(3, 1fr);  /* Three columns on desktop */
  }
}
```

### CSS Animations

```css
/* Navigation.css - Hamburger menu animation */
.bar {
  width: 25px;
  height: 3px;
  background-color: #fff;
  border-radius: 3px;
  transition: all 0.3s ease;  /* Smooth animation */
}

/* When menu is open */
.bar.open:nth-child(1) {
  transform: rotate(-45deg) translate(-5px, 6px);
}

.bar.open:nth-child(2) {
  opacity: 0;
}

.bar.open:nth-child(3) {
  transform: rotate(45deg) translate(-5px, -6px);
}
```

### Flexbox Layout

```css
/* Navigation.css - Horizontal layout for nav items */
.nav-menu {
  display: flex;
  list-style: none;
  text-align: center;
  gap: 2rem;  /* Space between items */
  margin: 0;
  padding: 0;
}

/* Example: Column layout on mobile */
@media screen and (max-width: 768px) {
  .nav-menu {
    flex-direction: column;  /* Stack vertically */
    gap: 0;
  }
}
```

### Gradients and Shadows

```css
/* Home.css & Contact.css */
.hero-section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.feature-card:hover {
  transform: translateY(-10px);  /* Move up on hover */
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);  /* Larger shadow */
}
```

---

## 3. React Router Setup

```javascript
// App.js - Setting up SPA routing
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
import Home from './pages/Home';
import Courses from './pages/Courses';
import About from './pages/About';
import Contact from './pages/Contact';

function App() {
  return (
    <Router>
      <Navigation />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/courses" element={<Courses />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </Router>
  );
}

export default App;
```

---

## 4. Key Concepts

### useState Hook Pattern
```javascript
// Syntax: const [state, setState] = useState(initialValue)
const [count, setCount] = useState(0);

// Update state
setCount(count + 1);

// Or use function update (for complex state)
setCount(prevCount => prevCount + 1);
```

### Conditional Rendering
```javascript
// Method 1: If statement
if (enrolledCourses.includes(courseId)) {
  return <div>✓ Enrolled</div>;
}

// Method 2: Ternary operator (in JSX)
return (
  <div>
    {enrolledCourses.includes(courseId) ? '✓ Enrolled' : 'Enroll'}
  </div>
);

// Method 3: && operator
{submitted && <div className="success">Message sent!</div>}
```

### Array Operations in State

```javascript
// Add item to array
setEnrolledCourses([...enrolledCourses, courseId]);

// Remove item from array
setEnrolledCourses(enrolledCourses.filter(id => id !== courseId));

// Filter array
const filtered = courses.filter(c => c.category === selectedCategory);

// Map array (for rendering)
{courses.map(course => <CourseCard key={course.id} course={course} />)}
```

### Object Operations in State

```javascript
// Update one property in object
setFormData(prevState => ({
  ...prevState,
  [fieldName]: fieldValue
}));

// Reset entire object
setFormData({ name: '', email: '', message: '' });
```

---

## 5. Component Structure Example

```javascript
// Template for creating a React component with CSS integration
import React, { useState } from 'react';
import './ComponentName.css';  // Import CSS

function ComponentName() {
  // 1. Declare hooks at top
  const [state, setState] = useState(initialValue);

  // 2. define handlers
  const handleClick = () => {
    setState(newValue);
  };

  // 3. Render JSX with CSS classes
  return (
    <div className="component-wrapper">
      <h1 className="component-title">Title</h1>
      <button 
        className="component-button"
        onClick={handleClick}
      >
        Click me
      </button>
    </div>
  );
}

export default ComponentName;
```

---

## 6. Complete mini-example: Todo Counter

```javascript
import React, { useState } from 'react';
import './TodoCounter.css';

function TodoCounter() {
  // State for count
  const [count, setCount] = useState(0);
  
  // State for todos list
  const [todos, setTodos] = useState([]);
  
  // State for input
  const [input, setInput] = useState('');

  // Add todo
  const addTodo = () => {
    if (input.trim()) {
      setTodos([...todos, { id: Date.now(), text: input }]);
      setInput('');  // Clear input
      setCount(count + 1);
    }
  };

  // Remove todo
  const removeTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
    setCount(count - 1);
  };

  return (
    <div className="todo-counter">
      <h2>Todos: {count}</h2>
      
      <div className="input-group">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && addTodo()}
          placeholder="Add a todo..."
        />
        <button onClick={addTodo}>Add</button>
      </div>

      <ul className="todo-list">
        {todos.map(todo => (
          <li key={todo.id}>
            {todo.text}
            <button onClick={() => removeTodo(todo.id)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoCounter;
```

---

## 7. Testing & Debugging Tips

### Console Logging State Changes
```javascript
// Log state when it changes
useEffect(() => {
  console.log('State updated:', formData);
}, [formData]);
```

### React DevTools
- Install React DevTools browser extension
- Inspect components and their props/state
- Track component renders

### Common Errors

**Error: "Cannot assign to read only property"**
- Don't try to mutate state directly: ❌ `state.field = value`
- Use setState instead: ✅ `setState({ ...state, field: value })`

**Error: "Too many re-renders"**
- Don't call setState directly in render: ❌ `setState(...)`
- Put it in event handler or useEffect: ✅ `onClick={() => setState(...)}`

**Warning: "Key prop missing"**
- Always use unique `key` prop in lists: ✅ `map((item, index) => <div key={item.id}>`

---

**Created**: March 29, 2025
**For**: Lab 4 - E-Learning Platform SPA
