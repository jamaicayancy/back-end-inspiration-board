from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board


boards_bp = Blueprint("boards", __name__, url_prefix="/boards")


@boards_bp.route("", methods=["GET"])
def get_all_boards():
    board_query = Board.query
    boards = board_query.all()
    boards_response = [board.to_dict() for board in boards]

    return jsonify(boards_response), 200
