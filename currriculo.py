from fpdf import FPDF
import os

# Corrige os caracteres incompatíveis com a codificação 'latin1'
def limpar_texto(texto):
    return texto.replace("–", "-").replace("—", "-")

# Aplicar a limpeza nos textos
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, limpar_texto('Currículooooo - Nome Completo'), ln=True, align='C')
        self.ln(5)

    def section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_text_color(30, 30, 30)
        self.cell(0, 10, limpar_texto(title), ln=True)
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', '', 11)

    def section_body(self, body):
        self.multi_cell(0, 8, limpar_texto(body))
        self.ln()

# Cria o PDF
pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font('Arial', '', 11)

pdf.section_title('Contato')
pdf.section_body("Cidade - Estado\n(00) 91234-5678\nseuemail@exemplo.com\nLinkedIn ou GitHub (opcional)")

pdf.section_title('Formação Acadêmica')
pdf.section_body("Curso de Análise e Desenvolvimento de Sistemas\n[Nome da Faculdade] - [Cidade/Estado]\nPrevisão de conclusão: [Ano]\nCursando atualmente o [Xº] semestre")

pdf.section_title('Habilidades')
pdf.section_body("- Lógica de Programação (Python, JavaScript)\n- Banco de Dados (SQLite, MySQL)\n- HTML, CSS, JavaScript\n- Git e GitHub\n- Boa comunicação e trabalho em equipe\n- Facilidade com aprendizado prático")

pdf.section_title('Experiência Profissional (se houver)')
pdf.section_body("[Cargo anterior] - [Empresa, Cidade]\nAno de início - Ano de saída\nResumo breve do que fazia, mesmo que fora da área de TI")

pdf.section_title('Projetos Acadêmicos ou Pessoais')
pdf.section_body("- Mini Sistema de Cadastro (Python + SQLite)\n  Desenvolvido como exercício prático de CRUD com interface CLI.\n- Página Estática com HTML/CSS\n  Criação de um portfólio pessoal usando HTML e estilização com CSS.")

pdf.section_title('Objetivo')
pdf.section_body("Busco uma oportunidade de estágio em Tecnologia da Informação para aplicar e desenvolver meus conhecimentos em programação, banco de dados e desenvolvimento de sistemas, com foco em aprendizado prático e crescimento na área.")

pdf.section_title('Observações Finais')
pdf.section_body("Disponibilidade: manhã/tarde/noite\nFlexível quanto à modalidade: presencial, híbrido ou remoto")

# Exporta o PDF
pdf_path = os.path.join(os.path.dirname(__file__), "Curriculo_Estagiario_40_anos.pdf")
pdf.output(pdf_path)

print(f"PDF gerado com sucesso: {pdf_path}")
