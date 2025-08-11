from jinja2 import Environment, FileSystemLoader
import os

prompt_dir = os.path.join(os.path.dirname(__file__), "..", "prompts")
env = Environment(loader=FileSystemLoader(prompt_dir))

def render_prompt(template_name: str, context: dict) -> str:
    """
    Renders a prompt template with context using Jinja2.
    """
    template = env.get_template(template_name)
    return template.render(context)