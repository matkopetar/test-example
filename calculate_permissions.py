user_applications_list = [{"app_id": 1}, {"app_id": 2}, {"app_id": 3}, {"app_id": 126}, ]
applications_with_features_list = [
    {"app_id": 1, "features_available": [1, 2, 3]},
    {"app_id": 2, "features_available": [3, 4, 5, 7]},
    {"app_id": 3, "features_available": [3, 12]},
]
users_list = [
    {"user_id": 1, "features_allowed": [1, 2, 5]},
    {"user_id": 2, "features_allowed": [1, 2, 3, 4]},
    {"user_id": 3, "features_allowed": []},
]


def extract_user(user_id, users):
    user_dict = None
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
