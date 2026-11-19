# Sección 8. Gestión de riesgos del plan (PETI — Municipalidad Distrital de Alto Selva)

---

## 8.1 Alcance, contexto y criterios

La presente sección gestiona los **riesgos estratégicos y de ejecución del Plan Estratégico de Tecnologías de Información (PETI)** de la **Municipalidad Distrital de Alto Selva** en un horizonte de **3 años (Año 1 – Año 3)**, abarcando sus cinco objetivos estratégicos (`OD-01` a `OD-05`) y diez proyectos del portafolio (`PR-01` a `PR-10`). Se excluyen los incidentes operativos cotidianos de mesa de ayuda (atendidos por soporte TI) y los riesgos políticos o institucionales generales propios del Plan Estratégico Institucional (PEI).

La evaluación utiliza una matriz `5 × 5` (`Valor = Probabilidad × Impacto`, rango `1–25`) cuyas escalas operativas fueron acordadas y registradas con anterioridad a la valoración en [`RG01_contexto.md`](RG01_contexto.md) (fecha de acuerdo: **19 de noviembre de 2026**, verificable en `git log 08_riesgos/RG01_contexto.md`):

- **Escala de Probabilidad (P):** `1 Muy baja` (< 10 %), `2 Baja` (10 %–25 %), `3 Media` (26 %–50 %), `4 Alta` (51 %–80 %, condiciones causales activas en la entidad), `5 Muy alta` (> 80 %).
- **Escala de Impacto (I):** `1 Insignificante`, `2 Menor`, `3 Moderado` (retraso 1–3 meses / caída 4–24 h / sobrecosto 6 %–15 %), `4 Mayor` (retraso > 3 meses / caída 24–72 h / sanción PCM-SGTD o ANPD), `5 Catastrófico` (fracaso del PETI / caída > 72 h / recorte > 30 %).
- **Criterio de aceptación (Apetito de riesgo):**
  - **≤ 6 (Bajo):** Aceptable con documentación y seguimiento ordinario.
  - **7 – 11 (Medio) y 12 – 14 (Alto):** Requiere plan de tratamiento con responsable por cargo, plazo definido y señal temprana.
  - **≥ 15 (Crítico):** Requiere decisión expresa de la **Gerencia Municipal** antes de aprobar el PETI, registro en SimpleRisk (junto con los riesgos ≥ 12) y aceptación formal firmada si el riesgo residual supera el umbral `6`.

---

## 8.2 Método

El análisis se sustenta en la norma **ISO 31000:2018** (Proceso de gestión del riesgo), complementada con **ISO/IEC 27005:2022** y **COBIT 2019** (`APO12` y `EDM03`). Las fuentes de identificación empleadas para la Municipalidad Distrital de Alto Selva fueron:

1. **Análisis documental y contraste de práctica real:** Revisión de la política de respaldo vigente (`politica-de-respaldo.md`, código `POL-TI-007` v1.0, sin revisión desde agosto de 2024), el Análisis de Impacto al Negocio (`bia.csv`, elaborado en setiembre de 2024 sin validación de áreas) y el universo auditable junto con el registro histórico de riesgos de Administración (`universo-auditable-y-riesgos.md`, 17 entidades auditables y 9 riesgos abiertos al 1 de noviembre de 2025).
2. **Pre-mortem del portafolio PETI:** Identificación prospectiva de escenarios de falla presupuestal, de patrocinio y de alcance durante las tres olas.
3. **Evaluación cuantitativa y análisis residual:** Ejecución reproducible mediante los programas [`RG03_evaluacion.py`](RG03_evaluacion.py) y [`RG05_residual.py`](RG05_residual.py).

---

## 8.3 Registro de riesgos

Se identificaron **14 riesgos** (`R-01` a `R-14`) redactados con la estructura **evento + causa + consecuencia**, cubriendo **las nueve categorías obligatorias** (`Presupuestal`, `Patrocinio`, `Capacidad de ejecución`, `Personal clave`, `Resistencia al cambio`, `Proveedor`, `Técnico`, `Normativo`, `De alcance`) más la categoría característica **`Ejecución del plan`**.

> **Declaración de categorías sin riesgo identificado:** **Ninguna categoría fue omitida** (verificación automática en `RG03_evaluacion.py`: `Categorías SIN riesgo identificado: ninguna ✔`).

| ID | Categoría | Riesgo (evento + causa + consecuencia) | Objetivos / proyectos | Origen | P | I | Valor | Nivel |
|---|---|---|---|---|---|---|---|---|
| **R-01** | Ejecución del plan | Que el PETI de la municipalidad se apruebe y no se ejecute por ausencia de responsable designado y de seguimiento periódico, retrasando o paralizando el cumplimiento integral del plan al año 3 | OD-01 a OD-05 · PR-01 a PR-10 | Riesgo característico · `universo-auditable-y-riesgos.md` | 4 | 5 | **20** | Crítico |
| **R-02** | Técnico | Que una falla severa o ransomware comprometa la disponibilidad e integridad de Rentas y Catastro y Trámite Documentario por falta de pruebas de restauración, uso de disco externo sin cifrar trasladado por el Jefe de TI los viernes y ausencia de BCP, paralizando servicios críticos > 72 h con pérdida de hasta 96 h de datos | OD-01, OD-02, OD-03 · PR-04 | `politica-de-respaldo.md` · `bia.csv` · RG-04, RG-05, UA-13 | 4 | 5 | **20** | Crítico |
| **R-03** | Normativo | Que la municipalidad reciba sanciones, multas o medidas correctivas de PCM-SGTD, Contraloría o la Autoridad de Protección de Datos por incumplir el marco de Gobierno Digital y carecer de registro de tratamiento de datos de contribuyentes y auditorías (UA-17 nunca auditado), obligando a detener despliegues y reasignar recursos | OD-04 · PR-05, PR-06 | `universo-auditable-y-riesgos.md` (UA-17, RG-01, RG-03, RG-06, RG-07) | 4 | 4 | **16** | Crítico |
| **R-04** | Proveedor | Que la interrupción del servicio o término contractual del único proveedor de soporte/nube bloquee la modernización de Rentas y Catastro y los servicios alojados, por dependencia de un único proveedor sin código fuente documentado ni SLA/cifrado verificados, paralizando PR-02 y PR-08 | OD-02, OD-05 · PR-02, PR-08 | `universo-auditable-y-riesgos.md` (UA-15, UA-16, RG-02, RG-08) | 4 | 4 | **16** | Crítico |
| **R-06** | Presupuestal | Que el PIM asignado al PETI en el año 2 se recorte o reasigne a gasto corriente municipal ante caída en recaudación o falta de expedientes validados, retrasando la Ola 2 y postergando PR-04 y PR-03 | OD-01, OD-02, OD-03 · PR-02, PR-03, PR-04 | Pre-mortem · `bia.csv` (BIA02, BIA04) · `politica-de-respaldo.md` | 4 | 4 | **16** | Crítico |
| **R-05** | Patrocinio | Que un cambio de gestión municipal o rotación en la Gerencia Municipal y Gerencia de Administración retire el respaldo ejecutivo al PETI antes del año 2 por no existir Comité de Gobierno Digital institucionalizado ni apetito de riesgo formalizado, dejando los proyectos sin prioridad | OD-01 a OD-05 · PR-01 a PR-10 | Pre-mortem · `politica-de-respaldo.md` · `universo-auditable-y-riesgos.md` | 3 | 5 | **15** | Crítico |
| **R-07** | Técnico | Que los proyectos PR-01, PR-02, PR-04 y PR-09 fallen en su dimensionamiento por sustentarse en un BIA no validado con incoherencias severas (RPO 96 h > RTO 72 h en BIA01; RTO 4 h vs 72 h sobre Rentas en BIA02/BIA03; BIA04 sin sistema; SIAF-SP RTO 2 h) y un inventario UA-07..UA-11 desalineado | OD-01, OD-02, OD-03, OD-05 · PR-01, PR-02, PR-03, PR-04, PR-09 | `bia.csv` (BIA01–BIA06) · `universo-auditable-y-riesgos.md` (UA-07..UA-11) | 4 | 3 | **12** | Alto |
| **R-08** | Personal clave | Que la renuncia o ausencia prolongada del Jefe de TI paralice la gestión de respaldos y el despliegue técnico de la Ola 1, al concentrar ese cargo la ejecución, verificación y custodia física del disco externo junto con el conocimiento tácito de sistemas sin código fuente | OD-03, OD-05 · PR-04, PR-09 | `politica-de-respaldo.md` (Sec. 4 y 6) · RG-02 | 4 | 3 | **12** | Alto |
| **R-09** | Capacidad de ejecución | Que Auditoría Interna y TI no cubran las verificaciones de control y cumplimiento del PETI en paralelo a la operación diaria, porque las 838 h-auditor anuales (sin cálculo de carga) no alcanzan para auditar las 17 entidades acumuladas | OD-04, OD-05 · PR-07, PR-10 | `universo-auditable-y-riesgos.md` (Sec. 2 y 4) | 4 | 3 | **12** | Alto |
| **R-10** | Resistencia al cambio | Que el personal de las gerencias usuarias resista el uso de los nuevos sistemas y controles, manteniendo registros en papel o archivos locales, debido a difusión pasiva («se envió por correo») y falta de involucramiento | OD-01, OD-02 · PR-01, PR-03, PR-07 | `politica-de-respaldo.md` · `bia.csv` (BIA04) | 3 | 4 | **12** | Alto |
| **R-11** | De alcance | Que las áreas usuarias soliciten módulos o reportes ad hoc sin caso de negocio ni filtro del Comité de TI, consumiendo la capacidad técnica y desplazando entregas críticas | OD-01, OD-02, OD-05 · PR-01 a PR-10 | Pre-mortem · `universo-auditable-y-riesgos.md` | 3 | 3 | **9** | Medio |
| **R-13** | Presupuestal | Que el gasto operativo acumulado (OPEX) en nube, enlaces (UA-12) y soporte supere el presupuesto del año 3 por falta de dimensionamiento contractual, obligando a recortar servicios | OD-01, OD-03 · PR-01, PR-04, PR-08 | Pre-mortem · `universo-auditable-y-riesgos.md` (UA-12, UA-16) | 3 | 3 | **9** | Medio |
| **R-12** | Normativo | Que se produzcan irregularidades o fraude interno en compras y pagos (SIAF-SP y Logística) por falta de segregación de funciones y auditoría en UA-05 y UA-14 | OD-04 · PR-07 | `universo-auditable-y-riesgos.md` (UA-05, UA-07, UA-14, RG-09) | 2 | 4 | **8** | Medio |
| **R-14** | Resistencia al cambio | Que la comunicación únicamente por correo de las directivas de respaldo resulte insuficiente para evitar el guardado local en PC, ocasionando pérdidas menores de archivos no críticos | OD-03 · PR-04 | `politica-de-respaldo.md` (Ficha y Sec. 4) | 2 | 3 | **6** | Bajo |

El registro completo con la justificación cuantitativa por riesgo obra en [`RG02_registro.csv`](RG02_registro.csv) y [`RG03_evaluado.csv`](RG03_evaluado.csv).

---

## 8.4 Evaluación y mapa de calor

La distribución resultante de los 14 riesgos evaluados mediante [`RG03_evaluacion.py`](RG03_evaluacion.py) es:

| Nivel | Rango | Cantidad | Porcentaje | Riesgos |
|---|---|---|---|---|
| **Crítico** | 15 – 25 | **6** | 42.9 % | `R-01` (20), `R-02` (20), `R-03` (16), `R-04` (16), `R-06` (16), `R-05` (15) |
| **Alto** | 12 – 14 | **4** | 28.6 % | `R-07` (12), `R-08` (12), `R-09` (12), `R-10` (12) |
| **Medio** | 7 – 11 | **3** | 21.4 % | `R-11` (9), `R-13` (9), `R-12` (8) |
| **Bajo** | 1 – 6 | **1** | 7.1 % | `R-14` (6) |
| **Total** | | **14** | **100 %** | |

- **Riesgos ≥ 15 que requieren decisión expresa de la Gerencia Municipal antes de aprobar el PETI:** `R-01`, `R-02`, `R-03`, `R-04`, `R-06` y `R-05` (6 riesgos).
- **Riesgos ≥ 12 registrados para seguimiento en SimpleRisk:** Los 10 riesgos críticos y altos (`R-01` a `R-10`).
- **Mapa de calor:** Generado en [`../graficos/RG_mapa_calor.png`](../graficos/RG_mapa_calor.png).

---

## 8.5 Tratamiento y riesgo residual

Todos los riesgos con valor **> 6** (**13 riesgos**, `R-01` a `R-13`) cuentan con estrategia de tratamiento, acciones concretas, responsable por cargo, plazo, costo estimado y riesgo residual en [`RG04_tratamiento.csv`](RG04_tratamiento.csv). El riesgo `R-14` (`Valor = 6`) se acepta con documentación conforme al criterio vigente.

Resumen de reducción lograda (calculada por [`RG05_residual.py`](RG05_residual.py)):

| ID | Valor inicial | Decisión | Responsable (cargo) | Plazo | Costo | P res. | I res. | Valor residual | Reducción |
|---|---|---|---|---|---|---|---|---|---|
| `R-01` | 20 | Mitigar | Gerencia Municipal | Al aprobar el plan | Bajo | 2 | 4 | **8** | -12 (-60 %) |
| `R-02` | 20 | Mitigar | Jefatura de Tecnologías de la Información | 60 días | Medio | 2 | 4 | **8** | -12 (-60 %) |
| `R-03` | 16 | Mitigar | Oficial de Datos Personales / Asesoría Jurídica | 90 días | Medio | 2 | 4 | **8** | -8 (-50 %) |
| `R-04` | 16 | Transferir + Mitigar | Gerencia de Administración y Finanzas | Antes de PR-02 | Medio | 2 | 4 | **8** | -8 (-50 %) |
| `R-06` | 16 | Mitigar + Asumir con contingencia | Gerencia de Administración / Planeamiento | Al aprobar el plan | Bajo | 3 | 3 | **9** | -7 (-44 %) |
| `R-05` | 15 | Mitigar | Gerencia Municipal | Al aprobar el plan | Bajo | 2 | 4 | **8** | -7 (-47 %) |
| `R-07` | 12 | Mitigar | Jefatura de TI / Gerencias usuarias | 30 días | Bajo | 1 | 3 | **3** | -9 (-75 %) |
| `R-08` | 12 | Mitigar | Jefatura de TI / RR. HH. | 90 días | Medio | 2 | 3 | **6** | -6 (-50 %) |
| `R-09` | 12 | Mitigar | Jefatura de Auditoría Interna | 45 días | Bajo | 2 | 4 | **8** | -4 (-33 %) |
| `R-10` | 12 | Mitigar | Gerencia de Administración / Gerencias usuarias | Antes de piloto PR-01/PR-03 | Bajo | 2 | 3 | **6** | -6 (-50 %) |
| `R-11` | 9 | Mitigar | Comité de Gobierno Digital | Continuo | Bajo | 2 | 3 | **6** | -3 (-33 %) |
| `R-13` | 9 | Mitigar + Transferir | Gerencia de Administración / Jefatura de TI | Antes de Ola 2 | Bajo | 2 | 3 | **6** | -3 (-33 %) |
| `R-12` | 8 | Mitigar | Jefatura de Auditoría Interna / Jefatura de TI | 90 días | Bajo | 1 | 4 | **4** | -4 (-50 %) |

- **Valor inicial agregado (13 riesgos > 6):** `177 puntos`.
- **Valor residual agregado:** `88 puntos`.
- **Reducción total lograda por el plan de tratamiento:** **`89 puntos` (`50 %` de reducción)**.

---

## 8.6 Señales tempranas y umbrales de alerta

Cada uno de los 13 riesgos con valor > 6 cuenta con señal temprana observable y umbral numérico/temporal definido (**0 riesgos sin señal temprana**):

| ID | Señal temprana observable | Umbral de alerta |
|---|---|---|
| `R-01` | Comité de Gobierno Digital sin sesionar ni levantar acta | 1 trimestre sin sesión formal |
| `R-02` | Prueba de restauración trimestral vencida o respaldo sin cifrado activo | 1 trimestre sin acta de restauración verificada |
| `R-03` | Observación preventiva o requerimiento de PCM-SGTD / ANPD | 1 requerimiento sin respuesta en plazo o retraso > 15 días |
| `R-04` | Contrato vigente sin cláusula de código fuente/salida o SLA sin evidencia | A 60 días del inicio de PR-02 sin adenda firmada |
| `R-06` | Reducción en proyección de recaudación o demora en certificación | Desviación > 10 % del PIM asignado o 30 días sin certificación |
| `R-05` | Inasistencia de Gerencia Municipal o Administración a sesiones del comité | 2 sesiones consecutivas sin alta dirección |
| `R-07` | Inconsistencias abiertas entre sistemas del BIA y universo auditable | 1 semana de retraso sobre hito de validación del BIA |
| `R-08` | Una sola persona concentrando accesos administrativos o respaldo | Factor bus = 1 en sistema crítico o respaldo |
| `R-09` | Desviación en ejecución de horas-auditor o acumulación sin auditar | Avance trimestral < 75 % de las horas planificadas |
| `R-10` | Asistencia baja a capacitaciones o mantenimiento de cuadernos paralelos | Participación < 70 % en talleres o > 20 % trámites fuera de sistema |
| `R-11` | Solicitudes de desarrollo/reportes dirigidas a TI sin ticket de comité | 1 requerimiento atendido sin aprobación formal |
| `R-13` | Incremento no previsto en facturación mensual de nube o enlaces | Desviación > 10 % mensual sobre OPEX proyectado |
| `R-12` | Usuarios con perfiles incompatibles o cuentas huérfanas en SIAF-SP | 1 usuario con permisos conflictivos sin corrección en 48 h |

---

## 8.7 Matriz de comunicación del riesgo

La matriz completa de comunicación (ocho columnas) consta en [`RG06_comunicacion.csv`](RG06_comunicacion.csv), cubriendo los riesgos críticos y altos (`R-01` a `R-10`) y la sesión obligatoria previa a la aprobación del PETI para todos los riesgos `≥ 15`, especificando qué se comunica, a qué cargo, con qué frecuencia, canal, emisor, formato y decisión habilitada.

---

## 8.8 Riesgos residuales que requieren aceptación formal

Tras aplicar el plan de tratamiento, **7 riesgos mantienen un valor residual > 6** (por encima del criterio de aceptación) y **no pueden ser aceptados por el equipo formulador del PETI**; requieren **aceptación formal firmada por el dueño del riesgo** antes de aprobar el plan (Anexo de firmas de la Sección 9):

| ID | Riesgo (resumen) | Valor inicial | Valor residual | Responsable de la aceptación formal (cargo) |
|---|---|---|---|---|
| `R-01` | No ejecución del PETI por ausencia de gobierno y seguimiento | 20 | **8** | **Gerencia Municipal** |
| `R-02` | Falla/ransomware sobre respaldos no probados y sin BCP | 20 | **8** | **Gerencia Municipal** |
| `R-03` | Sanciones PCM-SGTD / ANPD por incumplimiento normativo | 16 | **8** | **Gerencia Municipal** |
| `R-04` | Bloqueo por único proveedor sin código fuente ni SLA | 16 | **8** | **Gerencia Municipal** |
| `R-06` | Recorte o reasignación del PIM del PETI en Año 2 | 16 | **9** | **Gerencia Municipal** |
| `R-05` | Pérdida de patrocinio ejecutivo ante rotación municipal | 15 | **8** | **Gerencia Municipal** |
| `R-09` | Capacidad insuficiente (838 h-auditor) ante 17 entidades | 12 | **8** | **Gerencia Municipal** |

---

## 8.9 Seguimiento y revisión

- **Frecuencia ordinaria:** Revisión **trimestral** en sesión formal del **Comité de Gobierno Digital / Comité de TI** con tablero de señales tempranas, avance de acciones de tratamiento y estado de los 9 riesgos históricos (`RG-01` a `RG-09`).
- **Responsable del seguimiento:** Líder de Gobierno Digital / Responsable del PETI designado por resolución, con reporte directo a la Gerencia Municipal y coordinación con Auditoría Interna y Jefatura de TI.
- **Disparadores de revisión extraordinaria:**
  1. Activación de cualquier **umbral de alerta** definido en la Sección 8.6.
  2. Cambio de gestión municipal, rotación de Gerencia Municipal/Administración o Jefatura de TI.
  3. Modificación presupuestal (PIM) > 10 % sobre proyectos del PETI.
  4. Incidente de seguridad, interrupción de sistemas críticos > 4 h o requerimiento formal de PCM-SGTD / Contraloría / ANPD.
  5. Transición entre Olas 1, 2 y 3 de la hoja de ruta.
