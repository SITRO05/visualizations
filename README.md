# Mathematical Visualizations with Manim

This project focuses on creating mathematical visualizations inspired by 3blue1brown's style using the Manim library.

## Project Structure

```
visualizations/
├── examples/           # Example visualizations
│   ├── basic_shapes.py # Basic shape animations
│   └── math_visualization.py # Mathematical concept visualizations
├── tutorials/          # Step-by-step tutorials
├── assets/             # Images, sounds, and other media
└── README.md           # This file
```

## Getting Started

### Prerequisites

- Python 3.7+
- FFmpeg (for video rendering)
- LaTeX (optional, for high-quality math typesetting)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/SITRO05/visualizations.git
   cd visualizations
   ```

2. Install Manim Community Edition:
   ```bash
   pip install manim
   ```

3. Install FFmpeg (if not already installed):
   - Ubuntu/Debian: `sudo apt-get install ffmpeg`
   - macOS: `brew install ffmpeg`
   - Windows: Download from https://ffmpeg.org/download.html

### Running Examples

To render the basic shapes example:
```bash
manim -p -ql examples/basic_shapes.py BasicShapes
```

To render the Pythagorean theorem visualization:
```bash
manim -p -ql examples/math_visualization.py PythagoreanTheorem
```

To render the function plot:
```bash
manim -p -ql examples/math_visualization.py FunctionPlot
```

### Flags Explained
- `-p`: Preview the video after rendering
- `-ql`: Low quality (faster rendering, good for testing)
- `-qm`: Medium quality
- `-qh`: High quality
- `-qk`: 4K quality (matches 3blue1brown's style)

## Learning Resources

- [Manim Community Documentation](https://docs.manim.community)
- [3blue1brown's Manim Repository](https://github.com/3b1b/manim)
- [3blue1brown's Video Code](https://github.com/3b1b/videos)
- [Try Manim Online](https://try.manim.community)

## Project Goals

- Learn and implement mathematical visualizations in the style of 3blue1brown
- Explore Manim's capabilities for educational content
- Create a library of reusable visualization components
- Develop clear, intuitive explanations of mathematical concepts through animation

## Contributing

Feel free to fork this repository and submit pull requests with your own visualizations!

## License

This project is open source and available under the MIT License.