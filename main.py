def main():
    prompt_string = ("Choose the type of document you'd like to summarize.\n"
                     "Type 1 for plain text files.\n"
                     "Type 2 for Word documents (.doc or .docx).\n"
                     "Type 3 for PDF files.\n"
                     "Type 4 for images (.jpg or .png).\n"
                     "Type 5 for HTML websites.\n")

    print(prompt_string)
    choice = input("Enter your choice here: ")

    if choice == "1":
        file_path = input("Enter the relative path of the text file: ")
        from inputs.text_parser import Text_Parser
        my_parser = Text_Parser(file_path)
        parsed_text = my_parser.parse()

    elif choice == "2":
        file_path = input("Enter the relative path of the Word document: ")
        from inputs.docx_parser import Docx_Parser
        my_parser = Docx_Parser(file_path)
        parsed_text = my_parser.parse()

    elif choice == "3":
        file_path = input("Enter the relative path of the PDF file: ")
        from inputs.pdf_parser import Pdf_Parser
        my_parser = Pdf_Parser(file_path)
        parsed_text = my_parser.parse()

    elif choice == "4":
        file_path = input("Enter the relative path of the image file: ")
        from inputs.image_parser import Image_Parser
        my_parser = Image_Parser(file_path)
        parsed_text = my_parser.parse()

    elif choice == "5":
        url = input("Enter the URL of the website: ")
        from inputs.html_parser import Html_Parser
        my_parser = Html_Parser(url)
        parsed_text = my_parser.parse()

    else:
        print("That is not a valid choice. Exiting...")
        return

    from summarizer.summarizer import Summarizer
    my_summarizer = Summarizer(parsed_text)
    print("Below is a summary of the document:")
    print(my_summarizer.summarize())

if __name__ == "__main__":
    main()
