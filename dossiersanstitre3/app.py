from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Route pour la racine (/)
@app.route('/')
def index():
    return redirect(url_for('validation'))  # Redirige vers /validation

# Route pour la page de validation
@app.route('/validation', methods=['GET'])
def validation():
    return render_template('validation.html')

# Route pour traiter la commande
@app.route('/commander', methods=['POST'])
def commander():
    # Récupérer les données du formulaire
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    address = request.form.get('address')
    billing_address = request.form.get('billing-address')
    quantity = request.form.get('quantity')
    subtotal = request.form.get('subtotal')
    delivery_cost = request.form.get('delivery-cost')
    discount = request.form.get('discount')
    final_total = request.form.get('final-total')
    note = request.form.get('note')
    payment_method = request.form.get('payment-method')
    cardholder_name = request.form.get('cardholder-name')
    card_number = request.form.get('card-number')
    expiry_date = request.form.get('expiry-date')
    cvv = request.form.get('cvv')
    installment_plan = request.form.get('installment-plan')

    # Données supplémentaires pour la confirmation
    product_name = "Lot de 10 unités de foie gras Labeyrie 285g"
    payment_date = datetime.now().strftime("%d %B %Y")  # Format : 10 octobre 2023

    # Préparer les données à envoyer à la page de confirmation
    order_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'address': address,
        'billing_address': billing_address,
        'quantity': quantity,
        'subtotal': subtotal,
        'delivery_cost': delivery_cost,
        'discount': discount,
        'final_total': final_total,
        'note': note,
        'payment_method': payment_method,
        'cardholder_name': cardholder_name,
        'card_number': card_number,
        'expiry_date': expiry_date,
        'cvv': cvv,
        'installment_plan': installment_plan,
        'product_name': product_name,
        'payment_date': payment_date
    }

    # Rediriger vers la page de confirmation avec les données
    return redirect(url_for('confirmation', **order_data))

# Route pour la page de confirmation
@app.route('/confirmation')
def confirmation():
    # Récupérer les données passées en paramètres
    order_data = {
        'first_name': request.args.get('first_name'),
        'last_name': request.args.get('last_name'),
        'email': request.args.get('email'),
        'phone': request.args.get('phone'),
        'address': request.args.get('address'),
        'billing_address': request.args.get('billing_address'),
        'quantity': request.args.get('quantity'),
        'subtotal': request.args.get('subtotal'),
        'delivery_cost': request.args.get('delivery_cost'),
        'discount': request.args.get('discount'),
        'final_total': request.args.get('final_total'),
        'note': request.args.get('note'),
        'payment_method': request.args.get('payment_method'),
        'cardholder_name': request.args.get('cardholder_name'),
        'card_number': request.args.get('card_number'),
        'expiry_date': request.args.get('expiry_date'),
        'cvv': request.args.get('cvv'),
        'installment_plan': request.args.get('installment_plan'),
        'product_name': request.args.get('product_name'),
        'payment_date': request.args.get('payment_date')
    }

    return render_template('confirmation.html', data=order_data)

if __name__ == '__main__':
    app.run(debug=True)
