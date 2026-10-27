import json

# Leer las herramientas desde el archivo JSON
with open('tools.json', 'r', encoding='utf-8') as f:
    tools = json.load(f)

# Generar el diseño HTML de la web
html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Top IA Tools - Directorio Automatizado</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; line-height: 1.6; color: #333; background: #f9f9f9; }
        h1 { text-align: center; color: #111; }
        .subtitle { text-align: center; color: #666; margin-bottom: 40px; }
        .tool-card { background: white; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
        .category { font-size: 0.85rem; color: #0066cc; font-weight: bold; text-transform: uppercase; }
        .btn { display: inline-block; background: #000; color: #fff; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin-top: 10px; font-weight: bold; }
        .btn:hover { background: #333; }
    </style>
</head>
<body>
    <h1>Directorio de Herramientas de IA</h1>
    <p class="subtitle">Las mejores soluciones de inteligencia artificial actualizadas automáticamente.</p>
"""

for tool in tools:
    html_content += f"""
    <div class="tool-card">
        <span class="category">{tool['category']}</span>
        <h2>{tool['name']}</h2>
        <p>{tool['description']}</p>
        <a class="btn" href="{tool['affiliate_link']}" target="_blank">Probar Herramienta</a>
    </div>
    """

html_content += """
</body>
</html>
"""

# Guardar el resultado en index.html (la página que mostrará GitHub Pages)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("¡Página web generada con éxito a partir de los datos!")
