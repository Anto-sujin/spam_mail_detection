import joblib
import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="SpamGuard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():
    return joblib.load("spam_detector.pkl")


try:
    model = load_model()
except Exception as e:
    st.error("❌ Could not load spam_detector.pkl")
    st.error(str(e))
    st.stop()


# =========================================================
# SESSION STATE
# =========================================================

if "message" not in st.session_state:
    st.session_state.message = ""


# =========================================================
# GLOBAL CSS
# =========================================================

st.html("""
<style>

html, body {
    background: #070b18;
}

/* Main background */
.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(59, 130, 246, 0.18),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 15%,
            rgba(139, 92, 246, 0.18),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #050816 0%,
            #0b1225 50%,
            #111936 100%
        );
}

/* Main content width */
.block-container {
    max-width: 1180px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}


/* =========================================================
   HERO
   ========================================================= */

.hero {
    text-align: center;
    padding: 35px 20px 30px 20px;
}

.hero-icon {
    font-size: 55px;
    margin-bottom: 8px;
}

.hero-title {
    font-size: 52px;
    font-weight: 800;
    letter-spacing: -1px;
    color: #ffffff;
    margin: 0;
}

.hero-title span {
    background: linear-gradient(
        90deg,
        #60a5fa,
        #a78bfa,
        #f472b6
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    margin-top: 12px;
    font-size: 18px;
    color: #aab6d3;
}


/* =========================================================
   SECTION TITLE
   ========================================================= */

.section-title {
    font-size: 25px;
    font-weight: 750;
    color: #f8fafc;
    margin-top: 22px;
    margin-bottom: 15px;
}


/* =========================================================
   RESULT
   ========================================================= */

.result-spam {
    margin-top: 20px;
    padding: 28px;
    text-align: center;
    border-radius: 20px;

    background: linear-gradient(
        135deg,
        rgba(127, 29, 29, 0.75),
        rgba(69, 10, 10, 0.75)
    );

    border: 1px solid rgba(248, 113, 113, 0.5);
}

.result-ham {
    margin-top: 20px;
    padding: 28px;
    text-align: center;
    border-radius: 20px;

    background: linear-gradient(
        135deg,
        rgba(6, 78, 59, 0.75),
        rgba(4, 47, 46, 0.75)
    );

    border: 1px solid rgba(52, 211, 153, 0.5);
}

.result-icon {
    font-size: 42px;
}

.result-title {
    font-size: 30px;
    font-weight: 800;
    color: white;
    margin-top: 8px;
}

.result-description {
    color: #cbd5e1;
    font-size: 16px;
    margin-top: 8px;
}


/* =========================================================
   METRIC CARDS
   ========================================================= */

.metric-card {
    padding: 20px 10px;
    border-radius: 17px;
    text-align: center;

    background: linear-gradient(
        145deg,
        rgba(30, 41, 59, 0.95),
        rgba(15, 23, 42, 0.95)
    );

    border: 1px solid rgba(148, 163, 184, 0.18);

    box-shadow:
        0 8px 25px rgba(0, 0, 0, 0.25);
}

.metric-value {
    font-size: 27px;
    font-weight: 800;
    color: #93c5fd;
}

.metric-label {
    margin-top: 5px;
    font-size: 13px;
    color: #94a3b8;
}


/* =========================================================
   FEATURE CARDS
   ========================================================= */

.feature-card {
    min-height: 165px;
    padding: 22px;
    border-radius: 18px;

    background: linear-gradient(
        145deg,
        rgba(30, 41, 59, 0.85),
        rgba(15, 23, 42, 0.85)
    );

    border: 1px solid rgba(148, 163, 184, 0.16);

    transition: transform 0.2s ease;
}

.feature-card:hover {
    transform: translateY(-4px);
}

.feature-icon {
    font-size: 34px;
}

.feature-title {
    margin-top: 10px;
    font-size: 18px;
    font-weight: 700;
    color: #f8fafc;
}

.feature-text {
    margin-top: 8px;
    font-size: 14px;
    line-height: 1.55;
    color: #94a3b8;
}


/* =========================================================
   PIPELINE
   ========================================================= */

.pipeline-card {
    padding: 25px;
    border-radius: 18px;
    text-align: center;

    background: rgba(15, 23, 42, 0.75);

    border: 1px solid rgba(96, 165, 250, 0.18);
}

.pipeline-step {
    display: inline-block;
    padding: 12px 20px;
    margin: 5px;

    border-radius: 12px;

    background: linear-gradient(
        135deg,
        #1e3a8a,
        #312e81
    );

    color: white;
    font-weight: 650;
}

.pipeline-arrow {
    color: #60a5fa;
    font-size: 20px;
}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {
    text-align: center;
    margin-top: 40px;
    padding: 25px;

    color: #64748b;
    font-size: 13px;
}

</style>
""")


# =========================================================
# HERO
# =========================================================

st.html("""
<div class="hero">

    <div class="hero-icon">🛡️</div>

    <div class="hero-title">
        Spam<span>Guard</span>
    </div>

    <div class="hero-subtitle">
        Intelligent SMS Spam Detection using Machine Learning & NLP
    </div>

</div>
""")


# =========================================================
# MESSAGE INPUT
# =========================================================

st.html("""
<div class="section-title">
    📩 Analyze Your Message
</div>
""")

message = st.text_area(
    "Enter your SMS message",
    value=st.session_state.message,
    height=160,
    placeholder=(
        "Type or paste your message here...\n\n"
        "Example: Congratulations! You have won a free prize..."
    ),
    label_visibility="visible"
)

# Keep message in session state
st.session_state.message = message


# =========================================================
# EXAMPLE MESSAGES
# =========================================================

st.html("""
<div class="section-title">
    🧪 Try an Example
</div>
""")

col1, col2, col3 = st.columns(3)


with col1:

    if st.button(
        "🚨 Spam Example",
        use_container_width=True
    ):

        st.session_state.message = (
            "Congratulations! You have won a $1000 cash prize. "
            "Click now to claim your reward!"
        )

        st.rerun()


with col2:

    if st.button(
        "✅ Ham Example",
        use_container_width=True
    ):

        st.session_state.message = (
            "Hey, are we still meeting tomorrow at 10 AM?"
        )

        st.rerun()


with col3:

    if st.button(
        "💬 Normal Example",
        use_container_width=True
    ):

        st.session_state.message = (
            "Can you send me the project report when you get a chance?"
        )

        st.rerun()


# =========================================================
# ANALYZE BUTTON
# =========================================================

st.write("")

analyze = st.button(
    "🔍 Analyze Message",
    type="primary",
    use_container_width=True
)


if analyze:

    if not st.session_state.message.strip():

        st.warning(
            "⚠️ Please enter a message before analyzing."
        )

    else:

        text = st.session_state.message

        # Prediction
        prediction = model.predict([text])[0]

        # SVM decision score
        decision_score = model.decision_function([text])[0]


        # =================================================
        # SPAM RESULT
        # =================================================

        if prediction == 1:

            st.html("""
            <div class="result-spam">

                <div class="result-icon">
                    🚨
                </div>

                <div class="result-title">
                    SPAM DETECTED
                </div>

                <div class="result-description">
                    This message has been classified as spam.
                </div>

            </div>
            """)

            st.warning(
                "⚠️ Avoid clicking unknown links or sharing "
                "personal and financial information."
            )


        # =================================================
        # HAM RESULT
        # =================================================

        else:

            st.html("""
            <div class="result-ham">

                <div class="result-icon">
                    ✅
                </div>

                <div class="result-title">
                    LEGITIMATE MESSAGE
                </div>

                <div class="result-description">
                    This message has been classified as Ham.
                </div>

            </div>
            """)


        # =================================================
        # MODEL SCORE
        # =================================================

        with st.expander("🔎 View Technical Details"):

            st.write(
                f"**SVM Decision Score:** `{decision_score:.4f}`"
            )

            st.caption(
                "The decision score shows how strongly the SVM "
                "leans toward a class. It is not a probability."
            )


# =========================================================
# MODEL PERFORMANCE
# =========================================================

st.divider()

st.html("""
<div class="section-title">
    📊 Model Performance
</div>
""")


metrics = [
    ("98.83%", "Accuracy"),
    ("98.57%", "Precision"),
    ("92.62%", "Recall"),
    ("95.50%", "F1 Score"),
    ("98.80%", "ROC-AUC"),
    ("97.85%", "PR-AUC")
]


cols = st.columns(6)


for col, (value, label) in zip(cols, metrics):

    with col:

        st.html(
            f"""
            <div class="metric-card">

                <div class="metric-value">
                    {value}
                </div>

                <div class="metric-label">
                    {label}
                </div>

            </div>
            """
        )


# =========================================================
# HOW IT WORKS
# =========================================================

st.divider()

st.html("""
<div class="section-title">
    ⚙️ How SpamGuard Works
</div>
""")


col1, col2, col3, col4 = st.columns(4)


features = [
    (
        "📝",
        "Message",
        "The user enters an SMS message into the detector."
    ),

    (
        "🔤",
        "TF-IDF",
        "The text is converted into numerical features."
    ),

    (
        "🧠",
        "SVM",
        "The trained Linear SVM analyzes the text features."
    ),

    (
        "🎯",
        "Prediction",
        "The model classifies the message as Spam or Ham."
    )
]


for col, (icon, title, description) in zip(
    [col1, col2, col3, col4],
    features
):

    with col:

        st.html(
            f"""
            <div class="feature-card">

                <div class="feature-icon">
                    {icon}
                </div>

                <div class="feature-title">
                    {title}
                </div>

                <div class="feature-text">
                    {description}
                </div>

            </div>
            """
        )


# =========================================================
# ML PIPELINE
# =========================================================

st.divider()

st.html("""
<div class="section-title">
    🔬 Machine Learning Pipeline
</div>

<div class="pipeline-card">

    <span class="pipeline-step">
        📩 SMS
    </span>

    <span class="pipeline-arrow">
        →
    </span>

    <span class="pipeline-step">
        🧹 Text Processing
    </span>

    <span class="pipeline-arrow">
        →
    </span>

    <span class="pipeline-step">
        🔤 TF-IDF
    </span>

    <span class="pipeline-arrow">
        →
    </span>

    <span class="pipeline-step">
        🧠 Linear SVM
    </span>

    <span class="pipeline-arrow">
        →
    </span>

    <span class="pipeline-step">
        🎯 Spam / Ham
    </span>

</div>
""")


# =========================================================
# MODEL DETAILS
# =========================================================

st.divider()

with st.expander("⚙️ Final Model Configuration"):

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 🧠 SVM")

        st.write("**Algorithm:** Support Vector Machine")
        st.write("**Kernel:** Linear")
        st.write("**C:** 10")

    with col2:

        st.markdown("### 🔤 TF-IDF")

        st.write("**max_df:** 0.95")
        st.write("**min_df:** 2")
        st.write("**ngram_range:** (1, 2)")
        st.write("**sublinear_tf:** True")


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="footer">

    🛡️ <strong>SpamGuard</strong>

    <br><br>

    Machine Learning • Natural Language Processing •
    TF-IDF • Support Vector Machine

    <br><br>

    Built as an end-to-end Machine Learning project

</div>
""")