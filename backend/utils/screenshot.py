import requests
import os
from datetime import datetime
from io import BytesIO
from backend.utils.s3_upload import upload_to_s3

def capturar_screenshot(url, nome_projeto):
    API_KEY = os.getenv("SCREENSHOT_API_KEY")
    if not API_KEY:
        print("Erro: API Key da ScreenshotAPI não encontrada.")
        return ""

    if not url:
        print("Erro: URL vazia para capturar screenshot.")
        return ""

    # Formata nome de arquivo com timestamp para evitar sobrescritas
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    safe_name = nome_projeto.lower().replace(" ", "_")
    filename = f"{safe_name}_{timestamp}.png"

    params = {
        "token": API_KEY,
        "url": url,
        "output": "image",
        "file_type": "png",
        "wait_for_event": "load"
    }

    try:
        response = requests.get("https://shot.screenshotapi.net/screenshot", params=params, timeout=30)
        response.raise_for_status()

        # Envia para S3 direto da memória
        image_bytes = BytesIO(response.content)
        image_url = upload_to_s3(image_bytes, filename)

        print(f"Screenshot enviada para S3: {image_url}")
        return image_url  # Retorna o link público direto do S3

    except Exception as e:
        print("Erro ao capturar e enviar screenshot:", str(e))
        return ""