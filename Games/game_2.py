import pygame

class Game:
    def __init__(self, width=1535, height=780, title="Pygame Window Test"):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True

        # Load and scale background
        self.background = pygame.image.load(r"C:\Users\ASUS\Desktop\main\Games\assests\background.png")
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

        # Load and scale player
        self.player = pygame.image.load(r"C:\Users\ASUS\Desktop\main\Games\assests\shadow1.png")
        self.player = pygame.transform.scale(self.player, (100, 100))
        self.player_x = 100
        self.player_y = 550
        self.player_speed = 20

        # HP bar setup
        self.hp_color = (255, 0, 0)
        self.hp_rect = pygame.Rect(50, 50, 200, 20)  # x, y, width, height

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()

        # Move left
        if keys[pygame.K_LEFT]:
            if self.player_x > 0:  # check left border
                self.player_x -= self.player_speed

        # Move right
        if keys[pygame.K_RIGHT]:
            if self.player_x < self.width - 50:  # check right border
                self.player_x += self.player_speed

    def draw(self):
        # Draw background
        self.screen.blit(self.background, (0, 0))
        # Draw player
        self.screen.blit(self.player, (self.player_x, self.player_y))
        # Draw HP bar
        pygame.draw.rect(self.screen, self.hp_color, self.hp_rect)
        # Update display
        pygame.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
