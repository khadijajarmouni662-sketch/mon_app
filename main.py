from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Khadija Jarmouni - Licence GPTACQ</title>
        <style>
            body { margin:0; font-family: Arial, sans-serif; background:#f0f4ff; color:#1a1a1a; text-align:center; }
            .header { background: linear-gradient(135deg, #1e3a8a, #4f46e5); color:white; padding:60px 20px; }
            .header h1 { font-size:48px; margin:0; }
            .header h2 { font-size:24px; font-weight:normal; opacity:0.9; margin-top:10px; }
            .box { background:white; max-width:700px; margin:-30px auto 30px; padding:30px; border-radius:20px; box-shadow:0 10px 30px rgba(0,0,0,0.1); }
            .box h3 { color:#1e3a8a; font-size:26px; }
            .box p { font-size:18px; line-height:1.7; }
            .badge { display:inline-block; background:#e0e7ff; color:#1e3a8a; padding:8px 18px; border-radius:20px; margin:5px; font-weight:bold; }
            .footer { padding:20px; color:#666; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Khadija Jarmouni</h1>
            <h2>Licence Professionnelle - GPTACQ</h2>
            <p>Gestion de Projets et Techniques d'Animation et de Communication de Qualité</p>
        </div>
        <div class="box">
            <h3>Bienvenue sur mon application</h3>
            <p>Bonjour Monsieur, je suis <b>Khadija Jarmouni</b>, étudiante en Licence GPTACQ.<br>
            Cette application a été créée dans le cadre de mon projet.</p>
            <div>
                <span class="badge">Python</span>
                <span class="badge">FastAPI</span>
                <span class="badge">GitHub</span>
                <span class="badge">Render</span>
            </div>
            <p style="margin-top:25px;">Merci pour votre visite !</p>
        </div>
        <div class="footer">© 2026 - Khadija Jarmouni - Tous droits réservés</div>
    </body>
    </html>
    """
