import json

def parse_bmc(path):
    with open(path, 'r') as f:
        raw = json.load(f)

    nodes = []
    edges = []

    # Assuming BMC structure has entries like this:
    # {
    #   "workflow_steps": [
    #     {
    #       "id": "AP1",
    #       "label": "Approval: Manager",
    #       "next": ["TSK1", "TSK2"]
    #     },
    #     {
    #       "id": "TSK1",
    #       "label": "Task: Provision Account",
    #       "next": ["END"]
    #     }
    #   ]
    # }

    step_map = {step["id"]: step["label"] for step in raw.get("workflow_steps", [])}

    for step in raw.get("workflow_steps", []):
        nodes.append(step["label"])
        for next_id in step.get("next", []):
            target_label = step_map.get(next_id, next_id)
            edges.append((step["label"], target_label))

    return {"nodes": nodes, "edges": edges}
