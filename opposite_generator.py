import os
from groq import Groq

def createOpposite(OGsentence):
    os.environ['GROQ_API_KEY'] = 'KEY'
    client = Groq(api_key=os.getenv('GROQ_API_KEY'))
    chat_completion = client.chat.completions.create(
        # Required parameters
        messages=[
            # Set an optional system message. This sets the behavior of the
            # assistant and can be used to provide specific instructions for
            # how it should behave throughout the conversation.
            {
                "role": "system",
                "content": "you are a helpful assistant."
            },
            # Set a user message for the assistant to respond to.
            {
                "role": "user",
                "content": "Give me the opposite of the main key word in the sentence. Don't greet me. Don't tell me this is or anything. I necessary want it to be a little funny and change the context to sound sarcastic. the goal is to be funny and give entirely different of what's asked yet be relatable about it. Still give me the result that is searchable. I dont want it to seem that it's result of a prompt, but mannually searched. replace the entire sentence. It should be relatable to the sentence I originally entered. My sentence is " + OGsentence,
            }
        ],

        # The language model which will generate the completion.
        model="llama3-8b-8192",

        # Optional parameters

        # Controls randomness: lowering results in less random completions.
        # As the temperature approaches zero, the model will become deterministic
        # and repetitive.
        temperature=0.5,

        # The maximum number of tokens to generate. Requests can use up to
        # 32,768 tokens shared between prompt and completion.
        max_tokens=1024,

        # Controls diversity via nucleus sampling: 0.5 means half of all
        # likelihood-weighted options are considered.
        top_p=1,

        # A stop sequence is a predefined or user-specified text string that
        # signals an AI to stop generating content, ensuring its responses
        # remain focused and concise. Examples include punctuation marks and
        # markers like "[end]".
        stop=None,

        # If set, partial message deltas will be sent.
        stream=False,
    )

    # Print the completion returned by the LLM.
    returned_query = chat_completion.choices[0].message.content
    return returned_query