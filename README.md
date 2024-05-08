# cog-easytex

replicate api for easily generating tex documents - live at https://replicate.com/georgedavila/cog-easytex

Love the look of TeX but hat working with it? So do I. This api is intended to be an easy way to generate TeX documents and pdfs using nothing but plain text. You don't need anything more than notepad to generate cleanly formatted written reports. Not intended for advanced uses, not inclusive of most features of tex but it will output both a pdf document and a TeX document if you want to edit it further. 

Yes there's this or that program, X Y and Z online platform and whatnot but you shouldn't have to compile tex or download bulky unoptimized programs just to generate a pdf. This is an easy straightforward solution. Write something in notepad, copy and paste into the api wait a few seconds and you have a well-formatted report. 


## how it works
Take the very hackish approach of rewriting the document fill function code itself be rewriting file `builtFillFunc.py`. (Simple eval of the code string currently producing errors so we go with this approach). 

### References 
https://github.com/hygull/pylatex/tree/master - examples
https://github.com/JelteF/PyLaTeX/issues/261#issuecomment-499619565 - require these extra packages to built chapters