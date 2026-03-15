from model.concept_extractor import extract_concepts
from model.scene_generator import generate_scene


def run_pipeline(text):

    # Step 1: extract concepts
    concepts = extract_concepts(text)
    print("Concepts:", concepts)

    # Step 2: generate scenes
    scenes = generate_scene(concepts)

    print("\nGenerated Scenes:")
    for i, scene in enumerate(scenes, 1):
        print(f"Scene {i}: {scene}")


if __name__ == "__main__":

    topic = input("Enter topic: ")

    run_pipeline(topic)