if __name__ == '__main__':
    import WebSCraping
    import PDFParse

    a = PDFParse.PhysRev('C:/Users/yudai/Dropbox/takahashi_lab/paper/Cu2OSeO3/PhysRevB.85.220406.pdf').get_URL()
    print(WebSCraping.Scraper(a).get_title())