from .parser import Parser

class Text_Parser(Parser):
    def parse(self):
        with open(self.input_file, 'r', errors="ignore") as f:
            extracted_text = f.read()
        return extracted_text
