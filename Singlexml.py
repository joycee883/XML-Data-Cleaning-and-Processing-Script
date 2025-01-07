import xml.etree.ElementTree as ET
import re
from bs4 import BeautifulSoup

# Specify the full path to the XML file
xml_file_path = r"C:\Users\91939\Desktop\AI&DS\Data science projects\XML scrapping\xml_single articles\769952.xml"

# Parse the XML file directly using the specified path
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Convert the XML to string format
xml_string = ET.tostring(root, encoding='utf8').decode('utf8')

# Function to strip HTML tags using BeautifulSoup with XML parser
def strip_html(text):
    soup = BeautifulSoup(text, "xml")  # Specify XML parser
    return soup.get_text()

# Function to remove text between square brackets
def remove_between_square_brackets(text):
    return re.sub(r'\[[^]]*\]', '', text)

# Denoising function to clean up the text
def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    return text

# Apply denoising to the XML string content
sample = denoise_text(xml_string)

# Save output to a file with UTF-8 encoding
output_path = r"C:\Users\91939\Desktop\AI&DS\Data science projects\XML scrapping\singlexmlcleaned_output.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(sample)

print("The cleaned XML content has been saved to:", output_path)

