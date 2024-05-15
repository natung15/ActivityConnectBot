from random import randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello'in lowered:
        return 'Hello there!'
    elif 'burger' in lowered:
        return 'I love burgers and I am brazillian'
    elif 'bye' in lowered:
        return 'bye'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1,6)}'
    
        