# this file will convert 'scenes' into Three.js instructions
# this code will return Json file
# this Json file will further be read by three.js
import json

def generate_animation_data(scenes):

    animation_data = []

    for scene in scenes:

        if "object at rest" in scene.lower():
            animation_data.append({
                "type": "sphere",
                "action": "create",
                "position": [0,0,0]
            })

        if "apply a force" in scene.lower():
            animation_data.append({
                "type": "arrow",
                "action": "show_force",
                "direction": [1,0,0]
            })

        if "object starts moving" in scene.lower():
            animation_data.append({
                "type": "sphere",
                "action": "move",
                "to": [5,0,0]
            })

    return animation_data


if __name__ == "__main__":

    test_scenes = [
        "Show an object at rest",
        "Apply a force to the object",
        "Object starts moving"
    ]

    data = generate_animation_data(test_scenes)

    print(json.dumps(data, indent=4))