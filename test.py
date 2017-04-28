from core import PdfReport

report = PdfReport("test.tmpl")
report.render(output_filename="pepe.pdf", name="Steve")
