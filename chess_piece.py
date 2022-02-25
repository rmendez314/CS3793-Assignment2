class chessPiece():

    def __init__(self, piece_type, location, value, is_active, color):
        self.piece_type = piece_type
        self.value = value
        self.color = color

    def set_is_active(self, is_active):
        self.is_active = is_active

    def set_location(self, location):
        self.location = location

    def get_is_active(self):
        return self.is_active

    def get_location(self):
        return self.location

    def get_value(self):
        return self.value

    def get_color(self):
        return self.color


class pawn(chessPiece):
    def __init__(self):
        pass

    def valid_moves(self):
        move_list = []
        return move_list


class queen(chessPiece):
    def __init__(self):
        pass

    def valid_moves(self):
        move_list = []
        return move_list


class king(chessPiece):
    def __init__(self):
        pass

    def valid_moves(self):
        move_list = []
        return move_list


class bishop(chessPiece):
    def __init__(self):
        pass

    def valid_moves(self):
        move_list = []
        return move_list


class rook(chessPiece):
    def __init__(self):
        pass

    def valid_moves(self):
        move_list = []
        return move_list


class knight(chessPiece):
    def __init__(self):
        pass

    def valid_moves(self):
        move_list = []
        return move_list