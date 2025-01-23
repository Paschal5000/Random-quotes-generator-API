from flask import Flask, jsonify, request, render_template
import random
import json

app = Flask(__name__)

# Load quotes from JSON file
def load_quotes():
    with open("quotes.json", "r") as file:
        return json.load(file)

quotes = load_quotes()

@app.route('/')
def home():
    print("Home route accessed")
    return render_template('index.html')

@app.route("/api/quotes", methods=["GET"])
def get_all_quotes():
    """Return all quotes."""
    return jsonify(quotes)

@app.route("/api/quote/random", methods=["GET"])
def get_random_quote():
    print("Random quote endpoint accessed")
    random_quote = random.choice(quotes)
    return jsonify(random_quote)

@app.route("/api/quotes/category/<string:category>", methods=["GET"])
def get_quotes_by_category(category):
    """Return quotes filtered by category."""
    filtered_quotes = [quote for quote in quotes if quote["category"].lower() == category.lower()]
    if not filtered_quotes:
        return jsonify({"error": "No quotes found for this category"}), 404
    return jsonify(filtered_quotes)

@app.route("/api/quotes", methods=["POST"])
def add_quote():
    """Add a new quote."""
    new_quote = request.json
    quotes.append(new_quote)
    with open("quotes.json", "w") as file:
        json.dump(quotes, file)
    return jsonify(new_quote), 201

if __name__ == '__main__':
    app.run(debug=True)
