# Directorio de Empleados API

API REST para la gestión de un directorio de empleados desarrollada con Flask y Python.

## Descripción

DirectorioEmpleadosAPI es una aplicación backend que proporciona una interfaz RESTful para gestionar información de empleados. La API permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre un directorio de empleados, almacenando la información en una base de datos SQLite.

## Características

- API RESTful completa para gestión de empleados
- Base de datos SQLite para persistencia de datos
- Containerización con Docker para fácil despliegue
- Arquitectura modular y escalable
- Endpoints bien definidos para operaciones CRUD

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal
- **Flask**: Framework web para Python
- **SQLite**: Base de datos ligera para almacenamiento
- **Docker**: Containerización de la aplicación
- **Docker Compose**: Orquestación de contenedores

## Estructura del Proyecto

```
DirectorioEmpleadosAPI/
├── app/                    # Código fuente de la aplicación
├── .env                    # Variables de entorno
├── .idea/                  # Configuración del IDE
├── database.db             # Base de datos SQLite
├── Dockerfile              # Configuración de Docker
├── docker-compose.yml      # Configuración de Docker Compose
├── requirements.txt        # Dependencias de Python
└── DirectorioEmpleadosAPI.iml
```

## Requisitos Previos
- Python 3.x
- Docker y Docker Compose (opcional, para despliegue containerizado)
- pip (gestor de paquetes de Python)

## Instalación

### Instalación Local

1. **Clonar el repositorio:**
```bash
git clone https://github.com/claun0ch3/DirectorioEmpleadosAPI.git
cd DirectorioEmpleadosAPI
```

2. **Crear un entorno virtual:**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno:**
```bash
cp .env.example .env  # Si existe
# Editar .env con tus configuraciones
```

5. **Ejecutar la aplicación:**
```bash
python app/main.py  # O el archivo principal correspondiente
```

### Instalación con Docker

1. **Clonar el repositorio:**
```bash
git clone https://github.com/claun0ch3/DirectorioEmpleadosAPI.git
cd DirectorioEmpleadosAPI
```

2. **Construir y ejecutar con Docker Compose:**
```bash
docker-compose up -d
```

La API estará disponible en `http://localhost:8000` (o el puerto configurado).

## Uso de la API

### Endpoints Principales

#### Obtener todos los empleados
```http
GET /empleados
```

#### Obtener un empleado específico
```http
GET /empleados/{id}
```

#### Crear un nuevo empleado
```http
POST /empleados
Content-Type: application/json

{
  "nombre": "Juan Pérez",
  "email": "juan.perez@empresa.com",
  "departamento": "IT",
  "puesto": "Desarrollador"
}
```

#### Actualizar un empleado
```http
PUT /empleados/{id}
Content-Type: application/json

{
  "nombre": "Juan Pérez",
  "email": "juan.perez@empresa.com",
  "departamento": "IT",
  "puesto": "Senior Developer"
}
```

#### Eliminar un empleado
```http
DELETE /empleados/{id}
```

## Docker

### Construir la imagen Docker
```bash
docker build -t directorio-empleados-api .
```

### Ejecutar el contenedor
```bash
docker run -p 5000:5000 directorio-empleados-api
```

### Usando Docker Compose
```bash
# Iniciar servicios
docker-compose up

# Iniciar en segundo plano
docker-compose up -d

# Detener servicios
docker-compose down

# Ver logs
docker-compose logs -f
```

## Variables de Entorno

Configurar las siguientes variables en el archivo `.env`:

```env
FLASK_APP=app
FLASK_ENV=development
DATABASE_URL=sqlite:///database.db
SECRET_KEY=tu_clave_secreta_aqui
PORT=5000
```

## Modelo de Datos

### Empleado

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | Integer | Identificador único (PK) |
| nombre | String | Nombre completo del empleado |
| email | String | Correo electrónico |
| departamento | String | Departamento al que pertenece |
| puesto | String | Cargo o puesto |
| fecha_ingreso | DateTime | Fecha de ingreso a la empresa |

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Autor

**claun0ch3**

- GitHub: [@claun0ch3](https://github.com/claun0ch3)

## Agradecimientos

- Flask por el excelente framework web
- La comunidad de Python por las herramientas y librerías

## Soporte

Si tienes alguna pregunta o problema, por favor abre un [issue](https://github.com/claun0ch3/DirectorioEmpleadosAPI/issues) en el repositorio.

---

Si este proyecto te fue útil, considera darle una estrella en GitHub
