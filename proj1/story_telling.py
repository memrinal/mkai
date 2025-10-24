import requests
import json

def get_user_inputs():
    print("Welcome to the Personalized Story Generator!")
    character_name = input("Enter the main character's name: ")
    setting = input("Enter the setting of the story: ")
    theme = input("Enter the theme of the story (e.g., adventure, mystery): ")
    return character_name, setting, theme

def generate_story(character_name, setting, theme):
    prompt = f"""Create a short story (about 200 words) with the following details:

Main Character: {character_name}
Setting: {setting}
Theme: {theme}

Write an engaging story incorporating these elements. Please provide the story only once."""

    try:
        response = requests.post('http://localhost:11434/api/generate',
                               json={
                                   "model": "mistral",
                                   "prompt": prompt,
                                   "stream": False,
                                   "options": {
                                       "temperature": 0.7
                                   }
                               })
        response.raise_for_status()
        try:
            data = response.json()
            if 'error' in data:
                return f"Error from API: {data['error']}"
            story = data.get('response', 'No response generated')
            # Remove any duplicate content
            if story.count(story.split('\n')[0]) > 1:
                story = '\n'.join(story.split('\n')[:story.count('\n')//2])
            return story
        except json.JSONDecodeError as e:
            return f"Error parsing response: {str(e)}\nResponse text: {response.text[:200]}..."
    except Exception as e:
        return f"Error generating story: {str(e)}"

if __name__ == "__main__":
    character, setting, theme = get_user_inputs()
    story = generate_story(character, setting, theme)
    print("\nHere's your story:\n")
    print(story)
    print(story)

