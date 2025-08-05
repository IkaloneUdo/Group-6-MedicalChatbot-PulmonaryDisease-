#Script to change Word/.docx file to .txt on google colab.

#Script to import file.
from google.colab import files
uploaded = files.upload()  # Select your .docx file.

#Script to install python-docx.
!pip install python-docx

#Script to change the format of the ducument.
from docx import Document

# Load the document
doc = Document('Pulmonary_Diseases.docx')

# Extract all text
text = "\n".join([paragraph.text for paragraph in doc.paragraphs])

# Save as .txt
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(text)

# Download the .txt file
files.download('output.txt')

