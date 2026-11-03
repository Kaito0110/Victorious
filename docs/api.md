# API de Victorious

## 1. Información general

- Tecnología: Python + Flask
- Contenedor: Docker
- Servidor: Amazon EC2
- Base de datos: Amazon DynamoDB
- Tabla: Productos
- Región AWS: us-east-1
- Puerto: 5000

## 2. URL del backend

**URL base:**

`http://98.84.176.111:5000`

El backend está desplegado en EC2 y puede recibir peticiones desde internet.

## 3. Endpoints disponibles

### GET /

Comprueba que el backend está funcionando.

Respuesta esperada:

```json
{
  "message": "Bienvenido a la API de Victorious"
}
```

Estado: Probado desde internet.

### GET /productos

Consulta todos los productos almacenados en DynamoDB.

URL:

`http://98.84.176.111:5000/productos`

Estado: Probado desde internet. Se obtuvieron correctamente los productos registrados en la tabla.

### POST /productos

Registra un nuevo producto en DynamoDB.

URL:

`http://98.84.176.111:5000/productos`

Método: POST

Content-Type: application/json

Ejemplo del cuerpo:

```json
{
  "producto_id": "TEST001",
  "nombre": "Album de prueba",
  "categoria": "cd",
  "precio": 200,
  "stock": 8,
  "imagen_url": "https://example.com/test.jpg"
}
```

Respuesta esperada: 201 Created.

Estado: Probado desde Postman y verificado en DynamoDB.

## 4. Configuración para API Gateway

El equipo puede utilizar la siguiente URL como destino de la integración HTTP:

`http://98.84.176.111:5000`

Rutas que deben configurarse:

- GET /productos
- POST /productos

Tipo de integración sugerido: HTTP Proxy.

## 5. Infraestructura desplegada

- Instancia EC2: Victorious-Backend
- Sistema operativo: Amazon Linux 2023
- Contenedor: victorious-container
- Imagen Docker: victorious-backend
- Puerto expuesto: 5000
- Perfil IAM: LabInstanceProfile
- Base de datos: DynamoDB (Productos)