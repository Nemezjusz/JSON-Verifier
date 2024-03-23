import json


def verify_policy_json(json_data):
    """
    verifies the input JSON data
    args json_data (str or dict)
    returns bool True if is valid, False otherwise.
    """

    # parse the input
    if isinstance(json_data, str):
        policy = json.loads(json_data)
    else:
        policy = json_data

    # check if the PolicyDocument exists
    if "PolicyDocument" not in policy:
        return True

    policy_document = policy["PolicyDocument"]

    # check if the Statement is a list
    if not isinstance(policy_document.get("Statement"), list):
        return True

    for statement in policy_document["Statement"]:
        resource = statement.get("Resource")

        # resource is a string
        if isinstance(resource, str):
            if resource == "*":
                return False

        # resource is a list
        elif isinstance(resource, list):
            for res in resource:
                if res == "*":
                    return False

    return True


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

