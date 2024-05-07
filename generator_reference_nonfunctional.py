from pylatex import Document, Section, Subsection, Subsubsection, Command
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
    sectionLevel = 0

    #we use sectionLevel to control indentation level per pylatex structure 
    for i in linesList:
        if "#CHAPTER" in i:
            sectionLevel = 1
            title = i.replace("#CHAPTER", "")
            while (title[0] == " "):
                title = title[1:]
            
            createType = "Chapter"
            codeString = f"with doc.create({createType}(\"{title}\")):"
            generatedLines.append(codeString)
            continue #format disallows something else being on same line
        if "#SECTION" in i:
            sectionLevel = 2
            title = i.replace("#SECTION", "")
            while (title[0] == " "):
                title = title[1:]
            
            createType = "Section"
            codeString = f"with doc.create({createType}(\"{title}\")):"
            generatedLines.append(codeString)
            continue #format disallows something else being on same line
        if "#SUBSECTION" in i:
            sectionLevel = 3
            title = i.replace("#SUBSECTION", "")
            while (title[0] == " "):
                title = title[1:]
            
            createType = "Subsection"
            codeString = f"with doc.create({createType}(\"{title}\")):"
            generatedLines.append(codeString)
            continue #format disallows something else being on same line
        if "#SUBSUBSECTION" in i:
            sectionLevel = 4
            title = i.replace("#SUBSUBSECTION", "")
            while (title[0] == " "):
                title = title[1:]
            
            createType = "Subsubsection"
            codeString = f"with doc.create({createType}(\"{title}\")):"
            generatedLines.append(codeString)
            continue #format disallows something else being on same line
        if i == "":
            generatedLines.append("") #keep empty lines as empty strings
            continue

        tabIndentationLevel = "\t"*sectionLevel
        codeString = f"{tabIndentationLevel}doc.append( NoEscape(\"{i}\") )"
        generatedLines.append(codeString)

    generatedCodeString = "\n".join(generatedLines)
    print(generatedCodeString)

    
    return eval(generatedCodeString)



test1 = '''
hello

#SECTION ab
bye
#SECTION cd
0
1
2
3

#SECTION ef
bye
#SUBSECTION gh
0
#SUBSUBSECTION ij
11
#SUBSECTION kl
22
'''

if __name__ == '__main__':
    # Basic document
    doc = Document('basic')
    generate_document_from_string(doc, test1)

    doc.generate_tex()