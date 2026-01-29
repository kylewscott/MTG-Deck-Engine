# Structure
## Backend 
The Python backend will hold all the logic for the app including handling user input, grabbing card data, running analysis algorithm, calculating synergy, and handling database entries in the future. 
The plan will be to creat endpoints from the backend using fast api for the frontend to hit. 
### api
Handle functions for fast api to create endpoints for the frontend to hit
### models 
All the necessary data classes to help organize data. 
### parsers 
Handle parsing input, api data, and any future text parsing. 
### services 
Most of the core logic including api services, alogorithms, and database interactions. 
### test_data 
Any needed test data. 
### utils 
Any small utility functions to help keep primary functions cleaned up. 
### validations 
Logic for validating input 
## Frontend
Plan will be to have a typescript + react frontend. More to come
<br>
<br>
<br>
# TODO
The next items we to work on 
1. Be able to tokenize card text for key words and phrases.
2. Detecting synergy from the tokenized text, maybe use a map/dict with hardcoded synergieis (could be gross), myabe use LLM (difficult to deploy), could build fancy alogorithm.
3. Create graphs of the deck using weighted edges to represent synergy between cards.
4. Figure out what data our own endpoints will need to return and how they will be formatted.
5. Stronger flexibility with input
6. Layout framework for UI and start sending in real input to help with #5
7. Look into libraries that could help with this possibly
8. Need to heavily think about the design/layout of the UI
<br>
<br>
<br>
# Developing
Will each have our own branch
When you have work to add push it up to your branch and create a PR so we can see what each other adding or add feadback
Not super serious but will keep changes organized and prevent stepping on each others toes.
Follow file strucutre and naming conventions to keep things consistent and clean
