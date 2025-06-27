from transformers import T5Tokenizer, T5ForConditionalGeneration

class TextSummarizer:
    def __init__(self):
        self.model = T5ForConditionalGeneration.from_pretrained("t5-small")
        self.tokenizer = T5Tokenizer.from_pretrained("t5-small")

    def summarize(self, text, max_length=150):
        input_text = "summarize: " + text.strip().replace("\n", " ")
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
        summary_ids = self.model.generate(
            input_ids,
            max_length=max_length,
            min_length=30,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
