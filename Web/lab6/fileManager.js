/**
 * fileManager.js - User-defined Module for CRUD Operations
 * This module provides functions for Create, Read, Update, and Delete operations
 * using Node.js fs module
 */

const fs = require('fs');
const path = require('path');

// Directory where files will be stored
const DATA_DIR = path.join(__dirname, 'data');

// Ensure data directory exists
function ensureDataDir() {
  if (!fs.existsSync(DATA_DIR)) {
    fs.mkdirSync(DATA_DIR);
    console.log('✓ Data directory created');
  }
}

/**
 * CREATE - Create a new file with content
 * @param {string} filename - Name of the file to create
 * @param {string} content - Content to write to the file
 * @returns {boolean} - Returns true if file created successfully
 */
function createFile(filename, content) {
  try {
    ensureDataDir();
    const filepath = path.join(DATA_DIR, filename);
    
    if (fs.existsSync(filepath)) {
      console.log(`✗ File "${filename}" already exists`);
      return false;
    }
    
    fs.writeFileSync(filepath, content, 'utf8');
    console.log(`✓ File "${filename}" created successfully`);
    return true;
  } catch (error) {
    console.error(`✗ Error creating file: ${error.message}`);
    return false;
  }
}

/**
 * READ - Read content from a file
 * @param {string} filename - Name of the file to read
 * @returns {string|null} - Returns file content or null if error
 */
function readFile(filename) {
  try {
    const filepath = path.join(DATA_DIR, filename);
    
    if (!fs.existsSync(filepath)) {
      console.log(`✗ File "${filename}" does not exist`);
      return null;
    }
    
    const content = fs.readFileSync(filepath, 'utf8');
    console.log(`✓ File "${filename}" read successfully`);
    return content;
  } catch (error) {
    console.error(`✗ Error reading file: ${error.message}`);
    return null;
  }
}

/**
 * UPDATE - Update content of an existing file
 * @param {string} filename - Name of the file to update
 * @param {string} newContent - New content to write
 * @returns {boolean} - Returns true if update successful
 */
function updateFile(filename, newContent) {
  try {
    const filepath = path.join(DATA_DIR, filename);
    
    if (!fs.existsSync(filepath)) {
      console.log(`✗ File "${filename}" does not exist`);
      return false;
    }
    
    fs.writeFileSync(filepath, newContent, 'utf8');
    console.log(`✓ File "${filename}" updated successfully`);
    return true;
  } catch (error) {
    console.error(`✗ Error updating file: ${error.message}`);
    return false;
  }
}

/**
 * DELETE - Delete a file
 * @param {string} filename - Name of the file to delete
 * @returns {boolean} - Returns true if deletion successful
 */
function deleteFile(filename) {
  try {
    const filepath = path.join(DATA_DIR, filename);
    
    if (!fs.existsSync(filepath)) {
      console.log(`✗ File "${filename}" does not exist`);
      return false;
    }
    
    fs.unlinkSync(filepath);
    console.log(`✓ File "${filename}" deleted successfully`);
    return true;
  } catch (error) {
    console.error(`✗ Error deleting file: ${error.message}`);
    return false;
  }
}

/**
 * LIST - List all files in data directory
 * @returns {array} - Returns array of filenames
 */
function listFiles() {
  try {
    ensureDataDir();
    const files = fs.readdirSync(DATA_DIR);
    console.log(`✓ Found ${files.length} file(s)`);
    return files;
  } catch (error) {
    console.error(`✗ Error listing files: ${error.message}`);
    return [];
  }
}

/**
 * APPEND - Append content to a file
 * @param {string} filename - Name of the file to append to
 * @param {string} content - Content to append
 * @returns {boolean} - Returns true if successful
 */
function appendToFile(filename, content) {
  try {
    const filepath = path.join(DATA_DIR, filename);
    fs.appendFileSync(filepath, content, 'utf8');
    console.log(`✓ Content appended to "${filename}" successfully`);
    return true;
  } catch (error) {
    console.error(`✗ Error appending to file: ${error.message}`);
    return false;
  }
}

// Export the module functions
module.exports = {
  createFile,
  readFile,
  updateFile,
  deleteFile,
  listFiles,
  appendToFile
};
