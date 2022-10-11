from fastapi import FastAPI
#from utils/scraper import Scraper


app = FastAPI()
# data = Scraper() - The scraper class

@app.get("/Properties/palermo")
async def read_item(cat):
  return #data.method_that_return_the_data(cat)