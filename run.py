import argparse
import cv2
import logging
import easygui as eg
from pathlib import Path
from typing import List
import easygui
from pathlib import Path


def cleanup_data(file_path: Path) -> List[str]:
    with file_path.open() as f:
        list_of_names = [line.strip() for line in f]
    return list_of_names
from datetime import datetime

def generate_certificates(names: List[str], template_path: Path, output_dir: Path) -> None:
    for index, name in enumerate(names):
        try:
            certificate_template_image = cv2.imread(str(template_path))
            cv2.putText(certificate_template_image, name, (2628, 2010), cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 0), 5, cv2.LINE_AA)
            
            # Get current date
            current_date = datetime.now().strftime('%Y-%m-%d')
            # Add the date to the certificate
            cv2.putText(certificate_template_image, current_date, (3981,3279), cv2.FONT_HERSHEY_COMPLEX, 5, (0, 0, 0), 5, cv2.LINE_AA)
            
            output_path = output_dir / f"{name.replace(' ', '_')}.jpg"
            cv2.imwrite(str(output_path), certificate_template_image)
            logging.info(f"Processing {index + 1} / {len(names)}")
        except Exception as e:
            logging.error(f"Failed to process {name}: {e}")


def main():
    # Set up some styles
    eg.msgbox("Welcome to the Certificate Generator!\nCreated by Mrinmay Nath", "Welcome")

    # Ask user for input type
    input_type = eg.buttonbox("Choose how you want to input the names:", "Input Type", ["Single Name", "Multiple Names"])

    # Handle user choice
    if input_type == "Single Name":
        name = eg.enterbox("Enter the name you want to generate a certificate for:", "Enter Name")
        names = [name]  # Just a list of names, not tuples
    else:
        names_file = eg.fileopenbox("Select your names file. The file should be a .txt file with one name per line.", "Select Names File", default='*.txt')
        # Read names and texts from file
        names = cleanup_data(Path(names_file))

    # Get user input once
    template_path = eg.fileopenbox("Select your certificate template. The template should be a .jpg file.", "Select Template", default='*.jpg')
    output_dir = eg.diropenbox("Select the directory where you want to save the generated certificates.", "Select Output Directory")

    # Call generate_certificate once for each name
    for name in names:  # Iterate over each name in the list
        filename = f"{name.replace(' ', '_')}"  # Use the name as the filename, replacing spaces with underscores
        generate_certificates([filename], Path(template_path), Path(output_dir))

    # Wait for user input before closing
    eg.msgbox("All certificates have been generated! Press OK to close.", "Finished")

if __name__ == "__main__":
    main()