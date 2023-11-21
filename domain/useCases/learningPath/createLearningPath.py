import openai
import ast

openai.api_key = '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'

timeBetweenRequests = 2

def extract_main_topic(user_input):
    """
    Extracts the main topic or concept from a user input using OpenAI's GPT-3.

    Parameters:
    - user_input (str): The user's input sentence.

    Returns:
    - str: The main topic or concept extracted by GPT-3.
    """
    prompt = f"User: {user_input}\nWhat is the main topic or concept in this sentence in a noun, in a single word?"

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=100
        )

        if response and response['choices'] and response['choices'][0]['text']:
            return response['choices'][0]['text'].strip()
        else:
            return "Could not get a response at this time."

    except openai.error.OpenAIError as e:
        print(f"Error calling the OpenAI API: {str(e)}")
        return "Could not get a response at this time."

def getChatGptResponse(user_description, level, course_set):
    """
    Generates a response using GPT-3 based on the user's description and course set.

    Parameters:
    - user_description (str): The user's description of the desired topic.
    - level (str): The difficulty level of courses ('easy', 'intermediate', 'difficult').
    - course_set (list): List of course objects.

    Returns:
    - str: GPT-3 generated response.
    """
    course_descriptions = [course.description for course in course_set]
    user_description = extract_main_topic(user_description)

    prompt = (
        f"User: I want to learn about {user_description}. "
        f"I have this set of courses: {(course_descriptions)}. "
        f"Which courses from the set are topic-related to what I want to learn? "
        f"Provide the course descriptions in a list separated by enter. "
        f"If there are no related courses, indicate that."
    )

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=150
        )

        if response and response['choices'] and response['choices'][0]['text']:
            return response['choices'][0]['text'].strip()
        else:
            print("OpenAI response is empty.")
            return "Could not get a response at this time."

    except openai.error.OpenAIError as e:
        print(f"Error calling the OpenAI API: {str(e)}")
        return "Could not get a response at this time."

memory = {}

def getChatGptResponseCached(user_description, level, course_set):
    """
    Generates a cached response using GPT-3 based on the user's description, level, and course set.

    Parameters:
    - user_description (str): The user's description of the desired topic.
    - level (str): The difficulty level of courses ('easy', 'intermediate', 'difficult').
    - course_set (list): List of course objects.

    Returns:
    - str: GPT-3 generated response.
    """
    chatGptResponse = getChatGptResponse(user_description, level, course_set)

    if user_description in memory and memory[user_description] == chatGptResponse:
        print(memory[user_description])
        return memory[user_description]

    memory[user_description] = chatGptResponse
    return chatGptResponse

def filterCourses(course_set, level, user_description):
    """
    Filters courses based on GPT-3 generated response.

    Parameters:
    - course_set (list): List of course objects.
    - level (str): The difficulty level of courses ('easy', 'intermediate', 'difficult').
    - user_description (str): The user's description of the desired topic.

    Returns:
    - dict: Recommended courses categorized by difficulty level.
    """
    recommended_courses = {'easy': [], 'intermediate': [], 'difficult': []}

    chatGptResponse = getChatGptResponseCached(user_description, level, course_set)

    descriptions_set = [course.description for course in course_set]
    chat_descriptions = [course.strip() for course in chatGptResponse.split('\n')]

    for description in chat_descriptions:
        for course in course_set:
            if description == course.description:
                recommended_courses[course.difficulty].append(course)

    return recommended_courses

def categorizeCourses(course_set, level, user_description):
    """
    Categorizes courses based on GPT-3 generated response.

    Parameters:
    - course_set (list): List of course objects.
    - level (str): The difficulty level of courses ('easy', 'intermediate', 'difficult').
    - user_description (str): The user's description of the desired topic.

    Returns:
    - list: Final list of recommended courses.
    """
    courses = filterCourses(course_set, level, user_description)
    final_courses = []

    if level == 'easy':
        final_courses = courses['easy'] + courses['intermediate'] + courses['difficult']
    elif level == 'intermediate':
        final_courses = courses['intermediate'] + courses['difficult']
    else:
        final_courses = courses['difficult']

    print(final_courses)
    return final_courses
