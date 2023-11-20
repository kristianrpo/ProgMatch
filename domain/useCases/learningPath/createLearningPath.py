import openai
#from domain.entities.course.courseEntity import Course

openai.api_key = ''

temporaryDatabase = {
    "C001": {
        "name": "Introduction to Programming",
        "length": "8 weeks",
        "price": 49.99,
        "modality": "Online",
        "content": "Basic programming concepts",
        "description": "Learn the fundamentals of programming in this introductory course.",
        "idInstitution": 1,
        "link": "https://example.com/courses/c001",
        "difficulty": "easy",
    },
    "C002": {
        "name": "Advanced Algorithms",
        "length": "12 weeks",
        "price": 79.99,
        "modality": "In-person",
        "content": "Advanced algorithms and data structures",
        "description": "Explore advanced algorithms and optimization techniques in this advanced course.",
        "idInstitution": 2,
        "link": "https://example.com/courses/c002",
        "difficulty": "difficult",
    },
    "C003": {
    "name": "Web Development with HTML and CSS",
    "length": "10 weeks",
    "price": 59.99,
    "modality": "Online",
    "content": "Design and development of static web pages",
    "description": "Learn to create attractive web pages using HTML and CSS in this practical course.",
    "idInstitution": 3,
    "link": "https://example.com/courses/c003",
    "difficulty": "intermediate",
    },
    "C004": {
        "name": "Artificial Intelligence for Beginners",
        "length": "6 weeks",
        "price": 39.99,
        "modality": "Online",
        "content": "Basic concepts of Artificial Intelligence",
        "description": "Discover the fundamental concepts of Artificial Intelligence in this beginner-friendly course.",
        "idInstitution": 1,
        "link": "https://example.com/courses/c004",
        "difficulty": "easy",
    },
    "C005": {
        "name": "Object-Oriented Programming with Python",
        "length": "8 weeks",
        "price": 69.99,
        "modality": "Online",
        "content": "Principles of object-oriented programming (OOP) with Python",
        "description": "Master the principles of OOP using Python as the programming language in this advanced course.",
        "idInstitution": 2,
        "link": "https://example.com/courses/c005",
        "difficulty": "intermediate",
    },
    "C006": {
        "name": "Mobile App Development with React Native",
        "length": "14 weeks",
        "price": 89.99,
        "modality": "Online",
        "content": "Construction of cross-platform mobile applications",
        "description": "Learn to develop mobile applications with React Native and address specific challenges of cross-platform development.",
        "idInstitution": 3,
        "link": "https://example.com/courses/c006",
        "difficulty": "difficult",
    }
}

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
