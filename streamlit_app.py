import streamlit as st
import pandas as pd
from datetime import datetime

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Premium Property Listing",
    page_icon="🏡",
    layout="centered"
)

# -----------------------------
# CUSTOM CSS (PREMIUM UI)
# -----------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.card {
    padding: 20px;
    border-radius: 12px;
    background-color: white;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
.badge {
    display: inline-block;
    padding: 6px 10px;
    background-color: #e6f0ff;
    border-radius: 8px;
    margin: 4px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.title("🏡 1BHK for Sale")

st.markdown("""
**550 sqft | ₹35L**  
📍 Mohan Highlands Society  
""")

# BADGES
st.markdown("""
<span class="badge">Parking</span>
<span class="badge">Lift</span>
<span class="badge">Near School</span>
<span class="badge">Highway Access</span>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# EXACT OPTION 1 AD
# -----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("""
### 1BHK for Sale | 550 sqft | ₹35L  
📍 Mohan Highlands Society  
✔ Parking + Lift  
✔ Next to Gurukul School  
✔ Near Upcoming Panvel Highway  
DM for details
""")

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# VIDEO
# -----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🎥 Property Video")
video_file = st.file_uploader("Upload video", type=["mp4"])

if video_file:
    st.video(video_file)

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# IMAGE GALLERY
# -----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🖼️ Property Gallery")

images = st.file_uploader(
    "Upload images",
    type=["jpg", "png", "jpeg"],
    accept_multiple_files=True
)

if images:
    cols = st.columns(2)
    for i, img in enumerate(images):
        cols[i % 2].image(img, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# MAP
# -----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📍 Location")

st.markdown("[👉 Open in Google Maps](https://maps.app.goo.gl/JpieX23fPKirAgXK7)")

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# WHATSAPP BUTTON
# -----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📞 Contact")

phone_number = "919999999999"  # CHANGE THIS
message = "Hi, I am interested in your 1BHK property."

st.markdown(f"""
<a href="https://wa.me/{phone_number}?text={message}" target="_blank">
<button style="background-color:#25D366;color:white;padding:10px 20px;border:none;border-radius:8px;">
💬 WhatsApp Now
</button>
</a>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# LEAD FORM + CSV SAVE
# -----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📝 Enquiry Form")

with st.form("lead_form"):
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    msg = st.text_area("Message")

    submit = st.form_submit_button("Submit")

    if submit:
        if name and phone:
            data = {
                "Name": name,
                "Phone": phone,
                "Message": msg,
                "Time": datetime.now()
            }

            df = pd.DataFrame([data])

            try:
                old = pd.read_csv("leads.csv")
                df = pd.concat([old, df], ignore_index=True)
            except:
                pass

            df.to_csv("leads.csv", index=False)

            st.success("✅ Lead saved successfully!")
        else:
            st.error("Please fill required fields")

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# DOWNLOAD BROCHURE
# -----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📄 Download Details")

text = """
1BHK for Sale | 550 sqft | ₹35L
Mohan Highlands Society
Parking + Lift
Near Gurukul School
Near Upcoming Panvel Highway
"""

st.download_button("Download Brochure", text, file_name="property.txt")

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
<center>
<small>Premium Property Listing App | Built with Streamlit</small>
</center>
""", unsafe_allow_html=True)