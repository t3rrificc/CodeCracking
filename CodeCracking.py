#CODE CRACKING: PIN

import random
import pygame
import pyautogui

class Lamanie:
    def __init__(self):
        self.chars = "1234567890"
        self.chars_list = list(self.chars)
        pygame.init()
        self.password = pyautogui.password("Enter a password: ")
        self.guess_password = ""

        while (self.guess_password != self.password):
            self.guess_password = random.choices(self.chars_list, k=len(self.password))
            print("<==========" + str(self.guess_password) + "===========>")

            if (self.guess_password == list(self.password)):
                window_size = (900, 300)
                screen = pygame.display.set_mode(window_size)
                pygame.display.set_caption("Moje okno")

                font = pygame.font.Font(None, 36)
                text = font.render("Your password is" + " " + " ".join(self.guess_password), True, (255, 255, 255))
                screen.blit(text, (325, 125))

                pygame.display.flip()

                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()

if __name__ == "__main__":
    Lamanie()

