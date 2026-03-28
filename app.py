import gradio as gr

def generate_response(user_input):
    user_input = user_input.lower()

    if "damaged" in user_input:
        return "We sincerely apologize for the damaged product. A refund or replacement has been initiated."

    elif "delay" in user_input:
        return "We apologize for the delay. Your order will be delivered soon."
   
    elif "refund" in user_input:
        return "Your refund has been successfully initiated and will be processed within 3-5 business days."
 
    elif "angry" in user_input or "upset" in user_input:
        return "We understand your frustration and sincerely apologize."

    else:
        return "Thank you for contacting us. We will resolve your issue soon."

interface = gr.Interface(
    fn=generate_response,
    inputs="text",
    outputs="text",
    title="Customer Support AI"
)

interface.launch()