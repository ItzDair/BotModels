# from openai import OpenAI


# # Assuming `client` has already been initialized somewhere else
# def triage_agent(client, query):
#     # Convert input to lowercase for easier matching (you can also use transliteration if needed)
#     query_lower = query.lower()

#     # Sales/Product related request (English + Russian)
#     sales_keywords_en = ["buy", "purchase", "product", "order", "price", "cost", "sales", "shop", "available", "offer", "catalog"]
#     sales_keywords_ru = ["купить", "покупка", "товар", "заказ", "цена", "стоимость", "продажа", "магазин", "доступно", "предложение", "каталог"]
    
#     company_keywords_en = ["partner", "affiliation", "collaboration", "business relationship", "alliance", "partnering", "company", "collaborate", "join forces", "work with"]
#     company_keywords_ru = ["партнер", "сотрудничество", "бизнес-отношения", "альянс", "партнерство", "компания", "сотрудничать", "работать с"]
#     # Checking if any sales-related word is in the user input
#     if any(keyword in query_lower for keyword in sales_keywords_en + sales_keywords_ru):
#         return sales_agent(client, query)
    

#     # Checking if any company/partner-related word is in the user input
#     elif any(keyword in query_lower for keyword in company_keywords_en + company_keywords_ru):
#         return company_partner_agent(client, query)
    
#     # If no specific keywords are found, process the request as a general query using OpenAI API
#     else:
#         try:
#             print(f"Query in triage_agent: {query}")

#             # Request to OpenAI API
#             completion = client.chat.completions.create(
#                 model="gpt-3.5-turbo",  # Using gpt-3.5-turbo model
#                 messages=[
#                     {"role": "user", "content": query}
#                 ]
#             )

#             # Extracting the response
#             response = completion.choices[0].message.content
#             print(f"Response from triage_agent: {response}")
#             return response

#         except Exception as e:
#             print(f"Error occurred in triage_agent: {e}")
#             return f"Error occurred: {e}"
from openai import OpenAI
from agents.sales_agent import sales_agent
from agents.company_partner_agent import company_partner_agent  # If it's in a separate module

# Assuming `client` has already been initialized somewhere else
def triage_agent(client, query):
    query_lower = query.lower()

    # Sales/Product related request (English + Russian)
    sales_keywords_en = ["buy", "purchase", "product", "order", "price", "cost", "sales", "shop", "available", "offer", "catalog"]
    sales_keywords_ru = ["купить", "покупка", "товар", "заказ", "цена", "стоимость", "продажа", "магазин", "доступно", "предложение", "каталог"]
    
    company_keywords_en = ["partner", "affiliation", "collaboration", "business relationship", "alliance", "partnering", "company", "collaborate", "join forces", "work with"]
    company_keywords_ru = ["партнер", "сотрудничество", "бизнес-отношения", "альянс", "партнерство", "компания", "сотрудничать", "работать с"]
    
    # Checking if any sales-related word is in the user input
    if any(keyword in query_lower for keyword in sales_keywords_en + sales_keywords_ru):
        return sales_agent(client, query)
    
    # Checking if any company/partner-related word is in the user input
    elif any(keyword in query_lower for keyword in company_keywords_en + company_keywords_ru):
        return company_partner_agent(client, query)
    
    # If no specific keywords are found, process the request as a general query using OpenAI API
    else:
        try:
            print(f"Query in triage_agent: {query}")

            # Request to OpenAI API
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": query}]
            )

            # Extracting the response
            response = completion.choices[0].message.content
            print(f"Response from triage_agent: {response}")
            return response

        except Exception as e:
            print(f"Error occurred in triage_agent: {e}")
            return f"Error occurred: {e}"
