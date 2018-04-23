import sys
from cx_Freeze import setup, Executable

# -------
# Setup
# -------
packages = []
includes = ["PyQt5.QtWidgets", "PyQt5.QtGui", "os", "sqlite3", "pdfminer.pdfparser", "pdfminer.pdfinterp",
            "pdfminer.layout", "pdfminer.converter", "bs4", "re", "requests", "DataBase.py", "PDFParse.py",
            "WebScraping.py", "LaTeX.py", "queue", "idna.idnadata"]
excludes = []
base = None

if sys.platform == 'win32' : base = 'Win32GUI'

# exe にしたい python ファイルを指定
exe = Executable(script = 'main.py',
                 base = base)

# セットアップ
setup(name = 'PaperManager',
      version = '0.2.1',
      description = 'Help you manage journal papers',
      options = {"build_exe": {"includes":includes,
                               "excludes":excludes, "packages":packages}},
      executables = [exe])

