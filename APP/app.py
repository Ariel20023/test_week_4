from fastapi import FastAPI, HTTPException
import uvicorn
from data import *
from APP.schemes import *
from encryption_decoding.Caesar import *
from encryption_decoding.Fence import *
app = FastAPI()


@app.get("/")
def get_test ():
    return {"msg": "hi from test"}


@app.get("/test/:name")
def get_test_name (name:str):
    with open("data/name.txt", "a") as f:
        f.write(name)
    return {name}


@app.post("/caesar")
def caesar_cipher_endpoint(body: Caesar):
    if body.mode ==  "encrypt":
        encryption =  caesar_encryption(body.text,body.offset)
        return { "encrypted_text":encryption }
    else:
        decoding = caesar_decoding(body.text,body.offset)
        return { "decrypted_text": decoding }



@app.get("/fence/encrypt")
def fence_cipher_endpoints(text: str):
    encryption = fence_encryption(text)
    return { "encrypted_text": encryption}



@app.post("/fence/decrypt")
def cipher_fence_decryption(body: Fence):
    encryption = fence_decoding(body.text)
    return { "decrypted":encryption}































