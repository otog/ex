import pygame

pygame.init() #초기화

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Nado Game") #게임 이름

#FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:/backup/Y6952657/KYG/worksapce/python/ex/pygame_basic/background.png")

# 캐릭터 불러오기
character = pygame.image.load("C:/backup/Y6952657/KYG/worksapce/python/ex/pygame_basic/character.png")
character_size = character.get_rect().size #이미지 크기 구함
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1]   # 캐릭터 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 
character_y_pos = screen_height -character_height # 화면 새로 크기의 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.6


#이벤트 루프
runnig = True # 게임이 진행 중 인가?
while runnig:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수 설정
    
    
    
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생 여부
            runnig = False # 게임 진행 중 아님
        
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            
            if event.key == pygame.K_LEFT: #캐릭터 왼쪽으로 이동
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT: #캐릭터 오른쪽으로 이동
                to_x += character_speed 
            elif event.key == pygame.K_UP:  #캐릭터 위로 이동
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:  #캐릭터 아래로 이동
                to_y += character_speed
        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0  
                
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    
    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width 
        
    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height           
    
    screen.blit(background, (0,0))  #배경 그리기 
    
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    
    pygame.display.update() # 게임화면을 다시 그리기!

# 게임 종료
pygame.quit()
