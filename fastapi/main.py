from fastapi import FastAPI
 
# Create a FastAPI application
app = FastAPI()
 
# Define a route at the root web address ("/")
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


#with path param param 
@app.get("/{course}")
def get_data(course: str):
    return {"CourseName": course}

@app.get("/number/{param}")
def get_number(param: int):
    return {"Number Input": param}
@app.get("/inputnum/{param}")
def get_number(param: float):
    return {"Number Input": param}