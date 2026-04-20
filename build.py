#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build script pour La Salamandre v2.1
Lit template.html, genere la galerie VIP dynamiquement, et cree index.html
"""

import os
import sys

# --- CONFIGURATION ---
TEMPLATE_FILE = "template.html"
OUTPUT_FILE = "index.html"
VIP_PHOTOS_DIR = "photos/vip"

def generate_vip_gallery():
    """Genere le HTML de la galerie VIP en scannant le dossier photos/vip"""
    vip_gallery_html = ""
    
    if not os.path.exists(VIP_PHOTOS_DIR):
        # Dossier n'existe pas - afficher placeholder
        vip_gallery_html = """<div class="col-span-2 text-center py-8">
                                <div class="inline-block p-4 rounded-sm bg-creme text-charbon/30 mb-3">
                                    <i class="fas fa-camera text-2xl"></i>
                                </div>
                                <p class="text-sm text-charbon/50">La galerie est vide pour l'instant.</p>
                                <p class="text-xs text-charbon/30 mt-1">Ajoutez vos photos dans le dossier photos/vip et renommez-les en 1.jpg, 2.jpg... pour qu'elles apparaissent.</p>
                            </div>"""
        return vip_gallery_html
    
    # Scanner le dossier pour les images
    try:
        vip_files = [f for f in os.listdir(VIP_PHOTOS_DIR) 
                     if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    except PermissionError:
        print(f"?? Erreur : Impossible d'acceder au dossier '{VIP_PHOTOS_DIR}'", file=sys.stderr)
        vip_files = []
    
    if vip_files:
        vip_gallery_html = '<div class="grid grid-cols-2 gap-4">'
        for idx, photo in enumerate(sorted(vip_files), 1):
            photo_path = f"{VIP_PHOTOS_DIR}/{photo}"
            name = os.path.splitext(photo)[0].replace('_', ' ').title()
            vip_gallery_html += f"""
                        <div class="bg-white p-2 rounded-sm shadow-sm overflow-hidden">
                            <div class="aspect-[3/4] bg-charbon/20 rounded-sm overflow-hidden relative group">
                                <img src="{photo_path}" class="w-full h-full object-cover group-hover:scale-105 transition duration-500" alt="{name}">
                                <div class="absolute bottom-0 left-0 w-full bg-gradient-to-t from-charbon/80 to-transparent p-2">
                                    <span class="text-white text-[10px] font-bold">{name}</span>
                                </div>
                            </div>
                        </div>"""
        vip_gallery_html += '\n                    </div>'
    else:
        # Dossier vide
        vip_gallery_html = """<div class="col-span-2 text-center py-8">
                                <div class="inline-block p-4 rounded-sm bg-creme text-charbon/30 mb-3">
                                    <i class="fas fa-camera text-2xl"></i>
                                </div>
                                <p class="text-sm text-charbon/50">La galerie est vide pour l'instant.</p>
                                <p class="text-xs text-charbon/30 mt-1">Ajoutez vos photos dans le dossier photos/vip et renommez-les en 1.jpg, 2.jpg... pour qu'elles apparaissent.</p>
                            </div>"""
    
    return vip_gallery_html


def build():
    """Construit le fichier index.html a partir du template"""
    
    print("Building La Salamandre v2.1...")
    
    # Verifier l'existence du template
    if not os.path.exists(TEMPLATE_FILE):
        print(f"ERROR: Le fichier '{TEMPLATE_FILE}' n'existe pas.", file=sys.stderr)
        print("Assurez-vous que 'template.html' est present dans le repertoire courant.", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Lire le template
        with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Generer la galerie VIP
        vip_gallery_html = generate_vip_gallery()
        
        # Remplacer le placeholder
        html_content = html_content.replace("{vip_gallery_html}", vip_gallery_html)
        
        # Ecrire le fichier final
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Afficher le statut
        photo_count = len([f for f in os.listdir(VIP_PHOTOS_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]) if os.path.exists(VIP_PHOTOS_DIR) else 0
        print(f"✓ Template '{TEMPLATE_FILE}' charge")
        print(f"✓ Galerie VIP trouvee: {photo_count} photos")
        print(f"✓ Fichier '{OUTPUT_FILE}' genere avec succes")
        print("\nPret a deployer! Ouvrez http://localhost:8000 pour tester.")
        
    except FileNotFoundError as e:
        print(f"ERROR: Fichier non trouve - {e}", file=sys.stderr)
        sys.exit(1)
    except PermissionError as e:
        print(f"ERROR: Permission refusee - {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Erreur inattendue - {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    build()
