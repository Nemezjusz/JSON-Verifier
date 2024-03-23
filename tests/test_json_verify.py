import pytest
from source import json_verify


def test_verify_policy_json():
    policy_dict = {
        "PolicyName": "root",
        "PolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "IamListAccess",
                    "Effect": "Allow",
                    "Action": [
                        "iam:ListRoles",
                        "iam:ListUsers"
                    ],
                    "Resource": "*"
                }
            ]
        }
    }
    assert json_verify.verify_policy_json(policy_dict) == False

    policy_dict = {
        "PolicyName": "root",
        "PolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "IamListAccess",
                    "Effect": "Allow",
                    "Action": [
                        "iam:ListRoles",
                        "iam:ListUsers"
                    ],
                    "Resource": ["*"]
                }
            ]
        }
    }
    assert json_verify.verify_policy_json(policy_dict) == False

    policy_dict = {
        "PolicyName": "root",
        "PolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "IamListAccess",
                    "Effect": "Allow",
                    "Action": [
                        "iam:ListRoles",
                        "iam:ListUsers"
                    ],
                    "Resource": ["arn:aws:s3:::my_corporate_bucket/*"]
                }
            ]
        }
    }
    assert json_verify.verify_policy_json(policy_dict) == True

    policy_dict = {
        "PolicyName": "root",
        "PolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "IamListAccess",
                    "Effect": "Allow",
                    "Action": [
                        "iam:ListRoles",
                        "iam:ListUsers"
                    ],
                    "Resource": ["arn:aws:s3:::my_corporate_bucket/*", "*"]
                }
            ]
        }
    }
    assert json_verify.verify_policy_json(policy_dict) == False

    policy_dict = {
        "PolicyName": "root"
    }
    assert json_verify.verify_policy_json(policy_dict) == True

    policy_dict = {
        "PolicyName": "root",
        "PolicyDocument": {
            "Version": "2012-10-17",
            "Statement": {
                "Sid": "IamListAccess",
                "Effect": "Allow",
                "Action": [
                    "iam:ListRoles",
                    "iam:ListUsers"
                ],
                "Resource": "arn:aws:iam::123456789012:role/MyRole"
            }
        }
    }

    assert json_verify.verify_policy_json(policy_dict) == True


def test_read_json_file():
    policy_dict = json_verify.read_json_file("example.json")
    assert policy_dict == {
        "PolicyName": "root",
        "PolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "IamListAccess",
                    "Effect": "Allow",
                    "Action": [
                        "iam:ListRoles",
                        "iam:ListUsers"
                    ],
                    "Resource": "*"
                }
            ]
        }
    }
    assert policy_dict["PolicyName"] == "root"
    assert policy_dict["PolicyDocument"]["Version"] == "2012-10-17"
    assert policy_dict["PolicyDocument"]["Statement"][0]["Sid"] == "IamListAccess"
    assert policy_dict["PolicyDocument"]["Statement"][0]["Effect"] == "Allow"
    assert policy_dict["PolicyDocument"]["Statement"][0]["Action"] == ["iam:ListRoles", "iam:ListUsers"]
    assert policy_dict["PolicyDocument"]["Statement"][0]["Resource"] == "*"


