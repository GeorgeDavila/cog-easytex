# Prediction interface for Cog ⚙️
# https://github.com/replicate/cog/blob/main/docs/python.md

from cog import BasePredictor, Input, Path
import os
import shutil
from zipfile import ZipFile
from pylatex import Document, Section, Subsection, Subsubsection, Command
from pylatex.utils import italic, NoEscape
from pylatex.section import Chapter, Paragraph, Subparagraph

from generator import *

def zipOutputDirectory(path2zipInput, zipOutName):
    # Create object of ZipFile
    with ZipFile(zipOutName, 'w') as zip_object:
        # Traverse all files in directory
        for folder_name, sub_folders, file_names in os.walk(path2zipInput):
            for filename in file_names:
                # Create filepath of files in directory
                file_path = os.path.join(folder_name, filename)
                # Add files to zip file
                zip_object.write(file_path, os.path.basename(file_path))

    if os.path.exists(zipOutName):
        print("ZIP file created")
    else:
        print("ZIP file not created")

class Predictor(BasePredictor):
    def setup(self) -> None:
        pass

    def predict(
        self,
        bodyInput: str = Input(
            description="Text", 
            default="#SECTION A \n Hello \n #SUBSECTION B \n Lorem ipsum...",
            ),
        #userFile: Path = Input(
        #    description="Upload a tex file",
        #    ),
    ) -> Path:
        """Run a single prediction on the model"""

        documentName = "generated"
        outputDirectory = "outputs"
        zipOutName = "outputs.zip"

        doc = Document(documentName)
        generate_document_from_string(doc, bodyInput)

        from builtFillFunc import fill_document
        fill_document(doc)

        doc.generate_pdf(clean_tex=False)
        doc.generate_tex()

        #shutil.move(f"{documentName}.tex", f"{outputDirectory}/{documentName}.tex")
        #shutil.move(f"{documentName}.pdf", f"{outputDirectory}/{documentName}.pdf")

        #zipOutputDirectory(outputDirectory, zipOutName)

        output_paths = Path(f"{documentName}.pdf") #, Path(f"{documentName}.tex")
        return output_paths
