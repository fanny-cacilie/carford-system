from app.cars.models import ColorEnum, ModelEnum

def validate_color(value):
    try:
        return ColorEnum[value]
    except KeyError:
        raise ValueError(f"{value} is not a valid color. Possible values: {[color.name for color in ColorEnum]}.")

def validate_model(value):
    try:
        return ModelEnum[value]
    except KeyError:
        raise ValueError(f"{value} is not a valid model. Possible values: {[model.name for model in ModelEnum]}.")
