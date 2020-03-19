import random, os, time
a1, a2, a3 = ' ', ' ', ' '
b1, b2, b3 = ' ', ' ', ' '
c1, c2, c3 = ' ', ' ', ' '
user_inputs, ai_inputs = [], []
turn, whose_turn = 0, random.randint(0, 1)
win_condition, all_pos = [], []

def flatten_list(a, result=None):
  if result is None:
    result = []
  for x in a:
    if isinstance(x, list):
      flatten_list(x, result)
    else:
      result.append(x)
  return result

def column_row_cross(a, result=None):
  if result == None:
    result = []
    y = []
    z = []
  for x in range(len(a)):
    result.append(a[x])
    result.append([row[x] for row in a])
  for x in range(len(a)):
    y.append(a[x][x])
    z.append(a[x][abs(x-2)])
  result.append(y)
  result.append(z)
  return result

def grid():
  global all_pos, win_condition
  grid = [['a1', 'a2', 'a3'],
          ['b1', 'b2', 'b3'],
          ['c1', 'c2', 'c3']]
  all_pos = flatten_list(grid)
  win_condition = column_row_cross(grid)


def board():
  print('c ' + c1 + '│' + c2 + '│' + c3)
  print('  ─┼─┼─')
  print('b ' + b1 + '│' + b2 + '│' + b3)
  print('  ─┼─┼─')
  print('a ' + a1 + '│' + a2 + '│' + a3)
  print('\n  1 2 3')
      
def user_input():
  global user_inputs, turn
  if (whose_turn == 0) or (turn != 0):
    user_choice = input('\nEnter your move(ex. b3): ')
    while user_choice in (user_inputs + ai_inputs):
      print('The move is taken')
      user_choice = input('\nEnter your move(ex. b3): ')
    else:
      user_inputs.append(user_choice)
      exec(user_choice + " = 'x'", globals())
    turn += 1

def check_win():
  l, k = 0, 0
  for j in range(len(all_pos)):
    if all_pos[j] in (user_inputs + ai_inputs): k += 1
  if k == 9:
    print('Tied')
    return False
  for i in range(len(win_condition)):
    l = 0
    m = 0
    for j in range(len(win_condition[i])):
      if win_condition[i][j] in ai_inputs: m += 1
      if win_condition[i][j] in user_inputs: l += 1
      if l == 3:
        print('You win')
        return True
      elif m == 3:
        print('You lose')
        return False
  return None

def ai_move():
  global user_inputs, turn, ai_inputs
  side_piece = ['a2', 'b3', 'b1', 'c2']
  corner_piece = ['a1', 'a3', 'c3', 'c1']
  if whose_turn == 1 and turn == 0:
    exec("b2 = 'o'", globals())
    ai_inputs.append('b2')
    turn += 1
  else:
    if whose_turn == 0 and turn == 1:
      if b2 == 'x':
        i = random.randint(1, len(corner_piece)) - 1
        exec(corner_piece[i] + " = 'o'", globals())
        ai_inputs.append(corner_piece[i])
      elif user_inputs[0] in (corner_piece + side_piece):
        exec("b2 = 'o'", globals())
        ai_inputs.append('b2')
    elif turn >= 2:
      m, p, s, n, q, t = 0, 0, 0, [], [], []
      for x in range(len(win_condition)):
        for y in range(len(win_condition[x])):
          q = win_condition[x]
          p += 1
          if win_condition[x][y] in ai_inputs:
            s += 1
            t.append(win_condition[x][y])
          if win_condition[x][y] in user_inputs: m = 1
          if s == 2 and m == 0 and p == 3:
            for u in range(len(q)):
              if not q[u] in t:
                exec(q[u] + " = 'o'", globals())
                ai_inputs.append(q[u])
                return
          if p == 3: m, p, s, q, t = 0, 0, 0, [], []
      for i in range(len(win_condition)):
        for j in range(len(win_condition[i])):
          q = win_condition[i]
          p += 1
          if win_condition[i][j] in user_inputs:
            m += 1
            n.append(win_condition[i][j])
          if win_condition[i][j] in ai_inputs: s = 1
          if m == 2 and s == 0 and p == 3:
            for k in range(len(q)):
                if not q[k] in n:
                  exec(q[k] + " = 'o'", globals())
                  ai_inputs.append(q[k])
                  return
          if p == 3: m, p, s, q, n = 0, 0, 0, [], []
      for r in range(len(corner_piece)):
        if not corner_piece[r] in (ai_inputs + user_inputs):
          exec(corner_piece[r] + " = 'o'", globals())
          ai_inputs.append(corner_piece[r])
          return
      for r in range(len(corner_piece)):
        if not side_piece[r] in (ai_inputs + user_inputs):
          exec(side_piece[r] + " = 'o'", globals())
          ai_inputs.append(side_piece[r])
          return

global ai_inputs, user_inputs, turn, whose_turn
grid()
while True:
  if turn == 0:
    who_turn = 'User' if whose_turn == 0 else 'AI'
    print('It\'s ' + who_turn + '\'s turn')
  time.sleep(1)
  os.system('clear')
  board()
  user_input()
  ai_move()
  result = check_win()
  if result != None:
    board()
    input('Press Enter to play again')
    user_inputs = []
    ai_inputs = []
    turn = 0
    whose_turn = random.randint(0, 1)
    for i in range(len(all_pos)):
      exec(all_pos[i] + " = ' '", globals())
    os.system('clear')
  