import openai

openai.api_key = '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'


timeBetweenRequests = 2

def getChatGptResponse(userDescription, level):
    prompt = f"User: I want to learn about {userDescription}. My difficulty level is {level}."

    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=0.7,
            max_tokens=150,
            stop=None
        )

        if response and response.choices and response.choices[0].text:
            return response.choices[0].text.strip()
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
    recommendedCourses = []

    for courseId, courseInfo in courseSet.items():
        chatGptResponse = getChatGptResponseCached(userDescription, level)

        recommendedCourse = {
            'name': courseInfo['name'],
            'length': courseInfo['length'],
            'modality': courseInfo['modality'],
            'price': courseInfo['price'],
            'description': courseInfo['description'],
            'difficulty': courseInfo['difficulty'],
            'institution': courseInfo['idInstitution'],
            'link': courseInfo['link'],
            'chatGptResponse': chatGptResponse
        }

        recommendedCourses.append(recommendedCourse)

    return recommendedCourses

def categorizeCourses(courseSet, level, userDescription):
    courses = filterCourses(courseSet, level, userDescription)
    finalCourses = {'easy': [], 'intermediate': [], 'difficult': []}

    for i in courses:
        finalCourses[i['difficulty']].append(i)

    return finalCourses



