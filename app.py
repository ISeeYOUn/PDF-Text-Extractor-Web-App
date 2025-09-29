from flask import Flask, render_template, request
from PyPDF2 import PdfReader

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        pdf_reader = PdfReader(file)
        num_pages = len(pdf_reader.pages)
        text = ""

        for page in range(num_pages):
            pdf_page = pdf_reader.pages[page]
            text += pdf_page.extract_text()

        return render_template('result.html', text=text)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
