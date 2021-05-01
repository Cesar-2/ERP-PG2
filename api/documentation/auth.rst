===============================
    Recurso Autentificacion
===============================

Recurso POST
------------

    .. http:post:: /api/v1/auth

    Crea un token para la sesion

    * **Campos Obligatorios**

        :email: **(string)** Correo de la empresa
        :password: **(string)** Contraseña de la cuenta de la empresa
        :keep_logged_in: **(boolean)** Estar logeado en la cuenta

    * **Ejemplo de petición**

        .. sourcecode:: http

            POST /api/v1/auth HTTP/1.1
            Content-Type: application/json

            {
                "email":"rodrigo@gmail.com",
                "password":"astaroth2021",
                "keep_logged_in":true
            }
    * **Ejemplos de respuesta**

        .. sourcecode:: http

            HTTP/1.1 201 CREATED

        .. sourcecode:: http

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: application/json

            {
                "code": "invalid_filtering_params",
                "detailed": "Parámetros de búsqueda inválidos",
                "data": {
                    "keep_logged_in": [
                        "required field"
                    ]
                }
            }
        
        .. sourcecode:: http

            HTTP/1.1 404 NOT FOUND
            Content-Type: application/json

            {
                "code": "enterprise_not_found",
                "detailed": "Empresa no encontrada"
            }

        .. sourcecode:: http
            HTTP/1.1 401 UNAUTHORIZED

    :status 201: Token creado
    :status 400: Cuerpo con estructura inválida
    :statys 401: No autorizado
    :status 404: Empresa no encontrada
