CREATE TABLE IF NOT EXISTS weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100),
    temperature NUMERIC(5,2),
    humidity INTEGER,
    weather VARCHAR(50),
    wind_speed NUMERIC(5,2),
    timestamp BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);