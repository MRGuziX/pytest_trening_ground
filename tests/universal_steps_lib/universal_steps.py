class UniversalSteps:
    def __init__(self, data_storage):
        self.data_storage = data_storage

    def change_b(self):

        if self.data_storage.variable_a == 2:
            print("\nVariable A from Object created at FeatureSteps\n")
            print(self.data_storage.variable_a)

        else:
            print("\nVariable A created from Universal Steps\n")
            print(self.data_storage.variable_a)
