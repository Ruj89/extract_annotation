# PDF Annotation Extractor

A Python script to extract highlighted or underlined text along with annotations from a PDF file.

## Requirements

- Python 3.7+
- Libraries listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with the path to the PDF file:
```bash
python extract_highlighted_text.py path/to/input.pdf
```

## Output

The script outputs a list of highlighted or underlined texts along with annotations, in the format:
```
"Highlighted text" (page X) Annotation content
```