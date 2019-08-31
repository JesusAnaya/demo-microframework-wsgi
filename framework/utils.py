import importlib
import os


def import_object(full_path):
    module_path, object_name = full_path.rsplit('.', 1)
    module = importlib.import_module(module_path)
    return getattr(module, object_name)


def load_template(template_name, params={}):
    from framework.config import settings

    templates_dir = settings.TEMPLATES_DIR or './'
    template_path = os.path.join(templates_dir, template_name)
    template = ""

    with open(template_path, "r") as f:
        template = f.read()

    return template.format(**params)
