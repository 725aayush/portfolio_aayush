import streamlit as st
import json
from streamlit_option_menu import option_menu

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Aayush Pareek | Portfolio",
    page_icon="🚀",
    layout="wide"
)

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
def load_data():
    try:
        # Loading projects and skills from provided JSON files
        with open("skills.json", "r") as f:
            skills = json.load(f)
        with open("projects.json", "r") as f:
            projects = json.load(f)
        return skills, projects
    except Exception as e:
        st.error(f"Error loading JSON files: {e}")
        return [], []

skills, projects = load_data()

# -------------------------------------------------
# CSS - FIXED IMAGE HEIGHT & PREMIUM SOCIALS
# -------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    /* Fixed Image Size for Projects */
    .project-img-container img {
        height: 220px !important;
        object-fit: cover !important;
        width: 100% !important;
        border-radius: 10px;
    }

    .premium-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        text-align: center;
        transition: 0.3s;
    }
    
    .premium-card:hover {
        border-color: #2563eb;
        transform: translateY(-5px);
    }

    /* Premium Social Buttons */
    .social-btn {
        display: flex;
        align-items: center;
        padding: 12px 20px;
        background-color: #f8fafc;
        color: #1e293b !important;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 600;
        margin-bottom: 12px;
        transition: 0.3s;
    }

    .social-btn:hover {
        background-color: #eff6ff;
        border-color: #2563eb;
        transform: translateX(5px);
    }

    .social-logo {
        width: 24px;
        height: 24px;
        margin-right: 15px;
    }

    .nav-btn {
        display: inline-block;
        padding: 8px 16px;
        background-color: #2563eb;
        color: white !important;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        font-size: 0.8rem;
        width: 100%;
        text-align: center;
    }

    .tag {
        display: inline-block;
        background: #f1f5f9;
        color: #475569;
        padding: 2px 8px;
        border-radius: 5px;
        font-size: 0.7rem;
        margin: 2px;
    }
    /* Fixed Image Size for Project Cards */
    [data-testid="stMarkdownContainer"] .project-img-container img {
        width: 100% !important;
        height: 200px !important;
        object-fit: cover !important;
        border-radius: 10px 10px 0 0; /* Rounds top corners */
    }

    /* Optional: Ensure the container itself doesn't grow */
    .project-img-container {
        height: 200px;
        overflow: hidden;
        border-radius: 10px;
        margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER & BIO
# -------------------------------------------------
st.markdown("<h1 style='text-align: center; font-size: 4rem; margin-bottom:0;'>Aayush Pareek</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 1.2rem;'>Hello and welcome to my portfolio!</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 1.2rem;'>B.Tech in Computer Science • Artificial Intellegence enthusiast</p>", unsafe_allow_html=True)

col_a, col_b = st.columns([1.5, 1], gap="large")
with col_a:
    st.markdown("""
    <div style="background: white; padding: 30px; border-radius: 20px; border: 1px solid #e2e8f0;">
        <h3 style="margin-top:0;">About Me</h3>
        <p style="color: #475569; line-height: 1.6;">
            I'm Aayush Pareek, an aspiring AI Engineer with a strong foundation in computer science.
            I specialize in building intelligent systems that solve real-world problems. 
            Passionate about Deep Learning, NLP, and deploying scalable AI solutions.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        st.link_button("📩 Contact Me", url="mailto:aayushpareek725@gmail.com" ,use_container_width=True)
    with btn_col2:
        st.download_button("📄 Resume", data=b"resume", file_name="Resume.pdf", use_container_width=True)

with col_b:
    st.image("assets/image.jpeg", use_container_width=True)

st.write("---")

selected = option_menu(
    menu_title=None,
    options=["Skills & Tools", "Projects", "Contact"],
    icons=["cpu", "folder", "envelope"],
    orientation="horizontal"
)

# -------------------------------------------------
# SKILLS SECTION
# -------------------------------------------------
if selected == "Skills & Tools":
    cols = st.columns(6)
    for index, s in enumerate(skills):
        with cols[index % 6]:
            st.markdown(f"""
            <div class="premium-card">
                <img src="{s['logo']}" width="40">
                <p style="font-size: 0.8rem; font-weight: 600; margin-top: 10px;">{s['name']}</p>
            </div>
            """, unsafe_allow_html=True)

# -------------------------------------------------
# PROJECTS SECTION (FIXED IMAGE SIZE)
# -------------------------------------------------
elif selected == "Projects":
    p_cols = st.columns(2)
    for index, p in enumerate(projects):
        with p_cols[index % 2]:
            with st.container(border=True):
                # FIXED: The CSS above targets this specific class
                st.markdown(f'''
                    <div class="project-img-container">
                        <img src="{p['image']}" alt="{p['title']}">
                    </div>
                ''', unsafe_allow_html=True)
                
                st.markdown(f"#### {p['title']}")
                st.write(p['description'])
                
                tags_html = "".join([f'<span class="tag">{t}</span>' for t in p["tools"]])
                st.markdown(tags_html, unsafe_allow_html=True)
                
                st.write("")
                b1, b2 = st.columns(2)
                with b1:
                    st.markdown(f'<a href="{p["github"]}" class="nav-btn">GitHub</a>', unsafe_allow_html=True)
                with b2:
                    if p["demo"]:
                        st.markdown(f'<a href="{p["demo"]}" class="nav-btn" style="background-color:#1e293b;">Live Demo</a>', unsafe_allow_html=True)
# -------------------------------------------------
# CONTACT SECTION (WITH LOGOS)
# -------------------------------------------------
elif selected == "Contact":
    st.subheader("Connect with Me")
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        with st.container(border=True):
            # Defined social media list with official logos
            social_data = [
                {
                    "name": "Email", 
                    "url": "mailto:aayushpareek725@gmail.com", 
                    "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/google/google-original.svg"
                },
                {
                    "name": "LinkedIn", 
                    "url": "www.linkedin.com/in/aayush-pareek-565a53277", 
                    "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg"
                },
                {
                    "name": "GitHub", 
                    "url": "https://github.com/725aayush", 
                    "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"
                },
                {
                    "name": "Twitter / X", 
                    "url": "https://x.com/725DJANGO", 
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/5/57/X_logo_2023_original_fixed.svg"
                },
                {
                    "name": "YouTube", 
                    "url": "https://www.youtube.com/@P25-AAYUSH", 
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg"
                },
                {
                    "name": "LeetCode", 
                    "url": "https://leetcode.com/u/aayush25_47/", 
                    "logo": "https://upload.wikimedia.org/wikipedia/commons/1/19/LeetCode_logo_black.png"
                }
            ]

            for social in social_data:
                st.markdown(f"""
                <a href="{social['url']}" class="social-btn" target="_blank">
                    <img src="{social['logo']}" class="social-logo">
                    <span>{social['name']}</span>
                </a>
                """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #94a3b8;'>made with :heart: by Aayush Pareek [31/12/25]</p>", unsafe_allow_html=True)