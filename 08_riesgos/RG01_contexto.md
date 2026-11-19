# Contexto y criterios de gestión de riesgos del PETI

**Organización:** Municipalidad Distrital de Alto Selva  
**Documento:** `08_riesgos/RG01_contexto.md`  
**Marco metodológico:** ISO 31000:2018 · ISO/IEC 27005:2022 · COBIT 2019 (APO12, EDM03) · Lineamientos PCM-SGTD (R.S.G.D. N.° 005-2018-PCM/SEGDI)

---

## 1. Definición del contexto

| Campo | Contenido |
|---|---|
| **Alcance del análisis** | Riesgos que amenazan la **ejecución del PETI Año 1 – Año 3** (portafolio de proyectos PR-01 a PR-10 y objetivos estratégicos OD-01 a OD-05) de la **Municipalidad Distrital de Alto Selva**. Excluye los incidentes operativos cotidianos de mesa de ayuda (atendidos por soporte TI) y los riesgos políticos o macroeconómicos generales del Plan Estratégico Institucional (PEI) ajenos a TI. |
| **Horizonte** | 3 años (Año 1 – Año 3, en tres olas de implementación). |
| **Escalas de probabilidad e impacto** | Matriz 5 × 5 (Probabilidad 1–5 × Impacto 1–5 = Valor 1–25), con definición operativa escrita en la Sección 2 de este documento. |
| **Criterio de aceptación (Apetito de riesgo)** | **≤ 6 (Bajo):** Aceptable con documentación y seguimiento ordinario.<br>**7 – 11 (Medio) y 12 – 14 (Alto):** Requiere plan de tratamiento con responsable por cargo, plazo definido y señal temprana.<br>**≥ 15 (Crítico):** Inaceptable sin intervención; **requiere decisión expresa de la Gerencia Municipal antes de aprobar el PETI** (y firma formal de aceptación del riesgo residual si tras el tratamiento permanece > 6). |
| **Dueños de riesgo (por cargo)** | Asignados por categoría de riesgo (ver Sección 3), nunca a personas individuales. |
| **Frecuencia de revisión** | **Trimestral** ante el Comité de Gobierno Digital / Comité de TI, y de forma extraordinaria ante cada hito de cambio de ola, recorte de PIM o alerta normativa de PCM-SGTD / ANPD. |
| **Fecha de acuerdo de criterios** | **19 de noviembre de 2026** (acordada y versionada en Git **antes** de la identificación y evaluación de riesgos, verificable en `git log 08_riesgos/RG01_contexto.md`). |

---

## 2. Escalas operativas de Probabilidad e Impacto

### 2.1 Escala de Probabilidad (P)

| Nivel | Descriptor | Definición operativa (Municipalidad Distrital de Alto Selva) |
|---|---|---|
| **1** | **Muy baja** | Evento excepcional; sin antecedentes en la municipalidad ni en entidades locales similares. Probabilidad estimada < 10 % en el horizonte de 3 años. |
| **2** | **Baja** | Evento poco probable, pero concebible; ocurrió alguna vez en la historia institucional o existen controles parciales vigentes. Probabilidad 10 % – 25 %. |
| **3** | **Media** | Evento factible; existen debilidades estructurales conocidas o antecedentes en los últimos 2–3 años (p. ej. rotación administrativa, cambios de alcance). Probabilidad 26 % – 50 %. |
| **4** | **Alta** | Evento probable; las condiciones causales ya están presentes hoy en la municipalidad (p. ej. políticas vencidas sin revisión, controles ausentes, 16 de 17 entidades sin auditar, riesgos abiertos sin plan). Probabilidad 51 % – 80 %. |
| **5** | **Muy alta** | Evento casi seguro en el horizonte del plan si no se interviene de inmediato; recurrencia comprobada o falla sistémica activa. Probabilidad > 80 %. |

### 2.2 Escala de Impacto (I)

| Nivel | Descriptor | Impacto en plazo del PETI | Impacto en servicios ciudadanos y continuidad | Impacto presupuestal / normativo |
|---|---|---|---|---|
| **1** | **Insignificante** | Retraso < 2 semanas en un entregable menor. | Sin interrupción perceptible en atención al ciudadano. | Sobrecosto < 2 % del presupuesto TI; sin observación regulatoria. |
| **2** | **Menor** | Retraso de 2 a 4 semanas en una actividad; no afecta hitos de ola. | Degradación leve en un proceso no crítico (< 4 h). | Sobrecosto de 2 % – 5 %; observación menor de control interno. |
| **3** | **Moderado** | Retraso de 1 a 3 meses en un proyecto del PETI; requiere ajuste de cronograma. | Interrupción parcial en un proceso municipal (entre 4 h y 24 h) o retrabajo operativo. | Sobrecosto de 6 % – 15 % del presupuesto TI; observación formal de auditoría. |
| **4** | **Mayor** | Retraso > 3 meses en proyectos clave o paralización de una ola completa. | Interrupción de procesos críticos (Recaudación, Trámite, Contrataciones) entre 24 h y 72 h o pérdida significativa de datos. | Sobrecosto de 16 % – 30 % o sanción administrativa / multa de PCM-SGTD, Contraloría o ANPD. |
| **5** | **Catastrófico** | Fracaso integral o abandono del PETI en el horizonte de 3 años. | Paralización prolongada (> 72 h) de servicios municipales críticos o pérdida irreversible de información tributaria/documental. | Recorte o sobrecosto > 30 %, sanción grave al titular / funcionarios o inhabilitación de sistemas críticos. |

### 2.3 Matriz de valoración y niveles (según `RG03_evaluacion.py`)

| Rango de Valor (`P × I`) | Nivel | Regla de gestión |
|---|---|---|
| **1 – 6** | **Bajo** | Aceptable con documentación y monitoreo ordinario. |
| **7 – 11** | **Medio** | Requiere tratamiento con plazo y señal temprana. |
| **12 – 14** | **Alto** | Requiere tratamiento prioritario, registro en SimpleRisk y señal temprana. |
| **15 – 25** | **Crítico** | Requiere decisión de la **Gerencia Municipal** antes de aprobar el PETI, tratamiento inmediato, registro en SimpleRisk y aceptación formal firmada si el residual supera 6. |

---

## 3. Dueños de riesgo por categoría

| Categoría de riesgo | Dueño del riesgo (cargo) |
|---|---|
| **Ejecución del plan** | Gerencia Municipal / Comité de Gobierno Digital |
| **Presupuestal** | Gerencia de Administración y Finanzas / Oficina de Planeamiento y Presupuesto |
| **Patrocinio** | Gerencia Municipal |
| **Capacidad de ejecución** | Jefatura de Tecnologías de la Información / Jefatura de Auditoría Interna |
| **Personal clave** | Jefatura de Tecnologías de la Información / Oficina de Recursos Humanos |
| **Resistencia al cambio** | Gerencia de Administración y Finanzas / Gerencias usuarias (Rentas, Secretaría General) |
| **Proveedor** | Gerencia de Administración y Finanzas (Abastecimiento) / Jefatura de TI |
| **Técnico** | Jefatura de Tecnologías de la Información |
| **Normativo** | Oficina de Asesoría Jurídica / Oficial de Gobierno Digital y Protección de Datos |
| **De alcance** | Comité de Gobierno Digital / Comité de TI |
