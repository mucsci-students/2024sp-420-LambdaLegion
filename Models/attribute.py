from Models.diagram import Diagram


class Attributes:
    def __init__(self):
        self.diagram = Diagram()

    def add_attribute(self, name, class_name):
        # Katie Dowlin: Check if the class you want to add the attribute to exists.
        if class_name in self.diagram.classes.keys():
            self.diagram.classes[class_name].append(name)
            print(f"{name} Added Successfully")
            # return name
        # Katie Dowlin: If the class you want to add the attribute to doesn't exist.
        else:
            raise valueError(f"Add Failed- {class_name} Doesn't Exist")

    def delete_attribute(self, name, class_name):
        # Katie Dowlin: Check if class exists.
        if class_name in self.diagram.classes.keys():
            # Katie Dowlin: Check if an attribute with that name exists in that class.
            if name in self.diagram.classes[class_name]:
                self.diagram.classes[class_name].remove(name)
                print(f"{name} Deleted Successfully")
            # Katie Dowlin: If there is no attribute with that name in that class.
            else:
                raise valueError(f"Delete Failed- {name} Doesn't Exist")
        # Katie Dowlin: If the class doesn't exist.
        else:
            raise valueError(f"Delete Failed- {class_name} Doesn't Exist")

    def rename_attribute(self, old_name, new_name, class_name):
        # Katie Dowlin: Check if class exists.
        if class_name in self.diagram.classes.keys():
            # Katie Dowlin: Check if old name is an attribute in that class.
            if old_name in self.diagram.classes[class_name]:
                self.diagram.classes[class_name].remove(old_name)
                self.diagram.classes[class_name].append(new_name)
                print(f"{old_name} Has Been Renamed To {new_name}")
                return new_name
            # Katie Dowlin: If the old name does not exist.
            else:
                raise valueError(f"Rename Failed- {old_name} Doesn't Exist")
        # Katie Dowlin: If the class doesn't exist.
        else:
            raise valueError(f"Rename Failed- {class_name} Doesn't Exist")
