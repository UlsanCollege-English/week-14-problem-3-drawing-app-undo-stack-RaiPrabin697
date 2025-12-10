def simulate_history(actions):
    # Do not mutate the input list
    history = []

    for action in actions:
        if action == "UNDO":
            if history:
                history.pop()
        else:
            # any non-UNDO action is added to history
            history.append(action)

    return history