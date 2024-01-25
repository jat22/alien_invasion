import pygame


class Ship:
	"""Class to manage ship"""
	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Place new ship at midbottom of window
		self.rect.midbottom = self.screen_rect.midbottom

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False


	
	def update(self):
		if self.moving_right:
			self.x += self.settings.ship_speed
		if self.moving_left:
			self.x -= self.settings.ship_speed
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.y -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed

		if self.rect.right > self.screen_rect.right + (self.rect.width / 2):
			self.x = self.screen_rect.left - (self.rect.width / 2)
		elif self.rect.left < self.screen_rect.left - (self.rect.width / 2):
			self.x = self.screen_rect.right - (self.rect.width - (self.rect.width / 2))
		
		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		self.screen.blit(self.image, self.rect)