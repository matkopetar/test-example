import unittest
from application_permissions.fixtures import (user_applications_list,
                                              applications_with_features_list,
                                              users_list,
                                              user_fixture,
                                              features_available_fixture)
from application_permissions.calculate_permissions import (extract_user,
                                                           extract_features_available,
                                                           calculate_permissions_for_user)


class TestExtractUser(unittest.TestCase):

    def test_extract_user_when_exists(self):
        extracted_user = extract_user(1, users_list)
        self.assertEqual(user_fixture, extracted_user)

    def test_extract_user_when_doesnt_exist(self):
        extracted_user = extract_user(4, users_list)
        self.assertEqual({}, extracted_user)


class TestExtractFeaturesAvailable(unittest.TestCase):

    def test_extract_features_available_when_exists(self):
        extracted_features_available = extract_features_available(1, applications_with_features_list)
        self.assertEqual(features_available_fixture, extracted_features_available)

    def test_extract_user_when_doesnt_exist(self):
        extracted_features_available = extract_features_available(4, applications_with_features_list)
        self.assertEqual([], extracted_features_available)


class TestCalculatePermissionsForUser(unittest.TestCase):

    def test_calculate_permissions_for_user_when_apps_not_in_users_app(self):
        expected_result = {
            'user_id': 1,
            'application_permissions': []
        }

        calculated_permissions = calculate_permissions_for_user(
            user_id=1,
            user_applications=[],
            applications_with_features=applications_with_features_list,
            users=users_list)
        self.assertEqual(expected_result, calculated_permissions)

    def test_calculate_permissions_for_user_when_apps_in_users_app(self):
        expected_result = {
            'user_id': 1,
            'application_permissions': [
                {'app_id': 1, 'features_allowed': [1, 2]},
                {'app_id': 2, 'features_allowed': [5]},
                {'app_id': 3, 'features_allowed': []},
                {'app_id': 126, 'features_allowed': []},
            ]
        }

        calculated_permissions = calculate_permissions_for_user(
            user_id=1,
            user_applications=user_applications_list,
            applications_with_features=applications_with_features_list,
            users=users_list)
        self.assertEqual(expected_result, calculated_permissions)


if __name__ == '__main__':
    unittest.main()
