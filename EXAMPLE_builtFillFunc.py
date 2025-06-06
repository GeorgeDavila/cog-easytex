from pylatex import Document, Section, Subsection, Subsubsection, Command
from pylatex.utils import italic, NoEscape
from pylatex.section import Chapter, Paragraph, Subparagraph

def fill_document(doc):
	
	doc.append( NoEscape("hello") )
	
	with doc.create(Chapter("AAA")):
		with doc.create(Section("ab")):
			doc.append( NoEscape("bye") )
		with doc.create(Section("cd")):
			doc.append( NoEscape("0") )
			doc.append( NoEscape("1") )
			doc.append( NoEscape("2") )
			doc.append( NoEscape("3") )
	
	with doc.create(Chapter("BBB")):
		with doc.create(Section("ef")):
			doc.append( NoEscape("bye") )
			with doc.create(Subsection("gh")):
				doc.append( NoEscape("0") )
				with doc.create(Subsubsection("ij")):
					doc.append( NoEscape("11") )
			with doc.create(Subsection("kl")):
				doc.append( NoEscape("22") )