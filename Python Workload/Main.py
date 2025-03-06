import vertexai
from vertexai.preview.generative_models import GenerativeModel

def generate_text(prompt, project_id="your-project-id", location="us-central1", model_name="gemini-1.5-flash-002"):
    """Generates text using Google Cloud Vertex AI's Gemini model (Python equivalent of Java code)."""

    # Initialize Vertex AI with the project and location
    vertexai.init(project=project_id, location=location)

    # Load the Gemini model
    model = GenerativeModel(model_name)

    # Generate response
    response = model.generate_content(prompt)

    return response.text  # Extract generated text

# Example Usage
if __name__ == "__main__":
    import os
    project_id = "jlp-engineering-ai-experiments"  # Ensure you have PROJECT_ID in your environment variables
    location = "us-central1"  # Default to us-central1 if not set

    prompt = "What is performance testing?"
    generated_text = generate_text(prompt, project_id=project_id, location=location)
    print(generated_text)