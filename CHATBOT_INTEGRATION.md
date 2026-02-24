# 🤖 Guide d'Intégration du Chatbot
## L'Assistant de la Salamandre

---

## Vue d'ensemble

Le chatbot (**L'Assistant**) est un composant flottant qui offre une concierge numérique pour les clients. L'interface est déjà intégrée et prête ; il suffit de brancher une API backend.

---

## Architecture actuelle

### Interface HTML/CSS
✅ **Déjà implémenté** :
- Bouton flottant (fixed, bottom-24 right-6)
- Modale avec sliding animation
- Header avec statut "En ligne"
- Zone de messages (scrollable)
- Boutons "Questions rapides"
- Champ input + bouton envoyer

### Logique JavaScript
```javascript
function toggleChatbot() {
  const modal = document.getElementById('chatbot-modal');
  modal.classList.toggle('hidden');
}
```

**À implémenter** : Logique de communication avec l'API

---

## Trois Approches d'Intégration

### 🟦 **Option 1 : Landbot (Recommandé pour rapide)**

**Avantages** :
- Setup en 5 min
- Dashboard intuitif
- Pas de code côté backend
- Support multilingue intégré
- Analytics gratuit

**Étapes** :
1. Créer compte sur https://landbot.io
2. Configurer le chatbot avec les réponses La Salamandre
3. Copier le script d'intégration
4. Remplacer la modale HTML par l'iframe Landbot

**Code d'intégration** (remplacer le contenu de `#chatbot-modal`) :
```html
<script src="https://static.landbot.io/landbot-3.0.0.js"></script>
<div id="landbot"></div>
<script>
  var myLandbot = new Landbot.Livechat({
    configUrl: 'https://chats.landbot.io/v3/...', // Your Landbot URL
  });
</script>
```

---

### 🔴 **Option 2 : OpenAI API (Plus de contrôle)**

**Avantages** :
- Texte généré par IA (GPT-4)
- Contexte personnalisable
- Intégration native à votre code
- Coûts proportionnels à l'usage

**Étapes** :

#### 1. **Configuration initiale**
```bash
npm install openai
# ou en CDN :
<script src="https://cdn.jsdelivr.net/npm/openai/dist/openai.min.js"></script>
```

#### 2. **Créer une fonction d'appel API**
```javascript
async function sendMessageToBot(userMessage) {
  const apiKey = 'sk-...'; // À stocker en backend seulement
  
  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      model: 'gpt-4',
      messages: [
        {
          role: 'system',
          content: `Vous êtes un concierge numérique pour "La Salamandre", 
          une maison d'hôtes luxeuses à Beauvais...`
        },
        {
          role: 'user',
          content: userMessage
        }
      ],
      max_tokens: 150,
      temperature: 0.7
    })
  });
  
  const data = await response.json();
  return data.choices[0].message.content;
}
```

#### 3. **Intégrer au formulaire**
```javascript
document.querySelector('input[placeholder="Écrivez..."]')
  .addEventListener('keypress', async (e) => {
    if (e.key === 'Enter') {
      const message = e.target.value;
      const reply = await sendMessageToBot(message);
      addMessageToChat(message, 'user');
      addMessageToChat(reply, 'bot');
      e.target.value = '';
    }
  });
```

---

### 🟩 **Option 3 : Backend Node.js Custom (Maximum flexibilité)**

**Structure** :
```
backend/
├── index.js (serveur)
├── routes/
│   └── chatbot.js
├── prompts/
│   └── salamandre.js
└── package.json
```

#### 1. **Backend Express + OpenAI**
```javascript
const express = require('express');
const { OpenAI } = require('openai');

const app = express();
app.use(express.json());
app.use(cors());

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

app.post('/api/chatbot/message', async (req, res) => {
  const userMessage = req.body.message;
  
  const systemPrompt = `Vous êtes L'Assistant, concierge numérique de La Salamandre.
  
  Informations clés :
  - WiFi : "La Salamandre" / "lasalamandre15052015"
  - Petit-déjeuner semaine : 07h15-09h00
  - Petit-déjeuner WE : 08h30-10h00
  - Départ avant 11h00
  - Bar & Terrasse : avril-octobre
  - Adresse : 10 rue Marcelle Geudelin, 60000 Beauvais
  - Contact : +33614875953 (WhatsApp)
  
  Répondez en français, soyez courtois et concis.`;
  
  try {
    const message = await client.chat.completions.create({
      model: 'gpt-4',
      messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: userMessage }
      ],
      max_tokens: 200
    });
    
    res.json({ reply: message.choices[0].message.content });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.listen(3000, () => console.log('Chatbot API running on :3000'));
```

#### 2. **Frontend fetch**
```javascript
async function sendMessageToBot(userMessage) {
  const response = await fetch('/api/chatbot/message', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: userMessage })
  });
  
  const data = await response.json();
  return data.reply;
}
```

---

## Prompt Optimisé pour La Salamandre

```
Vous êtes L'Assistant, le concierge numérique de La Salamandre, 
une petite maison d'hôtes de prestige à Beauvais.

VOTRE ROLE
- Accueillir chaleureusement les clients
- Fournir des informations précises sur l'établissement
- Recommander des restaurants et attractions
- Organiser les transports et déplacements

INFORMATIONS ÉTABLISSEMENT
=== WiFi ===
Réseau: La Salamandre
Code: lasalamandre15052015

=== Petit-Déjeuner ===
Semaine: 07h15 - 09h00
Weekend: 08h30 - 10h00

=== Départ ===
Avant 11h00

=== Bar & Terrasse ===
Période: Avril - Octobre
Spécialités: Vins sélectionnés, bières artisanales, planches mixtes

=== Restaurants Recommandés ===
1. La Bohemia - Belle ambiance, plats généreux ⭐⭐⭐⭐☆
2. La Place - Menu changeant hebdo ⭐⭐⭐⭐
3. L'Autrement - Cuisine gastronomique ⭐⭐⭐⭐⭐

=== Visites à Beauvais ===
- Cathédrale St-Pierre (10h-17h15)
- MUDO - Musée de l'Oise (GRATUIT)
- Le Quadrilatère - Art & Architecture
- Office de Tourisme: visitbeauvais.fr

=== Transports ===
- Bus Ligne 6: Arrêt Maillart
- Taxis: Jean Pierre, Taxi Mounir, Taxi Asin
- Train: Beauvais → Paris Gare du Nord
- Navette Aéroport: Porte Maillot

=== Contact ===
Stéphane: +33614875953 (WhatsApp)
Adresse: 10 rue Marcelle Geudelin, 60000 Beauvais

DIRECTIVES
- Répondez UNIQUEMENT en français
- Soyez courtois, pro, concis
- Limitez les réponses à 3-4 phrases
- Si hors contexte, redirigeez vers Stéphane (WhatsApp)
- N'inventialisez jamais d'informations
- Utilisez ton chaleureux "petit hôtel de caractère"
```

---

## Intégration UI (Modifications Minimales)

### Messages système initial
```javascript
// Au chargement du chatbot
addMessageToChat(
  'Bienvenue à La Salamandre. Je suis votre concierge numérique. Comment puis-je vous aider ?',
  'bot'
);
```

### Fonction `addMessageToChat()`
```javascript
function addMessageToChat(text, sender) {
  const messagesZone = document.querySelector('#chatbot-modal main');
  const messageDiv = document.createElement('div');
  
  if (sender === 'user') {
    messageDiv.innerHTML = `
      <div class="flex flex-col items-end ml-auto max-w-[85%]">
        <div class="bg-charbon text-white p-4 rounded-tl-2xl rounded-bl-2xl rounded-br-2xl">
          <p class="text-sm leading-relaxed">${text}</p>
        </div>
        <span class="text-[10px] mt-2 mr-1 text-charbon/40 uppercase">À l'instant</span>
      </div>
    `;
  } else {
    messageDiv.innerHTML = `
      <div class="flex flex-col items-start max-w-[85%]">
        <div class="bg-creme p-4 rounded-tr-2xl rounded-br-2xl rounded-bl-2xl">
          <p class="text-sm leading-relaxed text-charbon">${text}</p>
        </div>
        <span class="text-[10px] mt-2 ml-1 text-charbon/40 uppercase">À l'instant</span>
      </div>
    `;
  }
  
  messagesZone.appendChild(messageDiv);
  messagesZone.scrollTop = messagesZone.scrollHeight;
}
```

### Bouton envoi fonctionnel
```javascript
document.querySelector('#chatbot-modal button[class*="paper-plane"]')
  .addEventListener('click', async () => {
    const input = document.querySelector('#chatbot-modal input[type="text"]');
    const message = input.value.trim();
    
    if (!message) return;
    
    addMessageToChat(message, 'user');
    input.value = '';
    
    // Appel API
    const reply = await sendMessageToBot(message);
    addMessageToChat(reply, 'bot');
  });
```

---

## Boutons "Questions Rapides"

Les boutons suggèrent des thèmes fréquents. À adapter :

```html
<div class="px-6 py-3 flex gap-2 overflow-x-auto">
  <button onclick="askChatbot('Quel est le code WiFi ?')">WiFi</button>
  <button onclick="askChatbot('À quelle heure le petit-déjeuner ?')">Petit-déj</button>
  <button onclick="askChatbot('Quels restaurants recommandez-vous ?')">Restaurants</button>
</div>

<script>
function askChatbot(question) {
  const input = document.querySelector('#chatbot-modal input');
  input.value = question;
  input.dispatchEvent(new KeyboardEvent('keypress', { key: 'Enter' }));
}
</script>
```

---

## Statut "En ligne"

Le point vert `bg-green-500` indique que le bot est actif. À mettre à jour dynamiquement :

```javascript
async function checkBotStatus() {
  try {
    const response = await fetch('/api/chatbot/status');
    const { online } = await response.json();
    
    const statusDot = document.querySelector('#chatbot-modal .bg-green-500');
    if (!online) {
      statusDot.classList.replace('bg-green-500', 'bg-red-500');
    }
  } catch (error) {
    console.log('Erreur vérification statut chatbot');
  }
}

// Vérifier au démarrage et toutes les 30s
checkBotStatus();
setInterval(checkBotStatus, 30000);
```

---

## Sauvegarder l'historique

```javascript
// LocalStorage simple
function saveConversation() {
  const messages = document.querySelectorAll('#chatbot-modal .flex.flex-col');
  const conversation = Array.from(messages).map(msg => ({
    sender: msg.classList.contains('items-end') ? 'user' : 'bot',
    text: msg.querySelector('p').innerText,
    timestamp: new Date()
  }));
  
  localStorage.setItem('salamandre-chat-history', JSON.stringify(conversation));
}

// Charger au redémarrage
function loadConversation() {
  const history = JSON.parse(localStorage.getItem('salamandre-chat-history') || '[]');
  history.forEach(msg => addMessageToChat(msg.text, msg.sender));
}
```

---

## Tests & Déploiement

### Checklist avant pub
- [ ] Tester réponses WiFi, petit-déj, horaires
- [ ] Tester avec textes longs (overflow)
- [ ] Vérifier animations (mobile)
- [ ] Tester sur iPhone / Android
- [ ] Vérifier lien WhatsApp redirect
- [ ] Logs console propres (pas d'errors)

### Monitoring en prod
```javascript
window.addEventListener('error', (e) => {
  console.error('Chatbot error:', e);
  // Optionnel: envoyer à service de monitoring
  fetch('/api/logs/error', { 
    method: 'POST', 
    body: JSON.stringify({ error: e.message }) 
  });
});
```

---

## FAQ Intégration

**Q: Combien coûte l'API OpenAI ?**  
R: ~$0.001 par 1000 tokens. Comptez ~5 cents/1000 messages.

**Q: Puis-je langues multiples ?**  
R: Oui, remplacez le prompt par une version multilingue ou détectez la langue cliente.

**Q: Comment sécuriser ma clé API ?**  
R: JAMAIS en frontend. Utilisez un proxy backend qui authifie les requêtes client.

**Q: Mon chatbot met trop longtemps à répondre ?**  
R: Utilisez le streaming (réponse par chunks) pour meilleure UX.

---

## Ressources Utiles

- 📖 [OpenAI API Docs](https://platform.openai.com/docs)
- 🤖 [Landbot Getting Started](https://docs.landbot.io)
- 💬 [Dialogflow Quickstart](https://cloud.google.com/dialogflow/docs)
- 🎨 [Tailwind Docs](https://tailwindcss.com)

---

**Prêt à intégrer ?** Choisissez l'option qui convient à votre ressources et expertise ! 🚀
