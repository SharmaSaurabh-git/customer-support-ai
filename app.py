import gradio as gr

def generate_response(user_input):
    user_input = user_input.lower()

    if "damaged" in user_input:
        return "We sincerely apologize for the damaged product. A refund or replacement has been initiated."

    elif "delay" in user_input:
        return "We apologize for the delay. Your order will be delivered soon."

    else:
        return "Thank you for contacting us. We will resolve your issue."

interface = gr.Interface(
    fn=generate_response,
    inputs="text",
    outputs="text"
)

interface.launch()
