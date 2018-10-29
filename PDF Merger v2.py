
# coding: utf-8

import os, PyPDF2, sys

def PDF_merge(pdfs,output):
    

    pdf_merger= PyPDF2.PdfFileMerger()

    for pdf in pdfs:
        if pdf.endswith('.pdf'):
            pdf_merger.append(pdf)
        else:
            continue

    with open(output,'wb') as f:
        pdf_merger.write(f)
        

def main(): 
    
    os.chdir(sys.path[0])
    
    # pdf files to merge 
    pdfs = sorted(os.listdir())
     
    # output pdf file name 
    output  = 'output.pdf'
      
    # calling pdf merge function 
    PDF_merge(pdfs = pdfs, output = output)
  
if __name__ == "__main__": 
    # calling the main function 
    main() 

