# merge-pdfs

Simple Python tool for merging PDF files on a local machine.

## Development

`pipenv` venv manager could be used to install all required dependencies for the project.

```bash
git clone git@github.com:lukaszKielar/merge-pdfs.git
cd merge-pdfs
python -m venv ./.venv
pipenv install --dev
```
## Building process

### pyinstaller

```bash
pyinstaller --noconsole --onefile --windowed --name MergePDFs .\merge_pdfs\gui\app.py
```

### cx freeze

```bash
# create installer
python setup.py bdist_msi

# create executable
python setup.py build
```
