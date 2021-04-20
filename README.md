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

### Create installer

```bash
python setup.py bdist_msi
```

### Create executable

```bash
python setup.py build
```
