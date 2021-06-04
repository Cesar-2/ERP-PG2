==========================
    Recurso Valoracion
==========================

Recurso POST
--------------

    .. http:post:: /api/v1/assessment

    Crea una evaluacion de un empleado en la plataforma

    * **Campos Obligatorios**

        :type: **(string)** Clase de evaluacion
        :employee_evaluated: **(string)** Pk del empleado evaluado
        :employee_evaluator: **(string)** Pk del empleado evaluador
        :qualification:  **(string)** Nota de la calificacion

    * **Ejemplo de petición**

        .. sourcecode:: http

            POST /api/v1/assessment HTTP/1.1
            Content-Type: application/json
            Authorization Bearer eyyetrjhhggsdgffsgdhkjg

            {
                "type":"Asistencia",
                "employee_evaluated":1,
                "employee_evaluator":1,
                "feedback":"Asistio a todas las capacitaciones"
                "qualification":85
            }
    
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
                    "qualification": [
                        "Este campo es requerido."
                    ]
                }
            }

    :status 201: Evaluacion creada
    :status 400: Parámetros de búsqueda inválidos
    :status 401: El token es incorrecto o expiro
    :status 403: No tiene los permisos necesarios

Recurso get
-------------

    Retorna una evaluacion de los empleados de una empresa en la plataforma

    * **Ejemplo de petición**

        .. sourcecode:: http

            GET /api/v1/assessment HTTP/1.1
            Content-Type: application/json
            Authorization Bearer eyyetrjhhggsdgffsgdhkjg
            Range: 0-9

    * **Ejemplo de respuesta**

        .. sourcecode:: http

            {
                "count": 0,
                "results": []
            }

    :status 200: Operacion exitosa
    :status 401: El token es incorrecto o expiro
    :status 403: No tiene los permisos necesarios