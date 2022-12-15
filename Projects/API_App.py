import asyncio
from fastapi import FastAPI
company_list = ['Oracle','Google','Microsoft','Amazon','Deloitte','123','abc']
app = FastAPI()

@app.get("/replace-string")
def replace_words(company=None):

    if company in company_list and '©️' not in company:
        new_name = company+'©️'

    elif company in company_list and '©️' in company:
        new_name = company
    else:
        new_name = 'Entered name is not in the company list'


    return new_name
