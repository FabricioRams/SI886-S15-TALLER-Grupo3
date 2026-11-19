# Guía Técnica de Despliegue y Configuración de SimpleRisk
**SI-886 Planeamiento Estratégico de TI — Taller Semana 15**  
**Organización:** Municipalidad Distrital de Alto Selva | **Equipo:** Grupo 3

---

## 1. Arquitectura del Entorno Docker

El despliegue de SimpleRisk Community se realiza mediante dos contenedores interconectados en una red puente local:

```bash
# 1. Levantar base de datos MariaDB 11
docker run -d --name peti_srdb \
  -e MARIADB_ROOT_PASSWORD=peti_sr \
  -e MARIADB_DATABASE=simplerisk \
  mariadb:11

# 2. Levantar la aplicación SimpleRisk vinculada a la base de datos
docker run -d --name peti_simplerisk \
  --link peti_srdb:db \
  -p 127.0.0.1:8084:80 \
  simplerisk/simplerisk:latest
```

Acceso web local: **`http://127.0.0.1:8084`**  
Credenciales iniciales por defecto: Usuario `admin` / Contraseña `admin`.

---

## 2. Configuración Metodológica de Escalas y Criterio de Aceptación

Para asegurar estricta concordancia con el documento de contexto institucional (`08_riesgos/RG01_contexto.md`):

1. **Fórmula de Cálculo:**  
   Navegar a *Configure -> Risk Formula* y seleccionar la opción **Classic Risk Calculation** (`Risk Score = Likelihood × Impact`).
2. **Escalas Operativas de Probabilidad (Likelihood):**  
   Configurar los 5 niveles con sus definiciones operativas escritas:
   - `1 Muy baja (< 10 % anual)`
   - `2 Baja (10 – 25 % anual)`
   - `3 Media (26 – 50 % anual)`
   - `4 Alta (51 – 80 % anual)`
   - `5 Muy alta (> 80 % anual)`
3. **Escalas Operativas de Impacto (Impact):**  
   Configurar los 5 niveles:
   - `1 Insignificante`
   - `2 Menor (retraso < 1 mes)`
   - `3 Moderado (retraso 1-3 m / caída 4-24 h)`
   - `4 Mayor (retraso > 3 m / caída 24-72 h / sanción PCM o ANPD)`
   - `5 Catastrófico (fracaso PETI / caída > 72 h / recorte > 30 %)`
4. **Criterio de Aceptación:**  
   Definir el umbral de aceptación en **6 puntos**. Todo riesgo con puntuación `> 6` requiere plan de mitigación obligatorio y los riesgos con valoración residual `> 6` exigen aprobación de la Gerencia Municipal.

Alternativamente, se puede ejecutar el script SQL automatizado proporcionado:
```bash
docker exec -i peti_srdb mysql -uroot -ppeti_sr simplerisk < 08_riesgos/simplerisk_config_escalas.sql
```

---

## 3. Carga de Riesgos y Generación de Evidencias

Los 10 riesgos críticos y altos (`Valor ≥ 12`), junto con los de valor medio y bajo, se encuentran estructurados y listos para su importación masiva en el archivo:
- **`08_riesgos/simplerisk_import_riesgos.csv`**

### Pasos de Carga en Interfaz SimpleRisk:
1. Ingresar al módulo *Risk Management -> Import Risks*.
2. Subir el archivo `simplerisk_import_riesgos.csv` mapeando los campos estándar.
3. Verificar la matriz resultante en *Reporting -> Dynamic Risk Report* y *Heat Map*.
4. Comprobar que los riesgos `R-01` y `R-02` lideran la zona crítica con puntuación 20, seguidos por `R-03`, `R-04`, `R-06` (16) y `R-05` (15).

---

## 4. Estado de Ejecución Local y Contingencia

Durante la sesión práctica en la estación de trabajo local, el daemon de Docker Desktop no se encontraba activo en segundo plano, por lo que se diseñó la solución turnkey completa (`simplerisk_config_escalas.sql` y `simplerisk_import_riesgos.csv`) garantizando total reproducibilidad del despliegue en cualquier servidor o equipo con Docker activo.
