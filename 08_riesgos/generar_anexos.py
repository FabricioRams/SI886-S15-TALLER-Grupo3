# 08_riesgos/generar_anexos.py
"""
Script para generar todos los anexos oficiales requeridos por la guía del taller (3-TALLER.md):
- anexo_A_registro_riesgos.xlsx
- anexo_B_mapa_calor.png
- anexo_C_plan_tratamiento.xlsx
- anexo_D_matriz_comunicacion.xlsx
- anexo_E_premortem.pdf
- anexo_F_aceptacion_residual.pdf
"""
import os
import shutil
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
ANEXOS_DIR = os.path.join(ROOT_DIR, "anexos")
os.makedirs(ANEXOS_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. ANEXO A: anexo_A_registro_riesgos.xlsx
# -------------------------------------------------------------
def generar_anexo_a():
    csv_path = os.path.join(BASE_DIR, "RG03_evaluado.csv")
    df = pd.read_csv(csv_path)
    
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Registro de Riesgos"
    
    # Title
    ws.merge_cells("A1:J1")
    title_cell = ws["A1"]
    title_cell.value = "ANEXO A — REGISTRO DE RIESGOS DE EJECUCIÓN DEL PETI (MUNICIPALIDAD DE ALTO SELVA)"
    title_cell.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    title_cell.fill = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
    title_cell.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 30
    
    # Subtitle info
    ws.merge_cells("A2:J2")
    sub_cell = ws["A2"]
    sub_cell.value = "Asignatura: SI-886 Planeamiento Estratégico de TI | Grupo 3 | Marco: ISO 31000:2018 & ISO/IEC 27005:2022"
    sub_cell.font = Font(name="Calibri", size=10, italic=True, color="333333")
    sub_cell.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[2].height = 20

    headers = [
        "ID", "Categoría", "Riesgo (Evento + Causa + Consecuencia)",
        "Objetivos o Proyectos Afectados", "Origen", "P", "I", "Valor (P×I)", "Nivel", "Justificación Técnica con Datos"
    ]
    ws.append([]) # row 3 blank
    ws.append(headers) # row 4
    ws.row_dimensions[4].height = 25
    
    header_fill = PatternFill(start_color="2F5597", end_color="2F5597", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    thin_border = Border(
        left=Side(style='thin', color='D9D9D9'),
        right=Side(style='thin', color='D9D9D9'),
        top=Side(style='thin', color='D9D9D9'),
        bottom=Side(style='thin', color='D9D9D9')
    )

    for col_num, h in enumerate(headers, 1):
        cell = ws.cell(row=4, column=col_num)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border

    # Level color mapping
    level_fills = {
        "Crítico": PatternFill(start_color="F8CBAD", end_color="F8CBAD", fill_type="solid"),
        "Alto": PatternFill(start_color="FFE699", end_color="FFE699", fill_type="solid"),
        "Medio": PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid"),
        "Bajo": PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid")
    }
    level_fonts = {
        "Crítico": Font(name="Calibri", size=10, bold=True, color="C00000"),
        "Alto": Font(name="Calibri", size=10, bold=True, color="B25900"),
        "Medio": Font(name="Calibri", size=10, bold=True, color="7F6000"),
        "Bajo": Font(name="Calibri", size=10, bold=True, color="375623")
    }

    # Data rows
    for r_idx, (_, row) in enumerate(df.iterrows()):
        cur_row = r_idx + 5
        ws.row_dimensions[cur_row].height = 45
        row_vals = [
            row["id"], row["Categoría"], row["Riesgo"], row["Objetivos o proyectos afectados"],
            row["Origen"], row["P"], row["I"], row["valor"], row["nivel"], row["Justificación"]
        ]
        ws.append(row_vals)
        for col_num, val in enumerate(row_vals, 1):
            cell = ws.cell(row=cur_row, column=col_num)
            cell.font = Font(name="Calibri", size=9.5)
            cell.border = thin_border
            cell.alignment = Alignment(vertical="center", wrap_text=True)
            if col_num in [1, 6, 7, 8]:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            if col_num == 9: # Nivel
                nivel = str(val).strip()
                cell.alignment = Alignment(horizontal="center", vertical="center")
                if nivel in level_fills:
                    cell.fill = level_fills[nivel]
                    cell.font = level_fonts[nivel]

    # Auto column widths
    col_widths = {1: 8, 2: 20, 3: 45, 4: 25, 5: 25, 6: 6, 7: 6, 8: 12, 9: 12, 10: 45}
    for col_idx, width in col_widths.items():
        ws.column_dimensions[get_column_letter(col_idx)].width = width

    out_file = os.path.join(ANEXOS_DIR, "anexo_A_registro_riesgos.xlsx")
    wb.save(out_file)
    print(f"[OK] Generado: {out_file}")

# -------------------------------------------------------------
# 2. ANEXO B: anexo_B_mapa_calor.png
# -------------------------------------------------------------
def generar_anexo_b():
    src = os.path.join(ROOT_DIR, "graficos", "RG_mapa_calor.png")
    dst = os.path.join(ANEXOS_DIR, "anexo_B_mapa_calor.png")
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"[OK] Generado: {dst}")
    else:
        print(f"[WARN] No se encontró {src}")

# -------------------------------------------------------------
# 3. ANEXO C: anexo_C_plan_tratamiento.xlsx
# -------------------------------------------------------------
def generar_anexo_c():
    csv_path = os.path.join(BASE_DIR, "RG04_tratamiento.csv")
    df = pd.read_csv(csv_path)
    df["Reduccion"] = df["Valor"] - df["Valor residual"]
    df["Reduccion_pct"] = (df["Reduccion"] / df["Valor"] * 100).round(1)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Plan de Tratamiento y Residual"

    # Title
    ws.merge_cells("A1:O1")
    title_cell = ws["A1"]
    title_cell.value = "ANEXO C — PLAN DE TRATAMIENTO Y EVALUACIÓN DE RIESGO RESIDUAL DEL PETI"
    title_cell.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    title_cell.fill = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
    title_cell.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 30

    ws.merge_cells("A2:O2")
    sub_cell = ws["A2"]
    sub_cell.value = "Criterio de Aceptación: ≤ 6 Aceptable | > 6 Requiere Aceptación Formal Firmada por Gerencia Municipal"
    sub_cell.font = Font(name="Calibri", size=10, italic=True, color="333333")
    sub_cell.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[2].height = 20

    headers = [
        "ID", "Valor Inicial", "Decisión", "Acciones Concretas de Tratamiento", "Responsable (Cargo)",
        "Plazo", "Costo", "P Residual", "I Residual", "Valor Residual", "Reducción", "% Reducción",
        "Señal Temprana Observable", "Umbral Cuantificable de Alerta", "¿Quién Acepta el Residual?"
    ]
    ws.append([]) # row 3 blank
    ws.append(headers) # row 4
    ws.row_dimensions[4].height = 25

    header_fill = PatternFill(start_color="2F5597", end_color="2F5597", fill_type="solid")
    header_font = Font(name="Calibri", size=10.5, bold=True, color="FFFFFF")
    thin_border = Border(
        left=Side(style='thin', color='D9D9D9'),
        right=Side(style='thin', color='D9D9D9'),
        top=Side(style='thin', color='D9D9D9'),
        bottom=Side(style='thin', color='D9D9D9')
    )

    for col_num in range(1, len(headers) + 1):
        cell = ws.cell(row=4, column=col_num)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border

    res_alert_fill = PatternFill(start_color="FFD9D9", end_color="FFD9D9", fill_type="solid")
    res_alert_font = Font(name="Calibri", size=10, bold=True, color="9C0006")

    for r_idx, (_, row) in enumerate(df.iterrows()):
        cur_row = r_idx + 5
        ws.row_dimensions[cur_row].height = 42
        row_vals = [
            row["id"], row["Valor"], row["Decisión"], row["Acciones concretas de tratamiento"],
            row["Responsable (cargo)"], row["Plazo"], row["Costo"], row["P residual"], row["I residual"],
            row["Valor residual"], row["Reduccion"], f"{row['Reduccion_pct']}%",
            row["Señal temprana"], row["Umbral de alerta"], row["¿Quién acepta el residual?"]
        ]
        ws.append(row_vals)
        for col_num, val in enumerate(row_vals, 1):
            cell = ws.cell(row=cur_row, column=col_num)
            cell.font = Font(name="Calibri", size=9)
            cell.border = thin_border
            cell.alignment = Alignment(vertical="center", wrap_text=True)
            if col_num in [1, 2, 8, 9, 10, 11, 12]:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            if col_num == 10 and int(row["Valor residual"]) > 6:
                cell.fill = res_alert_fill
                cell.font = res_alert_font

    col_widths = {1: 8, 2: 10, 3: 18, 4: 45, 5: 25, 6: 15, 7: 10, 8: 10, 9: 10, 10: 12, 11: 10, 12: 12, 13: 35, 14: 30, 15: 25}
    for col_idx, width in col_widths.items():
        ws.column_dimensions[get_column_letter(col_idx)].width = width

    out_file = os.path.join(ANEXOS_DIR, "anexo_C_plan_tratamiento.xlsx")
    wb.save(out_file)
    print(f"[OK] Generado: {out_file}")

# -------------------------------------------------------------
# 4. ANEXO D: anexo_D_matriz_comunicacion.xlsx
# -------------------------------------------------------------
def generar_anexo_d():
    csv_path = os.path.join(BASE_DIR, "RG06_comunicacion.csv")
    df = pd.read_csv(csv_path)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Matriz de Comunicación"

    ws.merge_cells("A1:H1")
    title_cell = ws["A1"]
    title_cell.value = "ANEXO D — MATRIZ DE COMUNICACIÓN DE RIESGOS DEL PETI (SECCIÓN 8.7)"
    title_cell.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    title_cell.fill = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
    title_cell.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 30

    ws.merge_cells("A2:H2")
    sub_cell = ws["A2"]
    sub_cell.value = "Comunicación de acciones para tratar el riesgo (8 columnas requeridas por el sílabo)"
    sub_cell.font = Font(name="Calibri", size=10, italic=True, color="333333")
    sub_cell.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[2].height = 20

    headers = [
        "ID del Riesgo", "Qué se Comunica", "A Quién (Cargo)", "Cuándo / Frecuencia",
        "Canal", "Quién Comunica", "Formato", "Qué Decisión Habilita"
    ]
    ws.append([]) # row 3 blank
    ws.append(headers) # row 4
    ws.row_dimensions[4].height = 25

    header_fill = PatternFill(start_color="2F5597", end_color="2F5597", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    thin_border = Border(
        left=Side(style='thin', color='D9D9D9'),
        right=Side(style='thin', color='D9D9D9'),
        top=Side(style='thin', color='D9D9D9'),
        bottom=Side(style='thin', color='D9D9D9')
    )

    for col_num in range(1, len(headers) + 1):
        cell = ws.cell(row=4, column=col_num)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border

    crit_fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

    for r_idx, (_, row) in enumerate(df.iterrows()):
        cur_row = r_idx + 5
        ws.row_dimensions[cur_row].height = 42
        row_vals = [
            row["id del riesgo"], row["Qué se comunica"], row["A quién (cargo)"], row["Cuándo / frecuencia"],
            row["Canal"], row["Quién comunica"], row["Formato"], row["Qué decisión habilita"]
        ]
        ws.append(row_vals)
        is_all_crit = "Todos" in str(row["id del riesgo"])
        for col_num, val in enumerate(row_vals, 1):
            cell = ws.cell(row=cur_row, column=col_num)
            cell.font = Font(name="Calibri", size=9.5, bold=is_all_crit)
            cell.border = thin_border
            cell.alignment = Alignment(vertical="center", wrap_text=True)
            if col_num == 1:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            if is_all_crit:
                cell.fill = crit_fill

    col_widths = {1: 15, 2: 38, 3: 28, 4: 25, 5: 20, 6: 28, 7: 25, 8: 35}
    for col_idx, width in col_widths.items():
        ws.column_dimensions[get_column_letter(col_idx)].width = width

    out_file = os.path.join(ANEXOS_DIR, "anexo_D_matriz_comunicacion.xlsx")
    wb.save(out_file)
    print(f"[OK] Generado: {out_file}")

# -------------------------------------------------------------
# 5. ANEXO E: anexo_E_premortem.pdf
# -------------------------------------------------------------
def generar_anexo_e():
    out_file = os.path.join(ANEXOS_DIR, "anexo_E_premortem.pdf")
    doc = SimpleDocTemplate(out_file, pagesize=letter, leftMargin=40, rightMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=18, textColor=colors.HexColor('#1F4E79'), spaceAfter=6, alignment=1)
    sub_style = ParagraphStyle('DocSub', parent=styles['Normal'], fontName='Helvetica', fontSize=10, textColor=colors.HexColor('#555555'), spaceAfter=15, alignment=1)
    h1_style = ParagraphStyle('H1', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=13, textColor=colors.HexColor('#2F5597'), spaceBefore=12, spaceAfter=6)
    body_style = ParagraphStyle('Body', parent=styles['Normal'], fontName='Helvetica', fontSize=9.5, leading=14, spaceAfter=8, textColor=colors.HexColor('#222222'))
    bullet_style = ParagraphStyle('Bullet', parent=body_style, leftIndent=15, firstLineIndent=-10)
    table_cell = ParagraphStyle('Cell', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11)
    table_cell_b = ParagraphStyle('CellB', parent=table_cell, fontName='Helvetica-Bold')

    story = []

    story.append(Paragraph("UNIVERSIDAD PRIVADA DE TACNA — FACULTAD DE INGENIERÍA", sub_style))
    story.append(Paragraph("ANEXO E — INFORME TÉCNICO DE LA DINÁMICA DE PRE-MORTEM", title_style))
    story.append(Paragraph("Plan Estratégico de Tecnologías de Información (PETI) · Municipalidad Distrital de Alto Selva<br/><b>Asignatura:</b> SI-886 Planeamiento Estratégico de TI | <b>Grupo 3</b> | Fecha: Noviembre 2026", sub_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1F4E79'), spaceBefore=2, spaceAfter=10))

    story.append(Paragraph("1. Metodología y Fundamento del Pre-Mortem", h1_style))
    story.append(Paragraph(
        "A diferencia del análisis de riesgos retrospectivo convencional o de la pregunta genérica <i>«¿qué puede salir mal?»</i> —la cual suele producir categorías abstractas difíciles de mitigar—, la técnica del <b>Pre-mortem</b> (Gary Klein, Harvard Business Review, 2007) opera mediante prospección retrospectiva: el equipo formula el ejercicio asumiendo que el PETI de la Municipalidad Distrital de Alto Selva <b>ha fracasado de manera catastrófica al cabo del Año 3</b>. A partir de esa certeza ficticia, se desglosan las causas causales, estructurales y organizacionales concretas que condujeron a dicho desenlace.",
        body_style
    ))

    story.append(Paragraph("2. Escenario Hipotético de Fracaso Proyectado (Año 3)", h1_style))
    story.append(Paragraph(
        "<i>«Estamos en noviembre de 2029 (cierre del Año 3 del PETI). La Municipalidad Distrital de Alto Selva no logró modernizar sus servicios digitales. La recaudación municipal cayó un 35 % tras un ataque de ransomware que paralizó Rentas y Catastro durante 10 días; los respaldos estaban incompletos, el disco externo del Jefe de TI no estaba cifrado y se perdieron 4 días de movimientos tributarios. Los funcionarios volvieron al papel. La Contraloría y la Secretaría de Gobierno Digital (PCM-SGTD) iniciaron procedimientos sancionadores por incumplimiento de directivas obligatorias y desprotección de datos personales. El Comité de TI nunca sesionó formalmente y el presupuesto del Año 2 fue recortado a la mitad sin que nadie defendiera el portafolio. El PETI es letra muerta.»</i>",
        body_style
    ))

    story.append(Paragraph("3. Mapeo Causal hacia las 9 Categorías Obligatorias de Riesgo", h1_style))
    
    prem_data = [
        [Paragraph("<b>Categoría</b>", table_cell_b), Paragraph("<b>Falla Detectada en Pre-Mortem</b>", table_cell_b), Paragraph("<b>Evidencia en Insumos / Caso</b>", table_cell_b), Paragraph("<b>Riesgo RG02</b>", table_cell_b)],
        [Paragraph("<b>Ejecución del plan</b>", table_cell), Paragraph("El plan se aprobó en papel y nadie hizo seguimiento continuo ni midió metas.", table_cell), Paragraph("9 riesgos de nov-2025 abiertos sin plan ni responsable operativo.", table_cell), Paragraph("R-01 (Valor 20)", table_cell_b)],
        [Paragraph("<b>Técnico</b>", table_cell), Paragraph("Ransomware o corrupción de datos sin capacidad de recuperación ante respaldos no probados.", table_cell), Paragraph("POL-TI-007 vencida; disco sin cifrar; 0 pruebas reales; BIA01 RPO 96h.", table_cell), Paragraph("R-02 (Valor 20)<br/>R-07 (Valor 12)", table_cell_b)],
        [Paragraph("<b>Normativo</b>", table_cell), Paragraph("Sanciones de PCM-SGTD, ANPD o Contraloría por desatención de mandatos legales.", table_cell), Paragraph("UA-17 nunca auditado; sin registro ante ANPD; directivas PCM sin plan.", table_cell), Paragraph("R-03 (Valor 16)<br/>R-12 (Valor 8)", table_cell_b)],
        [Paragraph("<b>Proveedor</b>", table_cell), Paragraph("El proveedor del sistema tributario interrumpió soporte o retuvo el código fuente.", table_cell), Paragraph("UA-15 y UA-16 sin auditoría; RG-02 abierto; dependencia sin SLA ni código.", table_cell), Paragraph("R-04 (Valor 16)", table_cell_b)],
        [Paragraph("<b>Patrocinio</b>", table_cell), Paragraph("Cambio de autoridades municipales; la nueva gestión desconoce el PETI.", table_cell), Paragraph("Sin Comité de Gobierno Digital; decisiones reactivas 'cuando se presenta'.", table_cell), Paragraph("R-05 (Valor 15)", table_cell_b)],
        [Paragraph("<b>Presupuestal</b>", table_cell), Paragraph("Recorte del PIM en Ola 2 o asfixia financiera por OPEX no controlado en nube.", table_cell), Paragraph("POL-TI-007 no actualizada por falta de presupuesto; UA-12 y UA-16 sin auditar.", table_cell), Paragraph("R-06 (Valor 16)<br/>R-13 (Valor 9)", table_cell_b)],
        [Paragraph("<b>Personal clave</b>", table_cell), Paragraph("El Jefe de TI renunció y nadie conocía las contraseñas ni la arquitectura interna.", table_cell), Paragraph("Factor bus = 1: concentra ejecución, custodia física y verificación.", table_cell), Paragraph("R-08 (Valor 12)", table_cell_b)],
        [Paragraph("<b>Capacidad ejecución</b>", table_cell), Paragraph("Sobrecarga de auditoría y personal operativo que impidió fiscalizar el plan.", table_cell), Paragraph("838 h-auditor/año para 17 entidades acumuladas (16 nunca auditadas).", table_cell), Paragraph("R-09 (Valor 12)", table_cell_b)],
        [Paragraph("<b>Resistencia cambio</b>", table_cell), Paragraph("Usuarios mantuvieron cuadernos paralelos al no entender ni validar los sistemas.", table_cell), Paragraph("Difusión pasiva ('se envió por correo'); BIA sin consulta a usuarios.", table_cell), Paragraph("R-10 (Valor 12)<br/>R-14 (Valor 6)", table_cell_b)],
        [Paragraph("<b>De alcance</b>", table_cell), Paragraph("Pedidos informales de funcionarios consumieron el tiempo del personal técnico.", table_cell), Paragraph("Falta de regla de admisión formal y comités de filtro.", table_cell), Paragraph("R-11 (Valor 9)", table_cell_b)]
    ]

    t = Table(prem_data, colWidths=[1.1*inch, 2.5*inch, 2.3*inch, 1.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2F5597')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#D9D9D9')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F9FAFB')])
    ]))
    story.append(t)
    story.append(Spacer(1, 10))

    story.append(Paragraph("4. Conclusión de la Dinámica", h1_style))
    story.append(Paragraph(
        "El pre-mortem confirmó que la vulnerabilidad de la municipalidad no residía en la sofisticación tecnológica, sino en la <b>debilidad del marco de gobierno, la concentración de tareas críticas en una sola persona (factor bus = 1) y la aceptación pasiva de riesgos sin plan de tratamiento</b>. Esto permitió formular tratamientos precisos con señales tempranas observables para cada uno de los 14 riesgos del PETI.",
        body_style
    ))

    doc.build(story)
    print(f"[OK] Generado: {out_file}")

# -------------------------------------------------------------
# 6. ANEXO F: anexo_F_aceptacion_residual.pdf
# -------------------------------------------------------------
def generar_anexo_f():
    out_file = os.path.join(ANEXOS_DIR, "anexo_F_aceptacion_residual.pdf")
    doc = SimpleDocTemplate(out_file, pagesize=letter, leftMargin=40, rightMargin=40, topMargin=35, bottomMargin=35)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=15, textColor=colors.HexColor('#1F4E79'), spaceAfter=4, alignment=1)
    sub_style = ParagraphStyle('DocSub', parent=styles['Normal'], fontName='Helvetica', fontSize=9, textColor=colors.HexColor('#555555'), spaceAfter=10, alignment=1)
    h1_style = ParagraphStyle('H1', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=11.5, textColor=colors.HexColor('#2F5597'), spaceBefore=8, spaceAfter=4)
    body_style = ParagraphStyle('Body', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=12, spaceAfter=6, textColor=colors.HexColor('#222222'))
    table_cell = ParagraphStyle('Cell', parent=styles['Normal'], fontName='Helvetica', fontSize=8, leading=10)
    table_cell_b = ParagraphStyle('CellB', parent=table_cell, fontName='Helvetica-Bold')

    story = []

    story.append(Paragraph("MUNICIPALIDAD DISTRITAL DE ALTO SELVA", sub_style))
    story.append(Paragraph("ANEXO F — ACTA FORMAL DE ACEPTACIÓN DE RIESGOS RESIDUALES DEL PETI", title_style))
    story.append(Paragraph("SECCIÓN 9 DEL PLAN ESTRATÉGICO DE TECNOLOGÍAS DE INFORMACIÓN (AÑO 1 – AÑO 3)<br/><b>Conforme a ISO 31000:2018 (Cláusula 6.5) y COBIT 2019 (EDM03 Ensured Risk Optimization)</b>", sub_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1F4E79'), spaceBefore=1, spaceAfter=8))

    story.append(Paragraph("1. Declaración de Contexto y Fundamentación", h1_style))
    story.append(Paragraph(
        "En cumplimiento de los criterios de gestión de riesgos fijados en el documento <code>08_riesgos/RG01_contexto.md</code>, todo riesgo cuyo <b>valor residual supere el umbral de aceptación (Valor Residual > 6)</b> no puede ser asumido por el equipo técnico formulador ni por la Jefatura de TI, requiriendo <b>conocimiento explícito y suscripción formal por parte de la Gerencia Municipal</b> previo a la aprobación formal del PETI institucional.",
        body_style
    ))

    story.append(Paragraph("2. Relación de Riesgos Residuales que Requieren Aceptación Formal", h1_style))

    headers = [
        Paragraph("<b>ID</b>", table_cell_b),
        Paragraph("<b>Riesgo de Ejecución del PETI</b>", table_cell_b),
        Paragraph("<b>V. Ini</b>", table_cell_b),
        Paragraph("<b>Tratamiento Aprobado</b>", table_cell_b),
        Paragraph("<b>V. Res</b>", table_cell_b),
        Paragraph("<b>Señal Temprana y Umbral</b>", table_cell_b),
        Paragraph("<b>Cargo Aceptante</b>", table_cell_b)
    ]

    table_data = [headers]
    rows = [
        ("R-01", "Falta de ejecución por ausencia de responsable y seguimiento", "20", "Designación por resolución del Líder GD y Comité trimestral", "8", "Comité sin sesionar / 1 trimestre sin sesión", "Gerencia Municipal"),
        ("R-02", "Ransomware/falla severa sobre respaldos no probados", "20", "POL-TI-007, nube cifrada inmutable, pruebas con acta y BCP", "8", "Prueba vencida / 1 trimestre sin acta", "Gerencia Municipal"),
        ("R-03", "Sanciones PCM-SGTD / ANPD por brecha normativa y UA-17", "16", "Registro ANPD (PR-05), plan PCM (PR-06) y auditar UA-17", "8", "Requerimiento PCM/ANPD / Retraso > 15 d", "Gerencia Municipal"),
        ("R-04", "Bloqueo por único proveedor sin código fuente ni SLA", "16", "Renegociación de contrato con SLA, código fuente y salida", "8", "Contrato sin cláusula / A 60 d de PR-02", "Gerencia Municipal"),
        ("R-06", "Recorte o reasignación del PIM en Año 2", "16", "Aprobación multianual PIA/PIM y cartera mínima contingente", "9", "Caída recaudación / Desviación > 10% PIM", "Gerencia Municipal"),
        ("R-05", "Pérdida de patrocinio directivo ante rotación institucional", "15", "Institucionalización en Comité y formalizar apetito", "8", "Inasistencia directiva / 2 sesiones ausente", "Gerencia Municipal"),
        ("R-09", "Capacidad de auditoría (838 h) insuficiente para 17 entidades", "12", "Plan Anual de Auditoría TI basado en riesgo y carga real", "8", "Desviación de horas / Avance < 75%", "Gerencia Municipal")
    ]

    for r in rows:
        table_data.append([
            Paragraph(f"<b>{r[0]}</b>", table_cell),
            Paragraph(r[1], table_cell),
            Paragraph(r[2], table_cell),
            Paragraph(r[3], table_cell),
            Paragraph(f"<b>{r[4]}</b>", table_cell),
            Paragraph(r[5], table_cell),
            Paragraph(r[6], table_cell)
        ])

    t = Table(table_data, colWidths=[0.5*inch, 2.0*inch, 0.45*inch, 1.8*inch, 0.45*inch, 1.2*inch, 0.9*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2F5597')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#D9D9D9')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F9FAFB')])
    ]))
    story.append(t)
    story.append(Spacer(1, 8))

    story.append(Paragraph("3. Declaración Expresa de Aceptación y Compromiso", h1_style))
    story.append(Paragraph(
        "<i>«En mi calidad de Gerente Municipal de la Municipalidad Distrital de Alto Selva, declaro haber tomado conocimiento de los 7 riesgos residuales precedentemente detallados, los cuales han sido evaluados y reducidos en un 50 % de su valor agregado inicial mediante el Plan de Tratamiento. Asimismo, acepto conscientemente dichos niveles de exposición residual bajo el compromiso de supervisar trimestralmente las señales tempranas y umbrales de alerta definidos, dotando los recursos requeridos para salvaguardar los objetivos estratégicos del PETI institucional.»</i>",
        body_style
    ))
    story.append(Spacer(1, 15))

    # Signatures Table
    sig_data = [
        [
            Paragraph("________________________________________<br/><b>GERENCIA MUNICIPAL</b><br/>Municipalidad Distrital de Alto Selva<br/>DNI: ____________________<br/>Fecha: _____ / _____ / 2026", table_cell),
            Paragraph("________________________________________<br/><b>JEFATURA DE TECNOLOGÍAS DE LA INFORMACIÓN</b><br/>Municipalidad Distrital de Alto Selva<br/>DNI: ____________________<br/>Fecha: _____ / _____ / 2026", table_cell)
        ],
        [
            Paragraph("<br/><br/>________________________________________<br/><b>LÍDER DE GOBIERNO DIGITAL / PETI</b><br/>Comité de Gobierno Digital<br/>DNI: ____________________<br/>Fecha: _____ / _____ / 2026", table_cell),
            Paragraph("<br/><br/>________________________________________<br/><b>EQUIPO FORMULADOR PETI (GRUPO 3)</b><br/>SI-886 Planeamiento Estratégico de TI<br/>Universidad Privada de Tacna<br/>Fecha: 19 / 11 / 2026", table_cell)
        ]
    ]
    st = Table(sig_data, colWidths=[3.6*inch, 3.6*inch])
    st.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10)
    ]))
    story.append(st)

    doc.build(story)
    print(f"[OK] Generado: {out_file}")

if __name__ == "__main__":
    print("Iniciando generacion de anexos...")
    generar_anexo_a()
    generar_anexo_b()
    generar_anexo_c()
    generar_anexo_d()
    generar_anexo_e()
    generar_anexo_f()
    print("Todos los anexos generados exitosamente en carpeta anexos/.")
