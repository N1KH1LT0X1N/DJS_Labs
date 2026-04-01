# EduLearn - E-Learning Platform SPA

A modern Single Page Application (SPA) built with React that demonstrates best practices in web development, responsive design, and component-based architecture.

## 🎯 Project Overview

EduLearn is a fully functional E-Learning platform showcasing:
- **Multiple Routes**: Home, Courses, About, and Contact pages
- **State Management**: React Hooks (useState) for managing component state
- **Responsive Design**: CSS styling with mobile-first approach
- **Interactive Features**: Course filtering, enrollment management, form validation

## ✨ Features Implemented

### 1. **React Hooks & State Management** ✓
- `useState` hook used in Navigation component for menu toggle
- `useState` in Courses page for:
  - Managing courses list
  - Filter by category
  - Track enrolled courses
- `useState` in Contact page for:
  - Form data management
  - Form validation and error handling
  - Success message state

### 2. **CSS Integration & Styling** ✓
- Modular CSS files for each page and component
- CSS Grid for responsive layouts
- CSS Flexbox for alignment
- Animations and transitions for better UX
- Media queries for mobile responsiveness
- CSS custom properties (variables) ready for theming
- Hover effects, shadows, and smooth transitions

### 3. **Single Page Application (SPA)** ✓
- React Router DOM for seamless navigation
- Four main pages:
  - **Home**: Hero section, features showcase, statistics
  - **Courses**: Course catalog with filtering and enrollment
  - **About**: Mission, values, team, timeline, FAQs
  - **Contact**: Contact info, contact form with validation

## 📁 Project Structure

```
lab4/
├── public/
│   └── index.html                    # Main HTML file
├── src/
│   ├── components/
│   │   ├── Navigation.js            # Navigation component with mobile menu
│   │   └── Navigation.css           # Navigation styling
│   ├── pages/
│   │   ├── Home.js                  # Home page
│   │   ├── Home.css                 # Home styling
│   │   ├── Courses.js               # Courses page with state management
│   │   ├── Courses.css              # Courses styling
│   │   ├── About.js                 # About page
│   │   ├── About.css                # About styling
│   │   ├── Contact.js               # Contact page with form
│   │   └── Contact.css              # Contact styling
│   ├── App.js                       # Main app component with routing
│   ├── App.css                      # Global styles
│   ├── index.js                     # React entry point
│   └── index.css                    # Global CSS
├── package.json                     # Dependencies and scripts
└── README.md                        # This file
```

## 🚀 Getting Started

### Prerequisites
- Node.js (v14 or higher)
- npm or yarn

### Installation

1. Navigate to the lab4 directory:
```bash
cd Web/lab4
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

4. Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

## 📚 Component Breakdown

### Navigation Component
**Features:**
- Uses `useState` for mobile menu toggle
- Responsive hamburger menu
- Active link highlighting
- Smooth animations

**State Management:**
- `isOpen`: Controls mobile menu visibility

### Courses Page
**Features:**
- Display 6 courses across different categories
- Filter courses by category
- Enroll/Unenroll functionality
- Show enrollment summary
- Course cards with ratings and student count

**State Management:**
- `courses`: Course list data
- `selectedCategory`: Current filter category
- `enrolledCourses`: Track user enrollments

### Contact Page
**Features:**
- Contact information cards
- Contact form with validation
- Real-time error messages
- Success notification
- FAQ section

**State Management:**
- `formData`: Manage form input values
- `submitted`: Show success message
- `errors`: Track validation errors

## 🎨 CSS Features

### Global Styling
- Consistent color scheme (Primary: #3498db, Dark: #2c3e50)
- Font-family: Segoe UI, Tahoma, Geneva, Verdana, sans-serif
- Mobile-first responsive design

### Advanced CSS Techniques
- Grid layout for responsive grids
- Flexbox for component alignment
- CSS animations (floating effect, hamburger animation)
- Box shadows for depth
- Gradients for visual interest
- Transitions for smooth interactions
- Media queries for responsive breakpoints

### Responsive Breakpoints
- Desktop: Full layout
- Tablet (≤768px): Adjusted grid, hamburger menu
- Mobile: Single column layouts, touch-friendly buttons

## 🔄 State Management Examples

### 1. Navigation Mobile Menu
```javascript
const [isOpen, setIsOpen] = useState(false);

const toggleMenu = () => {
  setIsOpen(!isOpen);
};
```

### 2. Course Filtering
```javascript
const [selectedCategory, setSelectedCategory] = useState('All');
const filteredCourses = selectedCategory === 'All'
  ? courses
  : courses.filter(course => course.category === selectedCategory);
```

### 3. Form Validation
```javascript
const [formData, setFormData] = useState({
  name: '', email: '', subject: '', message: ''
});
const [errors, setErrors] = useState({});

const handleChange = (e) => {
  const { name, value } = e.target;
  setFormData(prevState => ({ ...prevState, [name]: value }));
};
```

## 🎯 Key Learnings Demonstrated

1. **React Fundamentals**
   - Functional components
   - Hooks (useState)
   - Component composition
   - Props and children

2. **Routing**
   - React Router DOM setup
   - Route configuration
   - Navigation between pages
   - Nested routing structures

3. **State Management**
   - Local component state with hooks
   - State lifting patterns
   - Conditional rendering
   - Form handling

4. **CSS Best Practices**
   - Modular CSS architecture
   - BEM-like naming conventions
   - Responsive design
   - CSS Grid and Flexbox
   - Animations and transitions

## 📱 Responsive Design

The application is fully responsive:
- **Desktop**: Full-width layouts with multi-column grids
- **Tablet**: Optimized grid columns, improved spacing
- **Mobile**: Single column layouts, hamburger navigation, touch-friendly buttons

## 🎓 Assignment Requirements Met

### ✅ Requirement 1: Import and Use CSS in React Component
- Global CSS in `App.css`
- Component-specific CSS files for each page
- CSS modules pattern with modular structure
- CSS imported and used in React components

### ✅ Requirement 2: React Hooks (useState)
- Used in Navigation for menu state
- Used in Courses for filtering and enrollment
- Used in Contact for form management and validation
- Real-time state updates and re-renders

### ✅ Requirement 3: Single Page Application with Navigation
- Home Page: Hero section, features, statistics
- Courses Page: Course catalog with interactive features
- About Page: Company info, team, timeline, FAQs
- Contact Page: Contact info, form, FAQs
- All pages accessible via navigation without full page reloads

## 🚀 Build for Production

```bash
npm run build
```

Builds the app for production to the `build` folder.

## 📝 License

This project is created for educational purposes as part of the Web Development Lab course.

---

**Created**: 2025
**Version**: 1.0.0
