import pytest
from main import get_piece_value, evaluate_board
import chess

def test_piece_values():
    assert get_piece_value('P') == 100
    assert get_piece_value('q') == -900

def test_evaluate_board():
    board = chess.Board()
    assert evaluate_board(board) == 0  # Posición inicial