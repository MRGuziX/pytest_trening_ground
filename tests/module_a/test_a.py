def test_a(universal_step, feature_step, data_storage):
    print("\n Variable A from Datastorage")
    print(data_storage.variable_a)
    assert data_storage.variable_a == 1

    feature_step.change_a()

    universal_step.change_b()


def test_b(self, universal_step, feature_step, data_storage):
    print("\n Variable A from Datastorage SCOPE FUNCTION")
    print(data_storage.variable_a)
