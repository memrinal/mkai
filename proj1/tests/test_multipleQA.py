import unittest
from unittest.mock import patch, MagicMock
import os
import tempfile

import multipleQA


class TestMultipleQA(unittest.TestCase):
    def setUp(self):
        # Create temporary files for questions and answers
        self.qfd, self.qpath = tempfile.mkstemp(text=True)
        os.close(self.qfd)
        self.afd, self.apath = tempfile.mkstemp(text=True)
        os.close(self.afd)

    def tearDown(self):
        try:
            os.remove(self.qpath)
        except OSError:
            pass
        try:
            os.remove(self.apath)
        except OSError:
            pass

    def make_mock_response(self, text):
        mock_resp = MagicMock()
        mock_resp.json.return_value = {"response": text}
        mock_resp.raise_for_status.return_value = None
        return mock_resp

    @patch("requests.post")
    def test_process_questions_writes_answers(self, mock_post):
        # Prepare questions file contents
        questions = [
            "What is 2+2?\n",
            "Say hello.\n",
        ]
        with open(self.qpath, "w", encoding="utf-8") as f:
            f.writelines(questions)

        # Configure the mock to return different responses depending on model
        def side_effect(url, json, timeout):
            model = json.get("model")
            if model == "llama2":
                return self.make_mock_response("llama2 response")
            elif model == "mistral":
                return self.make_mock_response("mistral response")
            else:
                return self.make_mock_response("unknown")

        mock_post.side_effect = side_effect

        # Run the processor
        multipleQA.process_questions(questions_file=self.qpath, answers_file=self.apath)

        # Read answers and assert expected content
        with open(self.apath, "r", encoding="utf-8") as f:
            out = f.read()

        # Basic assertions that both model responses appear for each question
        self.assertIn("Question 1: What is 2+2?", out)
        self.assertIn("llama2:", out)
        self.assertIn("llama2 response", out)
        self.assertIn("Mistral:", out)
        self.assertIn("mistral response", out)


if __name__ == "__main__":
    unittest.main()
