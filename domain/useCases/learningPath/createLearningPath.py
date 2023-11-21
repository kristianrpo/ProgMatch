import openai
import ast
import spacy

openai.api_key = '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'

timeBetweenRequests = 2


def extract_main_topic(user_input):
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




def getChatGptResponse(user_description,level, course_set):
    course_descriptions = [course.description for course in course_set]
    user_description = extract_main_topic(user_description)
    print(1111111,user_description)
    prompt = (
        f"User: I want to learn about {user_description}. "
        f"I have this set of courses: {(course_descriptions)}. "
        f"Which courses from the set are topic related to what I want to learn? "
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
        print(response)
        if response and response['choices'] and response['choices'][0]['text']:
            return response['choices'][0]['text'].strip()
        else:
            print("OpenAI response is empty.")
            return "Could not get a response at this time."

    except openai.error.OpenAIError as e:
        print(f"Error calling the OpenAI API: {str(e)}")
        return "Could not get a response at this time."




def getChatGptResponseCached(userDescription, level, courseSet):

    chatGptResponse = getChatGptResponse(userDescription, level, courseSet)
    return chatGptResponse

def filterCourses(courseSet, level, userDescription):
    recommendedCourses = {'easy': [], 'intermediate': [], 'difficult': []}

    chatGptResponse = getChatGptResponseCached(userDescription, level, courseSet)

    descriptions_set = [course.description for course in courseSet]

    chat_descriptions = [course.strip() for course in chatGptResponse.split('\n')]

    for description in chat_descriptions:
        for course in courseSet:
            if description == course.description:
                recommendedCourses[course.difficulty].append(course)

    return recommendedCourses



def categorizeCourses(courseSet, level, userDescription):

    courses = filterCourses(courseSet, level, userDescription)

    finalCourses = []

    if(level == 'easy'):
        finalCourses = courses['easy'] + courses['intermediate'] + courses['difficult']
    elif(level == 'intermediate'):
        finalCourses = courses['intermediate'] + courses['difficult']
    else:
        finalCourses = courses['difficult']
    
 
    print(finalCourses)
    return finalCourses

