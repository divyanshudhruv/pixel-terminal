import numpy as np
import cv2

class ClassicEffect:
    
    def __init__(self, ascii_chars: str = None):
        self.ascii_chars = ascii_chars or "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
        
    def render_frame(self, frame: np.ndarray, terminal_width: int, terminal_height: int) -> str:
        resized_frame = cv2.resize(frame, (terminal_width, terminal_height))
        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
        
        output_lines = []
        
        for y in range(terminal_height):
            line_chars = []
            for x in range(terminal_width):
                b, g, r = resized_frame[y, x]
                brightness = gray_frame[y, x]
                char = self.get_ascii_char(brightness)
                
                line_chars.append(f"\033[38;2;{r};{g};{b}m{char}" )
            
            output_lines.append("".join(line_chars))
        
        return "\n".join(output_lines) + "\033[0m"
    
    def get_ascii_char(self, brightness: int) -> str:
        index = int((brightness / 255) * (len(self.ascii_chars) - 1))
        return self.ascii_chars[index]
