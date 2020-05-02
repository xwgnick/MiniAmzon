import concurrent.futures
import psycopg2
import socket
import world_amazon_pb2
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _EncodeVarint

# test_set = set()
# test_int = 0

# def add_to_set(test_list):
#     for element in test_list:
#         test_set.add(element)
#     print(test_set)

# def add_to_int(coming):
#     test_int += coming
#     print(test_int)

# add_to_int(1)
# print(test_int)

# Send