from .parser import Parser
import bs4
import urllib.request
import re

class Html_Parser(Parser):
    def is_tag_visible(self, html_element):
        if html_element.parent.name in ['meta', 'title', 'head', 'style', 'script', '[document]']:
            return False

        if isinstance(html_element, bs4.element.Comment):
            return False

        if re.match(r"[\s\r\n]+", str(html_element)):
            return False
        return True

    def extract_text_from_html(self, html):
        soup = bs4.BeautifulSoup(html, 'html.parser')

        all_texts = soup.findAll(text=True)

        visible_texts = filter(self.is_tag_visible, all_texts)

        joined_texts = u" ".join(t.strip() for t in visible_texts)
        return joined_texts

    def parse(self):
        html = urllib.request.urlopen(self.input_file).read()
        extracted_text = self.extract_text_from_html(html)
        return extracted_text
