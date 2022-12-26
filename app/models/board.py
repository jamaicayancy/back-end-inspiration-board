from app import db

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    owners_name = db.Column(db.String)
    cards = db.relationship("Card", back_populates="board")
# One to many relationship between board and card.

    def create_dict(self):
        board_dict = {}
        board_dict["board_id"] = self.board_id
        board_dict["owners_name"] = self.owners_name
        board_dict["cards"] = "replace me"

        return board_dict



