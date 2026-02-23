import os
import sys

def get_terminal_size():
    try:
        return os.get_terminal_size()
    except OSError:
        return (80, 24)

def clear_screen():
    sys.stdout.write('\033[2J')
    sys.stdout.flush()

def hide_cursor():
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write('\033[?25h')
    sys.stdout.flush()

def move_cursor_home():
    sys.stdout.write('\033[H')
    sys.stdout.flush()

def enable_ansi_colors():
    if os.name == 'nt':
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
            mode = ctypes.c_ulong()
            handle = kernel32.GetStdHandle(-11)
            
            kernel32.GetConsoleMode(handle, ctypes.byref(mode))
            
            new_mode = mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING
            kernel32.SetConsoleMode(handle, new_mode)
        except Exception:
            pass
