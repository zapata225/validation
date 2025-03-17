from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route pour la page d'accueil (validation.html)
@app.route('/')
def index():
    return render_template('validation.html')

# Route pour la page de confirmation
@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

# Route pour la page jumeler.html
@app.route('/jumeler')
def jumeler():
    return render_template('jumeler.html')

# Route pour traiter la soumission du formulaire
@app.route('/submit', methods=['POST'])
def submit():
    # Récupérer les données du formulaire
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    address = request.form.get('address')
    billing_address = request.form.get('billing-address-input')
    quantity = request.form.get('quantity')
    subtotal = request.form.get('subtotal')
    delivery_cost = request.form.get('delivery-cost')
    discount = request.form.get('discount')
    final_total = request.form.get('final-total')
    note = request.form.get('note')
    payment_method = request.form.get('payment')

    # Ici, vous pouvez traiter les données (par exemple, les enregistrer dans une base de données)

    # Rediriger vers la page de confirmation
    return redirect(url_for('confirmation'))

# Route pour traiter le clic sur "Jumeler votre compte"
@app.route('/jumeler-account', methods=['POST'])
def jumeler_account():
    # Récupérer les données nécessaires
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    total = request.form.get('final-total')

    # Ici, vous pouvez traiter les données (par exemple, les enregistrer dans une base de données)

    # Rediriger vers la page jumeler.html
    return redirect(url_for('jumeler'))

if __name__ == '__main__':
    app.run(debug=True)