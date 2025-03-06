from abc import ABC, abstractmethod


# Product
class Report:
    def __init__(self):
        self.title = None
        self.introduction = None
        self.sections = []
        self.conclusion = None
        self.attachments = []

    def __str__(self):
        report_str = f"Title: {self.title}\n"
        report_str += f"Introduction: {self.introduction}\n"
        report_str += "Sections:\n"
        for i, section in enumerate(self.sections):
            report_str += f"  {i + 1}. {section}\n"
        report_str += f"Conclusion: {self.conclusion}\n"
        report_str += f"Attachments: {', '.join(self.attachments)}\n"
        return report_str


# Abstract Builder
class ReportBuilder(ABC):
    def __init__(self):
        self.report = Report()

    @abstractmethod
    def set_title(self, title):
        pass

    @abstractmethod
    def set_introduction(self, introduction):
        pass

    @abstractmethod
    def add_section(self, section):
        pass

    @abstractmethod
    def set_conclusion(self, conclusion):
        pass

    @abstractmethod
    def add_attachment(self, attachment):
        pass

    def get_report(self):
        return self.report


# Concrete Builder
class FinancialReportBuilder(ReportBuilder):
    def set_title(self, title):
        self.report.title = title
        return self

    def set_introduction(self, introduction):
        self.report.introduction = introduction
        return self

    def add_section(self, section):
        self.report.sections.append(section)
        return self

    def set_conclusion(self, conclusion):
        self.report.conclusion = conclusion
        return self

    def add_attachment(self, attachment):
        self.report.attachments.append(attachment)
        return self


# Director
class ReportDirector:
    def __init__(self, builder: ReportBuilder):
        self.builder = builder

    def construct_financial_report(self, title, introduction, sections, conclusion,
                                   attachments):
        self.builder.set_title(title).set_introduction(introduction)
        for section in sections:
            self.builder.add_section(section)
        self.builder.set_conclusion(conclusion)
        for attachment in attachments:
            self.builder.add_attachment(attachment)

    def construct_summary_report(self, title, introduction, sections, conclusion):
        self.builder.set_title(title).set_introduction(introduction)
        for section in sections:
            self.builder.add_section(section)
        self.builder.set_conclusion(conclusion)


# Client Code
def client_code():
    builder = FinancialReportBuilder()
    director = ReportDirector(builder)

    sections = [
        "Revenue Analysis",
        "Expense Analysis",
        "Profit and Loss Statement",
        "Cash Flow Statement"
    ]
    attachments = ["Financial Data.xlsx", "Audit Report.pdf"]

    director.construct_financial_report(
        title="Annual Financial Report",
        introduction="This report provides an overview of the company's financial performance in the past year.",
        sections=sections,
        conclusion="The company showed significant growth in revenue and maintained a healthy financial position.",
        attachments=attachments)

    report = builder.get_report()
    print(report)


if __name__ == "__main__":
    client_code()
