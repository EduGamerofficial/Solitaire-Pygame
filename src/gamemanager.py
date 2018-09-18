import pygame, os
from gameboard import GameBoard
from constants import *

class GameManager(object):
    def __init__(self):
        # Base initialization
        pygame.init()
        pygame.display.set_caption("Solitaire")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # Textures
        self.my_path = "%s/.." % os.path.dirname(os.path.realpath(__file__))
        self.background_tex = pygame.image.load("%s/img/background.png" % self.my_path)

        card_tex = pygame.image.load("%s/img/card.png" % self.my_path)
        empty_holder_tex = pygame.image.load("%s/img/empty_holder.png" % self.my_path)

        suit_textures = {
            "HEARTS"   : pygame.transform.scale(pygame.image.load("%s/img/suits/big_hearts.png"   % self.my_path), CARD_SMALL_ITEM_SIZE),
            "DIAMONDS" : pygame.transform.scale(pygame.image.load("%s/img/suits/big_diamonds.png" % self.my_path), CARD_SMALL_ITEM_SIZE),
            "CLUBS"    : pygame.transform.scale(pygame.image.load("%s/img/suits/big_clubs.png"    % self.my_path), CARD_SMALL_ITEM_SIZE),
            "SPADES"   : pygame.transform.scale(pygame.image.load("%s/img/suits/big_spades.png"   % self.my_path), CARD_SMALL_ITEM_SIZE)
        }

        black_value_textures = {
            1:  pygame.transform.scale(pygame.image.load("%s/img/numbers/ace_black.png"    % self.my_path), CARD_SMALL_ITEM_SIZE),
            2:  pygame.transform.scale(pygame.image.load("%s/img/numbers/two_black.png"    % self.my_path), CARD_SMALL_ITEM_SIZE),
            3:  pygame.transform.scale(pygame.image.load("%s/img/numbers/three_black.png"  % self.my_path), CARD_SMALL_ITEM_SIZE),
            4:  pygame.transform.scale(pygame.image.load("%s/img/numbers/four_black.png"   % self.my_path), CARD_SMALL_ITEM_SIZE),
            5:  pygame.transform.scale(pygame.image.load("%s/img/numbers/five_black.png"   % self.my_path), CARD_SMALL_ITEM_SIZE),
            6:  pygame.transform.scale(pygame.image.load("%s/img/numbers/six_black.png"    % self.my_path), CARD_SMALL_ITEM_SIZE),
            7:  pygame.transform.scale(pygame.image.load("%s/img/numbers/seven_black.png"  % self.my_path), CARD_SMALL_ITEM_SIZE),
            8:  pygame.transform.scale(pygame.image.load("%s/img/numbers/eight_black.png"  % self.my_path), CARD_SMALL_ITEM_SIZE),
            9:  pygame.transform.scale(pygame.image.load("%s/img/numbers/nine_black.png"   % self.my_path), CARD_SMALL_ITEM_SIZE),
            10: pygame.transform.scale(pygame.image.load("%s/img/numbers/ten_black.png"    % self.my_path), CARD_SMALL_ITEM_SIZE),
            11: pygame.transform.scale(pygame.image.load("%s/img/numbers/knight_black.png" % self.my_path), CARD_SMALL_ITEM_SIZE),
            12: pygame.transform.scale(pygame.image.load("%s/img/numbers/queen_black.png"  % self.my_path), CARD_SMALL_ITEM_SIZE),
            13: pygame.transform.scale(pygame.image.load("%s/img/numbers/king_black.png"   % self.my_path), CARD_SMALL_ITEM_SIZE)
        }

        red_value_textures = {
            1:  pygame.transform.scale(pygame.image.load("%s/img/numbers/ace_red.png"    % self.my_path), CARD_SMALL_ITEM_SIZE),
            2:  pygame.transform.scale(pygame.image.load("%s/img/numbers/two_red.png"    % self.my_path), CARD_SMALL_ITEM_SIZE),
            3:  pygame.transform.scale(pygame.image.load("%s/img/numbers/three_red.png"  % self.my_path), CARD_SMALL_ITEM_SIZE),
            4:  pygame.transform.scale(pygame.image.load("%s/img/numbers/four_red.png"   % self.my_path), CARD_SMALL_ITEM_SIZE),
            5:  pygame.transform.scale(pygame.image.load("%s/img/numbers/five_red.png"   % self.my_path), CARD_SMALL_ITEM_SIZE),
            6:  pygame.transform.scale(pygame.image.load("%s/img/numbers/six_red.png"    % self.my_path), CARD_SMALL_ITEM_SIZE),
            7:  pygame.transform.scale(pygame.image.load("%s/img/numbers/seven_red.png"  % self.my_path), CARD_SMALL_ITEM_SIZE),
            8:  pygame.transform.scale(pygame.image.load("%s/img/numbers/eight_red.png"  % self.my_path), CARD_SMALL_ITEM_SIZE),
            9:  pygame.transform.scale(pygame.image.load("%s/img/numbers/nine_red.png"   % self.my_path), CARD_SMALL_ITEM_SIZE),
            10: pygame.transform.scale(pygame.image.load("%s/img/numbers/ten_red.png"    % self.my_path), CARD_SMALL_ITEM_SIZE),
            11: pygame.transform.scale(pygame.image.load("%s/img/numbers/knight_red.png" % self.my_path), CARD_SMALL_ITEM_SIZE),
            12: pygame.transform.scale(pygame.image.load("%s/img/numbers/queen_red.png"  % self.my_path), CARD_SMALL_ITEM_SIZE),
            13: pygame.transform.scale(pygame.image.load("%s/img/numbers/king_red.png"   % self.my_path), CARD_SMALL_ITEM_SIZE)
        }

        deck_tex = card_tex

        # Initialize gameboard
        self.gameBoard = GameBoard(card_tex, empty_holder_tex, suit_textures, [black_value_textures, red_value_textures], deck_tex)

        # Input
        self.mouse_held = False

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            else:
                self.handleMouseInput(event)

    def handleMouseInput(self, event):
        self.gameBoard.mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.mouse_held: # Left mouse pressed
                self.mouse_held = True
                self.gameBoard.mouseClicked()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.mouse_held: # Left mouse released
                self.mouse_held = False
                self.gameBoard.mouseReleased()

    def playGame(self):
        running = True
        while running:
            if self.handleInput() == 1:
                running = False
            self.drawGame()

    def drawGame(self):
        self.screen.blit(self.background_tex, (0,0))
        self.gameBoard.drawBoard(self.screen)
        pygame.display.flip()