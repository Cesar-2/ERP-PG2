========================
    Recurso empresas
========================

Recurso POST
--------------

    .. http:post:: /api/v1/employer

    Crea un empleado de la empresa en la plataforma

    * **Campos Obligatorios**

        :name: **(string)** Nombre del empleado
        :last_name: **(string)** Apellido del empleado
        :initiation_date: **(date)** Fecha de inicio en la empresa
        :birthdate: **(date)** Fecha nacimiento del empleado
        :document: **(string)** Documento del empleado
        :email: **(string)** Correo del empleado
        :cellphone: **(string)** Celular del empleado
        :work_from_home: **(boolean)** Es remoto
        :job_tittle: **(string)** Cargo del empleado
        :address: **(string)** Direccion del empleado
        :state: **(string)** Departamento del empleado
        :city: **(string)** Ciudad del empleado
        :eps: **(string)** EPS del empleado
        :password: **(string)** Contraseña del empleado

    * **Ejemplo de petición**

        .. sourcecode:: http

            POST /api/v1/enterprise HTTP/1.1
            Content-Type: application/json
            Authorization: Bearer eydsfgfdhndfjsafdssddfds

            {
                "name": "Carlos",
                "last_name": "Lopez",
                "initiation_date": "2021-05-04",
                "birthdate": "1994-05-02",
                "document": "32161551",
                "email": "test@test.com",
                "cellphone": "3216457444",
                "work_from_home": true,
                "job_tittle": "Tech lead",
                "address": "Calle main #32 52 -45",
                "state": "Risaralda",
                "city": "Pereira",
                "eps": "SURA",
                "password": "123456789"
            },

    * **Ejemplos de respuesta**

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

    :status 201: Empresa creado
    :status 400: Cuerpo con estructura inválida
    :status 403: No tiene los permisos necesarios

Recurso GET
------------

    .. http:post:: /api/v1/employer

    Retorna todos los empleados de la empresa en la plataforma

    * **Ejemplo de petición**

        .. sourcecode:: http

            GET /api/v1/enterprise HTTP/1.1
            Content-Type: application/json
            Authorization: Bearer eydsfgfdhndfjsafdssddfds

    * **Ejemplos de respuesta**

        .. sourcecode:: http

            HTTP/1.1 200 OK
            {
                "count": 0,
                "results": []
            }



    :status 200: Empresa creado
    :status 401: El token es incorrecto o expiro
    :status 403: No tiene los permisos necesarios