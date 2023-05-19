import pygame

pygame.init() #초기화

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Nado Game") #게임 이름

#이벤트 루프
runnig = True # 게임이 진행 중 인가?
while runnig:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생 여부
            runnig = False # 게임 진행 중 아님

# 게임 종료
pygame.quit()
