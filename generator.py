from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape




def generate_document(doc, inputString):
    """Add a section, a subsection and some text to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    """
    text2type = str(text2type)
    
    with doc.create(Section('A section')):
        doc.append(text2type)
        #doc.append(italic(text2type))

        #with doc.create(Subsection('A subsection')):
        #    doc.append('Also some crazy characters: $&#{}')