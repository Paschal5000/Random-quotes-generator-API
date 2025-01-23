from flask import Flask, jsonify, request
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
    """Return a welcome message for the root URL."""
    return "Welcome to the Quotes API!"

@app.route("/api/quotes", methods=["GET"])
def get_all_quotes():
    """Return all quotes."""
    return jsonify(quotes)

@app.route("/api/quote/random", methods=["GET"])
def get_random_quote():
    """Return a random quote."""
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
    if not new_quote.get("quote") or not new_quote.get("author") or not new_quote.get("category"):
        return jsonify({"error": "Missing fields: 'quote', 'author', and 'category' are required"}), 400

    quotes.append(new_quote)
    with open("quotes.json", "w") as file:
        json.dump(quotes, file, indent=4)
    return jsonify({"message": "Quote added successfully!"}), 201

if __name__ == "__main__":
    app.run(debug=True)

