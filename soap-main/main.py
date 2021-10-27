import os
from pprint import pprint

ranksTorows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
rowsTornaks = {v: k for k, v in ranksTorows.items()}
filesTocols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
colsTofiles = {v: k for k, v in filesTocols.items()}


class GameState():
		def __init__(self):
			#bord is an 8x8 2d list, each element of the list has 2 characters.
			#the first character represents the color
			#the second characer represents the type
			#"--" represents an empty space with no piece
			self.board = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
										["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
										["--", "--", "--", "--", "--", "--", "--", "--"],
										["--", "--", "--", "--", "--", "--", "--", "--"],
										["--", "--", "--", "--", "--", "--", "--", "--"],
										["--", "--", "--", "--", "--", "--", "--", "--"],
										["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
										["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
			self.whiteToMove = True  #white starts
			self.movelog = []
			
		def logmake(self,move):
					if move.pieceMoved[1]=="P" :
						self.movelog.append(move.endsq)
					else:
						self.movelog.append(f"{move.pieceMoved[1]}{move.endsq}")

		def makemove(self, move):
			# mverify=moveVerify(move,self.board)
			if move.pieceMoved[0]=="w" and self.whiteToMove==True : #white turn move
			#and mverify=="Ture"
				self.board[move.startRow][move.startCol] = "--"
				self.board[move.endRow][move.endCol] = move.pieceMoved
				self.whiteToMove = not self.whiteToMove  #Turn swap
				return "moved"
				print("whitemoved")	
			
			elif move.pieceMoved[0]=="b" and self.whiteToMove==False : #black turn move
			#and mverify=="Ture"
				self.board[move.startRow][move.startCol] = "--"
				self.board[move.endRow][move.endCol] = move.pieceMoved
				self.whiteToMove = not self.whiteToMove  #Turn swap
				return "moved"
			
			elif move.pieceMoved=="--":
				print("EMPTY SQ!\n")
				return "not moved"

			elif move.pieceMoved[0]=="w" and self.whiteToMove==False:
				print("NOT YOUR TURN!\n")
				return "not moved"
			elif move.pieceMoved[0]=="b" and self.whiteToMove==True:
				print("NOT YOUR TURN!\n")
				return "not moved"
				
			# self.whiteToMove = not self.whiteToMove  #Turn swap

#move
class Move():
	def __init__(self, startsq, endsq, board):
		self.endsq=endsq
		self.startCol = filesTocols[startsq[0]]
		self.startRow = ranksTorows[startsq[1]]
		self.endCol = filesTocols[endsq[0]]
		self.endRow = ranksTorows[endsq[1]]
		self.pieceMoved = board[self.startRow][self.startCol]
		self.pieceCaptured = board[self.endRow][self.endCol]
		#Raw
		self.Raw_startCol = [startsq[0]]
		self.Raw_startRow = [startsq[1]]
		self.Raw_endCol = [endsq[0]]
		self.Raw_endRaw = [endsq[1]]

#  moveVerification
def moveVerify(self,move,board):
	if move.pieceMoved =="wP":
		return wPawnMoves(move,board)
	elif move.pieceMoved =="bP":
		return bPawnMoves(move,board)
	elif move.pieceMoved[1] =="N":
		return KnightMoves(move,board)
	elif move.pieceMoved[1] =="B":
		return BishopMoves(move,board)
	elif move.pieceMoved[1] =="R":
		return RookMoves(move,board)
	elif move.pieceMoved[1] =="K": #O-O-O
		return KingMoves(move,board)
	elif move.pieceMoved[1] =="Q":
		return QueenMoves(move,board)

def wPawnMoves(self,move,board):
	# front 2sq 
	if move.endsq == self.board[move.endRow-2][move.endCol] \
	and move.startRow=="2" \
	and move.endsq=="--" \
	and self.board[move.endRow-1][move.endCol]=="--":
		return True
	# front 1sq
	elif move.endsq==self.board[move.endRow-1][move.endCol]\
	and move.endsq=="--" :
		return True
	#diagnal 
	elif move.endsq==self.board[move.endRow-1][move.endCol-1]\
	and move.endsq!="--":
		return True
	elif move.endsq==self.board[move.endRow-1][move.endCol+1]\
	and move.endsq!="--":
		return True
	else :
		return False

def bPawnMoves(self,move,board):
	# front 2sq 
	if move.endsq == self.board[move.endRow+2][move.endCol] \
	and move.startRow=="2" \
	and move.endsq=="--" \
	and self.board[move.endRow-1][move.endCol]=="--":
		return True
	# front 1sq
	elif move.endsq==self.board[move.endRow+1][move.endCol]\
	and move.endsq=="--" :
		return True
	#diagnal 
	elif move.endsq==self.board[move.endRow+1][move.endCol-1]\
	and move.endsq!="--":
		return True
	elif move.endsq==self.board[move.endRow+1][move.endCol+1]\
	and move.endsq!="--":
		return True
	else :
		return False

def KnightMoves(self,move,board):
	pass
def BishopMoves(self,move,board):
	pass
def RookMoves(self,move,board):
	pass
def KingMoves(self,move,board):
	pass
def QueenMoves(self,move,board):
	pass




# 실행
game1 = GameState()
pprint(game1.board)

while True:
	if game1.whiteToMove ==True:
		print("White Turn")
	else : 
		print("Black Turn")
	movein = input("=>")
	
	os.system('clear')
	move1 = Move(movein[:2], movein[2:], game1.board)
	
	move11=game1.makemove(move1)
	
	if move11 == "moved":
		game1.logmake(move1)
	# else : 
	# 	print("logmake_fail")
	pprint(game1.board)
	print("\n")
	print(f"log{game1.movelog}")
	
# 확인	
	# print(movein[:2])
	# print(movein[2:])
	# print(f"start : {move1.startCol}-{move1.startRow}, end : {move1.endCol}-{move1.endRow}")
	# print(move1.pieceMoved[0])
	# print(game1.whiteToMove) 
	# print(move11)
