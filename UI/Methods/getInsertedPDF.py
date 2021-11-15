import os
import sys
import PyPDF2


def inserted(namelist):
    file = sys.argv[0]
    dirname = os.path.dirname(file)

    try:
        pdf_writer_even = PyPDF2.PdfFileWriter()
        pdf_writer_odd = PyPDF2.PdfFileWriter()
        flag = 0
        for name in namelist:
            pdf_document = dirname + f"/../Sources/{name}"
            try:
                pdf = PyPDF2.PdfFileReader(pdf_document)
                for page in range(pdf.getNumPages()):
                    current_page = pdf.getPage(page)
                    if page % 2 == 0:
                        pdf_writer_odd.addPage(current_page)
                    else:
                        pdf_writer_even.addPage(current_page)
                flag += 1
            except Exception as exception:
                print(f"{name} File is :")
                print("Exception: {}".format(type(exception).__name__))
                print("Exception message: {}".format(exception))

        # Output files for new PDFs
        output_filename_even = dirname + "/../Sources/even.pdf"
        output_filename_odd = dirname + "/../Sources/odd.pdf"

        # Get reach page and add it to corresponding
        # output file based on page number

        if flag:
            # Write the data to disk
            with open(output_filename_even, "wb") as out:
                pdf_writer_even.write(out)
                print("created", output_filename_even)

            # Write the data to disk
            with open(output_filename_odd, "wb") as out:
                pdf_writer_odd.write(out)
                print("created", output_filename_odd)
            return 1
        else:
            return 0

    except Exception as exception:
        print("Exception: {}".format(type(exception).__name__))
        print("Exception message: {}".format(exception))
