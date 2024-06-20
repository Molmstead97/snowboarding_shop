from fastapi import FastAPI, HTTPException
from schemas import Snowboard

import json

app = FastAPI()

with open('snowboards.json', 'r') as f:
    snowboard_data = json.load(f)
    
snowboard_list = []
for snowboard in snowboard_data:
    snowboard_list.append(snowboard)
    
@app.get('/snowboards')
async def get_snowboards() -> list[Snowboard]:
    
    return snowboard_list

@app.post('/snowboards')
async def create_snowboard(snowboard: Snowboard) -> Snowboard:
    
    snowboard_list.append(snowboard)
    return snowboard

@app.put('/snowboards/{snowboard_id}')
async def update_snowbard(snowboard_id: int, updated_snowboard: Snowboard):
    
    for snowboard in snowboard_list:
        if snowboard['id'] == snowboard_id:
            snowboard.update(updated_snowboard)
            return 'Updated successfully'
        
        else:
            snowboard_list.append(updated_snowboard)
            return updated_snowboard
        

@app.delete('/snowboards/{snowboard_id}')
async def delete_snowboard(snowboard_id: int):
    
    for snowboard in snowboard_list:
        if snowboard['id'] == snowboard_id:
            snowboard_list.remove(snowboard)
            return 'Deleted successfully'
        
    raise HTTPException(status_code=404, detail='Snowboard not found')

