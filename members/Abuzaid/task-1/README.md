# 🔍 Emoji Mood Analyzer

A sophisticated web-based sentiment analysis application that combines AI-powered text analysis with emoji sentiment detection to determine overall mood and emotional tone.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.50.0-red)
![Transformers](https://img.shields.io/badge/Transformers-4.57.1-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- 🤖 **AI-Powered Text Analysis**: Uses Twitter-RoBERTa transformer model for accurate sentiment classification
- 😊 **Emoji Sentiment Detection**: Analyzes emotional context from emojis in your text
- 📊 **Weighted Scoring System**: Combines text and emoji sentiment (70% text, 30% emoji)
- 🎨 **Interactive Web Interface**: Clean, modern UI built with Streamlit
- 📝 **Rich Examples**: Pre-loaded example sentences to test the analyzer
- 💡 **Detailed Breakdown**: View confidence scores, sentiment labels, and calculation details

## 🚀 Live Demo

[**Try it here!**](https://emoji-text-analyzer.streamlit.app/)

## 📸 Screenshots

![Emoji Mood Analyzer Interface](https://via.placeholder.com/800x400?text=Add+Screenshot+Here)

## 🛠️ Technologies Used

- **Python 3.11**
- **Streamlit** - Web framework
- **Transformers (HuggingFace)** - Sentiment analysis model
- **PyTorch** - Deep learning backend
- **Emoji** - Emoji processing library

## 📦 Installation

### Prerequisites

- Python 3.11 or higher
- pip package manager

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/Abuzaid-01/Emoji_Mood_analyzer.git
cd Emoji_Mood_analyzer
```

2. **Create a virtual environment**
```bash
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 🎯 Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### How to Use

1. Enter your text (with or without emojis) in the text area
2. Click the **"🔍 Analyze Mood"** button
3. View the detailed analysis including:
   - Overall mood classification
   - Text sentiment label
   - Confidence scores
   - Emoji sentiment contribution
   - Final weighted score

### Example Inputs

Try these examples:
- "I am so happy today! 😊"
- "This is terrible 😡"
- "Just another day 😐"
- "I love this so much! 😍🥰"
- "Feeling sad and lonely 😢😭"

## 🧮 How It Works

The analyzer uses a sophisticated weighted scoring system:

```
Final Score = 0.7 × Text Sentiment + 0.3 × Emoji Sentiment
```

### Text Sentiment Analysis
- Powered by `cardiffnlp/twitter-roberta-base-sentiment-latest`
- Returns: Positive, Neutral, or Negative with confidence score
- Optimized for social media and casual text

### Emoji Sentiment Mapping
Emojis are pre-classified with sentiment values:
- **Positive emojis** (😊, 😍, 🥰): +1 to +2
- **Negative emojis** (😢, 😡, 😭): -1 to -2
- **Neutral emojis** (😐, 📅, 📝): 0

### Classification Thresholds
- **Score > 0.5**: 😊 Positive
- **Score < -0.5**: 😞 Negative
- **Otherwise**: 😐 Neutral

## 📁 Project Structure

```
Emoji_Mood_analyzer/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── .gitignore         # Git ignore file
```

## 📋 Requirements

```
transformers
torch
emoji
streamlit
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] Add sentiment history tracking
- [ ] Export analysis results to CSV
- [ ] Support for multiple languages
- [ ] Custom emoji sentiment dictionary
- [ ] Batch text analysis
- [ ] API endpoint for integration
- [ ] Dark mode toggle

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Abuzaid**

- GitHub: [@Abuzaid-01](https://github.com/Abuzaid-01)
- Project Link: [https://github.com/Abuzaid-01/Emoji_Mood_analyzer](https://github.com/Abuzaid-01/Emoji_Mood_analyzer)

## 🙏 Acknowledgments

- [HuggingFace Transformers](https://huggingface.co/transformers/) for the sentiment analysis models
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Cardiff NLP](https://huggingface.co/cardiffnlp) for the Twitter-RoBERTa model

---

<div align="center">
Made with ❤️ by Abuzaid
</div>
