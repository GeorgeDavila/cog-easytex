from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape
from pylatex.section import Chapter, Paragraph, Subparagraph


def generate_document_from_string(doc, formattingString:str):
    """Add a section, a subsection and some text to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    """
    #formattingString is generally a multiline string
    
    #split into list of lines - for txt file input we can just use readlines()
    linesList = formattingString.splitlines() 
    print(linesList)

    #for i in range(len(linesList)):
    #    if linesList[i] == "":
    #        linesList = "\n"


    generatedLines = []
    for i in linesList:
        if "#CHAPTER" in i:
            title = i.replace("#CHAPTER", "")
            while (i[0] == " "):
                title = title[1:]
            
            createType = "Chapter"
            codeString = f"with doc.create({createType}({title})):"
            generatedLines.append(codeString)
            continue #format disallows something else being on same line
        if "#SECTION" in i:
            title = i.replace("#SECTION", "")
            while (i[0] == " "):
                title = title[1:]
            
            createType = "Section"
            codeString = f"with doc.create({createType}({title})):"
            generatedLines.append(codeString)
            continue #format disallows something else being on same line
        if "#SUBSECTION" in i:
            title = i.replace("#SUBSECTION", "")
            while (i[0] == " "):
                title = title[1:]
            
            createType = "Subsection"
            codeString = f"with doc.create({createType}({title})):"
            generatedLines.append(codeString)
            continue #format disallows something else being on same line
        if i == "":
            generatedLines.append("\n")

        codeString = f"\tdoc.append( NoEscape({title}) )"
        generatedLines.append(codeString)



    
    with doc.create(Section('A section')):
        doc.append(formattingString)

    with doc.create(Subsection('A subsection')):
        doc.append('Also some crazy characters: $&#{}')



test1 = '''
hello

bye 
'''

if __name__ == '__main__':
    # Basic document
    doc = Document('basic')
    generate_document_from_string(doc, test1)

    doc.generate_tex()