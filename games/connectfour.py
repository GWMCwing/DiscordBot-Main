import os
PREFIX = os.getenv("PREFIX")
class waitingqueue:
	def __init__ (self,message):
		self.player1 = message.author
		self.id = message.author.id
		self.playercount = 1
		await message.channel.send("The id of this game is: "+str(self.id) + "\n Enter "+ PREFIX +"join " + str(self.id)+ " to join the game")

	def addplayer(self,message):
		if(self.playercount == 1):
			self.player2 = message.author
			await message.channel.send("The game can be started " + PREFIX+"startGame")
		else:
			await message.channel.send("The game is full")
	def leave(self,message):
		if message.author == self.player1:
			self.player1 = None
			self.playercount -=1
		elif message.author == self.player2:
			self.player2 = None
			self.playercount -=1
		else: await message.channel.send("You are not in this game")
	def startGame(self,message):
		return connectfourboard(message,self.player1,self.player2)
			

class connectfourboard:
	def __init__(self,message,player1,player2):
		self.guild = message.guild
		self.channel = message.channel
		self.player1 = player1
		self.player2 = player2
		self.board = self.createboard()
		self.round = 1
		self.message = message
	def createboard():
		boardlist = []
		i = 0
		while i < 6:
			templist = []
			j = 0
			while j < 7:
				templist.append(0)
			boardlist.append(templist)
			i+=1
		return boardlist

	def printboard(self):
		# to be finished
		templist = []

	def addCircle(self,j):
		if self.board[0][j] != 0:
			return False
		i =0
		while i < 6:
			if self.board[i][j] != 0:
				self.board[i-1][j] = self.round
			i+= 1
		self.round *= -1
		return True

	def checkFinish(self,i,j):
		check = self.board[i][j]
		# check top
		tempcount = 1
		if i > 2:
			a = 1
			while a < 4:
				if self.board[i - a][j] == check:
					tempcount +=1
				else: 
					break
				a+=1
			if tempcount == 4:
				return True
		# check left
		tempcount = 1
		if j > 2:
			a = 1
			while a < 4:
				if self.board[i][j - a] == check:
					tempcount +=1
				else: 
					break
				a+=1
			if tempcount == 4:
				return True
		# check bot
		tempcount = 1
		if i <3:
			a = 1
			while a < 4:
				if self.board[i + a][j] == check:
					tempcount +=1
				else: 
					break
				a+=1
			if tempcount == 4:
				return True
		# check right
		tempcount = 1
		if j <4:
			a = 1
			while a < 4:
				if self.board[i][j + a] == check:
					tempcount +=1
				else: 
					break
				a+=1
			if tempcount == 4:
				return True
		# check topleft
		tempcount = 1
		if i > 2 and j > 2:
			a = 1
			while a < 4:
				if self.board[i - a][j - a] == check:
					tempcount +=1
				else: 
					break
				a+=1
			if tempcount == 4:
				return True
		# check botleft
		tempcount = 1
		if i <3  and j > 2:
			a = 1
			while a < 4:
				if self.board[i + a][j - a] == check:
					tempcount +=1
				else: 
					break
				a+=1
			if tempcount == 4:
				return True
		# check botright
		if i <3  and j <4:
			a = 1
			while a < 4:
				if self.board[i + a][j + a] == check:
					tempcount +=1
				else: 
					break
				a+=1
			if tempcount == 4:
				return True
		# check topright
		tempcount = 1
		if i > 2 and j <4:
			a = 1
			while a < 4:
				if self.board[i - a][j + a] == check:
					tempcount +=1
				else: 
					break
				a+=1
			if tempcount == 4:
				return True
		return False
		

	


