import json

def parse_servicenow(path):
    with open(path, 'r') as f:
        raw = json.load(f)

    nodes = []
    edges = []

    for step in raw.get("workflow_steps", []):
        nodes.append(step["name"])
        for next_step in step.get("transitions", []):
            edges.append((step["name"], next_step["to"]))

    return {"nodes": nodes, "edges": edges}
