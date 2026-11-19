# SI-886 Planeamiento Estratégico de TI — Taller Semana 15
## Registro de Riesgos del Plan y Matriz de Comunicación

**Universidad Privada de Tacna**  
**Facultad de Ingeniería — Escuela Profesional de Ingeniería de Sistemas**  
**Docente:** Dr. Oscar Juan Jimenez Flores  
**Organización asignada:** Empresa 03 — Municipalidad Distrital de Alto Selva  
**Equipo:** Grupo 3

---

### Integrantes del Grupo 3

| N.º | Apellidos y Nombres | Código de Estudiante | Rol en el Taller |
|---|---|---|---|
| 1 | RAMOS ATAHUACHI FABRICIO FARID EDMILSON | 2023076798 | Coordinador / Contexto y criterios (`RG01`) |
| 2 | COLQUE QUISPE RODRIGO SÍDNEY | 2023077078 | Identificación y evaluación (`RG02` / `RG03`) |
| 3 | AROCUTIPA AROCUTIPA GIAN FRANCO | 2023076790 | Tratamiento y residual (`RG04` / `RG05`) |
| 4 | PEREZ PERALTA FABRIZIO SALVADOR ELIAS | 2023077476 | Comunicación, Sección 8 y SimpleRisk (`RG06`) |

---

## 📌 Resumen del Trabajo Desarrollado

Este repositorio contiene la formulación completa de la **Sección 8 (Gestión de Riesgos del Plan)** y la **Matriz de Comunicación** para el Plan Estratégico de Tecnologías de Información (PETI Año 1 – Año 3) de la **Municipalidad Distrital de Alto Selva**, bajo los estándares **ISO 31000:2018**, **ISO/IEC 27005:2022** y **COBIT 2019 (APO12 / EDM03)**.

### Principales Resultados:
1. **Contexto y Criterios Previos:** Definidos en `08_riesgos/RG01_contexto.md` con fecha de acuerdo anterior a la evaluación (verificable en `git log` commit `c2ab4b0`).
2. **Registro Exhaustivo:** 14 riesgos identificados (`R-01` a `R-14`) cubriendo **las 9 categorías obligatorias** sin omitir ninguna, redactados como *evento + causa + consecuencia* y trazados a los objetivos (`OD-01` a `OD-05`) y proyectos (`PR-01` a `PR-10`).
3. **Evaluación Cuantitativa y Mapa de Calor:** 6 riesgos Críticos (≥ 15), 4 Altos (12–14), 3 Medios (7–11) y 1 Bajo (≤ 6). Generación automatizada del mapa de calor `5 × 5` en `graficos/RG_mapa_calor.png`.
4. **Plan de Tratamiento y Reducción Residual:** Tratamiento asignado a los 13 riesgos con valor `> 6`, reduciendo el valor acumulado de 177 a 88 puntos (**50 % de reducción**). Los 7 riesgos residuales `> 6` cuentan con responsable de aceptación identificado (**Gerencia Municipal**).
5. **Señales Tempranas y Umbrales Cuantificables:** 100 % de riesgos tratados poseen señal observable y umbral de alerta definido (**cero riesgos sin señal**).
6. **Matriz de Comunicación (8 columnas):** Detallada en `08_riesgos/RG06_comunicacion.csv`, estableciendo flujos periódicos y el hito crítico de aprobación previa de riesgos ≥ 15 ante Gerencia Municipal.
7. **Anexos Oficiales Generados:** Libros de trabajo Excel (`.xlsx`), mapa de calor (`.png`) y documentos PDF (`.pdf`) oficiales con el acta de firmas para la Sección 9 del PETI.
8. **SimpleRisk en Docker:** Scripts de configuración SQL y archivo de importación masiva de riesgos (`simplerisk_import_riesgos.csv`) listos para despliegue turnkey.

---

## 📂 Estructura del Repositorio

```text
SI886-S15-TALLER-Grupo3/
├── 08_riesgos/                                # Sección 8 del PETI y artefactos técnicos
│   ├── RG01_contexto.md                       # Alcance, escalas operativas y criterios
│   ├── RG02_registro.csv                      # Registro inicial de 14 riesgos
│   ├── RG03_evaluacion.py                     # Script de evaluación y mapa de calor
│   ├── RG03_evaluado.csv                      # Matriz evaluada y ordenada por valor
│   ├── RG04_tratamiento.csv                   # Plan de tratamiento, residual y señales
│   ├── RG05_residual.py                       # Script de análisis de reducción residual
│   ├── RG06_comunicacion.csv                  # Matriz de comunicación de riesgos
│   ├── RG07_validacion.py                     # Validación automatizada (Paso F)
│   ├── generar_anexos.py                      # Generador de anexos Excel y PDF
│   ├── simplerisk_config_escalas.sql          # Configuración SQL para SimpleRisk
│   ├── simplerisk_import_riesgos.csv          # Esquema de importación para SimpleRisk
│   └── seccion_08_gestion_riesgos.md          # Redacción completa de la Sección 8
├── anexos/                                    # Anexos oficiales requeridos por la guía
│   ├── anexo_A_registro_riesgos.xlsx          # Matriz de riesgos en Excel
│   ├── anexo_B_mapa_calor.png                 # Mapa de calor en alta resolución
│   ├── anexo_C_plan_tratamiento.xlsx          # Plan de tratamiento y residual en Excel
│   ├── anexo_D_matriz_comunicacion.xlsx       # Matriz de comunicación en Excel
│   ├── anexo_E_premortem.pdf                  # Informe técnico del Pre-mortem en PDF
│   └── anexo_F_aceptacion_residual.pdf        # Formato de firmas para Sección 9 en PDF
├── EMPRESA-03-municipalidad-alto-selva/       # Documentos de diagnóstico institucional
│   ├── bia.csv                                # BIA con análisis de 6 inconsistencias
│   ├── politica-de-respaldo.md                # POL-TI-007 contrastada con la realidad
│   └── universo-auditable-y-riesgos.md        # 17 entidades y 9 riesgos institucionales
├── evidencias/                                # Salidas de terminal y guías
│   └── S15/
│       ├── salidas/
│       │   ├── RG03_evaluacion.txt            # Salida del script de evaluación
│       │   ├── RG05_residual.txt              # Salida del script de residual
│       │   └── validacion.txt                 # Resultado de comprobaciones automáticas
│       └── simplerisk_guia_despliegue.md      # Guía paso a paso de SimpleRisk
├── graficos/                                  # Recursos visuales
│   └── RG_mapa_calor.png                      # Mapa de calor 5x5 generado
├── 3-TALLER.md                                # Guía metodológica del taller
├── RG03_evaluacion.py                         # Script de evaluación ejecutable en raíz
└── SI886-S15-INFORME-FINAL-Grupo3.md          # Informe técnico final consolidado
```

---

## 🚀 Cómo Ejecutar los Scripts

Desde la raíz del repositorio, con un entorno Python 3.10+ y las librerías `pandas`, `numpy`, `matplotlib`, `openpyxl` y `reportlab`:

```bash
# 1. Ejecutar evaluación cuantitativa y generar mapa de calor
python 08_riesgos/RG03_evaluacion.py

# 2. Ejecutar cálculo de reducción residual y verificación de señales tempranas
python 08_riesgos/RG05_residual.py

# 3. Ejecutar comprobaciones automáticas de validación (Paso F)
python 08_riesgos/RG07_validacion.py

# 4. Regenerar todos los anexos oficiales en Excel y PDF
python 08_riesgos/generar_anexos.py
```

---

## 🏷️ Trazabilidad y Etiquetas Git

- **`c2ab4b0`:** Fijación de contexto y criterios previa a la evaluación de riesgos.
- **`v0.15`:** Versión oficial del documento PETI — Sección 8 (Gestión de riesgos).
- **`taller-15`:** Etiqueta formal de entrega del Taller Semana 15.
