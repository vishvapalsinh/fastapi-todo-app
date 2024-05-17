from typing import Union
from models import Todo
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

todos =[] 

# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# Get single todo
@app.get("/todos/{todo_id}")
async def get_todos(todo_id: int):
    for  todo in todos:
        if todo.id == todo_id:
            return{"todo": todo} 
    return {"message": "No todos found"}

# Create a todo
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message": "Todo has been updated"}

# Update a todo
@app.put("/todos/{todo_id}")
async def update_todos(todo_id: int, todo_obj:Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"todo": todo}
        return {"messge": "No todos found to update"}  


# Delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todos(todo_id: int):
    for  todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return{"todo": "Removed the todo item"} 
    return {"message": "No todos found"}