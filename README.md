# Real-Time Currency Converter

This is a Real-Time Currency Converter built with Python, Flask, and FastAPI. It allows users to convert an amount from one currency to another using the latest exchange rates.

## Features

- Real-time currency conversion using the latest exchange rates
- User-friendly web interface for inputting conversion details
- FastAPI backend for efficient and scalable currency conversion

## Technologies Used

- Python
- Flask (web framework)
- FastAPI (backend API framework)
- HTML/CSS (for the web interface)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/currency-converter.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the FastAPI backend:

```bash
uvicorn main:app --reload
```

4. In a separate terminal, run the Flask web application:

```bash
python app.py
```

5. Open your web browser and visit `http://localhost:5000` to access the currency converter.

## Usage

1. Enter the amount you want to convert in the "Amount" field.
2. Enter the source currency code in the "From Currency" field (e.g., USD, EUR, GBP).
3. Enter the target currency code in the "To Currency" field (e.g., USD, EUR, GBP).
4. Click the "Convert" button to see the converted amount.

## API Endpoint

The FastAPI backend provides a single endpoint for currency conversion:

- Endpoint: `/convert`
- Method: GET
- Parameters:
  - `amount` (float): The amount to convert.
  - `from_currency` (string): The source currency code.
  - `to_currency` (string): The target currency code.
- Response: JSON object containing the converted amount.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
