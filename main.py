import sys
import subprocess
from parser.servicenow_parser import parse_servicenow
from parser.bmc_parser import parse_bmc
from render.mermaid_builder import build_mermaid

def main(input_path, output_path):
    # Detect parser based on filename
    data = parse_servicenow(input_path) if "bmc" not in input_path.lower() else parse_bmc(input_path)
    mermaid_text = build_mermaid(data)

    # Write Markdown file (commented for docs)
    with open(output_path, 'w') as f:
        f.write("<!-- ```mermaid\n")
        f.write(mermaid_text)
        f.write("\n``` -->")

    # Write raw Mermaid (.mmd)
    mmd_path = output_path.replace(".md", ".mmd")
    with open(mmd_path, 'w') as f:
        f.write(mermaid_text)

    print(f"[✓] Mermaid diagram written to {output_path} and {mmd_path}")

    # Optional: Export PNG and SVG via mermaid-cli
    try:
        svg_path = output_path.replace(".md", ".svg")
        png_path = output_path.replace(".md", ".png")

        subprocess.run(["mmdc", "-i", mmd_path, "-o", svg_path], check=True)
        subprocess.run(["mmdc", "-i", mmd_path, "-o", png_path], check=True)

        print(f"[✓] SVG diagram: {svg_path}")
        print(f"[✓] PNG diagram: {png_path}")
    except FileNotFoundError:
        print("⚠️ Mermaid CLI (mmdc) not found. Install it using: npm install -g @mermaid-js/mermaid-cli")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to generate diagrams via mmdc: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_json> <output_md>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
