from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap5
from config import Config
from modules import PDFCountForm

# create an instance of Flask
app = Flask(__name__)

# create secret key
app.config.from_object(Config)

# create Bootstrap object (after Flask object)
bootstrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/', methods=('GET', 'POST'))
def home_page():
    form = PDFCountForm()
    if form.validate_on_submit():
        # Get the number of PDFs from the form
        pdf_count = form.pdf_count.data
        # Redirect to the upload page with the specified number of PDFs
        return redirect(f'/upload/{pdf_count}')
    return render_template('index.html', form=form)

@app.route('/upload/<int:pdf_count>')
def upload_page(pdf_count):
    form = PDFCountForm()
    return render_template('upload.html', form=form, pdf_count=pdf_count)