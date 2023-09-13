from fastapi import FastAPI, Query, Form, File, UploadFile, HTTPException
from typing import Union
from models.models import Choice_Name, schema1

app = FastAPI()


@app.get("/")
def root():
    return {"message": "is display"}


@app.get("/items/{item}")
async def read_item(item):
    var_name = {"path_parameter": item}
    return (var_name)


# query parameter with the union validation
@app.get("/query")
async def read_item(name: Union[str, None] = None,
                    roll_no: Union[int, None] = Query(default=None, min_length=4, max_length=3)):
    var_name = {"name": name, "roll_no": roll_no}
    return (var_name)


# request body with enum class
@app.get("/models/{model_name}")
async def get_model(model_name: Choice_Name):
    return (model_name)


@app.get("/models/{model_name}")
async def get_model(model_name: Choice_Name):
    if model_name.value == "one":
        return {"model_name": model_name, "message": "you choose one"}

    if model_name.value == "two":
        return {"model_name": model_name, "message": "you choose two"}

    return {"model_name": model_name, "message": "Have some residuals"}


# request body with basedmodel its used for post request
@app.post("/items/")
async def create_item(item: schema1):
    return item


# post request sy form data kesy letyyn hain
# pehly form ko import krna phir ek pkg install krna pip install python-multipart
@app.post("/form/data")
# async def form_data(username: str= Form(), password: str= Form()):
async def form_data(item: schema1):
    return ({"item": item})


# file upload using pkg python_multipart and import file
@app.post("/file/upload")
async def file_bytes_len(file: bytes = File()):
    return ({"file": len(file)})


# just file upload karwani hn tu uploadfile import krna pary ga
@app.post("/upload/file")
async def file_upload(file: UploadFile):
    return ({"file":file})


# 3ino ko ek hi method main use karna file, form, upload
@app.post("/form_data/upload/file")
async def form_upload_file(file1: UploadFile, file2: bytes = File(), name: str = Form()):
    return ({"file1": file1.filename, "file2": len(file2), "name": name})


# error handling is k liya pehly import karna hn HTTPException
items = [2, 3, 4, 5, 6]


@app.get("/error/handling")
async def handle_error(item: int):
    if item not in items:
        return HTTPException(status_code=400, detail="file not found enter another number")
    return {"values": item}
