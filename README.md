# 🍦 Heladería Ice Baby – Aplicación Flask

## 📖 Descripción general
Este proyecto es una aplicación web desarrollada en **Flask** que gestiona una **heladería**, aplicando arquitectura modular (MVC) y base de datos relacional con **SQLAlchemy**.  
Permite manejar productos, ingredientes, usuarios y roles (admin, empleado y cliente), así como calcular ventas, costos y rentabilidad.

El sistema integra autenticación, roles de usuario, plantillas HTML con Bootstrap y pruebas unitarias automatizadas con `unittest`.

---

## 🏗️ Estructura del proyecto

```
project/
├── app/
│   ├── config/           → configuración de Flask, base de datos y seguridad
│   │   └─auth.py
│   │   └─config.py
│   │   └─db.py
│   │   └─routes.py
│   │   
│   ├── controllers/      → Blueprints con lógica de negocio y rutas
│   │   └─administracion.py
│   │   └─api.py
│   │   └─index.py
│   │   └─login.py
│   │   └─ventas.py
│   │  
│   ├── models/           → modelos ORM con SQLAlchemy.
│   │   └─heladeria.py
│   │   └─ingredientes.py
│   │   └─producto_ingrediente.py
│   │   └─producto.py
│   │   └─usuario.py
│   │  
│   ├── utils/            → funciones auxiliares y decoradores.
│   │   └─decorators.py
│   │  
│   └── views/            → plantillas HTML y recursos estáticos.
│       └─administracion.html
│       └─home_admin.html
│       └─home_client.html
│       └─home_employees.html
│       └─home_non_users.html
│       └─login.html
│       └─menu.html
│       └─ventas.html
│
├── test/ → pruebas unitarias con unittest
│   └── test_heladeria.py 
│   └── test_heladeria.py 
│   └── test_heladeria.py 
│   └── test_heladeria.py 
│
├── __init__.py       → inicializa Flask, DB, login y carga datos de prueba.
│
├── .env → configuración de entorno (.env)
│
├── venv → configuración de entorno virtual
│
├── funciones.py       → Funciones que utiliza el aplicativo.
│
└── requirements.txt       → dependencias del entorno
```

---

## ⚙️ Configuración e instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/ricardogarcia2604/UMBDisenoWeb_ActividadFinal.git
cd project
```

### 2. Crear entorno virtual e instalar dependencias
```bash
python -m venv venv
venv\Scripts\activate   # (Windows)
pip install -r requirements.txt
```

### 3. Variables de entorno
Crea un archivo `.env` en la raíz con las variables necesarias:
```env
DATABASE_URI=sqlite:///heladeria.db
```

### 4. Ejecutar la aplicación
```bash
python app/__init__.py
```
La aplicación se ejecutará en `http://127.0.0.1:5000`.

---


### 🔹 Ejecución de pruebas
Desde la raíz del proyecto:
```bash
python -m unittest discover -s test -v
```

Resultado esperado:
```

test_obtener_mejor_producto (test_heladeria.TestHeladeria.test_obtener_mejor_producto) ... ok
test_vender_producto_existente (test_heladeria.TestHeladeria.test_vender_producto_existente) ... ok
test_vender_producto_inexistente (test_heladeria.TestHeladeria.test_vender_producto_inexistente) ... ok
test_abastecer (test_ingrediente.TestIngredientes.test_abastecer) ... ok
test_es_sano_exception (test_ingrediente.TestIngredientes.test_es_sano_exception) ... ok
test_es_sano_true (test_ingrediente.TestIngredientes.test_es_sano_true) ... ok
test_renovar_inventario (test_ingrediente.TestIngredientes.test_renovar_inventario) ... ok
test_calcular_calorias (test_producto.TestProductos.test_calcular_calorias) ... ok
test_calcular_costo (test_producto.TestProductos.test_calcular_costo) ... ok
test_calcular_rentabilidad (test_producto.TestProductos.test_calcular_rentabilidad) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.003s

OK

```

---

## 🧠 Tecnologías utilizadas
- **Flask 3.1.0**
- **Flask-Login**
- **Flask-SQLAlchemy**
- **Werkzeug**
- **Bootstrap 5**
- **Unittest**
- **Dotenv**
- **HTML 5**
- **Javascript**
- **Blueprint**


---

## ✨ Autor
**Ricardo García**  
Estudiante de Ingeniería de Software.
