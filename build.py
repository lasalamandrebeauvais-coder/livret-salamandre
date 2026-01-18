import os
import subprocess
import sys

# --- 1. CONFIGURATION DU SITE (CONTENU) ---
html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Livret d'Accueil - La Salamandre</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script>
        tailwind.config = { theme: { extend: { colors: { velours: '#800020', anthracite: '#333333', sable: '#FAFAFA', } } } }
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@400;700&display=swap" rel="stylesheet">
    <style>body { font-family: 'Lato', sans-serif; background-color: #FAFAFA; }</style>
</head>
<body class="pb-24 text-anthracite">
    <header class="bg-white pt-8 pb-6 px-4 text-center shadow-sm relative">
        <div class="absolute top-4 right-4 flex space-x-2 grayscale opacity-50"><span>🇫🇷</span><span>🇬🇧</span><span>🇪🇸</span><span>🇮🇹</span></div>
        <div class="mx-auto w-32 h-32 rounded-full overflow-hidden border-4 border-velours shadow-lg mb-4">
            <img src="stephane.jpg" alt="Stéphane" class="w-full h-full object-cover">
        </div>
        <h1 class="text-2xl font-bold text-velours mb-1" style="font-family: 'Playfair Display'">Bienvenue à La Salamandre</h1>
        <p class="text-gray-600 text-lg italic">"Bonjour, je suis Stéphane."</p>
        <p class="text-xs font-bold mt-2 uppercase tracking-wide text-velours">Un p'tit clic et je m'occupe du reste</p>
    </header>

    <main class="px-4 py-6 max-w-md mx-auto space-y-6">
        <div class="bg-white p-5 rounded-xl shadow-sm border border-gray-100">
            <h3 class="font-bold text-lg mb-2"><i class="fas fa-wifi text-velours mr-2"></i>Wi-Fi</h3>
            <div class="flex justify-between items-center bg-gray-50 p-3 rounded-lg border border-gray-200">
                <p class="font-mono text-velours font-bold" id="wifi-code">lasalamandre15052015</p>
                <button onclick="copyWifi()" class="text-sm bg-gray-200 px-3 py-1 rounded hover:bg-gray-300 transition">Copier</button>
            </div>
            <p id="copy-msg" class="text-center text-green-600 text-xs mt-2 hidden">Copié !</p>
        </div>

        <div class="grid grid-cols-2 gap-4">
            <div class="bg-white p-4 rounded-xl shadow-sm text-center">
                <i class="fas fa-coffee text-2xl text-velours mb-2"></i>
                <h3 class="font-bold text-sm">Petit-Dej</h3>
                <p class="text-xs text-gray-600">Sem: 07h15-09h00</p>
                <p class="text-xs text-gray-600">WE: 08h30-10h00</p>
            </div>
            <div class="bg-white p-4 rounded-xl shadow-sm text-center">
                <i class="fas fa-suitcase text-2xl text-velours mb-2"></i>
                <h3 class="font-bold text-sm">Départ</h3>
                <p class="text-xs text-gray-600">Avant 11h00</p>
            </div>
        </div>

        <h2 class="text-xl font-bold text-velours" style="font-family: 'Playfair Display'">Mes Adresses</h2>
        
        <div class="bg-white p-5 rounded-xl shadow-sm border-l-4 border-velours">
            <h3 class="font-bold text-lg">La Bohemia</h3>
            <p class="text-gray-600 italic text-sm mt-1">"Je vous le recommande pour sa belle ambiance sympathique."</p>
            <div class="flex gap-2 mt-3">
                <a href="tel:+33344450000" class="flex-1 py-2 text-center text-sm border rounded hover:bg-gray-50">Appeler</a>
                <a href="https://www.google.com/maps/search/?api=1&query=La+Bohemia+Beauvais" target="_blank" class="flex-1 py-2 text-center text-sm bg-velours text-white rounded hover:opacity-90">Y aller</a>
            </div>
        </div>

        <div class="bg-white p-5 rounded-xl shadow-sm border-l-4 border-velours">
            <h3 class="font-bold text-lg">La Place</h3>
            <p class="text-gray-600 italic text-sm mt-1">"Mon conseil : allez-y pour découvrir leur menu qui change toutes les semaines."</p>
            <div class="flex gap-2 mt-3">
                <a href="tel:+33344450000" class="flex-1 py-2 text-center text-sm border rounded hover:bg-gray-50">Appeler</a>
                <a href="https://www.google.com/maps/search/?api=1&query=La+Place+Beauvais" target="_blank" class="flex-1 py-2 text-center text-sm bg-velours text-white rounded hover:opacity-90">Y aller</a>
            </div>
        </div>

        <div class="bg-white p-5 rounded-xl shadow-sm border-l-4 border-velours">
            <h3 class="font-bold text-lg">L'Autrement</h3>
            <p class="text-gray-600 italic text-sm mt-1">"Pour une soirée d'exception, le gastronome vous attend."</p>
            <div class="flex gap-2 mt-3">
                <a href="tel:+33344450000" class="flex-1 py-2 text-center text-sm border rounded hover:bg-gray-50">Appeler</a>
                <a href="https://www.google.com/maps/search/?api=1&query=Restaurant+L'Autrement+Beauvais" target="_blank" class="flex-1 py-2 text-center text-sm bg-velours text-white rounded hover:opacity-90">Y aller</a>
            </div>
        </div>
        
        <h2 class="text-xl font-bold text-velours" style="font-family: 'Playfair Display'">Mobilité</h2>
        <a href="https://www.corolis.fr" target="_blank" class="block bg-white p-4 rounded-xl shadow-sm flex justify-between items-center">
            <div class="flex items-center"><span class="bg-yellow-400 text-white font-bold w-8 h-8 flex items-center justify-center rounded-full mr-3">6</span><div><h3 class="font-bold text-sm">Bus Ligne 6</h3><p class="text-xs text-gray-500">Aéroport / Centre</p></div></div><i class="fas fa-chevron-right text-gray-300"></i>
        </a>
        <a href="https://www.sncf-connect.com/gare/beauvais" target="_blank" class="block bg-white p-4 rounded-xl shadow-sm flex justify-between items-center">
            <div class="flex items-center"><i class="fas fa-train w-8 text-center mr-3 text-gray-400 text-xl"></i><div><h3 class="font-bold text-sm">Gare SNCF</h3><p class="text-xs text-gray-500">Trains vers Paris</p></div></div><i class="fas fa-chevron-right text-gray-300"></i>
        </a>
        <a href="tel:0344454400" class="block bg-white p-4 rounded-xl shadow-sm flex justify-between items-center border-l-4 border-yellow-400">
            <div class="flex items-center"><i class="fas fa-taxi w-8 text-center mr-3 text-gray-400 text-xl"></i><div><h3 class="font-bold text-sm">Taxi Beauvais</h3><p class="text-xs text-gray-500">Appel direct</p></div></div><i class="fas fa-phone text-velours"></i>
        </a>

        <div class="text-center text-gray-400 text-xs mt-8 pb-8">
            <p>La Salamandre • 10 rue Marcelle Geudelin, Beauvais</p>
        </div>
    </main>

    <div class="fixed bottom-0 w-full bg-white border-t p-4 shadow-lg flex justify-between z-40">
        <div class="flex flex-col"><span class="text-xs text-gray-500">Envie de revenir ?</span><a href="https://lasalamandre-beauvais.fr" class="text-velours font-bold text-sm">Réserver</a></div>
        <a href="https://lasalamandre-beauvais.fr" class="bg-velours text-white px-6 py-2 rounded-full font-bold shadow-lg text-sm">Réserver</a>
    </div>
    <a href="https://wa.me/33600000000" class="fixed bottom-24 right-4 bg-green-500 text-white w-14 h-14 rounded-full flex items-center justify-center shadow-xl z-50 animate-bounce"><i class="fab fa-whatsapp text-3xl"></i></a>

    <script>
        function copyWifi() {
            navigator.clipboard.writeText(document.getElementById('wifi-code').innerText);
            document.getElementById('copy-msg').classList.remove('hidden');
            setTimeout(()=>document.getElementById('copy-msg').classList.add('hidden'), 2000);
        }
    </script>
</body>
</html>
"""

# --- 2. GENERATION DU FICHIER HTML ---
print("🏗️  Création du fichier index.html...")
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
print("✅ index.html créé avec succès.")

# --- 3. INSTALLATION AUTOMATIQUE DU MODULE QRCODE ---
print("🔧 Vérification de l'outil QR Code...")
try:
    import qrcode
except ImportError:
    print("📥 Installation de la librairie 'qrcode' en cours...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "qrcode[pil]"])
    import qrcode

# --- 4. GENERATION DU QR CODE ---
print("📷 Génération du QR Code...")
url_livret = "https://lasalamandre-beauvais.fr/livret-accueil" # À changer quand le site sera en ligne
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data(url_livret)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode_salamandre.png")
print("✅ qrcode_salamandre.png généré.")

print("\n🚀 TOUT EST PRÊT ! Ouvrez index.html pour voir le résultat.")