import rsa
import hashlib
import requests

public_key_A, private_key_A = rsa.newkeys(512)
public_key_B, private_key_B = rsa.newkeys(512)

def node_A_request():
    contract_server(public_key_A)

def contract_server(public_key_A):
    node_B_response(public_key_A)

def node_B_response(public_key_A):
    private_data_B = "I hope i did the assignment right"
    encrypted_data = rsa.encrypt(private_data_B.encode(), public_key_A)
    contract_server_response(encrypted_data)

def contract_server_response(encrypted_data):
    node_A_obtain_data(encrypted_data)

def node_A_obtain_data(encrypted_data):
    decrypted_data = rsa.decrypt(encrypted_data, private_key_A)
    print("Decrypted data: ", decrypted_data.decode())

node_A_request()
