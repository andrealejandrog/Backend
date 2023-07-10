import pyttsx3
import pdfplumber as pp


engine = pyttsx3.init()

all_the_data = ''
with pp.open('40413_1_PrimerCapitulo_HabitosAtomicos.pdf') as book:
    for page_no, page in enumerate(book.pages, start=1):
        data = page.extract_text()
        all_the_data += data

engine.save_to_file(all_the_data, 'audio_book.mp3')
engine.runAndWait()
engine.stop()