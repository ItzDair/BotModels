# from openai import OpenAI

# # Also using the `client`
# def sales_agent(query):
#     try:
#         print(f"Query in sales_agent: {query}")

#         # Request to OpenAI API
#         completion = client.chat.completions.create(
#             model="gpt-3.5-turbo",  # Using gpt-3.5-turbo model
#             messages=[
#                 {"role": "user", "content": query}
#             ]
#         )

#         # Extracting the response
#         response = completion.choices[0].message.content
#         print(f"Response from sales_agent: {response}")
#         return response

#     except Exception as e:
#         print(f"Error occurred in sales_agent: {e}")
#         return f"Error occurred: {e}"

# ///////////////////////
# def sales_agent(client, query):
#     try:
#         print(f"Query in sales_agent: {query}")
        
#         completion = client.chat.completions.create(
#             model="gpt-3.5-turbo",  # Using gpt-3.5-turbo model
#             messages=[
#                 {"role": "user", "content": query}
#             ]
#         )

#         response = completion.choices[0].message.content
#         print(f"Response from sales_agent: {response}")
#         return response
#     except Exception as e:
#         print(f"Error occurred in sales_agent: {e}")
#         return f"Error occurred: {e}"
# ////////
# def sales_agent(client, query):
#     try:
#         print(f"Query in sales_agent: {query}")
        
#         # Add the sales_prompt as the initial system message
#         messages = [
#             {"role": "system", "content": sales_prompt},  # Include the sales prompt to provide context
#             {"role": "user", "content": query}  # User query follows
#         ]
        
#         completion = client.chat.completions.create(
#             model="gpt-3.5-turbo",  # Using gpt-3.5-turbo model
#             messages=messages
#         )

#         response = completion.choices[0].message.content
#         print(f"Response from sales_agent: {response}")
#         return response
#     except Exception as e:
#         print(f"Error occurred in sales_agent: {e}")
#         return f"Error occurred: {e}"
# //////////////////////////
# sales_agents.py
from prom.sales_prompts import sales_prompt  # Import the sales_prompt

def sales_agent(client, query):
    try:
        print(f"Query in sales_agent: {query}")
        
        # Use the imported sales_prompt in the messages
        messages = [
            {"role": "system", "content": sales_prompt},  # Include the sales prompt to provide context
            {"role": "user", "content": query}  # User query follows
        ]
        
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Using gpt-3.5-turbo model
            messages=messages
        )

        response = completion.choices[0].message.content
        print(f"Response from sales_agent: {response}")
        return response
    except Exception as e:
        print(f"Error occurred in sales_agent: {e}")
        return f"Error occurred: {e}"

