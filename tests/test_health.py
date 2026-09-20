def test_health_devuelve_200(cliente):
    respuesta = cliente.get("/health")
    assert respuesta.status_code == 200

def test_health_formato_correcto(cliente):
    respuesta = cliente.get("/health")
    datos = respuesta.get_json()
    assert datos["status"] == "ok"
    assert datos["service"] == "alojamientos-api"
    assert datos["version"] == "v1"

def test_health_cors_activado(cliente):
    respuesta = cliente.get("/health")
    assert "Access-Control-Allow-Origin" in respuesta.headers