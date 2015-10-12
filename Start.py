from core import main

game = main.Game()
game.run_game()

# class test:
#     def __init__(self, a):
#         self.a = a
#
#     def __del__(self, y):
#         print(self.a, y, 'died')
#
# foo = test(6)
# foo.__del__('real')
# print('end')