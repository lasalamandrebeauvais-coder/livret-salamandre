# 📖 Guide de Style & Documentation
## LA SALAMANDRE - Livret d'Accueil Numérique

---

## 1️⃣ Architecture Technique

### Tech Stack
- **Framework** : Vanilla JavaScript + Tailwind CSS (CDN)
- **Type** : Single Page Application (SPA)
- **Responsive** : Mobile-first design (max-width: 28rem / 448px)
- **Accessibilité** : WCAG 2.1 AA

### Structure des fichiers
```
livret-salamandre/
├── index.html           # Fichier principal
├── build.py             # Générateur de contenu dynamique
├── photos/
│   └── vip/            # Galerie VIP (auto-scannée)
└── assets/
    ├── stephane.jpg
    ├── terrasse1.jpg
    ├── senteur.jpg
    ├── art.jpg
    └── telephone_rouge.jpg
```

---

## 2️⃣ Palette de Couleurs (Design System)

| Couleur | Code | Utilisation |
|---------|------|------------|
| **Crème** | `#F9F7F2` | Fond principal, surfaces secondaires |
| **Or** | `#D4AF37` | Accents, titres, bordures actives |
| **Charbon** | `#1A1A1A` | Texte principal, fonds sombres |
| **Blanc** | `#FFFFFF` | Cartes, fonds modulaires |

### Tailwind Configuration
```javascript
colors: {
  creme: '#F9F7F2',
  or: '#D4AF37',
  charbon: '#1A1A1A'
}
```

---

## 3️⃣ Typographie

### Polices
- **Titres** : `Playfair Display` (serif, élégante)
- **Corps** : System font stack (lisibilité optimale)

### Hiérarchie des titres
```
<h1> = 4xl, font-bold, tracking-widest, UPPERCASE
<h2> = 3xl, font-bold, text-charbon
<h3> = text-2xl, font-bold
<h4> = text-xl, font-bold
```

### Tailles de texte
- **Corps** : `text-sm` (14px)
- **Petit** : `text-xs` (12px)
- **Étiquettes** : `text-[10px]`

---

## 4️⃣ Composants Clés

### 1. **Tuile de Grille (Dashboard)**
```html
<button onclick="showSection('section-id')" 
  class="bg-white border border-charbon/10 p-6 rounded-sm 
         shadow-sm hover:border-or transition 
         flex flex-col items-center justify-center aspect-square group">
  <div class="text-or mb-3 group-hover:scale-110 transition-transform">
    <i class="fas fa-icon-name text-2xl"></i>
  </div>
  <span class="text-xs uppercase tracking-widest font-semibold">Titre</span>
</button>
```

**Points clés** :
- Aspect ratio 1:1 (carré)
- Coins arrondis minimaux (`rounded-sm`)
- Bordure grise légère (`border-charbon/10`)
- Icône orange au hover (`hover:border-or`)

### 2. **Carte d'Information**
```html
<div class="bg-white p-8 rounded-sm shadow-sm border border-charbon/10">
  <h3 class="font-bold text-xl text-charbon mb-4">Titre</h3>
  <p class="text-charbon/60 text-sm leading-relaxed">Contenu</p>
</div>
```

### 3. **Bouton Primaire**
```html
<button class="w-full bg-charbon text-white py-4 rounded-sm 
              font-bold text-xs uppercase tracking-widest 
              hover:bg-charbon/80 transition shadow">
  Action
</button>
```

### 4. **Bouton Secondaire**
```html
<button class="w-full border border-charbon/20 text-charbon py-3 
              rounded-sm hover:bg-creme transition text-xs uppercase">
  Action
</button>
```

---

## 5️⃣ Composant Chatbot (L'Assistant)

### Localisation
- **Position** : `fixed bottom-24 right-6`
- **Taille** : `w-14 h-14` (bouton flottant)
- **Couche** : `z-50`

### Modale Chatbot
```html
<div id="chatbot-modal" class="fixed bottom-0 right-0 max-w-md max-h-96 
     bg-white rounded-tl-sm rounded-tr-sm z-50 hidden">
```

**Zones** :
1. **Header** : Logo, titre "L'Assistant", statut "En ligne"
2. **Messages** : Zone de scroll, messages alternés (bot/user)
3. **Quick buttons** : 2-3 suggestions contextuelles
4. **Input** : Champ texte + bouton envoyer

### Styling des messages
- **Bot** : bg-creme, text-charbon, coins arrondis asymétriques
- **User** : bg-charbon, text-white, coins arrondis asymétriques

---

## 6️⃣ Barre de Sélection de Langue

### Localisation
- **Position** : `fixed bottom-0 left-0 right-0`
- **Hauteur** : `p-4 pb-8` (évite recouvrement by chatbot)
- **Fond** : `bg-white/95 backdrop-blur-md`
- **Bordure** : `border-t border-charbon/10`

### Boutons
```html
<button class="text-xs font-bold text-or border-b-2 border-or">FR</button>
<button class="text-xs text-charbon/30">EN</button>
<!-- etc. -->
```

**Langues supportées** : FR, EN, ES, IT, DE

---

## 7️⃣ Animations & Transitions

### Classes CSS définies
```css
.animate-fade-in { animation: fadeIn 0.8s ease-out; }
.animate-slide-up { animation: slideUp 0.8s ease-out; }

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
```

### Transitions Tailwind
- Hover effets : `group-hover:scale-110 transition-transform`
- Changement de bordure : `hover:border-or transition`
- Changement de fond : `hover:bg-creme transition`

---

## 8️⃣ Layout & Espacement

### Container Principal
```html
<main class="px-6 py-12 max-w-md mx-auto space-y-8">
```

- **Padding horizontal** : `px-6` (24px)
- **Padding vertical** : `py-12` (48px)
- **Max-width** : `max-w-md` (448px)
- **Espace entre sections** : `space-y-8` (32px)

### Grille Dashboard
```html
<div class="grid grid-cols-2 gap-4">
```
- **Colonnes** : 2
- **Écart** : `gap-4` (16px)
- **Cellules enfer** : `col-span-2` pour boutons larges

### Zones de Scroll
- Sections principales : `hidden` par défaut, affichées au clic
- Message zone : `overflow-y-auto`
- Quick buttons : `overflow-x-auto whitespace-nowrap`

---

## 9️⃣ Navigation & Logique

### Systèmes de navigation
1. **Dashboard → Section** : `onclick="showSection('section-id')"`
2. **Section → Dashboard** : `onclick="showDashboard()"`
3. **Onglets dans Livre d'Or** : `onclick="switchTab('tab-id')"`
4. **Chatbot** : `onclick="toggleChatbot()"`

### État des sections
```javascript
// Cacher toutes les sections
const sections = ['section-wifi', 'section-infos', ...];
sections.forEach(id => document.getElementById(id).classList.add('hidden'));

// Afficher une section
document.getElementById(sectionId).classList.remove('hidden');
```

---

## 🔟 Intégration du Chatbot

### API Recommandée
- **Option 1** : Landbot (simple, ready-made)
- **Option 2** : OpenAI API + prompt personnalisé
- **Option 3** : Dialogflow (Google)

### Prompt pour L'Assistant
```
Vous êtes un concierge numérique pour "La Salamandre", 
une maison d'hôtes luxeuses à Beauvais. 

Vous répondez en français sur :
- Wifi & horaires d'accès
- Petit-déjeuner (horaires: semaine 07h15-09h00, we 08h30-10h00)
- Bar & Terrasse (ouvert avril-octobre)
- Restaurants recommandés + adresses
- Transports & visites à Beauvais
- Numéros d'urgence

Soyez courtois, professionnel, concis. 
Restez dans le contexte de l'établissement.
```

---

## 1️⃣1️⃣ Icônes & Assets

### Icônes
- **Bibliothèque** : FontAwesome 6.4.0
- **Classes** : `fas` (solid), `fab` (brands)

**Exemples** :
- Wi-Fi : `fas fa-wifi`
- Café : `fas fa-coffee`
- Vin : `fas fa-wine-glass-alt`
- Bus : `fas fa-bus`
- Chat : `fas fa-comments`
- WhatsApp : `fab fa-whatsapp`

### Images recommandées
- **stephane.jpg** : Portrait (min. 200x200px)
- **terrasse1.jpg** : Vue bar/terrasse (1200x600px)
- **senteur.jpg** : Bien-être (1200x600px)
- **art.jpg** : Art/culture Beauvais (1200x400px)
- **telephone_rouge.jpg** : Accueil welcome (1080x1920px)

---

## 1️⃣2️⃣ Boutons Flottants

### Bouton L'Assistant (Chatbot)
```html
<button class="fixed bottom-24 right-6 w-14 h-14 bg-or rounded-full 
              shadow-2xl flex items-center justify-center text-white 
              hover:scale-110 transition z-50">
```

### Bouton WhatsApp
```html
<a href="https://wa.me/33614875953" 
   class="fixed bottom-24 left-6 w-14 h-14 bg-green-500 rounded-full">
```

**Positionnement** :
- `bottom-24` = 96px (au-dessus de la barre de langue)
- `right-6` = 24px (décalage droite)
- `left-6` = 24px (décalage gauche pour WA)

---

## 1️⃣3️⃣ Responsive & Mobile-First

### Breakpoints Tailwind
- **Mobile** : `< 640px` (par défaut)
- **Tablet** : `md: 768px`
- **Desktop** : `lg: 1024px`

### Adaptations actuelles
- Grille : 2 colonnes (mobile optimisé)
- Max-width : 448px (modal-friendly)
- Padding : `px-6` (confortable sur petit écran)
- Texte : `text-xs`, `text-[10px]` (lisibilité)

---

## 1️⃣4️⃣ Accessibilité

### A11Y Checklist
- ✅ Contraste des couleurs (WCAG AA)
- ✅ Texte alternatif sur images (`alt=""`)
- ✅ Boutons sémantiques (`<button>`, `<a>`)
- ✅ Hiérarchie des titres (`<h1>`, `<h2>`, etc.)
- ✅ Focus states pour clavier
- ✅ Étiquettes explicites pour icônes

---

## 1️⃣5️⃣ Bonnes Pratiques de Maintenance

### Ajouter une nouvelle section
1. Créer un bouton dans le dashboard :
```html
<button onclick="showSection('section-new')">...</button>
```

2. Créer la section correspondante :
```html
<div id="section-new" class="hidden space-y-6 animate-fade-in">
  <!-- Contenu -->
</div>
```

3. Ajouter l'ID à la liste `showDashboard()` :
```javascript
const sections = [..., 'section-new'];
```

### Mise à jour des couleurs
- Remplacer les textes : `text-or` → `text-[#D4AF37]` (si changement)
- Remplacer les fonds : `bg-or` → valeur Tailwind

### Optimisation images
- Compresser JPG (tinyjpg.com)
- Redimensionner à 1200x600px max
- Utiliser WebP si possible
- Ajouter lazy loading : `loading="lazy"`

---

## 📞 Support & Contacts

- **Email Stéphane** : À intégrer
- **WhatsApp** : +33 6 14 87 59 53
- **Adresse** : 10 rue Marcelle Geudelin, 60000 Beauvais

---

**Dernière mise à jour** : 24 février 2026  
**Version** : 2.0 - Design Minimaliste Crème/Or/Charbon
