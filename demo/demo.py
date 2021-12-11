import sys
sys.path.insert(0, "..//pythonpdf")

import pythonpdf
pythonpdf.merge(["example_pdf.pdf", "example_pdf.pdf"], "merge_result.pdf")
pythonpdf.extract("example_pdf.pdf", [3,5,7], "extract_result.pdf")
pythonpdf.split("example_pdf.pdf", 1, ["split_result1.pdf", "split_result2.pdf"])
pythonpdf.convert_png("example_png.png", "convert_png_result.pdf")