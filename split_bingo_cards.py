import PyPDF2
import os

input_file = "bingocards.pdf"
output_path = "./individual_cards/"
if not os.path.isdir(output_path):
	os.mkdir(output_path)

pdf = PyPDF2.PdfFileReader(input_file)											# Instantiate a PdfFileReader object using the input_file
num_pages = pdf.getNumPages()													# How many pages are there?

for i in range(num_pages):
	page = pdf.getPage(i)														# Grab the next page in the loop
	output = PyPDF2.PdfFileWriter()												# Instantiate a PdfFileWriter object
	output.addPage(page)														# Add the single page to the PdfFileWriter object
	outputStream = open(output_path + "bingocard_{}.pdf".format(i+1), "wb")		# Open an output stream to write a single page to
	output.write(outputStream)													# Write to the pdf
	outputStream.close()														# Close it
