from pdfminer.pdfparser import PDFParser
from pdfminer.pdfparser import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal

import re

class PDFAnalyze:

    def __init__(self, path):
        self.path = path

    def get_PDFLayout(self, p):

        fp = open(self.path, 'rb')
        try:
            parser = PDFParser(fp)
            document = PDFDocument()
            parser.set_document(document)

            document.set_parser(parser)
            rsrcmgr = PDFResourceManager()
            laparams = LAParams()
            device = PDFPageAggregator(rsrcmgr, laparams=laparams)
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            pages = list(document.get_pages())
            page_1 = pages[p]
            interpreter.process_page(page_1)
            layout = device.get_result()
        except :
            return -1
        fp.close()

        return layout






class PhysRev(PDFAnalyze):
    def __init__(self, path):
        super().__init__(path)



    def get_URL(self):
        layout = self.get_PDFLayout(0)
        for l in layout:
            if isinstance(l, LTTextBoxHorizontal):
                JournalInfo = re.search(r'DOI: \d+.\d+/\w+.\d+.\d+', l.get_text())

                if JournalInfo:
                    if 'PhysRevLett' in JournalInfo.group():
                        return 'https://journals.aps.org/prl/abstract/' + JournalInfo.group()[5:]

                    elif 'PhysRevB' in JournalInfo.group():
                        return 'https://journals.aps.org/prb/abstract/' + JournalInfo.group()[5:]


        return -1





class Nature(PDFAnalyze):
    def __init__(self, path):
        super().__init__(path)



    def get_URL(self):
        layout = self.get_PDFLayout(0)
        for l in layout:
            if isinstance(l, LTTextBoxHorizontal):
                JournalInfo = re.search(r'DOI: \d+.\d+/\w+\d+', l.get_text())
                if JournalInfo:
                    if 'NMAT' in JournalInfo.group():
                        return 'https://www.nature.com/articles/' + JournalInfo.group()[13:].lower()
                    elif 'ncomms' in JournalInfo.group():
                        return 'https://www.nature.com/articles/' + JournalInfo.group()[13:]
                    elif 'NPHYS' in JournalInfo.group():
                        return 'https://www.nature.com/articles/' + JournalInfo.group()[13:].lower()

                N_else = re.search(r'DOI: \d+.\d+/\w+.\d+.\d+', l.get_text())
                if N_else:
                    if 'NNANO' in N_else.group():
                        return 'https://www.nature.com/articles/' + N_else.group()[13:].lower()
                    elif 'NPHOTON' in N_else.group():
                        return 'https://www.nature.com/articles/' + N_else.group()[13:].lower()

        return -1





class JPSJ(PDFAnalyze):
    def __init__(self, path):
        super().__init__(path)



    def get_URL(self):
        layout = self.get_PDFLayout(0)
        for l in layout:
            if isinstance(l, LTTextBoxHorizontal):
                JournalInfo = re.search(r'DOI: \d+.\d+/\w+.\d+.\d+', l.get_text())
                if JournalInfo:
                    return 'http://journals.jps.jp/doi/abs/' + JournalInfo.group()[5:]

        return -1





class URL:
    def __init__(self, path):
        self.path = path



    def DecideJournal(self):
        return -1


    def get_URL(self):
        """
        Judge what is the journal name and get URL of the paper
        :return: URL of the paper.
        """
        return -1
