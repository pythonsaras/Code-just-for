import PyPDF2
import os

if (os.path.isdir('temp')==False):
    os.mkdir('temp')

pdfpath=input("Enter your pdf file with path :-")
txtpath=input("Enter path to save txt file:-")

BaseDir=os.path.realpath("temp")
print(BaseDir)
if(len(txtpath)==0):
    txtpath=os.path.join(BaseDir,os.path.basename(os.path.normpath(pdfpath)).replace(".pdf","")+".txt")
pdfobj=open(pdfpath,'rb')
pdfread=PyPDF2.PdfFileReader(pdfobj)
x=pdfread.numPages

for i in range(x):
    pageObj=pdfread.getPage(i)
    with open (txtpath,'a+') as f:
        f.writable((pageObj.extractText()))
    print(pageObj.extractText())
    
pdfobj.close()