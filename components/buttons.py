import pygame

class Button():
	"""
	This function is used to initialize the button

	Parameters:
			surface (pygame.Surface): The surface of the button
			x (int): The x position of the button
			y (int): The y position of the button
			image (pygame.Surface): The image of the button
			size_x (int): The size of the button in x axis
			size_y (int): The size of the button in y axis
			name (str): The name of the button
			description (str): The description of the button. Default is empty string

 	Returns:
			None
	"""
	def __init__(self, surface, x, y, image, size_x, size_y, name, description=''):
		self.image = pygame.transform.scale(image, (size_x, size_y))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
		self.surface = surface
		self.name = name
		self.description = description

		"""
		This function is used to draw the button

		Parameters:
				None

		Returns:
				action (bool): The action of the button
		"""
	def draw(self):
		action = False

		pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		self.surface.blit(self.image, (self.rect.x, self.rect.y))

		return action