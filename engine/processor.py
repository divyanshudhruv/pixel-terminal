import numpy as np
import cv2
from typing import Tuple, List

class ASCIIProcessor:
    
    def __init__(self, ascii_chars: str = None):
        self.ascii_chars = ascii_chars or "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
        
    def process_frame(self, frame: np.ndarray, terminal_width: int, terminal_height: int) -> Tuple[np.ndarray, np.ndarray]:
        resized_frame = cv2.resize(frame, (terminal_width, terminal_height))
        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
        ascii_indices = ((gray_frame / 255.0) * (len(self.ascii_chars) - 1)).astype(int)
        
        return ascii_indices, resized_frame
        
    def indices_to_chars(self, indices: np.ndarray) -> List[List[str]]:
        chars = []
        for row in indices:
            char_row = [self.ascii_chars[idx] for idx in row]
            chars.append(char_row)
        return chars
