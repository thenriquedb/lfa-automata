def map_states(state: dict):
    return {
        "initial": True if "initial" in state else False,
        "final": True if "final" in state else False,
        "name": state.get("@name"),
        # "id": state.get("@id"),
        # "x": state.get("x"),
        # "y": state.get("y"),
    }


def map_transitions(state: dict):
    return {
        "from": state.get("from"),
        "to": state.get("to"),
        "read": state.get("read"),
        # "id": state.get("@id"),
        # "x": state.get("x"),
        # "y": state.get("y"),
    }
