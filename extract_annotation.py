import fitz
import argparse

def extract_highlighted_text(pdf_path):
    doc = fitz.open(pdf_path)
    highlights = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        for annot in page.annots():
            if annot.type[0] == 8:
                quad_points = annot.vertices
                highlight_text = ""
                for i in range(0, len(quad_points), 4):
                    rect = fitz.Quad(quad_points[i:i+4]).rect
                    highlight_text += page.get_text("text", clip=rect).strip() + " "
                
                highlight_text = highlight_text.strip()
                content = annot.info.get("content", "No annotation content provided")
                highlights.append({
                    "highlight": highlight_text,
                    "page": page_num + 1,
                    "annotation": content
                })
    
    return highlights

def format_highlights(highlights):
    formatted = []
    for item in highlights:
        formatted.append(f'"{item["highlight"]}" (page {item["page"]}) {item["annotation"]}')
    return "\n".join(formatted)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract highlighted or underlined text from a PDF file.")
    parser.add_argument("pdf_path", help="Path to the input PDF file.")
    args = parser.parse_args()
    
    highlights = extract_highlighted_text(args.pdf_path)
    
    if highlights:
        print("Highlights and annotations found:")
        print(format_highlights(highlights))
    else:
        print("No highlights or underlines found in the provided PDF.")
