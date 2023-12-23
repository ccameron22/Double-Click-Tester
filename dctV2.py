import pygame
import sys
import math

pygame.init()

#Set screen dimensions
screen_width = 800
screen_height = 600

#Create a screen (display surface)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Mouse Double Click Test')

font = pygame.font.Font(None, 36)

#def mouseClick():
#    global previousClickTime
#    previousClickTime = None
#    currentClickTime = pygame.time.get_ticks()
#    timeBetween = currentClickTime - previousClickTime
#    previousClickTime = currentClickTime



def results(totalClicks, errors):
    endScreen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Mouse Double Click Test Fail Rate')

    while True:
        for event in pygame.event.get():
            # Handle program quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        failRate = 0
        if totalClicks > 0:
            failRate = round(errors / totalClicks, 4)
            failRate = failRate * 100

            passFail = ""
            if failRate < 11:
                passFail = "Pass"
                qaStatus = font.render(f"{passFail}", True, (0, 255, 0))
            else:
                passFail = "Fail"
                qaStatus = font.render(f"{passFail}", True, (255, 0, 0))

            finalClickCount = font.render(f"Total Clicks: {totalClicks}", True, (255, 255, 255))
            errorCount = font.render(f"Double Clicks: {errors}", True, (255, 255, 255))
            failRate = font.render(f"Fail Rate: {failRate}%", True, (255, 255, 255))

            endScreen.blit(finalClickCount, (10, 10))
            endScreen.blit(errorCount, (10, 50))
            endScreen.blit(failRate, (10, 90))
            endScreen.blit(qaStatus, (350, 250))

            pygame.display.update()
        else:
            errorMessage = font.render(f"Error", True, (255, 255, 255))
            endScreen.blit(errorMessage, (100, 100))
            pygame.display.update()

def main():
    #Initialize Variables
    previousClickTime = None
    clock = pygame.time.Clock()
    errors = 0
    numOfClicks = 0
    totalClicks = 0
    #font = pygame.font.Font(None, 36)
    targetPosition = (screen_width // 2, screen_height // 2)
    targetRadius = 30
    targetColor = (255, 255, 255)  #White color
    hitColor = (0, 255, 0)  #Green color

    while True:
        for event in pygame.event.get():
            #Handle program quit
            if event.type == pygame.QUIT:
                results(totalClicks, errors)

            if event.type == pygame.MOUSEBUTTONDOWN:
                #Check for previous click
                if previousClickTime:
                    #Find time between clicks
                    currentClickTime = pygame.time.get_ticks()
                    timeBetween = currentClickTime - previousClickTime
                    previousClickTime = currentClickTime
                        #Check if mouse position is within radius of target
                    mousePosition = pygame.mouse.get_pos()
                    if math.dist(mousePosition, targetPosition) <= targetRadius:
                        # Check is time between clicks is less than minimum acceptable length (in ms)
                        if timeBetween < 500:
                            errors += 1
                        else:
                            numOfClicks += 1
                            totalClicks += 1
                            targetColor = hitColor

                else:
                    #First click, initialize previousClickTime
                    previousClickTime = pygame.time.get_ticks()
                    mousePosition = pygame.mouse.get_pos()
                    #Check location of mouse
                    if math.dist(mousePosition, targetPosition) <= targetRadius:
                        numOfClicks += 1
                        totalClicks += 1
                        targetColor = hitColor

                #mouse_pos = pygame.mouse.get_pos()

                #if math.dist(mouse_pos, targetPosition) <= targetRadius:
                    #numOfClicks += 1
                    #targetColor = hitColor



        #Draw the target
        pygame.draw.circle(screen, targetColor, targetPosition, targetRadius)

        #Update the score
        clickCount = font.render(f"Score: {numOfClicks}", True, (255, 255, 255))
        screen.blit(clickCount, (10, 10))

        errorsCount = font.render(f"Errors: {errors}", True, (255, 255, 255))
        screen.blit(errorsCount, (150, 10))

        #Update the screen
        pygame.display.update()

        #Set the previous mouse position
        previous_mouse_pos = pygame.mouse.get_pos()

        #Reset the target color
        targetColor = (255, 255, 255)

        #Clear the screen
        screen.fill((0, 0, 0))

        #Tick the clock
        clock.tick(60)




if __name__ == '__main__':
    main()