class Colorizer:
    color_codes = {
        'reset': '\033[0m',
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m'
    }

    def __init__(self, color):
        self.color = color

    def __enter__(self):
        if self.color in Colorizer.color_codes:
            print(Colorizer.color_codes[self.color], end='')

    def __exit__(self, exc_type, exc_value, traceback):
        print(Colorizer.color_codes['reset'], end='')



with Colorizer('red'):
    print('printed in red')

print('printed in default color')
