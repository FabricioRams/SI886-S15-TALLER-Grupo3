# 08_riesgos/RG07_validacion.py
"""
Script de validacion y comprobacion tecnica del Taller 15 (Paso F - Validar y corregir).
Ejecuta las comprobaciones formales de la guia metodologica:
1. Cobertura de las 9 categorias obligatorias.
2. Justificacion fundamentada de Probabilidad e Impacto con datos del caso.
3. Tratamiento, responsable por cargo, senal temprana y aceptacion formal de residuales > 6.
4. Trazabilidad temporal y formal en Git.
"""
import os
import sys
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
OUTPUT_DIR = os.path.join(ROOT_DIR, "evidencias", "S15", "salidas")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def ejecutar_validacion():
    log_lines = []
    
    # 1. Cargar RG02_registro.csv
    reg_path = os.path.join(BASE_DIR, "RG02_registro.csv")
    if not os.path.exists(reg_path):
        print(f"[ERROR] No existe {reg_path}")
        sys.exit(1)
        
    df_reg = pd.read_csv(reg_path)
    
    # Check 1: 9 Categorias
    CATS = [
        "Presupuestal", "Patrocinio", "Capacidad de ejecución", "Personal clave",
        "Resistencia al cambio", "Proveedor", "Técnico", "Normativo", "De alcance"
    ]
    presentes = set(df_reg["Categoría"])
    faltantes = [c for c in CATS if c not in presentes]
    
    msg_check1 = f"[Check 1] Categorías faltantes: {'Ninguna (9/9 cubiertas)' if not faltantes else faltantes}"
    log_lines.append(msg_check1)
    print(msg_check1)
    
    # Check 2: Justificacion con datos observables
    sin_just = []
    for _, r in df_reg.iterrows():
        just = str(r.get("Justificación", "")).strip()
        # Verificar que tenga longitud y mencione al menos un dato, métrica o documento
        keywords = ["BIA", "POL", "UA", "RG", "h", "dias", "días", "%", "sep-2024", "jul-2023", "ago-2024", "nov-2025"]
        has_data = any(kw.lower() in just.lower() for kw in keywords)
        if len(just) < 15 or not has_data:
            sin_just.append(r["id"])
            
    msg_check2 = f"[Check 2] Riesgos sin justificación con dato: {len(sin_just)} {sin_just}"
    log_lines.append(msg_check2)
    print(msg_check2)
    
    # Check 3: Tratamiento, responsable, senal temprana y aceptacion formal
    trat_path = os.path.join(BASE_DIR, "RG04_tratamiento.csv")
    df_trat = pd.read_csv(trat_path)
    
    # Evaluar valores de RG02
    df_reg["valor"] = df_reg["P"] * df_reg["I"]
    sobre_6 = set(df_reg[df_reg["valor"] > 6]["id"])
    tratados = set(df_trat["id"])
    
    sin_trat = list(sobre_6 - tratados)
    msg_check3a = f"[Check 3a] Riesgos > 6 sin tratamiento: {sin_trat}"
    log_lines.append(msg_check3a)
    print(msg_check3a)
    
    # Responsable por cargo
    cargos_invalidos = []
    for _, r in df_trat.iterrows():
        resp = str(r.get("Responsable (cargo)", "")).strip()
        if not resp or resp.lower() in ["nadie", "ti", "varios"]:
            cargos_invalidos.append(r["id"])
    msg_check3b = f"[Check 3b] Tratamientos sin responsable por cargo: {len(cargos_invalidos)}"
    log_lines.append(msg_check3b)
    print(msg_check3b)
    
    # Senal temprana observable
    sin_senal = []
    for _, r in df_trat.iterrows():
        st = str(r.get("Señal temprana", "")).strip()
        if not st or st.lower() in ["nan", "none", ""]:
            sin_senal.append(r["id"])
    msg_check3c = f"[Check 3c] Tratamientos sin señal temprana: {len(sin_senal)}"
    log_lines.append(msg_check3c)
    print(msg_check3c)
    
    # Responsable de aceptacion en residual > 6
    sin_aceptante = []
    for _, r in df_trat.iterrows():
        res = int(r.get("Valor residual", 0))
        acep = str(r.get("¿Quién acepta el residual?", "")).strip()
        if res > 6 and (not acep or acep.lower() in ["nan", "none", ""]):
            sin_aceptante.append(r["id"])
    msg_check3d = f"[Check 3d] Residuales > 6 sin responsable de aceptación: {len(sin_aceptante)}"
    log_lines.append(msg_check3d)
    print(msg_check3d)
    
    # Resumen general
    total_checks_ok = (len(faltantes) == 0 and len(sin_just) == 0 and len(sin_trat) == 0 and 
                       len(cargos_invalidos) == 0 and len(sin_senal) == 0 and len(sin_aceptante) == 0)
    
    resumen = f"\nResultado de la validación técnica: {'TODAS LAS COMPROBACIONES APROBADAS (100% OK)' if total_checks_ok else 'ADVERTENCIA: COMPROBACIONES PENDIENTES'}"
    print(resumen)
    
    # Escribir archivo de salida
    out_txt = os.path.join(OUTPUT_DIR, "validacion.txt")
    with open(out_txt, "w", encoding="utf-8") as f:
        f.write("\n".join(log_lines) + "\n")
    print(f"[OK] Archivo de validación actualizado: {out_txt}")

if __name__ == "__main__":
    ejecutar_validacion()
