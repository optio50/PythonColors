#!/usr/bin/python3
# module for standard colors, foreground and background
"""Colors class: reset all colors with colors.reset
two sub classes
fg for foreground
bg for background
use as  colors.subclass.colorname
i.e. colors.fg.red or colors.bg.green
also, colors.reverse, the generic bold, colors.reverse, disable
colors.reverse, underline, colors.reverse, reverse, colors.reverse, strike through, 
colors.reverse, and invisible work with the main class i.e. colors.bold """


class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'
    blink = '\033[05m'

    class fg:
        red = '\033[38;5;1m'
        light_red = '\033[38;5;9m'
        cyan = '\033[38;5;6m'
        light_cyan = '\033[38;5;14m'
        gray = '\033[38;5;240m'
        light_gray = '\033[38;5;246m'
        white = '\033[38;5;15m'
        black = '\033[38;5;16m'
        orange = '\033[38;5;202m'
        light_orange = '\033[38;5;172m'
        blue = '\033[38;5;21m'
        light_blue = '\033[38;5;39m'
        green = '\033[38;5;28m'
        light_green = '\033[38;5;34m'
        purple = '\033[38;5;93m'
        light_purple = '\033[38;5;99m'
        yellow = '\033[38;5;220m'
        light_yellow = '\033[38;5;227m'
        pink = '\033[38;5;201m'
        light_pink = '\033[38;5;206m'

    class bg:
        red = '\033[48;5;1m'
        light_red = '\033[48;5;9m'
        cyan = '\033[48;5;6m'
        light_cyan = '\033[48;5;14m'
        gray = '\033[48;5;240m'
        light_gray = '\033[48;5;246m'
        white = '\033[48;5;15m'
        black = '\033[48;5;16m'
        orange = '\033[48;5;202m'
        light_orange = '\033[48;5;172m'
        blue = '\033[48;5;21m'
        light_blue = '\033[48;5;39m'
        green = '\033[48;5;28m'
        light_green = '\033[48;5;34m'
        purple = '\033[48;5;93m'
        light_purple = '\033[48;5;99m'
        yellow = '\033[48;5;220m'
        light_yellow = '\033[48;5;227m'


# Demo
def stand_colors():
    print(colors.blink, colors.fg.red, colors.reverse, f"{'Blinking & Red'.center(30)}", colors.reset, sep="")
    print(colors.fg.light_red, colors.reverse, f"{'Light Red'.center(30)}", sep="")
    print(colors.fg.cyan, colors.reverse, f"{'Cyan'.center(30)}", colors.reset, sep="")
    print(colors.bold, colors.fg.light_cyan, colors.reverse, f"{'Bold & Light Cyan'.center(30)}", colors.reset, sep="")
    print(colors.fg.gray, colors.reverse, f"{'Gray'.center(30)}", colors.reset, sep="")
    print(colors.fg.light_gray, colors.reverse, f"{'Light Gray'.center(30)}", sep="")
    print(colors.fg.white, colors.reverse, f"{'White'.center(30)}", colors.reset, sep="")
    print(colors.fg.orange, colors.reverse, f"{'Orange'.center(30)}", colors.reset, sep="")
    print(colors.fg.light_orange, colors.reverse, f"{'Light Orange'.center(30)}", colors.reset, sep="")
    print(colors.fg.pink, colors.reverse, f"{'Pink'.center(30)}", colors.reset, sep="")
    print(colors.fg.light_pink, colors.reverse, f"{'Light Pink'.center(30)}", colors.reset, sep="")
    print(colors.fg.white, colors.bg.black, f"{'Black'.center(30)}", colors.reset, sep="")
    print(colors.fg.blue, colors.reverse, f"{'Blue'.center(30)}", colors.reset, sep="")
    print(colors.fg.light_blue, colors.reverse, f"{'Light Blue'.center(30)}", sep="")
    print(colors.fg.green, colors.reverse, f"{'Green'.center(30)}", sep="")
    print(colors.underline, colors.fg.light_green, colors.reverse, f"{'Underline & Light Green'.center(30)}", colors.reset, sep="")
    print(colors.fg.purple, colors.reverse, f"{'Purple'.center(30)}", colors.reset, sep="")
    print(colors.fg.light_purple, colors.reverse, f"{'Light Purple'.center(30)}", colors.reset, sep="")
    print(colors.strikethrough, colors.fg.yellow, colors.reverse, f"{'Strikethrough & Yellow'.center(30)}", colors.reset, sep="")
    print(colors.fg.light_yellow, colors.reverse, f"{'Light Yellow'.center(30)}", colors.reset, sep="")

# Color Demonstration
#stand_colors()
