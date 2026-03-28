import gradio as gr

def respond(message):
    message = message.lower()

    if "damaged" in message:
        return "We sincerely apologize for the damaged product. A refund or replacement has been initiated."

    elif "delay" in message:
        return "We regret the delay and appreciate your patience."

    elif "refund" in message:
        return "Your refund has been successfully initiated and will be processed within 3-5 business days."

    elif "angry" in message or "upset" in message:
        return "We understand your frustration and sincerely apologize for the inconvenience caused."

    elif "exchange" in message:
        return "Your product exchange request has been successfully processed."

    elif "delivered" in message:
        return "Your order has been successfully delivered. Thank you for shopping with us."

    else:
        return "Thank you for contacting us. Our team will get back to you shortly."

iface = gr.Interface(
    fn=respond,
    inputs="text",
    outputs="text",
    title="Customer Support AI"
)

iface.launch()
