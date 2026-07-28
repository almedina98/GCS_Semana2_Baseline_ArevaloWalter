# Documento de Diseño del Software (SDD)

**Proyecto:** Sistema Básico de Inventario  
**Versión:** 1.0  
**Estado:** Candidato para línea base

## 1. Diseño general
Aplicación sencilla desarrollada en Python para demostrar gestión de configuración mediante documentos, código, pruebas y configuración versionados.

## 2. Arquitectura
Arquitectura simple:

**Usuario → Aplicación Python → Inventario → Resultado**

La entrada proporciona datos de productos; la lógica administra las operaciones; la salida presenta resultados al usuario.

## 3. Componentes
- **Producto:** código, nombre, cantidad y precio.
- **Inventario:** almacena y administra productos.
- **Programa principal:** crea un inventario y demuestra su funcionamiento.

## 4. Decisiones técnicas
- Python 3 como lenguaje.
- Git para control de versiones.
- GitHub o GitLab como repositorio remoto.
- `config.example` como configuración de demostración sin credenciales reales.

## 5. Línea base
Este documento será incluido junto con el SRS, código, prueba y configuración en Baseline v1.0.
