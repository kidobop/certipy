# Certipy: Bulk Certificate Generator using PNG Template and CSV Dataset
Ceritpy is a Python App that generates bulk certificates by taking csv dataset and png certificate template as inputs.

## Project To-Dos

- [ ] **Import the Image**  
  Use the Pillow library to open and load the image that contains the placeholder text.

- [ ] **Extract Placeholder Text**  
  Leverage pytesseract to perform Optical Character Recognition (OCR) and locate the placeholder text within the image.

- [ ] **Replace Placeholder Text**  
  After identifying the placeholder text, replace it with the desired dynamic text for each certificate.

- [ ] **Import Data from CSV**  
  Load and parse the dataset from a CSV file, where each row contains data (e.g., names, titles) to be used in generating individual certificates.

- [ ] **Generate Certificates in Bulk**  
  Iterate over the rows of the CSV dataset and create personalized certificates by replacing the placeholder text with data from each row.

- [ ] **Save Output**  
  Save each generated certificate as a separate image file (e.g., PNG or PDF) for distribution.
