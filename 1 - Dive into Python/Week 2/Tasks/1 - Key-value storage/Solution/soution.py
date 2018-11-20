import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()

database = {}

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if not os.path.isfile(storage_path):
    with open(storage_path, 'w') as f:
        json.dump(database, f)

with open(storage_path, 'r+') as f:
    database = json.load(f)

if not args.val:
    if args.key in database:
        print(", ".join(database[args.key]))
    else:
        print("")
else:
    if args.key in database:
        database[args.key].append(args.val)
    else:
        database[args.key] = [args.val]

with open(storage_path, 'w') as f:
    json.dump(database, f)
