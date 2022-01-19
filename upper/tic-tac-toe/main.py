import Board as Board

print('START!')
player = input('Kto ma zacząć X czy O: ')

board = Board.Board(player.upper())

while (not board.check_if_win()) and (not board.check_if_draw()):
  board.show_board()
  x, y = [int(x) for x in input('Podaj współrzędne pola na którym chcesz postawić X lub O: ').split()]
  board.put_to_board(x, y)

board.show_board()
print()
if board.check_if_win():
  if board.get_player() == 'X':
    print('Wygrał O')
  else:
    print('Wygrał X')
else:
  print('Remis!')