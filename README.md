
# Quadratic Equation Resolution with Manim

This repository contains a Manim script that visually demonstrates the step-by-step resolution of the quadratic equation:

`3x^2 - 108 = 0`

## Video Preview

![Equation Resolution Preview](preview.png)

## Project Contents

- `equation_resolution.py`: The Manim script that generates the animation.
- `AcousticGuitar1.mp3`: The background music used in the video.
- `README.md`: This file containing instructions and information about the project.

## Getting Started

Follow these instructions to run the code on your computer and produce the same video.

### Prerequisites

- **Python** 3.7 or higher
- **Manim Community Edition**
- **LaTeX** with necessary packages (`sfmath`, `amsmath`, etc.)
- **FFmpeg** (for audio and video processing)

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/Stabadev/manim.git
```

#### 2. Navigate to the Project Directory

```bash
cd manim
```

#### 3. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

#### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 5. Install LaTeX

- **Ubuntu/Debian**:

  ```bash
  sudo apt-get install texlive-full
  ```

- **macOS**:

  - Install MacTeX from [tug.org/mactex](https://tug.org/mactex/)

- **Windows**:

  - Install MiKTeX from [miktex.org](https://miktex.org/)

Ensure that LaTeX packages `sfmath` and `amsmath` are installed.

#### 6. Verify FFmpeg Installation

Manim uses FFmpeg for audio and video rendering. To verify that FFmpeg is installed:

```bash
ffmpeg -version
```

If FFmpeg is not installed, follow the instructions on [ffmpeg.org](https://ffmpeg.org/download.html).

## Running the Script

Execute the following command to render the video:

```bash
manim -pqh equation_resolution.py EquationResolutionScene
```

- **Options**:

  - `-p`: Preview the video after rendering.
  - `-q h`: Render in high quality. Other options include `l` (low quality), `k` (4K quality), and `p` (production quality).

## Post-processing with FFmpeg

### Trimming the Video and Adding an Audio Fade-Out

To trim the video to 1 minute and 30 seconds and add a 5-second audio fade-out at the end, use the following `ffmpeg` command:

```bash
ffmpeg -i EquationResolutionScene.mp4 -t 00:01:30 -af "afade=t=out:st=85:d=5" -c:v copy trimmed_faded_EqScene.mp4
```

- `-i EquationResolutionScene.mp4`: The input video file.
- `-t 00:01:30`: Sets the duration of the output video to 1 minute and 30 seconds.
- `-af "afade=t=out:st=85:d=5"`: Adds a fade-out effect to the audio starting at 1 minute 25 seconds (`st=85`) and lasting 5 seconds (`d=5`).
- `-c:v copy`: Copies the video stream without re-encoding to preserve quality.
- `trimmed_faded_EqScene.mp4`: The output file.

### Taking a Screenshot from the Video

To take a screenshot of the video at 9 seconds and save it as `preview.png`, use the following `ffmpeg` command:

```bash
ffmpeg -ss 00:00:09 -i EquationResolutionScene.mp4 -vframes 1 -q:v 2 preview.png
```

- `-ss 00:00:09`: Seeks to 9 seconds in the video.
- `-i EquationResolutionScene.mp4`: The input video file.
- `-vframes 1`: Captures a single frame.
- `-q:v 2`: Sets the quality of the output PNG (lower is better; 2 is a high-quality setting).
- `preview.png`: The name of the output image file.

## Background Music

### Music Information

- **Title**: AcousticGuitar1
- **Artist**: Jason Shaw
- **License**: Creative Commons Attribution 4.0 International License
- **Source**: [Audionautix.com](https://audionautix.com/)

### License Details

All music produced by Jason Shaw on AudionautiX is released under the **Creative Commons Attribution 4.0 International License**.

In simple terms, this means:

- **You are free to**:

  - **Share** — copy and redistribute the material in any medium or format.
  - **Adapt** — remix, transform, and build upon the material for any purpose, even commercially.

- **Under the following terms**:

  - **Attribution**:

    - You must give appropriate credit, provide a link to the license, and indicate if changes were made.
    - You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
    - You are free to use the music (even for commercial purposes) as long as you provide a link to this website or credit with: "Music by Audionautix.com".

**Read the full license here**: [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/)

### How to Provide Attribution

In any usage of the music, please include the following attribution:

```
Music by Audionautix.com
```

or

```
Creative Commons Music by Jason Shaw on Audionautix.com
```

## Customization

Feel free to modify the script to suit your preferences. You can adjust:

- Text content and language.
- Font sizes and styles.
- Colors and themes.
- Animation timing and transitions.
- Steps of the equation resolution.

## Font and Readability Enhancements

The script uses a bold, sans-serif font (**DejaVu Sans**) to improve readability on small smartphone screens.

### Custom Font Usage

- **Font**: DejaVu Sans (sans-serif)
- **Weight**: Bold

These settings ensure that the text and equations are clear and easy to read, even on smaller devices.

### Note on Mathematical Fonts

To render equations in sans-serif font, the script uses a custom `TexTemplate` with the LaTeX package `sfmath`. Ensure that this package is installed with your LaTeX distribution.

## Troubleshooting

### Issues with LaTeX or Fonts

- Ensure that LaTeX is correctly installed and that the necessary packages are available.
- If you encounter errors related to fonts, verify that the `DejaVu Sans` font is installed on your system.

### Issues with Audio

- Verify that FFmpeg is installed and accessible from your terminal.
- Ensure that the file `AcousticGuitar1.mp3` is in the same directory as the Python script.

### Issues with Video Rendering

- Update Manim to the latest version:

  ```bash
  pip install --upgrade manim
  ```

- Consult the [Manim Documentation](https://docs.manim.community/) for detailed instructions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Manim Community**: The animation engine used to create this video.
- **Jason Shaw**: For the background music provided under Creative Commons License.
- [alexandre.rogues.fr](https://alexandre.rogues.fr/cv) : Creator of the script and video.

---

If you have any questions or suggestions, feel free to open an issue or contact me.

