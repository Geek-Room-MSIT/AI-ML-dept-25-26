import streamlit as st
import re
import emoji
from transformers import pipeline

st.set_page_config(
    page_title="Emoji Mood Analyzer",
    page_icon="😊",
    layout="centered"
)

# @st.cache_resource
# def load_model():
#     return pipeline(
#         "sentiment-analysis",
#         model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
#     )
@st.cache_resource
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="cardiffnlp/twitter-roberta-base-sentiment-latest" 
    )

sentiment_model = load_model()

emoji_sentiments = {
    "😀": 1, "😃": 1, "😄": 1, "😁": 1, "😍": 2, "🥰": 2, "😊": 1,
    "😂": 1, "🤣": 1, "😅": 1, "😇": 1,
    "😢": -1, "😭": -2, "😞": -1, "😔": -1, "😡": -2, "😠": -1,
    "😫": -1, "😩": -2, "😤": -1, "🤬": -2, "😐": 0, "😶": 0, "😑": 0,
    
    "📅": 0, "📆": 0, "🗓️": 0,  # Calendar emojis
    "📝": 0, "📄": 0, "📋": 0,  # Document emojis
}



def get_emoji_sentiment(text: str) -> float:
    found = emoji.distinct_emoji_list(text)
    if not found:
        return 0.0
    values = [emoji_sentiments.get(e, 0) for e in found]
    return sum(values) / len(values)


def remove_emojis(text: str) -> str:
    return re.sub(r'[' + ''.join(emoji_sentiments.keys()) + r']', '', text)


# def analyze_mood(sentence: str):
#     clean_text = remove_emojis(sentence)
#     text_result = sentiment_model(clean_text[:512])[0]
#     text_label = text_result["label"]
#     text_score = text_result["score"]

#     if text_label.lower().startswith("pos"):
#         text_value = text_score
#     else:
#         text_value = -text_score

#     # Emoji sentiment
#     emoji_value = get_emoji_sentiment(sentence)

#     # Weighted fusion
#     final_score = 0.7 * text_value + 0.3 * emoji_value

#     # if final_score > 0.25:
#     #     mood = "😊 Positive"
#     # elif final_score < -0.25:
#     #     mood = "😞 Negative"
#     # else:
#     #     mood = "😐 Neutral"
#     if final_score > 0.5:  # Changed from 0.25
#         mood = "😊 Positive"
#     elif final_score < -0.5:  # Changed from -0.25
#         mood = "😞 Negative"
#     else:
#         mood = "😐 Neutral" 

#     return {
#         "text_sentiment": text_label,
#         "text_score": round(text_score, 3),
#         "emoji_sentiment": round(emoji_value, 3),
#         "final_score": round(final_score, 3),
#         "overall_mood": mood,
#     }
def analyze_mood(sentence: str):
    clean_text = remove_emojis(sentence)
    text_result = sentiment_model(clean_text[:512])[0]
    text_label = text_result["label"]
    text_score = text_result["score"]

    # Handle all three labels from the RoBERTa model
    if text_label.lower() == "positive":
        text_value = text_score
    elif text_label.lower() == "negative":
        text_value = -text_score
    else:  # neutral
        text_value = 0.0  # ✅ Neutral should be 0, not negative!

    # Emoji sentiment
    emoji_value = get_emoji_sentiment(sentence)

    # Weighted fusion
    final_score = 0.7 * text_value + 0.3 * emoji_value

    if final_score > 0.5:
        mood = "😊 Positive"
    elif final_score < -0.5:
        mood = "😞 Negative"
    else:
        mood = "😐 Neutral" 

    return {
        "text_sentiment": text_label,
        "text_score": round(text_score, 3),
        "emoji_sentiment": round(emoji_value, 3),
        "final_score": round(final_score, 3),
        "overall_mood": mood,
    }


# Initialize session state for text input
if 'text_input' not in st.session_state:
    st.session_state.text_input = ""

st.title("🔍 Advanced Emoji Mood Analyzer")
st.markdown("### Analyze the sentiment of your text with emojis!")
st.write("")

# Text input
user_input = st.text_area(
    "Enter your text (with or without emojis):",
    value=st.session_state.text_input,
    placeholder="e.g., I'm feeling great today! 😊",
    height=100
)

# Analyze button
if st.button("🔍 Analyze Mood", type="primary"):
    if user_input.strip():
        with st.spinner("Analyzing..."):
            result = analyze_mood(user_input)
        
        # Display results
        st.success("Analysis Complete!")
        
        # Create columns for better layout
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                label="Overall Mood",
                value=result["overall_mood"]
            )
            st.metric(
                label="Text Sentiment",
                value=result["text_sentiment"]
            )
        
        with col2:
            st.metric(
                label="Final Score",
                value=result["final_score"]
            )
            st.metric(
                label="Text Confidence",
                value=result["text_score"]
            )
        
        # Additional details
        st.write("---")
        st.subheader("📊 Detailed Analysis")
        
        col3, col4 = st.columns(2)
        with col3:
            st.write(f"**Emoji Sentiment:** {result['emoji_sentiment']}")
        with col4:
            # Count emojis in text
            emojis_found = emoji.distinct_emoji_list(user_input)
            st.write(f"**Emojis Found:** {len(emojis_found)}")
        
        if emojis_found:
            st.write(f"**Emojis Used:** {' '.join(emojis_found)}")
        
        # Show the formula
        with st.expander("ℹ️ How is the mood calculated?"):
            st.write("""
            The final mood score is calculated using a weighted average:
            
            **Final Score = 0.7 × Text Sentiment + 0.3 × Emoji Sentiment**
            
            - **Text Sentiment**: Analyzed using Twitter-RoBERTa transformer model
            - **Emoji Sentiment**: Based on predefined emoji sentiment values
            
            Classification:
            - Score > 0.5: 😊 Positive
            - Score < -0.5: 😞 Negative
            - Otherwise: 😐 Neutral
            """)
    else:
        st.warning("⚠️ Please enter some text to analyze!")

# Add sidebar with examples
with st.sidebar:
    st.header("💡 Try These Examples")
    
    examples = [
        "I am so happy today! 😊",
        "This is terrible 😡",
        "Just another day 😐",
        "I love this so much! 😍🥰",
        "Feeling sad and lonely 😢😭",
        "Work is stressful but I'm managing 😅"
    ]
    
    st.write("Click on an example to try it:")
    for example in examples:
        if st.button(example, key=example):
            st.session_state.text_input = example
            st.rerun()
    
    
    st.write("---")
    st.info("""
    **About this app:**
    
    This analyzer combines:
    - 🤖 AI-powered text sentiment analysis
    - 😊 Emoji sentiment evaluation
    - 📊 Weighted scoring system
    """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; padding: 20px;'>
        <p style='color: #666; font-size: 14px;'>
            Made with ❤️ by <a href='https://github.com/Abuzaid-01' target='_blank' style='color: #FF4B4B; text-decoration: none;'>Abuzaid</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
