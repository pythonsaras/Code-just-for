import PyPDF2
path="F:\\python\\random code\\a.pdf\\a.pdf"
pdReader=PyPDF2.PdfFileReader(open('a.pdf','rb'))
import pyttsx3

speaker=pyttsx3.init()

for page_num in range(pdReader.numPages):
    text=pdReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

speaker.save_to_file(text,'audio.mp3')
speaker.runAndWait()
