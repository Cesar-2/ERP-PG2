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
            
            {
                "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHBpcmF0aW9uX2RhdGUiOiIyMDIxLTA1LTI1IDE5OjQ5OjQxLjAxOTQxMCIsImVtYWlsIjoiYWRtaW5AYWRtaW4uY29tIiwibW9kdWxlcyI6WyJOb21pbmEiLCJJbmZvcm1lcyIsIlZhbG9yYWNpb24iLCJFbXBsZWFkb3MiXSwicmVmcmVzaCI6ImY1WTN1N1daM1RlNDZsdEZINVNIY21yS2ZIdTl0YyJ9.C0Nv1J5wghUd8fUAoYGGT6sIyhIo19F0qVd-6tY2hu4",
                "refresh": "f5Y3u7WZ3Te46ltFH5SHcmrKfHu9tc",
                "name": "Lolero",
                "modules": [
                    "Nomina"
                ]
            }

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
