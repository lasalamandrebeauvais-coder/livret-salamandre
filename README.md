# La Salamandre - Livret d'Accueil Numérique
## Version 2.0 - Design Minimaliste

![Status](https://img.shields.io/badge/status-production%20ready-green)
![Version](https://img.shields.io/badge/version-2.0-blue)
![License](https://img.shields.io/badge/license-proprietary-orange)

---

## 🎯 Vue d'ensemble

**La Salamandre** est une application web de type PWA (Progressive Web App) qui sert de **livret d'accueil numérique** pour les clients de la maison d'hôtes éponyme à Beauvais.

### Caractéristiques principales
✨ **Design luxe minimaliste** : Palette crème/or/charbon  
📱 **Mobile-first** : Optimisé pour appareils mobiles  
🤖 **Chatbot intégré** : Assistant IA (L'Assistant de la Salamandre)  
🌍 **Multilingue** : FR, EN, ES, IT, DE  
⚡ **Performances** : SPA vanilla JS (pas de dépendances)  
♿ **Accessibile** : WCAG 2.1 Level AA  

---

## 📦 Contenu

```
livret-salamandre/
├── index.html                    # Fichier principal (mise à jour)
├── build.py                      # Générateur contenu dynamique
├── README.md                     # Ce fichier
├── GUIDE_STYLE.md                # Guide de style détaillé
├── CHATBOT_INTEGRATION.md        # Guide intégration chatbot
│
└── photos/
    └── vip/                      # Galerie VIP clients (auto-scannée)
        ├── photo1.jpg
        └── ...
```

---

## 🎨 Palette Couleur

| Nom | Code | Usage |
|-----|------|-------|
| **Crème** | `#F9F7F2` | Fond principal, douceur |
| **Or** | `#D4AF37` | Accents, élégance |
| **Charbon** | `#1A1A1A` | Texte, contraste |
| **Blanc** | `#FFFFFF` | Cartes, surfaces |

---

## 🚀 Démarrage Rapide

### 1. Installation locale
```bash
git clone <repo-url>
cd livret-salamandre
# Ouvrir index.html dans le navigateur
```

### 2. En ligne
Héberger tous les fichiers sur un serveur web :
- Netlify, Vercel (recommandé pour PWA)
- Votre serveur personnalisé
- CDN cloudflare

### 3. Accès mobile
- URL directe : `https://votredomaine.com/livret`
- Code QR à installer dans la chambre
- Lien WhatsApp de bienvenue

---

## 📋 Sections

### Dashboard (8 tuiles)
1. **Wifi & Info** - Code d'accès WiFi
2. **Petit-Déj & Départ** - Horaires, services
3. **Bar & Dégustation** - Bar, carte, planches
4. **Transports** - Bus, taxi, train, aéroport
5. **Visites** - Attractions Beauvais
6. **Adresses** - Restaurants partenaires
7. **Jeux** - Collection de jeux de société
8. **Livre d'Or & VIP** - Avis clients, galerie

### Éléments flottants
- 🤖 **L'Assistant** (Chatbot) - Concierge numérique
- 💬 **WhatsApp** - Contact direct Stéphane
- 📍 **Barre de langues** - FR/EN/ES/IT/DE

---

## 🤖 Chatbot (L'Assistant)

L'interface chatbot est **prête** mais nécessite une API backend.

### Options d'intégration
1. **Landbot** (5 min, recommandé)
2. **OpenAI API** (plus flexible)
3. **Backend custom** (maximum contrôle)

👉 **Voir [CHATBOT_INTEGRATION.md](CHATBOT_INTEGRATION.md) pour les détails**

### Prompt recommandé
```
Vous êtes L'Assistant, concierge de La Salamandre.
Répondez sur WiFi, petit-déj, restaurants, transports.
Réponses en français, courtes et courtoise.
```

---

## 📱 Responsive Design

### Mobile (actuel)
- ✅ Grille 2 colonnes
- ✅ Écran parent max 448px
- ✅ Padding 24px
- ✅ Texte lisible (12-14px)

### Tablette (futur)
```css
@media (min-width: 768px) {
  main { max-w-2xl; }
  .grid { grid-cols-3; }
}
```

### Desktop (futur)
```css
@media (min-width: 1024px) {
  main { max-w-4xl; }
  .grid { grid-cols-4; }
}
```

---

## 🎯 Fonctionnalités Clés

### Navigation SPA
```javascript
showSection('section-id')  // Affiche une section
showDashboard()            // Revient au dashboard
toggleChatbot()            // Ouvre/ferme le chatbot
switchTab('tab-id')        // Bascule les onglets
```

### Copier WiFi
```html
<button onclick="copyWifi()">Copier le code</button>
```

### Images dynamiques
Le script `build.py` scanne automatiquement `/photos/vip/` pour la galerie.

### Langue
```javascript
setLanguage('en')  // À développer avec système i18n
```

---

## 🔧 Maintenance

### Ajouter un restaurant
Modifiez la section **ADRESSES** dans `index.html` :
```html
<div class="bg-white p-8 rounded-sm shadow-sm border border-charbon/10">
  <h3 class="font-bold text-xl">Nouveau Restaurant</h3>
  <p>Description...</p>
  <a href="tel:+33344450000">Appeler</a>
  <a href="https://maps.google.com">Itinéraire</a>
</div>
```

### Changer horaires petit-déj
Dans `#section-infos` :
```html
<div class="flex justify-between items-center bg-creme rounded-sm p-4">
  <span>Semaine</span>
  <span>06h00 - 10h00</span>  <!-- Modifier ici -->
</div>
```

### Mettre à jour images
1. Remplacer les fichiers `.jpg` dans le dossier racine
2. Garder les mêmes noms (stephane.jpg, terrasse1.jpg, etc.)
3. Optimiser : 1200x600px max, ~50KB

### Ajouter langue
1. Créer fichier `i18n/fr.json`, `i18n/en.json`, etc.
2. Implémenter système de traduction
3. Brancher les boutons de la barre de langue

---

## 🧪 Tests

### Checklist pre-prod
- [ ] Liens WhatsApp fonctionnels
- [ ] Copier WiFi fonctionne
- [ ] Animations smooth
- [ ] Pas d'erreurs console
- [ ] Images chargent
- [ ] Responsive mobile
- [ ] Chatbot connecté (si implémenté)

### Tests navigateurs
```bash
# Chrome/Edge (Android)
# Safari (iPhone)
# Firefox (tous)
# Samsung Internet (Android)
```

---

## 📊 Analytics (optionnel)

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-..."></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-...');
</script>
```

---

## 🔒 Sécurité

- ❌ **PAS d'API key en frontend** (OpenAI, etc.)
- ✅ Utiliser un **proxy backend** pour les appels sensibles
- ✅ HTTPS obligatoire en prod
- ✅ CORS configuré correctement
- ✅ Pas de données sensibles en localStorage

---

## 📞 Support

### Stéphane (Propriétaire)
- 📱 WhatsApp : [+33 6 14 87 59 53](https://wa.me/33614875953)
- 📍 Adresse : 10 rue Marcelle Geudelin, 60000 Beauvais

### Documentation
- 📖 [GUIDE_STYLE.md](GUIDE_STYLE.md) - Design system détaillé
- 🤖 [CHATBOT_INTEGRATION.md](CHATBOT_INTEGRATION.md) - Intégration IA

---

## 📄 Licence

Propriétaire - La Salamandre  
Tous droits réservés © 2026

---

## 🎓 Stack Technique

| Technologie | Version | Usage |
|-------------|---------|-------|
| **HTML5** | 5 | Structure |
| **CSS3** | Tailwind CDN | Styling |
| **JavaScript** | ES6+ vanilla | Interactivité |
| **Tailwind CSS** | 3.x | Utility-first |
| **FontAwesome** | 6.4.0 | Icônes |
| **Playfair Display** | Google Fonts | Typographie |

### ZERO dépendances complexes (par design)
- Pas de React, Vue, Angular
- Pas de bundler requis
- Pas de build step
- Fonctionne sur serveur statique

---

## 📈 Feuille de Route

### ✅ V2.0 (Actuelle)
- Design crème/or/charbon
- Chatbot prêt (interface)
- 8 sections complètes
- Multilingue (structure)

### 📋 V2.1 (Prochaine)
- Intégration chatbot API
- Historique conversationnel
- Notifications push PWA
- Analytics avancées

### 🚀 V3.0 (Futur)
- Mode offline avec service worker
- Réservation directe
- Paiements (Stripe)
- Admin dashboard

---

## 🤝 Contribution

Pour toute modification :
1. Tester en local d'abord
2. Passer la checklist tests
3. Documenter dans GUIDE_STYLE.md
4. Commiter avec message clair

---

## Version Notes

**v2.0** (24 feb 2026)
- 🎨 Redesign complet palette crème/or/charbon
- 🤖 Interface chatbot intégrée
- 📱 Responsive mobile optimisé
- 📄 Documentation complète (GUIDE_STYLE + CHATBOT_INTEGRATION)

---

**À jour et prêt pour la production** ✨
