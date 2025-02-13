from jinja2 import Environment, FileSystemLoader

def template_datasource(data, template_dir="templates", template_name="datasource.j2"):
    """
    Renders a template with the given data using Jinja2.

    This function loads a Jinja2 template from the specified directory
    and file name, then renders it with the provided data.

    :param data: The data to be used for rendering the template.
    :type data: dict
    :param template_dir: The directory where the template files are located. Default is "templates".
    :type template_dir: str, optional
    :param template_name: The name of the template file to be used. Default is "datasource.j2".
    :type template_name: str, optional
    :return: The rendered template as a string.
    :rtype: str
    """

    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    return template.render(data=data)
