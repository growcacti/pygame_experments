






class Explosion:
    

def __init__(self, center, size):
    pg.sprite.Sprite.__init__(self)
    self.size = size

    img = pg.image.load('regularExplosion00.png').convert()
    img.set_colorkey(BLACK)
    if size == 'lg':
        self.image = pg.transform.scale(img, (75, 75))
    elif size == 'sm':
        self.image = pg.transform.scale(img, (32, 32))

    self.rect = self.image.get_rect()
    self.rect.center = center
    self.frame = 0
    self.last_update = pg.time.get_ticks()
    self.frame_rate = 50

class Explosion(pygame.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.image = explosion_anim[0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50 # how long to wait for the next frame VELOCITY OF THE EXPLOSION

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(explosion_anim):
				self.kill() # if we get to the end of the animation we don't keep going.
			else:
				center = self.rect.center
				self.image = explosion_anim[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center

meteor_images = []
