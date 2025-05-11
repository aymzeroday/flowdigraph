def build_mermaid(data):
    lines = ["graph TD"]
    class_lines = []
    click_lines = []

    for edge in data["edges"]:
        lines.append(f'"{edge[0]}" --> "{edge[1]}"')

    for node in data["nodes"]:
        label = node.lower()
        node_id = node.replace(" ", "_")

        if "start" in label:
            class_lines.append(f'class "{node}" start;')
        elif "end" in label:
            class_lines.append(f'class "{node}" end;')
        elif "approval" in label:
            class_lines.append(f'class "{node}" approval;')
        elif "task" in label:
            class_lines.append(f'class "{node}" task;')

        # Add click interaction
        click_lines.append(f'click "{node}" call showNodeInfo("{node_id}")')

    lines.extend(class_lines)
    lines.extend(click_lines)

    # Mermaid class styles
    lines.append("classDef start fill:#d4f4dd,stroke:#2d7c3f,stroke-width:2px;")
    lines.append("classDef end fill:#ffe3e3,stroke:#a82828,stroke-width:2px;")
    lines.append("classDef task fill:#e0f0ff,stroke:#2573a7;")
    lines.append("classDef approval fill:#fdf4dc,stroke:#c19b00;")

    return "\n".join(lines)
