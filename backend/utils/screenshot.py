import requests
import os
import os.path
from datetime import datetime

def capturar_screenshot(url, nome_projeto):
    API_KEY = os.getenv("SCREENSHOT_API_KEY")
    if not API_KEY:
        print("Erro: API Key da ScreenshotAPI não encontrada.")
        return ""

    if not url:
        print("Erro: URL vazia para capturar screenshot.")
        return ""

    # Define diretório de saída absoluto e cria se não existir
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'static', 'img', 'projetos')
    os.makedirs(output_dir, exist_ok=True)

    # Formata nome de arquivo com timestamp para evitar sobrescritas
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    safe_name = nome_projeto.lower().replace(" ", "_")
    filename = f"{safe_name}_{timestamp}.png"
    output_path = os.path.join(output_dir, filename)

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
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"Screenshot salva em: {output_path}")
        # Retorna caminho relativo à pasta 'backend/' para uso em templates
        return output_path.replace(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + os.sep, "")
    except Exception as e:
        print("Erro ao capturar screenshot:", str(e))
        return ""