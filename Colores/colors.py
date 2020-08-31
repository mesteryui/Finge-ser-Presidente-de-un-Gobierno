from sys import stdout

#Color Rojo

def red() :
    RED = "\033[1;31m"
    stdout.write(RED)

#Color Cyan

def cyan() :
    CYAN = "\033[1;36m"
    stdout.write(CYAN)

#Color Azul

def blue() :
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

#Color Verde

def green() :
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

#Negrita

def bold() :
   BOLD ="\033[1m"
   stdout.write(BOLD)

#Resetear

def reset() :
    RESET = "\033[0m"
    stdout.write(RESET)

#Color Amariloo

def yellow() :
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)