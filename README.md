# PixelTerminal

A *high-performance*, ASCII camera feed system with **24-bit TrueColor** rendering.

## Features

- **Classic ASCII Rendering**: High-fidelity color ASCII with 70+ character density
- **24-bit TrueColor**: Full RGB color support using ANSI escape sequences
- **Auto-scaling**: Adapts to any terminal size automatically
- **Cross-platform**: Works on *Windows*, *Linux*, and *macOS*
- **Modular Design**: Clean, organized code structure

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python main.py
   ```

## Usage

### Basic Usage
```bash
# Classic high-fidelity ASCII
python main.py
```

## Terminal Setup for Best Results

### Font Size
Set your terminal font size to **2pt** or the *smallest possible size*. This allows more characters to fit on screen and creates a higher resolution ASCII image.

## Technical Details

### ASCII Character Density
Uses a *70+ character ramp* for realistic shading:
```
$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`. `
```

### Color Implementation
Uses **24-bit TrueColor** ANSI escape sequences:
```bash
\033[38;2;R;G;Bm
```
Where *R*, *G*, *B* are values from *0-255*.

## Classic Mode

Standard *high-fidelity ASCII* with full 24-bit color reproduction. Maintains original camera colors with realistic character density.

## Configuration

Edit `config.py` to customize:
- ASCII character sets
- Camera resolution settings
- Performance settings (FPS)

## Requirements

- **Python 3.7+**
- *OpenCV* (`opencv-python`)
- *NumPy*
- *Colorama*
- A webcam
- Terminal with **24-bit color support**

## License

Open source. Feel free to modify.
