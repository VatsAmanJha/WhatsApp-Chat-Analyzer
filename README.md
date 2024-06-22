# WhatsApp Chat Analyzer

This is a web application built with Django for analyzing and visualizing WhatsApp chat data.

## Features

- Upload WhatsApp chat export files (.txt format).
- Analyze chat statistics such as total messages, words, media files, URLs, etc.
- Visualize top users, word frequency, emoji usage, and activity trends.
- Generate word cloud and time-based analysis plots.
- Export analysis results and visualizations for further exploration.

## Prerequisites

- Python (3.x recommended)
- Django (3.x recommended)
- Plotly (for visualization)
- Pandas (for data manipulation)
- WordCloud (for generating word cloud)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/VatsAmanJha/WhatsApp-Chat-Analyzer.git
   ```

2. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

5. Access the web application at http://localhost:8000/ in your browser.

## Usage

1. Upload a WhatsApp chat export file (.txt format) using the upload form on the home page.
2. Navigate to the statistics page to view chat analysis results and visualizations.
3. Select a user for detailed analysis or view overall statistics.
4. Explore different analysis options such as word frequency, emoji usage, and time-based trends.
5. Generate word cloud and download visualizations for sharing or further analysis.

## NLP-based Text Analysis

This project utilizes Natural Language Processing (NLP) techniques for text analysis, including sentiment analysis, keyword extraction, and text summarization. The NLP features enhance the depth and insights derived from chat data.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new Pull Request.

## Acknowledgements

- Thanks to the Django community for their amazing documentation and support.
- Plotly, Pandas, WordCloud, and NLP libraries for making data analysis and visualization easier.
- Contributors to open-source libraries used in this project.