# merge-pdfs

Simple Python tool for merging PDF files on a local machine.

## Development

`pipenv` venv manager could be used to install all required dependencies for the project.

```bash
git clone git@github.com:lukaszKielar/merge-pdfs.git
cd merge-pdfs

python -m venv ./.venv

# adding --pre due to black version https://github.com/microsoft/vscode-python/issues/5171
pipenv install --pre
```
## Building process

```bash
pyinstaller --noconsole --onefile --windowed --name MergePDFs .\merge_pdfs\gui\app.py
```
