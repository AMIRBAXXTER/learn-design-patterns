from abc import ABC, abstractmethod
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from openpyxl import Workbook
import random


# Abstract Factory
class ReportFactory(ABC):
    @abstractmethod
    def create_header(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def create_chart(self):
        pass


# Concrete Factory for PDF
class PDFReportFactory(ReportFactory):
    def create_header(self):
        return PDFReportHeader()

    def create_table(self):
        return PDFReportTable()

    def create_chart(self):
        return PDFReportChart()


# Concrete Factory for Excel
class ExcelReportFactory(ReportFactory):
    def create_header(self):
        return ExcelReportHeader()

    def create_table(self):
        return ExcelReportTable()

    def create_chart(self):
        return ExcelReportChart()


# Abstract Product for Header
class ReportHeader(ABC):
    @abstractmethod
    def render(self, doc, title):
        pass


# Abstract Product for Table
class ReportTable(ABC):
    @abstractmethod
    def render(self, doc, data):
        pass


# Abstract Product for Chart
class ReportChart(ABC):
    @abstractmethod
    def render(self, doc, data):
        pass


# Concrete Product for PDF Header
class PDFReportHeader(ReportHeader):
    def render(self, doc: canvas.Canvas, title):
        doc.setFont("Helvetica-Bold", 16)
        doc.drawString(30, 750, title)


# Concrete Product for PDF Table
class PDFReportTable(ReportTable):
    def render(self, doc: canvas.Canvas, data):
        doc.setFont("Helvetica", 12)
        x = 30
        y = 720
        for row, (item, value) in enumerate(data, 1):

            doc.drawString(x, y, f"{item}:    {value}")
            y -= 20

            if row % 34 == 0:
                x += 90
                y = 720

            if row % (6 * 34) == 0:
                doc.showPage()
                x = 30
                y = 720


# Concrete Product for PDF Chart
class PDFReportChart(ReportChart):
    def render(self, doc: canvas.Canvas, data):
        x_start, y_start = 30, 720 - (len(data) % 34 * 20) if abs(len(data) - 204) < 34 else 70
        x_end, y_end = 30 + 550, y_start
        doc.line(x_start, y_start - 20, x_end, y_end - 20)
        doc.drawString(30, y_start - 35, "This is a simple line chart")


# Concrete Product for Excel Header
class ExcelReportHeader(ReportHeader):
    def render(self, doc: Workbook, title):
        sheet = doc.active
        sheet.append([title])


# Concrete Product for Excel Table
class ExcelReportTable(ReportTable):
    def render(self, doc: Workbook, data):
        sheet = doc.active
        for item, value in data:
            sheet.append([item, value])


# Concrete Product for Excel Chart
class ExcelReportChart(ReportChart):
    def render(self, doc: Workbook, data):
        sheet = doc.active
        sheet.append([])
        sheet.append(["Simple line chart would go here"])


# Client code
def client_code(factory: ReportFactory, filename: str, data: list):
    title = "Company Report"

    header = factory.create_header()
    table = factory.create_table()
    chart = factory.create_chart()

    if isinstance(factory, PDFReportFactory):
        doc = canvas.Canvas(filename, pagesize=letter)
        header.render(doc, title)
        table.render(doc, data)
        chart.render(doc, data)
        doc.save()

    elif isinstance(factory, ExcelReportFactory):
        doc = Workbook()
        header.render(doc, title)
        table.render(doc, data)
        chart.render(doc, data)
        doc.save(filename)


def main(data):
    client_code(PDFReportFactory(), "company_report.pdf", data)
    client_code(ExcelReportFactory(), "company_report.xlsx", data)


if __name__ == "__main__":
    data = [(f"Item {i + 1}", random.randint(1, 100)) for i in range(310)]
    main(data)
