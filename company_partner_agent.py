# from openai import OpenAI

# # Using the shared `client`
# def company_partner_agent(query):
#     try:
#         print(f"Query in company_partner_agent: {query}")

#         # Request to OpenAI API
#         completion = client.chat.completions.create(
#             model="gpt-3.5-turbo",  # Using gpt-3.5-turbo model
#             messages=[
#                 {"role": "user", "content": query}
#             ]
#         )

#         # Extracting the response
#         response = completion.choices[0].message.content
#         print(f"Response from company_partner_agent: {response}")
#         return response

#     except Exception as e:
#         print(f"Error occurred in company_partner_agent: {e}")
#         return f"Error occurred: {e}"
# def company_partner_agent(client, query):
#     try:
#         print(f"Query in company_partner_agent: {query}")
        
#         completion = client.chat.completions.create(
#             model="gpt-3.5-turbo",  # Using gpt-3.5-turbo model
#             messages=[
#                 {"role": "user", "content": query}
#             ]
#         )

#         response = completion.choices[0].message.content
#         print(f"Response from company_partner_agent: {response}")
#         return response
#     except Exception as e:
#         print(f"Error occurred in company_partner_agent: {e}")
#         return f"Error occurred: {e}"
# /////////////////

# company_partner_agent.py
from prom.company_partner_prompts import company_partner_prompt  # Import the updated company_partner_prompt

def company_partner_agent(client, query):
    try:
        print(f"Query in company_partner_agent: {query}")
        
        # Use the imported company_partner_prompt in the messages
        messages = [
            {"role": "system", "content": company_partner_prompt},  # Include the company_partner_prompt to provide context
            {"role": "user", "content": query}  # User query follows
        ]
        
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Using gpt-3.5-turbo model
            messages=messages
        )

        response = completion.choices[0].message.content
        print(f"Response from company_partner_agent: {response}")
        return response
    except Exception as e:
        print(f"Error occurred in company_partner_agent: {e}")
        return f"Error occurred: {e}"
