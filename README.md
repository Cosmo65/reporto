# Reporto

Reporto is a python library capable of generating PDF reports from `Jinja2` templates using [Prince](https://www.princexml.com/) as the conversor HTML->PDF.

## Requirements

- `requirements.txt`
- [`Prince`](https://www.princexml.com/download/) (free license for non-commercial use).

## Usage

If you want to generate a report and save it to the filesystem:

```python
from reporto.core import PdfReport

report = PdfReport("test.tmpl")
report.render(output_filename="test.pdf", name="Steve")
```

If you want to return a `HttpResponse` within a `django` application:

> views.py

```python
from reporto.core import PdfReport
from django.http import HttpResponse


def index(request):
    report = PdfReport("test.tmpl", HttpResponse)
    report.render(name="Steve")
    return report.http_response()
```
