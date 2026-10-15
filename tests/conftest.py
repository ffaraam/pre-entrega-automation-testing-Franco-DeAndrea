import base64
from datetime import datetime
from pathlib import Path
import re
import warnings

import pytest
from pytest_html import extras


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()

    # Captura el fallo antes de que la fixture cierre el navegador.
    if reporte.when not in ("setup", "call") or not reporte.failed:
        return

    navegador = item.funcargs.get("driver")
    if navegador is None:
        return

    try:
        carpeta = Path(item.config.rootpath) / "reports" / "screenshots"
        carpeta.mkdir(parents=True, exist_ok=True)
        nombre = re.sub(r"[^a-zA-Z0-9_-]", "_", item.nodeid)
        fecha = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        archivo = carpeta / f"{nombre}_{reporte.when}_{fecha}.png"
        captura = navegador.get_screenshot_as_base64()

        # Usa la misma imagen para el archivo PNG y el HTML autocontenido.
        archivo.write_bytes(base64.b64decode(captura))
        reporte.extras = getattr(reporte, "extras", []) + [
            extras.png(captura, name="Captura del fallo")
        ]
    except Exception as error:
        # Un problema al capturar no debe ocultar el fallo original del test.
        warnings.warn(f"No se pudo guardar la captura de {item.nodeid}: {error}")
