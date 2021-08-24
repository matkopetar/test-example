"""
Shortcoming of these functions are that they doesn't validate if the format of (passed) data is correct.
It doesn't inform you what should like the format be if it isn't correct.
"""

from .fixtures import user_applications_list, applications_with_features_list, users_list


def extract_user(user_id, users):
    user_dict = {}
    for user in users:
        if user.get('user_id') == user_id:
            user_dict = user
            break
    return user_dict


def extract_features_available(app_id, applications_with_features):
    features_available = []
    for app_with_features in applications_with_features:
        if app_with_features.get('app_id') == app_id:
            features_available = app_with_features.get('features_available')
            break
    return features_available


def calculate_permissions_for_user(user_id, user_applications, applications_with_features, users):
    result = {
        'user_id': user_id,
        'application_permissions': []
    }

    user = extract_user(user_id, users)
    features_allowed = user.get('features_allowed', [])

    for app in user_applications:
        features_available = extract_features_available(app.get('app_id'), applications_with_features)
        features = [feature for feature in features_allowed if feature in features_available]

        result['application_permissions'].append({
            'app_id': app.get('app_id'),
            'features_allowed': features
        })

    return result


print(calculate_permissions_for_user(1, user_applications_list, applications_with_features_list, users_list))
