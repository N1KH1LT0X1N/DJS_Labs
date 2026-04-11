/**
 * app.js - Main Application using Custom fileManager Module
 * Requirement 2: Implement CRUD Operations using fs module
 * Requirement 3: Create user defined module and use it in application
 */

const fileManager = require('./fileManager');

console.log('==========================================');
console.log('  Node.js CRUD Operations Demo');
console.log('  Using Custom fileManager Module');
console.log('==========================================\n');

// Demonstrate CREATE operation
console.log('--- CREATE Operations ---');
fileManager.createFile('users.txt', 'John Doe\nAge: 30\nCity: New York\n');
fileManager.createFile('config.txt', 'App: Node.js CRUD Demo\nVersion: 1.0.0\n');
fileManager.createFile('notes.txt', 'This is a sample note.\n');

console.log('\n--- LIST Files ---');
const files = fileManager.listFiles();
if (files.length > 0) {
  console.log('Files in data directory:');
  files.forEach((file, index) => {
    console.log(`  ${index + 1}. ${file}`);
  });
}

// Demonstrate READ operation
console.log('\n--- READ Operations ---');
const userData = fileManager.readFile('users.txt');
if (userData) {
  console.log('Content of users.txt:\n', userData);
}

const configData = fileManager.readFile('config.txt');
if (configData) {
  console.log('Content of config.txt:\n', configData);
}

// Demonstrate UPDATE operation
console.log('\n--- UPDATE Operations ---');
fileManager.updateFile('users.txt', 'John Doe\nAge: 31\nCity: Boston\nOccupation: Software Engineer\n');

const updatedUserData = fileManager.readFile('users.txt');
if (updatedUserData) {
  console.log('Updated content of users.txt:\n', updatedUserData);
}

// Demonstrate APPEND operation
console.log('\n--- APPEND Operations ---');
fileManager.appendToFile('notes.txt', 'Updated note with additional information.\n');
fileManager.appendToFile('notes.txt', 'Another line added successfully.\n');

const notesData = fileManager.readFile('notes.txt');
if (notesData) {
  console.log('Updated content of notes.txt:\n', notesData);
}

// Demonstrate DELETE operation
console.log('\n--- DELETE Operations ---');
fileManager.deleteFile('config.txt');

console.log('\n--- FINAL FILE LIST ---');
const finalFiles = fileManager.listFiles();
if (finalFiles.length > 0) {
  console.log('Remaining files in data directory:');
  finalFiles.forEach((file, index) => {
    console.log(`  ${index + 1}. ${file}`);
  });
}

console.log('\n==========================================');
console.log('  CRUD Operations Demonstration Complete');
console.log('==========================================');
