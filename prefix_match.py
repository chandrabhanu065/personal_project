"""
If the expected prefixes are:
["10.0.0.0/16", "192.168.0.0/16", "172.16.0.0/16"]

And the retrieved routes are:
[    {"prefix": "10.0.0.0/16", "next_hop": "192.168.1.1"},    {"prefix": "192.168.0.0/16", "next_hop": "192.168.1.2"},    {"prefix": "203.0.113.0/24", "next_hop": "192.168.1.3"}]

The script should output:
Missing prefixes: ["172.16.0.0/16"]
Unexpected prefixes: ["203.0.113.0/24"]
"""

expected_prfix = ["10.0.0.0/16", "192.168.0.0/16", "172.16.0.0/16"]
retrieved_prefix = [{"prefix": "10.0.0.0/16", "next_hop": "192.168.1.1"},
                    {"prefix": "192.168.0.0/16", "next_hop": "192.168.1.2"},
                    {"prefix": "203.0.113.0/24", "next_hop": "192.168.1.3"}]
#retrieved_prefix_list = ["10.0.0.0/16", "192.168.0.0/16", "203.0.113.0/24"]


def prefix_parse(expected_prfix, retrieved_prefix):
    retrieved_prefix_list = parse_retrieved_prefix(retrieved_prefix)
    for x in expected_prfix:
        if x not in retrieved_prefix_list:
            print("Missing prefixes:{}".format(x))

    # retrieved_prefix_list = parse_retrieved_prefix(retrieved_prefix)
    for x in retrieved_prefix_list:
        if x not in expected_prfix:
            print("Unexpected prefixes:{}".format(x))


def parse_retrieved_prefix(retrieved_prefix):
    lst = []
    for x in retrieved_prefix:
        lst.append(x["prefix"])
    return lst

if __name__ == "__main__":
    prefix_parse(expected_prfix,retrieved_prefix)