from fastapi import FastAPI, HTTPException
from models import ItemBody

app = FastAPI()
menu_items: dict[int, ItemBody] = {}


# POST new item
@app.post("/items/{item_name}/{item_price}/{item_description}")
def add_item(item_name: str, item_price: float, item_description: str):
    items_ids= {item.item_name: item.item_id if item.item_id is not None else 0 for item in menu_items.values()}

    if item_name in items_ids.keys():
        raise HTTPException(status_code=400, detail="Item already exists!")
    
    else:
        item_id = max(menu_items.keys()) + 1 if menu_items else 0
        menu_items[item_id] = ItemBody(
            item_id=item_id, item_name=item_name, item_price=item_price, item_description=item_description
        )
    
    return {"item": menu_items[item_id]}
# End POST


# GET all items
@app.get("/items")
def get_items():
    return {"items": menu_items}
# End GET


# GET item by Id
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in menu_items:
        raise HTTPException(status_code=404, detail="Item not found!")
    
    return {"item": menu_items[item_id]}
# End GET


# PUT could go here TL;DI
# End PUT


# DELETE item by Id
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in menu_items:
        raise HTTPException(status_code=404, detail="Item not found!")
    
    del menu_items[item_id]
    return {"result": f"Item {item_id} deleted successfully!"}
# End DELETE
