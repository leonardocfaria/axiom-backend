from docling.document_converter import DocumentConverter

class PDFParser:
    def __init__(self):
        self.converter = DocumentConverter()
        return

    def parse_pdf(self, source):
        source = source
        res = self.converter.convert(source) 

        return(res.document.export_to_markdown())