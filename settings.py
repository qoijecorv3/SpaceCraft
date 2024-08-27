import pygame, random
from PIL import Image, ImageFilter
pygame.init()
fps = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 740))
# hình ảnh 
background = pygame.image.load('GameStuff/3CDxl1.png'). convert_alpha()
background = pygame.transform.scale(background,(1000,740))
img = Image.open('GameStuff/3CDxl1.png')
img = img.filter(ImageFilter.GaussianBlur(radius=5))
img = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
img = pygame.transform.scale(img, (1000, 740))
dan = pygame.image.load('GameStuff/dan.png'). convert_alpha()
dan = pygame.transform.scale(dan,(40,40)) 
bad_bullet_pic = pygame.image.load('GameStuff/bad_bullet.png'). convert_alpha()
bad_bullet_pic = pygame.transform.scale(bad_bullet_pic,(15,40))
good_ship = pygame.image.load('GameStuff/goodship.png'). convert_alpha()
good_ship = pygame.transform.scale(good_ship,(81,96))
bad_ship = pygame.image.load('GameStuff/badship.png'). convert_alpha()
bad_ship = pygame.transform.scale(bad_ship,(81,96))
bullet_ship = pygame.image.load('GameStuff/shippng.png'). convert_alpha()
bullet_ship = pygame.transform.scale(bullet_ship,(81,96))
setting_button = pygame.image.load('GameStuff/setting_but.png'). convert_alpha()
setting_button = pygame.transform.scale(setting_button,(50,45))
right_button = pygame.image.load('GameStuff/right_button.png'). convert_alpha()
right_button = pygame.transform.scale(right_button,(160,160))
left_button = pygame.image.load('GameStuff/left_button.png'). convert_alpha()
left_button = pygame.transform.scale(left_button,(160,160))
pause_button = pygame.image.load('GameStuff/pause_button.png'). convert_alpha()
pause_button = pygame.transform.scale(pause_button,(200,200))
sound = pygame.image.load('GameStuff/sound.png'). convert_alpha()
sound = pygame.transform.scale(sound,(50,45))
unsound = pygame.image.load('GameStuff/unsoundpng.png'). convert_alpha()
unsound = pygame.transform.scale(unsound,(50,45))
music = [sound,	 unsound]
howplay = pygame.image.load('GameStuff/how_to_play_preview_rev_1.png'). convert_alpha()
howplay = pygame.transform.scale(howplay,(800,600))
quit_button = pygame.image.load('GameStuff/quit_buttonpng.png'). convert_alpha()
quit_button = pygame.transform.scale(quit_button,(30,30))
heart_pic = pygame.image.load('GameStuff/heartpng.png'). convert_alpha()
heart_pic = pygame.transform.scale(heart_pic,(30,30))
boss = pygame.image.load('GameStuff/boss.png'). convert_alpha()
boss = pygame.transform.scale(boss,(200,200))
canhbao = pygame.image.load('GameStuff/canhbao.png'). convert_alpha()
canhbao = pygame.transform.scale(canhbao,(40,40))
lazer = pygame.image.load('GameStuff/lazer.png'). convert_alpha()
lazer = pygame.transform.scale(lazer,(60,740))
ink_1 = pygame.image.load('GameStuff/ink_1.png'). convert_alpha()
ink_1 = pygame.transform.scale(ink_1,(30,60))
ink_2 = pygame.image.load('GameStuff/ink_2.png'). convert_alpha()
ink_2 = pygame.transform.scale(ink_2,(30,60))
ink_3 = pygame.image.load('GameStuff/ink_3.png'). convert_alpha()
ink_3 = pygame.transform.scale(ink_3,(30,60))
spin = pygame.image.load('GameStuff/spin.png'). convert_alpha()
spin = pygame.transform.scale(spin,(50,50))
boss_bullet = pygame.image.load('GameStuff/red_bulletpng.png'). convert_alpha()
boss_bullet = pygame.transform.scale(boss_bullet,(10,30))
boss_bullet_left = pygame.transform.rotate(boss_bullet, -15)
boss_bullet_right = pygame.transform.rotate(boss_bullet, 15)
# countdown time
bad_bullet_spawn = pygame.USEREVENT+3 
pygame.time.set_timer(bad_bullet_spawn, 3000) 
auto = pygame.USEREVENT+4 
pygame.time.set_timer(auto, 300)
time = pygame.USEREVENT+5
pygame.time.set_timer(time, 1000)
boss_move_time = pygame.USEREVENT+8
pygame.time.set_timer(boss_move_time, 10000)
# chữ 
font = pygame.font.Font('GameStuff/ARCADECLASSIC.TTF',200)
press = font.render("PRESS",True, (0,0,0))
press_rect = press.get_rect(center = (500,200))
to_start = font.render("START",True, (0,0,0))
to_start_rect = to_start.get_rect(center = (500,600))	
you_win = font.render("YOU   WIN", True, (0,0,0))
you_win_rect = you_win.get_rect(center = (500, 300))

font_game = pygame.font.Font('GameStuff/ARCADECLASSIC.TTF',70)
congra = font_game.render("congratulation!", True, (0,0,0))
congra_rect = congra.get_rect(center = (500, 500))
resume = font_game.render("PRESS   SPACE   AGAIN   TO   RESUME",True, (0,0,0))
resume_rect = resume.get_rect(center = (500,550))

font_time = pygame.font.Font('GameStuff/04B_19.TTF',40) # clock

# tàu phe xấu 
ship_list = []
bullet_ship_list = []
# hiệu ứng game 
game_off = False
game_win = False 
# âm thanh
gun = pygame.mixer.Sound('GameStuff/Tieng-sung-laser-ban-trong-phim-khoa-hoc-vien-tuong-www_tiengdong_com (mp3cut.net).wav')
point = pygame.mixer.Sound('GameStuff/explosion-6055 (mp3cut.net).mp3')	
bg_music = pygame.mixer.Sound('GameStuff/1.MainTheme-320bit.mp3')
lose = pygame.mixer.Sound('GameStuff/Am-thanh-that-vong-www_tiengdong_com.mp3')
warning = pygame.mixer.Sound('GameStuff/mixkit-classic-alarm-995 (mp3cut.net).wav')
clicking = pygame.mixer.Sound('GameStuff/beep-6-96243.mp3')  
winning = pygame.mixer.Sound('GameStuff/piglevelwin2mp3-14800.mp3')  
play = True
sound = True
# đạn phe tốt
bullet_list = []
auto_shot = False
# đạn phe xấu 
bad_bullet_list = [] 
# bấm nút setting
setting = False
# boss
boss_appear = False
boss_action = ['three', 'spin']
boss_bullet_list = []
boss_bullet_left_list = []
boss_bullet_right_list = []
check_act = False
stop_act = 0
action = 'nothing'

# spin 
x = random.choice([1,-1])
y = 1
# ink
ink = [ink_1, ink_2, ink_3]
# 3 column
ban = False
i = 0 