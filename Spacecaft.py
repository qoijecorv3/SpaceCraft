# import thư viện, file 
import pygame, sys, random
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.init()
from settings import *
pygame.display.set_caption('Space_Craft')
# đạn bắn 
class shots:
	def __unit__(seft):
		pass
	def bullet_move(seft,bullets):
		for bullet in bullets:
			bullet.centery -= 10
			if bullet.centery <= -10:
				bullets.remove(bullet)	
		return bullets
	def bad_bullet_move(seft,bullets):
		for bullet in bullets:
			bullet.centery += 8
			if bullet.centery >= 750:
				bullets.remove(bullet) 		
		return bullets
	def boss_bullet_move(seft,bullets, direc):
		for bullet in bullets:
			bullet.centery += 8
			if direc == 'left':
				bullet.centerx -= 100/128
			if direc == 'right':
				bullet.centerx += 100/128 		
		return bullets
	def spawn_bullet(seft, bullet_pic, x, y):
		new_bullet = bullet_pic.get_rect(center = (x,y))
		return new_bullet 
	def spawn_bad_bullet(seft, ships):
		for ship in ships:
			new_bad_bullet = bad_bullet_pic.get_rect(center = (ship.centerx, ship.centery))
			bad_bullet_list.append(new_bad_bullet)
			pygame.mixer.Channel(0).play(gun)
			gun.set_volume(0.03)
	def draw_bullet(seft,bullets, pic):	
		for bullet in bullets:
			screen.blit(pic, bullet)
# đạn mọi phe 		
good_bullet = shots()
bad_bullet = shots()
stranght = shots()
left = shots()
right = shots()
# tàu boss 
class boss_ship:
	def __unit__(seft):
		pass
	def hit_bullet(seft, bullets):
		global health, game_win
		for bullet in bullets:
			if bullet.colliderect(boss_rect):
				bullets.remove(bullet)
				pygame.mixer.Channel(1).play(point)
				point.set_volume(0.5)	
				health -= 2
		if health == 0:
			game_win = True
	def blit_heart(seft, health):
		pygame.draw.rect(screen, (255,255,255),(300,10,400,10))
		pygame.draw.rect(screen, (255,0,0),(300,10,health,10))
		pygame.draw.rect(screen, (0,0,0),(295,5,410,20), width = 5)
	def draw_boss(seft, ptr):
		global check_act
		boss_rect.centery += 2
		if boss_rect.centery == 98:
			check_act = True
	def move(seft):
		global ban, boss_move
		if boss_rect.centerx != boss_x:
			if boss_x > boss_rect.centerx and boss_rect.centerx != boss_x:
				boss_rect.centerx += 5
			if boss_x < boss_rect.centerx and boss_rect.centerx != boss_x:
				boss_rect.centerx -= 5
			ban = False
		else:
			boss_move = False
			ban = True
	def lazer(seft):
		global lazer_counttime, lazer_boolean
		lazer_counttime+=1
		screen.blit(lazer, lazer_rect)
		if lazer_rect.centery != 370 and lazer_counttime >= 530:
			lazer_rect.centery += 37
		if lazer_rect.centery == 370:
			lazer_counttime = 0
		else:
			screen.blit(canhbao, (lazer_rect[0]-11,600))
	def three_column_bullet(seft):
		global check_act, bullet_time, stop_act, boss_bullet_list, boss_bullet_left_list, boss_bullet_right_list, ban
		if ban:
			stop_act += 1
			bullet_time += 1
			if stop_act == 800:
				stop_act = 0
				check_act = True
				ink_rect = ink_1.get_rect(center = (random.randrange(30, 930, 100)+10, -100))
			if bullet_time == 150:
				boss_bullet_list.append(stranght.spawn_bullet(boss_bullet, boss_rect.centerx, boss_rect.centery))
				boss_bullet_left_list.append(left.spawn_bullet(boss_bullet_left, boss_rect.centerx, boss_rect.centery)) 
				boss_bullet_right_list.append(right.spawn_bullet(boss_bullet_right, boss_rect.centerx, boss_rect.centery))
				bullet_time = 0
			
			
	def ink(seft):
		global ink_count, ink_rect, ink_sprite
		ink_count += 1
		screen.blit(ink[ink_sprite], ink_rect)
		ink_sprite += 1;
		if ink_sprite == 2:
			ink_sprite = 0
		if ink_count == 500:
			ink_rect = ink_1.get_rect(center = (random.randrange(30, 930, 100), -100))
			ink_count = 0
		ink_rect.centery += 5	
	def ball(seft):
		global x, y, stop_act, check_act 
		stop_act += 1
		screen.blit(spin, spin_rect)	
		if spin_rect.centerx >= 975:
			x = -1
		elif spin_rect.centerx <= 25:
			x = 1	
		elif spin_rect.centery >= 715:
			y = -1
		elif spin_rect.centery <=25:
			y = 1
		spin_rect.centery += y*3
		spin_rect.centerx += x*3
		if stop_act == 800:
			stop_act = 0
			check_act = True
# boss 1 
green_boss = boss_ship()
# bắn tàu xấu 
def collide(bullets, ships):
	for ship in ships:
		for bullet in bullets:
			if  ship.centery >= 3 and bullet.colliderect(ship):
				bullets.remove(bullet)
				ships.remove(ship)
				pygame.mixer.Channel(1).play(point)
				point.set_volume(0.7)
# tạo tàu xấu 
class taus:
	def __unit__(seft):
		pass
	def ship_spawn(seft,pic):
		new_ship = pic.get_rect(topleft = (random.randrange(9,809,100),-100))
		return new_ship
	def ship_move(seft, ships): 
		for ship in ships:   
			ship.centery += 2
			if ship.centery > 790:
				ships.remove(ship)
		return ships
	def ship_movement(seft, ships): 
		for ship in ships:   
			if ship.centery <= 200:
				ship.centery += 2 
		return ships
	def draw_ship(seft,ships, pic):
		for ship in ships:
			screen.blit(pic, ship)
# tàu xấu 
bad_ship_1 = taus()
bad_ship_2 = taus()
# mất máu 
def game_over(ships, bullets):
	global heart
	for ship in ships:
		# tàu đen vượt vạch 
		if ship.centery == 788:
			pygame.mixer.Channel(0).play(warning)
			lose.set_volume(0.05)
			return True
		# tàu đen đụng tàu chính nghĩa 
		if ship.colliderect(good_ship_rect):
			pygame.mixer.Channel(1).play(point)
			point.set_volume(0.7)
			return True
	# tàu tím bắn trúng tàu đen 
	for bullet in bullets:
		if bullet.colliderect(good_ship_rect): 
			bullets.remove(bullet)
			pygame.mixer.Channel(0).play(point)
			point.set_volume(0.7)
			return True
	return False
# boss làm tàu chính nghĩa mất máu 
def boss_collide(bullets_t, bullets_l, bullets_r):
	global black
	if lazer_rect.colliderect(good_ship_rect):
		pygame.mixer.Channel(0).play(point)
		point.set_volume(0.7)
		return True
	if spin_rect.colliderect(good_ship_rect):
		pygame.mixer.Channel(0).play(point)
		point.set_volume(0.7)
		return True
	for bullet in bullets_t:
		if bullet.colliderect(good_ship_rect):
			pygame.mixer.Channel(0).play(point)
			point.set_volume(0.7)
			bullets_t.remove(bullet)
			return True
	for bullet in bullets_l:
		if bullet.colliderect(good_ship_rect):
			pygame.mixer.Channel(0).play(point)
			point.set_volume(0.7)
			bullets_l.remove(bullet)
			return True
	for bullet in bullets_r:
		if bullet.colliderect(good_ship_rect):
			pygame.mixer.Channel(0).play(point)
			point.set_volume(0.7)
			bullets_r.remove(bullet)
			return True
	if ink_rect.colliderect(good_ship_rect):
		black = True
	return False
# bắn đạn chính nghĩa 
def shoot():
	bullet_list.append(good_bullet.spawn_bullet(dan, good_ship_rect.centerx,good_ship_rect[1]))
	pygame.mixer.Channel(2).play(gun) 
	gun.set_volume(0.03)  
def clock(second):
	minutes = font_time.render(str(int(second/60))+" :",True, (0,0,0))
	minutes_rect = 	minutes.get_rect(center = (30,720))
	sec = font_time.render(str(second - int(second/60)*60),True, (0,0,0))
	sec_rect = 	sec.get_rect(center = (90,720))
	screen.blit(minutes, minutes_rect)
	screen.blit(sec, sec_rect) 
def minus_heart():
	global heart, minus
	if minus == False:
		minus = game_over(ship_list, bad_bullet_list)
	if minus:
		if heart > 0:
			heart -= 1
		minus = None
	if game_over(ship_list, bad_bullet_list) == False:
		minus = False  			
def boss_minus_heart():
	global heart, boss_minus
	if boss_minus == False:
		boss_minus = boss_collide(boss_bullet_list, boss_bullet_left_list, boss_bullet_right_list)
	if boss_minus:
		if heart > 0:
			heart -= 1
		boss_minus = None
	if boss_collide(boss_bullet_list, boss_bullet_left_list, boss_bullet_right_list) == False:
		boss_minus = False
#game hoạt động
while True:
	screen.blit(background,(0,0)) 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if not game_win:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					if game_off == False:
						global ship_time, ink_sprite, spin_rect, minus, black, wait_black, lazer_counttime, boss_minus, bullet_time, ink_rect, lazer_boolean, boss_move, boss_appear, boss_rect, good_ship_rect, heart, spawntime, bad_ship_spawntime, hard_time, boss_time, ink_count, wait_black, clock_second, black, bad_bulletship_boolean, health
						# đạn 
						bullet_list.clear()
						bad_bullet_list.clear()
						bullet_ship_list.clear()
						ship_list.clear()
						ship_time = 3000
						lazer_boolean = False
						ink_rect = ink_1.get_rect(center = (random.randrange(20, 920, 100)+10, -100))
						spin_rect = spin.get_rect(center = (random.randrange(100,900,100), 25))
						# ship
						boss_move = False
						boss_appear = False
						boss_rect = boss.get_rect(center = (500, -100))
						good_ship_rect = good_ship.get_rect(topleft = (409,640))	
						heart = 5
						boss_minus = False
						# time
						spawntime = pygame.USEREVENT 
						pygame.time.set_timer(spawntime, 85000, 1)
						bad_ship_spawntime = pygame.USEREVENT+1
						pygame.time.set_timer(bad_ship_spawntime, ship_time)
						hard_time = pygame.USEREVENT+2 
						pygame.time.set_timer(hard_time, 10000)
						boss_time = pygame.USEREVENT+6
						pygame.time.set_timer(boss_time, 181000, 1) 
						ink_count = 0
						wait_black = 300
						clock_second = 90
						lazer_counttime = 0
						bullet_time = 0
						# else
						game_off = True
						game_win = False  
						black = False	 
						bad_bulletship_boolean = False
						health = 400
						lose.stop()
						minus = False
						boss_minus = False
						black = False
						ink_sprite = 0
			if game_off:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT and good_ship_rect[0]>=109:
						good_ship_rect[0] -= 100
					if event.key == pygame.K_TAB:
						auto_shot = not auto_shot
					if event.key == pygame.K_RIGHT and good_ship_rect[0] <=809:
						good_ship_rect[0] += 100
					if event.key == pygame.K_a and game_off:
						if auto_shot == False:
							shoot() 
				if boss_appear == False:
					if event.type == spawntime:
						global spawn_bullet_ship
						bad_bulletship_boolean = True
						spawn_bullet_ship = pygame.USEREVENT +9
						pygame.time.set_timer(spawn_bullet_ship, 5000)
					if bad_bulletship_boolean:
						if event.type == spawn_bullet_ship:
							# spawn thuyền tím 	
							bullet_ship_list.append(bad_ship_2.ship_spawn(bullet_ship))
					if event.type == bad_bullet_spawn:
						bad_bullet.spawn_bad_bullet(bullet_ship_list)	
					if event.type == time:
						if clock_second > 0:
						    clock_second -= 1
						else:
							clock_second = 90
					if event.type == hard_time:
						if ship_time > 1501:
							ship_time -= 200
							bad_ship_spawntime = pygame.USEREVENT+1
							pygame.time.set_timer(bad_ship_spawntime, ship_time)
					if event.type == bad_ship_spawntime:
						ship_list.append(bad_ship_1.ship_spawn(bad_ship))
					if event.type == boss_time:
						global lazer_time
						boss_appear = True
						lazer_time = pygame.USEREVENT+7
						pygame.time.set_timer(lazer_time, 5000)
				else:
					

					if event.type == lazer_time:
						global lazer_rect
						lazer_rect = lazer.get_rect(topleft = (good_ship_rect[0]+33, -740))
						lazer_boolean = True	
					if event.type == boss_move_time:
						boss_move = True
						boss_x = random.randrange(100,900,100)
				if auto_shot == True:
					if event.type == auto:
						shoot()	
			mouse_pos = pygame.mouse.get_pos()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if mouse_pos[0] >=950:
					if mouse_pos[1] >= 5 and mouse_pos[1]<=55:
						setting = True
						pygame.mixer.Channel(0).play(clicking) 
						clicking.set_volume(0.5)
				if mouse_pos[0] >=950: 
					if mouse_pos[1] >= 60 and mouse_pos[1]<=105:
							sound = not sound
							pygame.mixer.Channel(0).play(clicking) 
							clicking.set_volume(0.5)
				if mouse_pos[0] >= 905 and mouse_pos[0] <= 935:
					if mouse_pos[1]>=55 and mouse_pos[1] <=85:
						setting = False
						pygame.mixer.Channel(0).play(clicking) 
						clicking.set_volume(0.5)
	if not game_win:	
		screen.blit(setting_button, (945,5))

		if sound:
			screen.blit(music[0], (945,60)) 
			bg_music.play(-1)
			bg_music.set_volume(0.04)
		else:
			screen.blit(music[1], (945,60))
			bg_music.stop()
		
		if game_off == True:	
			bullet_list = good_bullet.bullet_move(bullet_list)
			bad_bullet_list = bad_bullet.bad_bullet_move(bad_bullet_list)
			ship_list = bad_ship_1.ship_move(ship_list)
			bullet_ship_list = bad_ship_2.ship_movement(bullet_ship_list)
			screen.blit(good_ship, good_ship_rect)
			good_bullet.draw_bullet(bullet_list, dan)
			bad_bullet.draw_bullet(bad_bullet_list, bad_bullet_pic)
			bad_ship_1.draw_ship(ship_list, bad_ship)
			bad_ship_2.draw_ship(bullet_ship_list, bullet_ship) 
			collide(bullet_list, ship_list)
			collide(bullet_list, bullet_ship_list)
			if boss_appear:	
				green_boss.blit_heart(health)
				green_boss.hit_bullet(bullet_list)
				if lazer_boolean:
					green_boss.lazer()
					if check_act:
						action = random.choice(boss_action)
						check_act = False
					if action == 'three':
						green_boss.three_column_bullet()
						spin_rect = spin.get_rect(center = (random.randrange(100,900,100), 25))
					elif action == 'spin':
						green_boss.ball()			
						green_boss.ink()
					boss_bullet_list = stranght.bad_bullet_move(boss_bullet_list)
					boss_bullet_left_list = left.boss_bullet_move(boss_bullet_left_list, 'left')
					boss_bullet_right_list = right.boss_bullet_move(boss_bullet_right_list, 'right')
					left.draw_bullet(boss_bullet_left_list, boss_bullet_left)
					stranght.draw_bullet(boss_bullet_list, boss_bullet)
					right.draw_bullet(boss_bullet_right_list, boss_bullet_right)
					
					boss_minus_heart()
					if boss_rect.centery != 100:
						green_boss.draw_boss(boss)
					if boss_move:
						green_boss.move()
					screen.blit(boss, (boss_rect))
					if  black == True:
						wait_black -= 1
						if wait_black != 0:
							pygame.draw.rect(screen, (0,0,0), (0,0,1000,600))
						else:
							wait_black = 300
							black = False
			if clock_second > 0:
				clock(clock_second)
			elif clock_second == 0:
				clock(clock_second)
			minus_heart()
			for i in range(0,heart):
				screen.blit(heart_pic, (10+40*i,10))
			if heart == 0:
				game_off = False
				pygame.mixer.Channel(1).play(lose)
				lose.set_volume(0.1)
		else:
			screen.blit(press, press_rect)
			screen.blit(right_button, (550,300))
			screen.blit(left_button, (260,300))	
			screen.blit(to_start, to_start_rect)
		if setting:
			screen.blit(img,(0,0))	
			pygame.draw.rect(screen, (0, 26, 26), (50,50,900,640), border_radius=30)
			pygame.draw.rect(screen, (179, 255, 255), (45,45,905,645), width=5, border_radius=30)
			screen.blit(howplay, (70,50))
			screen.blit(quit_button, (905,55))
	else:
		screen.blit(you_win, you_win_rect)
		screen.blit(congra, congra_rect)
		bg_music.stop()
		if play: 
			winning.play()
			play = False
	pygame.display.update()
	fps.tick(120)