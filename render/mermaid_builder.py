def build_mermaid(data):
    lines = ["graph TD"]
    for edge in data["edges"]:
        lines.append(f"  {edge[0]} --> {edge[1]}")
    return "\n".join(lines)
