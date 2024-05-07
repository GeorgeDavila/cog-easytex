# Prediction interface for Cog ⚙️
# https://github.com/replicate/cog/blob/main/docs/python.md

from cog import BasePredictor, Input, Path
import os
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
            default="#CHAPTER A \n #SECTION B \n Lorem ipsum...",
            ),
        #userFile: Path = Input(
        #    description="Upload a tex file",
        #    ),
    ) -> str:
        """Run a single prediction on the model"""

        documentName = "generated"
        doc = Document(documentName)
        generate_document_from_string(doc, bodyInput)

        from builtFillFunc import fill_document
        fill_document(doc)

        doc.generate_pdf(clean_tex=False)
        doc.generate_tex()

        output_path = Path(f"{documentName}.pdf")
        return output_path
