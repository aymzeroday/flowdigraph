import sys
from parser.servicenow_parser import parse_servicenow
from render.mermaid_builder import build_mermaid
from parser.bmc_parser import parse_bmc

def main(input_path, output_path):
    if "bmc" in input_path.lower():
        data = parse_bmc(input_path)
    else:
        data = parse_servicenow(input_path)
    mermaid_text = build_mermaid(data)

    with open(output_path, 'w') as f:
        f.write("<!-- ```mermaid\n")
        f.write(mermaid_text)
        f.write("\n``` -->")

    print(f"[✓] Mermaid diagram written to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_json> <output_md>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
