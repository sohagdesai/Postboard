from . import redis_client
import sys

def update_cache(db_row_dict):
    if not db_row_dict or type(db_row_dict) != dict :  # empty row or non-dict
        return
    row_key = str(db_row_dict["id"])
    print (f"caching row with ID: {row_key}...", file=sys.stderr)
    redis_client.hmset(row_key, db_row_dict)
    return

def get_cache(row_key):
    byte_dict = redis_client.hgetall(str(row_key))
    row_dict = {}
    for key, value in byte_dict.items():
        row_dict[key.decode("utf-8")] = value.decode("utf-8")
    return str(row_dict)
