========================
    Recurso empresas
========================

Recurso POST
------------

.. http:post:: /api/v1/enterprises

Crea una empresa en la plataforma

**Campos Obligatorios**

:name: **(string)** Nombre de la empresa
:nit: **(string)** Nit de la empresa
:email: **(string)** Correo de la empresa
:password: **(string)** Contraseña de la empresa. Tamaño mínimo de 7 caracteres
:state: **(string)** Departamento. Solo se permiten los valores que se consultan en el recurso GET /country
:city: **(string)** Ciudad
:address: **(string)** Direccion. Se permite una string que contenga la direccion de residencia

**Ejemplo de petición**

.. sourcecode:: http

    POST /api/v1/enterprises HTTP/1.1
    Content-Type: application/json

    {
        "name": "",
        "nit":"1234567894",
        "email": "micorreo@correo.com",
        "password": "MiContraseña!*",
        "state":"Risaralda",
        "city": "Pereira",
        "address": "Calle 80 #32 - 29"
    }

**Ejemplos de respuesta**

.. sourcecode:: http

    HTTP/1.1 201 CREATED
    {
        "inserted":1
    }

.. sourcecode:: http

    HTTP/1.1 400 BAD_REQUEST
    Content-Type: application/json

    {
        "code": "invalid_body",
        "detail": "Cuerpo con estructura inválida",
        "data": {
            "gender": [
                "Este campo es requerido."
             ]
        }
    }

.. sourcecode:: http

    HTTP/1.1 409 CONFLICT
    {
        "code": "user_already_exist",
        "detailed": "El usuario ya existe en la base de datos"
    }

:status 201: Empresa creada creado
:status 400: Cuerpo con estructura inválida
:status 409: La empresa ya existe