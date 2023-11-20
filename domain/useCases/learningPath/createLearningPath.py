import openai

openai.api_key = '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'

timeBetweenRequests = 2

def getChatGptResponse(userDescription, level):
    prompt = f"User: I want to learn about {userDescription}."

    try:
        response = openai.ChatCompletion.create(
            model="text-davinci-002",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        if response and response['choices'] and response['choices'][0]['message']['content']:
            return response['choices'][0]['message']['content'].strip()
        else:
            print("OpenAI response is empty.")
            return "Could not get a response at this time."

    except openai.error.OpenAIError as e:
        print(f"Error calling the OpenAI API: {str(e)}")
        return "Could not get a response at this time."

responseCache = {}

def getChatGptResponseCached(userDescription, level):
    if (userDescription, level) in responseCache:
        return responseCache[(userDescription, level)]

    chatGptResponse = getChatGptResponse(userDescription, level)

    responseCache[(userDescription, level)] = chatGptResponse

    return chatGptResponse

def filterCourses(courseSet, level, userDescription):
    recommendedCourses = {}

    for courseInfo in courseSet.values():
        chatGptResponse = getChatGptResponseCached(userDescription, level)

        courseId = courseInfo['id']
        courseInfo['chatGptResponse'] = chatGptResponse
        recommendedCourses[courseId] = courseInfo

    return recommendedCourses


def categorizeCourses(courseSet, level, userDescription):
    courses = filterCourses(courseSet, level, userDescription)
    finalCourses = {'easy': [], 'intermediate': [], 'difficult': []}

    for i in courses.values():
        finalCourses[i['difficulty']].append(i)

    return finalCourses
