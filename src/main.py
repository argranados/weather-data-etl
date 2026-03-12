from extract import extract_weather
from transform import transform_weather


def run_pipeline():

    raw_data = extract_weather()

    df = transform_weather(raw_data)

    print(df)


if __name__ == "__main__":
    run_pipeline()