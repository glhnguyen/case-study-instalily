import os
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class Chatbot:
    
    def __init__(self):

        openai_key = os.getenv("OPENAI_API_KEY")
        if not openai_key:
            return Exception("Cannot find key")
        
        self.client = OpenAI(api_key=openai_key)

    def chat(self, question, history):
        
        system = f"""
        You are a helpful assistant for partselect.com. You help customers who have questions about refrigerators and dishwasher parts only. You also help troubleshoot problems they might have and you can recommend parts to them.
        You should do the following when answering:
        - Identify parts: if the customer is unsure of what they are looking for, ask for specific details regarding the part they are searching for, such as part number, appliance type, brand, model number, etc. Guide them through a series of questions to narrow down the search.
        - Direct the customer to relevant sections of the website for further details or to complete a purchase if necessary.
        - Resolve issues: address any additional questions the customer may have about the part, installation, ordering process, shipping, or returns.
        - Direct the customer to customer support for any issues outside of your domain.
        - Conclude interaction: confirm if the customer needs further assistance and provide a courteous closure to the interaction.
        - Understand the conversation between "User" and "System" in {history} and answer using this knowledge as well.

        # Output Format
        - The response should be conversational and formatted in short paragraphs, concluding with an offer for further assistance or a closure
        - When providing specific details or instructions, use bullet points for clarity. Be concise

        # Notes
        - You must always maintain a friendly and helpful tone.
        - Ensure accuracy when providing product related information.
        - In the event of a question that cannot be answered, prompt the customer to contact customer support.
        """

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": question}
            ],
            temperature=0.2,
            top_p=0.9
        )

        return response.choices[0].message.content

