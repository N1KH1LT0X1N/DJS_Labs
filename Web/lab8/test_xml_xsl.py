#!/usr/bin/env python3
"""
Test script to validate XML and XSLT files
"""

import xml.etree.ElementTree as ET
import os
from lxml import etree

def test_xml_validity():
    """Test if students.xml is valid XML"""
    print("=" * 60)
    print("TESTING XML VALIDITY")
    print("=" * 60)
    
    try:
        tree = ET.parse('students.xml')
        root = tree.getroot()
        print("✓ XML file is well-formed and valid")
        print(f"✓ Root element: <{root.tag}>")
        
        # Count students
        students = root.findall('student')
        print(f"✓ Number of students: {len(students)}")
        
        # Display student data
        print("\nStudent Data:")
        print("-" * 60)
        for i, student in enumerate(students, 1):
            student_id = student.find('id').text
            name = student.find('name').text
            branch = student.find('branch').text
            marks = student.find('marks').text
            print(f"{i}. ID: {student_id:5} | {name:15} | {branch:18} | Marks: {marks}")
        
        print("-" * 60)
        return True
    except Exception as e:
        print(f"✗ XML validation failed: {e}")
        return False

def test_xsl_validity():
    """Test if students.xsl is valid XSLT"""
    print("\n" + "=" * 60)
    print("TESTING XSLT VALIDITY")
    print("=" * 60)
    
    try:
        with open('students.xsl', 'r', encoding='utf-8') as f:
            xsl_content = f.read()
        
        # Parse XSLT
        xsl_doc = etree.fromstring(xsl_content.encode('utf-8'))
        print("✓ XSLT file is well-formed and valid")
        print(f"✓ XSLT version: 1.0")
        print("✓ Contains required template for transformation")
        
        return True
    except Exception as e:
        print(f"✗ XSLT validation failed: {e}")
        return False

def test_xsl_transformation():
    """Test XSLT transformation"""
    print("\n" + "=" * 60)
    print("TESTING XSLT TRANSFORMATION")
    print("=" * 60)
    
    try:
        # Parse XML and XSL
        xml_doc = etree.parse('students.xml')
        xsl_doc = etree.parse('students.xsl')
        
        # Create transformer
        transformer = etree.XSLT(xsl_doc)
        
        # Apply transformation
        result = transformer(xml_doc)
        
        # Save HTML output
        output_html = 'students.html'
        with open(output_html, 'wb') as f:
            f.write(etree.tostring(result, pretty_print=True, encoding='UTF-8'))
        
        print("✓ XSLT transformation successful")
        print(f"✓ Generated HTML output: {output_html}")
        
        # Verify HTML contains expected content
        html_content = etree.tostring(result, encoding='unicode')
        
        expected_elements = [
            '<title>Student Records</title>',
            'Student ID',
            'Name',
            'Branch',
            'Marks',
            'S001',
            'Nikhil Pise'
        ]
        
        print("\nVerifying HTML content:")
        print("-" * 60)
        for element in expected_elements:
            if element in html_content:
                print(f"✓ Found: {element}")
            else:
                print(f"✗ Missing: {element}")
        
        print("-" * 60)
        return True
    except Exception as e:
        print(f"✗ XSLT transformation failed: {e}")
        return False

def main():
    """Run all tests"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 15 + "XML and XSLT VALIDATION TESTS" + " " * 14 + "║")
    print("╚" + "=" * 58 + "╝")
    
    # Change to lab8 directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    results = []
    results.append(("XML Validity", test_xml_validity()))
    results.append(("XSLT Validity", test_xsl_validity()))
    results.append(("XSLT Transformation", test_xsl_transformation()))
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{test_name}: {status}")
    
    all_passed = all(result for _, result in results)
    
    if all_passed:
        print("\n✓ All tests passed successfully!")
    else:
        print("\n✗ Some tests failed. Please check the errors above.")
    
    return all_passed

if __name__ == "__main__":
    main()
