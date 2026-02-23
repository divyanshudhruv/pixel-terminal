#!/usr/bin/env python3
import argparse
import sys
import signal
import os
import cv2
# Default
sys.path.insert(0, '.')

from effects.classic import ClassicEffect
from config import DEFAULT_ASCII_SET, CAMERA_WIDTH, CAMERA_HEIGHT
from utils.terminal import get_terminal_size, clear_screen, hide_cursor, show_cursor, move_cursor_home, enable_ansi_colors

class PixelTerminal:
    """Main application class"""
    
    def __init__(self, camera_index: int = 0, width: int = None, height: int = None):
        self.camera_index = camera_index
        self.custom_width = width
        self.custom_height = height
        self.running = False
        self.effect = None
        
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
        
    def _signal_handler(self, signum, frame):
        print("\n[!] Stopping...")
        self.running = False
        
    def initialize_effect(self):
        self.effect = ClassicEffect(DEFAULT_ASCII_SET)
            
    def run(self):
        print("PixelTerminal - Classic Mode")
        print("Press Ctrl+C to exit")
        
        enable_ansi_colors()
        clear_screen()
        hide_cursor()
        
        cap = cv2.VideoCapture(self.camera_index)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)

        if not cap.isOpened():
            print("Error: Could not access camera.")
            self._cleanup()
            return
        
        self.initialize_effect()
        self.running = True
        
        try:
            while self.running:
                ret, frame = cap.read()
                if not ret:
                    break

                if self.custom_width and self.custom_height:
                    columns, lines = self.custom_width, self.custom_height
                else:
                    columns, lines = get_terminal_size()

                rendered = self.effect.render_frame(frame, columns, lines)
                
                move_cursor_home()
                sys.stdout.write(rendered)
                sys.stdout.flush()
                    
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cap.release()
            self._cleanup()
    def _cleanup(self):
        self.running = False
        show_cursor()
        clear_screen()
            
def list_cameras():
    print("Checking available cameras...")
    for i in range(5):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            print(f"Camera {i}: {width}x{height}")
            cap.release()
        else:
            print(f"Camera {i}: Not available")

def main():
    parser = argparse.ArgumentParser(
        description='PixelTerminal - High-performance ASCII camera feed',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py
  python main.py --camera 1
  python main.py --width 120 --height 30
        """
    )
    
    parser.add_argument(
        '--camera', '-c',
        type=int,
        default=0,
        help='Camera index (default: 0)'
    )
    
    parser.add_argument(
        '--width', '-w',
        type=int,
        help='Terminal width in characters (auto-detect if not specified)'
    )
    
    parser.add_argument(
        '--height',
        type=int,
        help='Terminal height in characters (auto-detect if not specified)'
    )
    
    parser.add_argument(
        '--list-cameras', '-l',
        action='store_true',
        help='List available cameras and exit'
    )
    
    args = parser.parse_args()
    
    if args.list_cameras:
        list_cameras()
        return
    
    app = PixelTerminal(
        camera_index=args.camera,
        width=args.width,
        height=args.height
    )
    
    try:
        app.run()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()