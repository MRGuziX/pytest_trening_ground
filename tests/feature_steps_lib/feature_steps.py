class FeatureSteps:
    def __init__(self, data_storage):
        self.data_storage = data_storage

    def change_a(self):
        print("\n Variable A from Datastorage")
        print(self.data_storage.variable_a)
        self.data_storage.variable_a = 2
