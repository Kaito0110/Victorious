
import os

import boto3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Configuración de DynamoDB
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
TABLE_NAME = os.getenv("TABLE_NAME", "Productos")

dynamodb = boto3.resource(
    "dynamodb",
    region_name=AWS_REGION
)

table = dynamodb.Table(TABLE_NAME)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Bienvenido a la API de Victorious"
    })


@app.route("/productos", methods=["GET"])
def get_productos():
    try:
        response = table.scan()
        productos = response.get("Items", [])

        return jsonify(productos), 200

    except Exception as error:
        return jsonify({
            "error": str(error)
        }), 500

@app.route("/productos", methods=["POST"])
def crear_producto():
    try:
        data = request.get_json()

        campos_requeridos = [
            "producto_id",
            "nombre",
            "categoria",
            "precio",
            "stock",
            "imagen_url"
        ]

        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({
                "error": "Faltan campos obligatorios"
            }), 400

        table.put_item(
            Item={
                "producto_id": data["producto_id"],
                "nombre": data["nombre"],
                "categoria": data["categoria"],
                "precio": int(data["precio"]),
                "stock": int(data["stock"]),
                "imagen_url": data["imagen_url"]
            },
            ConditionExpression="attribute_not_exists(producto_id)"
        )

        return jsonify({
            "message": "Producto creado correctamente",
            "producto": data
        }), 201

    except Exception as error:
        return jsonify({
            "error": str(error)
        }), 500
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
