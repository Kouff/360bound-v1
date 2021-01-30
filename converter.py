class ConverterData:
    def __init__(self, data: list):
        self.data = [dict(**element, children=[]) for element in data]  # add a "children" field to each element
        self.elements1 = []
        self.elements2 = []
        self.elements3 = []

    @property
    def converted_data(self) -> list:
        new_data = []
        for element in self.data:
            # split elements by depth levels
            # 1 -> 1 level
            # 1.1 -> 2 level
            # 1.1.1 -> 3 level
            level_of_name: int = len(element['code'].split('.'))
            if not 0 < level_of_name < 4:  # doesn`t add elements with depth level below 0 or above 4
                continue
            getattr(self, f'elements{level_of_name}').append(element)

        for element1 in self.elements1.copy():
            for element2 in self.elements2.copy():
                for element3 in self.elements3.copy():
                    if element3['code'].startswith(f"{element2['code']}."):
                        # add element to children if the code name of element startswith code name of element
                        # whose depth level is 1 lower
                        element2['children'].append(element3)
                        self.elements3.remove(element3)  # remove the element from a old list
                if element2['code'].startswith(f"{element1['code']}."):
                    # add element to children if the code name of element startswith code name of element
                    # whose depth level is 1 lower
                    element1['children'].append(element2)
                    self.elements2.remove(element2)  # remove the element from a old list
            new_data.append(element1)  # add a parent element to the "new_data" list

        for element in self.elements2 + self.elements3:
            # add elements with depth levels 2 and 3 that did not pass to the "children" field
            new_data.append(element)

        return new_data
