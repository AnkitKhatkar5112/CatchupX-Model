'''

Sentence
↓
Concept Extractor
↓
Scene Generator
↓
Animation Engine


input:- 
    ['newton','law','motion']
Output:-
    Scene 1:
    Object at rest

    Scene 2:
    Force applied

    Scene 3:
    Object starts moving

'''

def generate_scene(concepts):#the input 'concept' should be the output of 'concept_extractor.py' 

    scenes = []

    if "motion" in concepts:
        scenes.append("Show an object at rest")
        scenes.append("Apply a force to the object")
        scenes.append("Object starts moving")

    if "triangle" in concepts:
        scenes.append("Draw a triangle")
        scenes.append("Label sides a, b, c")

    if "gravity" in concepts:
        scenes.append("Show an apple falling from a tree")

    return scenes


if __name__ == "__main__":

    test_concepts = ["newton","law","motion"]

    result = generate_scene(test_concepts)

    print("Scenes:")
    for scene in result:
        print("-",scene)

