import importlib


def import_object(full_path):
    module_path, object_name = full_path.rsplit('.', 1)
    module = importlib.import_module(module_path)
    return getattr(module, object_name)
