import random
import os
from colors import RESET, GREEN, CYAN, YELLOW, LIGHT_RED, LIGHT_BLUE, RED, LIGHT_CYAN, LIGHT_GREEN, PURPLE, BLUE, LIGHT_GREY, BOLD

def ranks_from_scores(scores):
  alist = [(v, k) for k, v in scores.items()]
  alist.sort(reverse=False)
  return alist

def tuple_to_list(tuple):
  lst = []
  for value in tuple:
    lst.append(value[0])
  return lst

players = {"you": 0, "player 1": 0, "player 2": 0, "player 3": 0}
playernames = ['player 1', 'player 2', 'player 3']
print(F"{RED}WELCOME {YELLOW}TO {LIGHT_GREEN}KING {LIGHT_BLUE}MINISTER {PURPLE}THIEF {LIGHT_GREY}POLICE{RESET}")
rules = input("Do you want to see the rules? (y,n)\n>>")
if rules == "y":
  print(f"{CYAN}Rules:{RESET}")
  print(f"There are 4 roles: {RED}King{RESET}, {LIGHT_BLUE}Minister{RESET}, {PURPLE}Thief{RESET}, {LIGHT_GREY}Police")
  print(f"The {BLUE}aim{RESET} of the game is to get the {GREEN}most amount of points{RESET}")
  print(f"In each {LIGHT_RED}round{RESET}, you get {GREEN}one{RESET} of the {YELLOW}roles{RESET}")
  print(f"The {LIGHT_CYAN}Police{RESET} has to identify who the {RED}Thief{RESET} is, after the {YELLOW}King{RESET} has revealed who they are.")
  print(f"If the {LIGHT_CYAN}Police{RESET} gets it {GREEN}right{RESET}, they get {LIGHT_CYAN}500{RESET} points and the {RED}Thief doesn't get any points{RESET}.")
  print(f"If the {LIGHT_CYAN}Police{RESET} gets it wrong, they get {LIGHT_CYAN}0{RESET} points and the {RED}Thief{RESET} gets {RED}500{RESET} points.")
  print(f"The {YELLOW}King{RESET} always gets {LIGHT_BLUE}1000{RESET}.")
  print(f"The {PURPLE}Minister{RESET} always gets {LIGHT_GREEN}800{RESET} points.")
  input(f"Press {BOLD}ENTER{RESET} to start\n>>")
  os.system("clear")
rounds = int(input("Enter the amount of rounds you want to play for:"))
os.system("clear")
for i in range(rounds):
  print(f"Round {BLUE}{i + 1}{RESET}")
  for player in list(players.keys()):
    if player == "you":
      color = LIGHT_RED
    elif player == "player 1":
      color = LIGHT_CYAN
    elif player == "player 2":
      color = LIGHT_GREEN
    else:
      color = PURPLE
    print(f"{color}{player}{RESET}: {LIGHT_BLUE}{players[player]}{RESET}")
  playerroles = {}
  nowroles = ['King', 'Minister', 'Thief', 'Police']
  yourole = random.choice(nowroles)
  nowroles.remove(yourole)
  playerroles['you'] = yourole
  p1role = random.choice(nowroles)
  nowroles.remove(p1role)
  playerroles['player 1'] = p1role
  p2role = random.choice(nowroles)
  nowroles.remove(p2role)
  playerroles['player 2'] = p2role
  p3role = random.choice(nowroles)
  nowroles.remove(p3role)
  playerroles['player 3'] = p3role
  print(f"{RESET}You are a {CYAN}{yourole}{RESET}")
  police = list(playerroles.keys())[list(playerroles.values()).index("Police")]
  thief = list(playerroles.keys())[list(playerroles.values()).index("Thief")]
  minister = list(playerroles.keys())[list(playerroles.values()).index("Minister")]
  king = list(playerroles.keys())[list(playerroles.values()).index("King")]
  if yourole == "King":
    print(f"{police} is the {GREEN}Police{RESET}")
    playernamesrn = ['player 1', 'player 2', 'player 3']
    playernamesrn.remove(police)
    guess = random.choice(playernamesrn).lower()
    print(f"The Police guessed that {guess} is the Thief!")
    if playerroles[guess] == "Thief":
      print(f"{LIGHT_GREEN}{police} got it right! {guess} is the Thief!{RESET}")
      players['you'] = players['you'] + 1000
      players[police] = players[police] + 500
      players[minister] = players[minister] + 800
    else:
      print(f"{RED}{police} got it wrong! {thief} is the Thief!{RESET}")
      players['you'] = players['you'] + 1000
      players[thief] = players[thief] + 500
      players[minister] = players[minister] + 800
  elif yourole == "Minister":
    print(f"{king} is the {YELLOW}King{RESET}")
    print(f"{police} is the {GREEN}Police{RESET}")
    playernamesrn = ['you', thief]
    guess = random.choice(playernamesrn).lower()
    if guess == "you":
      print("The Police guessed that you are the Thief.")
    else:
      print(f"The Police guessed that {guess} is the Thief!")
    if playerroles[guess] == "Thief":
      print(f"{LIGHT_GREEN}{police} got it right! {guess} is the Thief!{RESET}")
      players['you'] = players['you'] + 800
      players[king] = players[king] + 1000
      players[police] = players[police] + 500
    else:
      print(f"{RED}{police} got it wrong! {thief} is the Thief!{RESET}")
      players['you'] = players['you'] + 800
      players[king] = players[king] + 1000
      players[thief] = players[thief] + 500
  elif yourole == "Thief":
    print(f"{king} is the {YELLOW}King{RESET}")
    print(f"{police} is the {GREEN}Police{RESET}")
    playernamesrn = ['you', thief]
    guess = random.choice(playernamesrn).lower()
    if guess == "you":
      print("The Police guessed that you are the Thief.")
    else:
      print(f"The Police guessed that {guess} is the Thief!")
    if playerroles[guess] == "Thief":
      print(f"{RED}{police} got it right! {guess} are the Thief!{RESET}")
      players[king] = players[king] + 1000
      players[police] = players[police] + 500
      players[minister] = players[minister] + 800
    else:
      print(f"{LIGHT_GREEN}{police} got it wrong! {thief} are the Thief!{RESET}")
      players[king] = players[king] + 1000
      players['you'] = players['you'] + 500
      players[minister] = players[minister] + 800
  elif yourole == "Police":
    print(f"{king} is the {YELLOW}King{RESET}.")
    playernamesrn = ['player 1', 'player 2', 'player 3']
    playernamesrn.remove(king)
    options = " or ".join(playernamesrn)
    guess = input(f"Do you think {options} is the thief?").lower()
    if guess not in playernamesrn:
      print(f"{RED}You didn't have the guts to pick anyone! The thief ran free!{RESET}")
      players[king] = players[king] + 1000
      players[minister] = players[minister] + 800
      players[thief] = players[thief] + 500
    else:
      if playerroles[guess] == "Thief":
        print(f"{LIGHT_GREEN}You are right! {guess} is the Thief{RESET}")
        players['you'] = players['you'] + 500
        players[king] = players[king] + 1000
        players[minister] = players[minister] + 800
      else:
        print(f"{RED}You are wrong! {thief} is the Thief{RESET}")
        players[thief] = players[thief] + 500
        players[king] = players[king] + 1000
        players[minister] = players[minister] + 800
  input(f"Press {BOLD}ENTER{RESET} for the next round\n>>")
  os.system("clear")
sorted_value_key_pairs = ranks_from_scores(players)
lst = tuple_to_list(sorted_value_key_pairs)
# if any(lst[i]==lst[i+1] for i in range(len(lst)-1)) == True:
#   for key, group in groupby(sorted_value_key_pairs, itemgetter(0)):
#     group = list(group)
#     if len(group) > 1:
#       for k, player in group:
#         assert k == key
#         print(f'{player} ties')
#       print()
# else:
for score in sorted_value_key_pairs:
  index = sorted_value_key_pairs.index(score)
  if index == 0:
    print(f"{RED}In 4th place, with {score[0]} points, is {score[1]}")
  elif index == 1:
    print(f"{YELLOW}In 3rd place, with {score[0]} points, is {score[1]}")
  elif index == 2:
    print(f"{LIGHT_GREY}In 2nd place, with {score[0]} points, is {score[1]}")
  else:
    print(f"{LIGHT_GREEN}In 1st place, with {score[0]} points, is {score[1]}")