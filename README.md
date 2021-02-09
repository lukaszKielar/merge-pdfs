# merge-pdfs

Tool for merging PDF files without sending them over the Network.

## Installation

### From source

```
git clone https://github.com/lukaszKielar/merge-pdfs.git
cd merge-pdfs
```

### Create virtual environment

#### Windows

```
virtualenv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

#### Linux

Linux users have to install `python3-dev` in order to build the tool.

```
sudo apt-get install python3.6-dev
virtualenv -p python3.6 venv
source ./venv/bin/activate
pip install -r requirements.txt
```

### Build tool

```
pyinstaller --onefile --windowed merge_pdfs.py
```

## Development

### Environment setup

I'm using `pipenv` venv manager. In order to create proper env simply type

```bash
# adding --pre due to black version https://github.com/microsoft/vscode-python/issues/5171
$ pipenv install --pre
```
