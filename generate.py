from jinja2 import Environment, FileSystemLoader


def write_file(filename, rendered_template):
    f = open("site/public/" + filename, 'w')
    f.write(rendered_template + '\n')
    f.close()

env = Environment(loader=FileSystemLoader('templates/'))

#output_files = [t.replace('.templ', '.html') for t in env.list_templates()]

# for of, template in zip(output_files, env.list_templates()):
#     write_file(of, env.get_template(template).render())

for template in env.list_templates():
    write_file(template.replace('.templ', '.html'), env.get_template(template).render())

#[write_file(filename, env.get_template(template).render()) for filename, template in [output_files, env.list_templates()]]
