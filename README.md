# fos-scraper-project

Built with Python, this project functions as a web scraper, collecting data from a targeted website and executing automated tasks.

## Prerequisites

- Python 3.11
- Docker (optional)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/youcefBOUKETHIR/fos-scraper-project

```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

3. Run the scraper:

```bash
python scrapper.py
```

This will start the scraper and create a results.txt that contains the output of scrapper.py

4. Run the scraper:

```bash
python soup.py
```

This will start the scraper and retrieves the population information for the city of Alger


## Docker

Alternatively, you can use Docker to run the scraper in a containerized environment:

1. Build the Docker image:

```bash
docker build -t my-scrapper .
```

2. Run the Docker container:

```bash
docker run my-scrapper
```

This will execute the scraper inside the Docker container.



