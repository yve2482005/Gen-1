from diffusers import StableDiffusionPipeline
import torch

def generate_image(prompt: str, output_path: str = "output.png"):
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

    # Generate image
    image = pipe(prompt).images[0]

    # Save image
    image.save(output_path)
    return output_path