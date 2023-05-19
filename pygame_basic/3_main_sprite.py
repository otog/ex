import pygame

pygame.init() #초기화

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Nado Game") #게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/backup/Y6952657/KYG/worksapce/python/ex/pygame_basic/background.png")

# 캐릭터 불러오기
character = pygame.image.load("C:/backup/Y6952657/KYG/worksapce/python/ex/pygame_basic/character.png")
character_size = character.get_rect().size #이미지 크기 구함
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1]   # 캐릭터 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 
character_y_pos = screen_height -character_height # 화면 새로 크기의 가장 아래에 해당하는 곳에 위치

#이벤트 루프
runnig = True # 게임이 진행 중 인가?
while runnig:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생 여부
            runnig = False # 게임 진행 중 아님
    
    screen.blit(background, (0,0))  #배경 그리기 
    
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    
    pygame.display.update() # 게임화면을 다시 그리기!

# 게임 종료
pygame.quit()
