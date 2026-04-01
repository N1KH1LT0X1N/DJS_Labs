from docx import Document
import os

def extract_images_from_docx(docx_path, output_dir):
    doc = Document(docx_path)
    
    # Extract from document relationships
    for rel in doc.part.rels.values():
        if "image" in rel.target_ref:
            image = rel.target_part.blob
            image_filename = os.path.basename(rel.target_ref)
            with open(os.path.join(output_dir, image_filename), 'wb') as f:
                f.write(image)
            print(f"Extracted: {image_filename}")

os.makedirs('lab1/images', exist_ok=True)
os.makedirs('lab2/images', exist_ok=True)

print("=== Extracting Lab 1 Images ===")
extract_images_from_docx('lab1/Practical_No_1.docx', 'lab1/images')

print("\n=== Extracting Lab 2 Images ===")
extract_images_from_docx('lab2/Practical_No_2.docx', 'lab2/images')

print("\nDone!")
