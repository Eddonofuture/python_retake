class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name
    
    def _set_name(self, name):
        if not name:
            raise Exception("invalid name")
        self._name = name

    def _get_name(self):
        return self._name
    
    name = property(_get_name, _set_name)

c = Color("#2335", "red")
print(c.name)
c.name = "blue"
print(c.name)
c.name= ''