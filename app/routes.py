from flask import Blueprint, request, jsonify, make_response
from app import db
from .models.board import Board 
from .models.card import Card 

boards_bp = Blueprint("boards", __name__, url_prefix="/boards")
cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

# Returns all boards
@boards_bp.route("", methods=["GET"])
def get_all_boards():
    board_query = Board.query
    boards = board_query.all()
    boards_response = [board.create_dict() for board in boards]

    return jsonify(boards_response), 200

# Returns all cards, or use query parameter to return cards with a given board_id 
@cards_bp.route("", methods=["GET"])
def get_all_cards():

    board_query = request.args.get("board_id")
    if board_query:
        cards = Card.query.filter_by(board_id=board_query)
    else:
        cards = Card.query.all()
    cards_response = [card.create_dict() for card in cards]

    return jsonify(cards_response), 200
    
# Returns cards with a given card ID number
@cards_bp.route("/<card_id>", methods=["GET"])
def get_one_card(card_id):
    card_query = Card.query
    card = card_query.get(card_id)
    
    return {"card": card.create_dict()}, 200
