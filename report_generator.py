from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os

def generate_report(target, results, output_file):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report.html')
    html_out = template.render(target=target, results=results)

    os.makedirs('reports', exist_ok=True)
    output_path = os.path.join('reports', output_file)
    HTML(string=html_out).write_pdf(output_path)
