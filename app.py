import streamlit as st
import base64

# --- PAGE SETTINGS ---
st.set_page_config(page_title="Happy Birthday 💖", page_icon="🎂", layout="centered")

# --- CUSTOM CSS STYLE ---
st.markdown("""
    <style>
    body {
        background: radial-gradient(circle at top left, #ffdef2, #fff0f6, #ffe6f9);
        font-family: 'Poppins', sans-serif;
        color: #333;
        overflow-x: hidden;
    }
    .main-title {
        text-align: center;
        color: #ff3385;
        font-size: 70px;
        font-weight: 900;
        text-shadow: 2px 2px #ffcce5;
        animation: glow 2s ease-in-out infinite alternate;
        margin-top: 25px;
    }
    @keyframes glow {
        from { text-shadow: 0 0 15px #ff80bf, 0 0 25px #ff4da6; }
        to { text-shadow: 0 0 35px #ff99cc, 0 0 45px #ff3385; }
    }
    .subtitle {
        text-align: center;
        color: #ff66b2;
        font-size: 28px;
        font-style: italic;
        margin-bottom: 40px;
    }
    .message {
        background: rgba(255, 245, 250, 0.95);
        padding: 35px;
        border-radius: 25px;
        box-shadow: 0px 0px 25px rgba(255, 105, 180, 0.4);
        font-size: 18px;
        line-height: 1.7;
        color: #333;
        transition: all 0.3s ease-in-out;
    }
    .message:hover {
        transform: scale(1.02);
        box-shadow: 0px 0px 30px rgba(255, 20, 147, 0.4);
    }
    .btn {
        display: block;
        margin: 30px auto;
        background-color: #ff4da6;
        color: white;
        font-size: 20px;
        font-weight: bold;
        padding: 15px 40px;
        border-radius: 30px;
        text-align: center;
        transition: 0.3s;
    }
    .btn:hover {
        background-color: #ff1a8c;
        transform: scale(1.05);
    }
    @keyframes float {
      0% { transform: translateY(0); opacity: 1; }
      100% { transform: translateY(-800px); opacity: 0; }
    }
    .hearts {
      position: fixed;
      bottom: 0;
      width: 100%;
      text-align: center;
      font-size: 30px;
      color: #ff66b2;
      animation: float 6s linear infinite;
    }
    </style>

    <div class="hearts">💖 💗 💞 💕 💓 💝 💘</div>
""", unsafe_allow_html=True)

# --- TITLE ---
st.markdown("<h1 class='main-title'>🎉 Happy Birthday, Amtual Aala Tooba! 🎂</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subtitle'>Wishing you laughter, joy, and the brightest smiles today 💫</h3>", unsafe_allow_html=True)

# --- EMBED IMAGE AS BASE64 ---
try:
    with open("photo.jpg.jpg", "rb") as img_file:
        img_data = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f'<img src="data:image/jpeg;base64,{img_data}" style="width:90%;border-radius:25px;display:block;margin:auto;box-shadow:0 0 20px rgba(255,182,193,0.5);">',
        unsafe_allow_html=True)
except Exception as e:
    st.error(f"Image not found 😢: {e}")

# --- MESSAGE SECTION ---
st.markdown("---")
st.markdown("## 💌 A Note Just for You AALA")
st.markdown("""
<div class="message">
Hey there! 🎈  
You’ve been such a kind and wonderful person — someone who makes ordinary days feel brighter for everyone🌸  
I’m really happy to have a junior like you 💕  
May your birthday be full of smiles, laughter, and beautiful little surprises 🎂  
Here’s to another amazing year ahead — keep shining, keep smiling, and keep being *you*! ✨  
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.info("“Good people are like stars — you don’t always see them, but you know they’re always there.” 🌟")

st.markdown("---")

# --- SURPRISE BUTTON ---
if st.button("🎁 Click for a Little Surprise!"):
    st.balloons()
    st.snow()
    st.success("💖 You deserve every bit of happiness today — enjoy your moment! ✨")

    try:
        with open("song.mp3.mp3", "rb") as music_file:
            music_data = base64.b64encode(music_file.read()).decode()
        music_html = f"""
        <audio autoplay loop>
            <source src="data:audio/mp3;base64,{music_data}" type="audio/mp3">
        </audio>
        """
        st.markdown(music_html, unsafe_allow_html=True)
        st.markdown("### 🎶A special Music is playing... enjoy the birthday vibe 💕")
    except Exception as e:
        st.error(f"Couldn't load music 😢: {e}")

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align:center;color:#888;'>Made with 💖 and great care by <b>Aniqa</b></p>", unsafe_allow_html=True)
