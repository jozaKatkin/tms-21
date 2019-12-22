EXIT = 0
SUM = 1
DIFF = 2
MULT = 3
DIV = 4

CONFIG = {
    'operations': {
        EXIT: {
            'choice_message': f'{EXIT}. Exit',
        },
        SUM: {
            'operation': 'plus',
            'choice_message': f'{SUM}. Calc sum',
            'result_pattern': '{} + {} = {}',
        },
        DIFF: {
            'operation': 'minus',
            'choice_message': f'{DIFF}. Calc diff',
            'result_pattern': '{} - {} = {}',
        },
        MULT: {
            'operation': 'multi',
            'choice_message': f'{MULT}. Calc mult',
            'result_pattern': '{} * {} = {}',
        },
        DIV: {
            'operation': 'divide',
            'choice_message': f'{DIV}. Calc div',
            'result_pattern': '{} / {} = {}',
        },
    },
    'available_operations': [
        EXIT,
        SUM,
        DIFF,
        MULT,
        DIV,
    ],
}
