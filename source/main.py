import json_verify, sys, os


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <json_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    # chceck is file path and file is correct
    if not os.path.exists(file_path):
        print("File path does not exist")
        sys.exit(1)

    if not file_path.endswith('.json'):
        print("File path must be a .json file")
        sys.exit(1)

    policy_dict = json_verify.read_json_file(file_path)
    is_valid = json_verify.verify_policy_json(policy_dict)
    print(is_valid)
    sys.exit(1)


if __name__ == "__main__":
    main()