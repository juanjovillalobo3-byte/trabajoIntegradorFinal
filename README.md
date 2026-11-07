# Sistema de Gestión Bancaria

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un Sistema de Gestión Bancaria realizado en Python, como Trabajo Práctico Integrador Final de Laboratorio I.

La aplicación permite administrar cuentas bancarias, realizar operaciones y generar reportes en formato PDF.

## Funcionalidades

- Crear y administrar cuentas bancarias.
- Gestionar cuentas de ahorro y cuentas corrientes.
- Consultar información de las cuentas.
- Realizar depósitos y retiros.
- Realizar transferencias entre cuentas.
- Generar reportes en formato PDF.
- Ejecutar pruebas unitarias para verificar el funcionamiento del sistema.

## Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Programación Orientada a Objetos (POO):** organización del sistema mediante clases y objetos.
- **FPDF2:** generación de reportes PDF.
- **Pytest:** ejecución de pruebas unitarias.
- **Git y GitHub:** control de versiones y almacenamiento del proyecto.

## Estructura del proyecto

```text
trabajoIntegradorFinal/
│
├── main.py
├── banco.py
├── cuentas.py
├── reportes.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── tests/
    ├── test_banco.py
    ├── test_cuentas.py
    └── test_reportes.py
```

## Conceptos de Programación Orientada a Objetos

El sistema implementa los siguientes conceptos:

- **Abstracción:** representación de las entidades principales del sistema bancario.
- **Herencia:** utilización de una clase base `Cuenta` y clases derivadas `CuentaAhorro` y `CuentaCorriente`.
- **Polimorfismo:** implementación de comportamientos específicos según el tipo de cuenta.
- **Encapsulamiento:** protección de los atributos mediante atributos privados y métodos de acceso.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/juanjovillalobo3-byte/trabajoIntegradorFinal
```

### 2. Ingresar a la carpeta del proyecto

```bash
cd trabajoIntegradorFinal
```

### 3. Crear el entorno virtual

```bash
python -m venv .venv
```

### 4. Activar el entorno virtual

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate
```

### 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 6. Ejecutar la aplicación

```bash
py main.py
```

## Pruebas unitarias

Para ejecutar las pruebas:

```bash
py -m pytest -v
```

Las pruebas permiten verificar el funcionamiento de las clases, las operaciones bancarias y la generación de reportes.

**Estado de las pruebas durante el desarrollo:** 17 pruebas aprobadas.

## Control de versiones

El proyecto utiliza Git y GitHub para administrar los cambios.

Se trabaja con dos ramas principales:

- `main`: contiene la versión definitiva del proyecto.
- `desarrollo`: contiene los cambios y las nuevas funcionalidades durante el desarrollo.

Los cambios se registran mediante commits con mensajes descriptivos.

## Autor

Villalobo Juan José