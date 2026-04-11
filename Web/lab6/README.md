# Lab 6: Node.js CRUD Application with Custom Modules

## Lab Assignment Overview

This lab covers three main requirements:
1. **Create a Simple Hello World Application using Node.js**
2. **Implement CRUD Operations using the fs module in Node.js**
3. **Create user defined module and use it in application**

---

## Project Structure

```
lab6/
├── package.json          # Node.js project configuration
├── hello.js              # Simple Hello World application (Requirement 1)
├── fileManager.js        # Custom module for CRUD operations (Requirement 3)
├── app.js                # Main application using fileManager (Requirement 2)
├── data/                 # Directory where files are created/managed
└── README.md             # This file
```

---

## Files Description

### 1. **hello.js** (Requirement 1)
A simple "Hello World" application that demonstrates basic Node.js functionality.

**How to run:**
```bash
node hello.js
```

**Output:**
```
==========================================
  Hello World Application using Node.js
==========================================
Hello, World!
==========================================
```

---

### 2. **fileManager.js** (Requirement 3 - Custom Module)
A user-defined Node.js module that provides the following CRUD operations:

**Functions provided:**
- `createFile(filename, content)` - Create a new file with content
- `readFile(filename)` - Read and display file content
- `updateFile(filename, newContent)` - Update existing file content
- `deleteFile(filename)` - Delete a file
- `appendToFile(filename, content)` - Append content to a file
- `listFiles()` - List all files in the data directory

**Module Export:**
```javascript
module.exports = {
  createFile,
  readFile,
  updateFile,
  deleteFile,
  listFiles,
  appendToFile
};
```

---

### 3. **app.js** (Requirement 2 - CRUD Operations)
Main application that demonstrates all CRUD operations using the custom fileManager module.

**What it does:**
1. Creates multiple files (users.txt, config.txt, notes.txt)
2. Lists all created files
3. Reads file contents
4. Updates files with new content
5. Appends additional content to files
6. Deletes a file
7. Lists remaining files

**How to run:**
```bash
node app.js
```

---

## Usage Examples

### Running Hello World:
```bash
node hello.js
```

### Running CRUD Operations Demo:
```bash
node app.js
```

### Using the fileManager module in your own code:
```javascript
const fileManager = require('./fileManager');

// Create a file
fileManager.createFile('myfile.txt', 'Hello, this is my file!');

// Read the file
const content = fileManager.readFile('myfile.txt');

// Update the file
fileManager.updateFile('myfile.txt', 'Updated content!');

// Append to the file
fileManager.appendToFile('myfile.txt', '\nAppended line!');

// List all files
const files = fileManager.listFiles();

// Delete the file
fileManager.deleteFile('myfile.txt');
```

---

## Key Features

✓ **Modular Design** - fileManager module can be reused in other applications
✓ **Error Handling** - All operations include try-catch error handling
✓ **User Feedback** - Clear console output with success/error messages
✓ **File Management** - Automatic data directory creation
✓ **CRUD Complete** - All four CRUD operations implemented and demonstrated

---

## Requirements Met

✅ **Requirement 1** - Simple Hello World application created (hello.js)
✅ **Requirement 2** - CRUD Operations implemented using fs module (fileManager.js functions)
✅ **Requirement 3** - User-defined module created and used (fileManager.js imported and used in app.js)

---

## Technical Details

- **Language:** JavaScript (Node.js)
- **Built-in Modules Used:** 
  - `fs` (file system operations)
  - `path` (file path handling)
- **Node.js Version:** Requires Node.js 12.0 or higher

---

## Notes

- Files are created in the `data/` subdirectory
- The data directory is created automatically when first needed
- All operations provide console feedback with success/error messages
- File operations are performed synchronously for simplicity

---

## Author
Lab 6 Submission
