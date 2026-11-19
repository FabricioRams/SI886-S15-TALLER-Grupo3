-- 08_riesgos/simplerisk_config_escalas.sql
-- Script de inicializacion y configuracion de escalas operativas para SimpleRisk
-- Base de datos: simplerisk (MariaDB 11)
-- Organizacion: Municipalidad Distrital de Alto Selva (Grupo 3 - SI-886)

USE simplerisk;

-- 1. Configuracion de Metodologia de Evaluacion: Formula Clasica (P x I)
UPDATE settings SET value = '1' WHERE name = 'risk_calculation_method';

-- 2. Definicion Operativa de Escalas de Probabilidad (Likelihood 1-5)
DELETE FROM likelihood;
INSERT INTO likelihood (id, name, score, sort_order) VALUES
(1, '1 Muy baja (< 10 % anual)', 1, 1),
(2, '2 Baja (10 - 25 % anual)', 2, 2),
(3, '3 Media (26 - 50 % anual)', 3, 3),
(4, '4 Alta (51 - 80 % anual - causas presentes)', 4, 4),
(5, '5 Muy alta (> 80 % anual - recurrente)', 5, 5);

-- 3. Definicion Operativa de Escalas de Impacto (Impact 1-5)
DELETE FROM impact;
INSERT INTO impact (id, name, score, sort_order) VALUES
(1, '1 Insignificante (sin afectacion observable)', 1, 1),
(2, '2 Menor (retraso < 1 mes / sobrecosto < 5 %)', 2, 2),
(3, '3 Moderado (retraso 1-3 meses / caida 4-24 h / sobrecosto 6-15 %)', 3, 3),
(4, '4 Mayor (retraso > 3 meses / caida 24-72 h / sancion PCM o ANPD)', 4, 4),
(5, '5 Catastrofico (abandono del PETI / caida > 72 h / recorte > 30 %)', 5, 5);

-- 4. Criterios de Aceptacion y Umbrales
-- Bajo: 1-6 (Aceptable con documentacion)
-- Medio: 7-11 (Tratamiento obligatorio con plazo)
-- Alto: 12-14 (Tratamiento prioritario con plazo y senal temprana)
-- Critico: 15-25 (Decision expresa de Gerencia Municipal antes de aprobar el PETI)
UPDATE settings SET value = '6' WHERE name = 'risk_acceptance_threshold';

-- 5. Dueños de Riesgo por Cargo (Estructurales, sin nombres propios)
INSERT IGNORE INTO users (username, role) VALUES
('gerencia_municipal', 'Risk Approver'),
('jefatura_ti', 'Risk Owner'),
('gerencia_administracion', 'Risk Owner'),
('auditoria_interna', 'Auditor'),
('comite_gobierno_digital', 'Risk Committee');
