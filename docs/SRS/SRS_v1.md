# Especificación de Requisitos del Software (SRS)

**Proyecto:** Sistema Básico de Inventario  
**Versión:** 1.0  
**Estado:** Candidato para línea base

## 1. Propósito
Definir los requisitos de un sistema básico para registrar y consultar productos de inventario.

## 2. Requisitos funcionales

### REQ-001 – Registrar producto
El sistema deberá permitir registrar un producto indicando código, nombre, cantidad y precio.

### REQ-002 – Consultar productos
El sistema deberá permitir visualizar los productos registrados.

### REQ-003 – Buscar producto
El sistema deberá permitir localizar un producto mediante su código único.

### REQ-004 – Actualizar cantidad
El sistema deberá permitir modificar la cantidad disponible de un producto registrado.

### REQ-007 - Alerta de stock mínimo
El sistema deberá generar una alerta cuando la cantidad disponible de un producto sea igual o inferior al nivel mínimo establecido.

## 3. Requisitos no funcionales

### RNF-001 – Facilidad de uso
El sistema deberá presentar mensajes comprensibles durante su ejecución.

### RNF-002 – Compatibilidad
El sistema deberá poder ejecutarse con Python 3.

## 4. Estado
REQ-001 a REQ-004 y RNF-001 a RNF-002 forman parte de la versión candidata para Baseline v1.0.

> Nota para el cambio controlado: REQ-007 se agregará únicamente después de crear el tag v1.0.
