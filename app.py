from flask import Flask, render_template, request, redirect

app = Flask(__name__)

transactions = [
    {"name": "Aakash", "details": "Engineer", "contact": "98923934"},
    {"name": "Vaishnavi", "details": "Creator", "contact": "98923935"}
]

@app.route('/')
def home():
    return render_template("transactions.html", transactions=transactions)

@app.route('/add', methods=['POST'])
def add_transaction():
    new_entry = {
        "name": request.form.get("name"),
        "details": request.form.get("details"),
        "contact": request.form.get("contact")
    }
    transactions.append(new_entry)
    return redirect('/')

# STEP 1: Show update form
@app.route('/edit/<int:index>')
def edit_transaction(index):
    transaction = transactions[index]
    return render_template("edit.html", transaction=transaction, index=index)

# STEP 2: Perform update
@app.route('/update/<int:index>', methods=['POST'])
def update_transaction(index):
    transactions[index]['name'] = request.form.get("name")
    transactions[index]['details'] = request.form.get("details")
    transactions[index]['contact'] = request.form.get("contact")

    return redirect('/')

@app.route('/delete/<int:index>', methods=['POST'])
def delete_transaction(index):
    transactions.pop(index)
    return redirect('/')
    

if __name__ == "__main__":
    app.run(debug=True)
