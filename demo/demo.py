import sys
sys.path.insert(0, ".//pythonpdf")

import pythonpdf
pythonpdf.merge(["example.pdf", "example.pdf"], "merge_result.pdf")
pythonpdf.extract("example.pdf", [3,5,7], "extract_result.pdf")
