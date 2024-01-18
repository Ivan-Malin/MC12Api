import re

class TemplateObject:
    def __init__(self, name, attributes, code):
        self._name = name
        self._code = code
        self._attributes = attributes
    
    def get_creator(self):
        def create_template_object(**attributes):
            for key in self._attributes:
                if key not in attributes:
                    attributes[key] = self._attributes[key]
            return TemplateObject(self._name,attributes,self._code)
        return create_template_object

    def fill_template(self):
        filled_code = self._code
        for attr_name, attr_value in self._attributes.items():
            filled_code = filled_code.replace("$(%s)" % attr_name, str(attr_value))
        return filled_code

    def __getattr__(self, attr):
        if attr in self._attributes:
            return self._attributes[attr]
        else:
            raise AttributeError(f"'TemplateObject' object has no attribute '{attr}'")

    def __setattr__(self, key, value):
        if key.startswith('_'):
            super(TemplateObject, self).__setattr__(key, value)
        else:
            self._attributes[key] = value    
    

class TemplatesObject:
    def __init__(self, templates: [TemplateObject,]):
        self._dict = {t._name: t.get_creator() for t in templates}
    def __getattr__(self, attr):
        if attr in self._dict:
            return self._dict[attr]
        else:
            raise AttributeError(f"'Template' object has no attribute '{attr}'")

def parse_templates(file_path):
    templates = []
    with open(file_path, 'r') as file:
        content = file.read()
        template_pattern = r'\${([^}]+)}\n\$([\s\S]*?)\n\]\$'
        matches = re.finditer(template_pattern, content)
        for match in matches:
            name_and_attrs = match.group(1).split('(')
            name = name_and_attrs[0]
            attrs = name_and_attrs[1][:-1].split(',')
            attributes = {}
            for attr in attrs:
                attributes[attr] = None
            code = match.group(2).strip()[2:]
            templates.append(TemplateObject(name, attributes, code))
    return TemplatesObject(templates)


if __name__=='__main__':
    # Example usage
    T = parse_templates("api\Or2.txt")
    or3 = T.Or3(y=5)
    print(or3._name)  # Or2
    print(or3.x)  # None
    or3.x = 1
    print(or3.fill_template())
