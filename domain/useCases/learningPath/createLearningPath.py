import openai
import ast

openai.api_key = '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'

timeBetweenRequests = 2

def getChatGptResponse(userDescription, level, courseSet):
    course_descriptions = [course.description for course in courseSet]

    prompt = (
        f"User: I want to learn about {userDescription}. "
        f"I have this set {course_descriptions}, "
        f"tell me the courses of the set that are more related to what I want to learn,just give me the descripctions in a list separated by enter. With no text before."
    )

    try:
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            temperature=0.7,
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


responseCache = {}

def getChatGptResponseCached(userDescription, level, courseSet):
    if (userDescription, level) in responseCache:
        return responseCache[(userDescription, level)]

    chatGptResponse = getChatGptResponse(userDescription, level, courseSet)

    responseCache[(userDescription, level)] = chatGptResponse

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

