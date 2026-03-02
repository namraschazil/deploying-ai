# Assignment 2: Design and implement an AI system with a conversational interface.

This project implements a chat-based AI system with three services inside ./05_src/assignment_chat.
The system follows all requirements for Assignment 2 which are as follows:

At least three services
Gradio chat interface
Guardrails
Restricted topics enforcement
ChromaDB persistent semantic search
No direct SQLite usage

**System Overview**
**Nature of the Chat Client:**
Unibuddy is a university AI assistant chatbot to assist students. Its main aim is to:
- Retrieves live weather data
- Answers policy questions via semantic search
- Calculates GPA using function calling

**Services used in the AI system:**
- _Service 1:_ OpenWeatherMap API
- _Service 2:_ ChromaDB persistent semantic search (ChromaDB + embeddings)
- _Service 3:_ GPA calculator function

**Embedding Process**
- Used text-embedding-3-small
- Stired embeddings in ChromaDB persistent folder
- Documents should be under 40MB

**Guardrails:**
- Blocked restricted topics
- Prevent system prompt exposure
- The system will not respond to:
1. Cats or dogs
2. Horoscopes or Zodiac signs
3. Taylor Swift

**Personality:**
Friendly but professional university assistant who helps students with:
- campus policies
- weather info
- GPA Calculations

**Overview of the 3 required Services:**
1. _Service 1_ API call
Weather API which calls OpenWeatherMap and rewrites the result in natural language
Example: weather is a city? 
How to run:
python 05_src/assignment_chat/app.py

2. _Service 2_ Semantic search
University Policy Search which uses ChromaDB and stores small text files like refund_policy.txt, exam_rules.txt and academic_integrity.txt.
For example the user can ask "How do refunds work?". The Unibuddy bot embeds questions and searches the ChromaDB. It then returns the best matching policy chunk and summarizes the response.

Embedding Process:

3. _Service 3_ Function Calling
GPA Calculator is used where the User types the request "Calculate my GPA. I got A,B+,A- and C." The Unibuddy generates the response by:
-Calling GPA function
-Computing GPA
- and then explaining the result.

**User Interface**
We want:
A friendly university assistant personality
Memory of conversation (short-term, stored in a list)
Integration with your three services:
Weather (API call)
GPA calculator (function call)
Semantic search (ChromaDB)

