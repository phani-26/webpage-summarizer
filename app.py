# pip install gradio
import gradio as gr
from summarizer import summarize

def summarize_with_error(url):
    try:
        return summarize(url)
    except Exception as e:
        return f"❌ Error: {type(e).__name__}: {e}"

gr.Interface(
    fn=summarize_with_error,                       # your function (with error handling)
    inputs=gr.Textbox(label="Website URL"),
    outputs=gr.Markdown(label="Summary"),
    title="🔎 AI Website Summarizer",
).launch(share=True)   # share=True → a public link you can post! 🎉