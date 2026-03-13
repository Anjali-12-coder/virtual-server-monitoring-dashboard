import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Virtual Server Monitoring Dashboard",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>

.main-title{
text-align:center;
font-size:60px;
font-weight:900;
margin-bottom:40px;
}

.section-title{
text-align:center;
font-size:36px;
font-weight:800;
margin-top:35px;
margin-bottom:25px;
}

.kpi-card{
background-color:#f4f6f8;
padding:30px;
border-radius:12px;
text-align:center;
box-shadow:0px 4px 10px rgba(0,0,0,0.15);
}

.kpi-title{
font-size:30px;
font-weight:800;
margin-bottom:10px;
}

.kpi-value{
font-size:48px;
font-weight:900;
color:#2c3e50;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# DASHBOARD TITLE
# ---------------------------------------------------
st.markdown(
'<div class="main-title">Virtual Server Monitoring Dashboard</div>',
unsafe_allow_html=True
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
df = pd.read_csv("processed_server_logs.csv")

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------
st.markdown('<div class="section-title">Server Performance Overview</div>', unsafe_allow_html=True)

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(f"""
    <div class="kpi-card">
    <div class="kpi-title">Average CPU Utilization</div>
    <div class="kpi-value">{df['CPU_Utilization (%)'].mean():.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="kpi-card">
    <div class="kpi-title">Average Memory Usage</div>
    <div class="kpi-value">{df['Memory_Usage (%)'].mean():.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="kpi-card">
    <div class="kpi-title">Average Network Traffic</div>
    <div class="kpi-value">{df['Total_Network_Traffic'].mean():.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    uptime = df['Uptime (%)'].mean() if "Uptime (%)" in df.columns else 99.5

    st.markdown(f"""
    <div class="kpi-card">
    <div class="kpi-title">Average Uptime</div>
    <div class="kpi-value">{uptime:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# NETWORK TRAFFIC BY SERVER LOCATION (BAR CHART)
# ---------------------------------------------------
st.markdown('<div class="section-title">Network Traffic by Server Location</div>', unsafe_allow_html=True)

traffic = df.groupby("Server_Location")["Total_Network_Traffic"].mean().reset_index()

fig1 = px.bar(
    traffic,
    x="Server_Location",
    y="Total_Network_Traffic",
    color="Server_Location",
    text_auto=True,
    height=600
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------------------------------------------
# SECOND ROW
# ---------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    st.markdown('<div class="section-title">Average CPU Utilization by Location</div>', unsafe_allow_html=True)

    cpu = df.groupby("Server_Location")["CPU_Utilization (%)"].mean().reset_index()

    fig2 = px.bar(
        cpu,
        x="Server_Location",
        y="CPU_Utilization (%)",
        color="Server_Location",
        height=550
    )

    st.plotly_chart(fig2, use_container_width=True)

with col2:

    if "Instance_Size" in df.columns:

        st.markdown('<div class="section-title">Server Instance Size Distribution</div>', unsafe_allow_html=True)

        size = df["Instance_Size"].value_counts().reset_index()
        size.columns = ["Instance_Size", "Count"]

        fig3 = px.pie(
            size,
            names="Instance_Size",
            values="Count",
            hole=0.5,
            height=550
        )

        st.plotly_chart(fig3, use_container_width=True)

# ---------------------------------------------------
# THIRD ROW
# ---------------------------------------------------
col3, col4 = st.columns(2)

with col3:

    st.markdown('<div class="section-title">Average Memory Usage by OS Type</div>', unsafe_allow_html=True)

    memory = df.groupby("OS_Type")["Memory_Usage (%)"].mean().reset_index()

    fig4 = px.bar(
        memory,
        x="Memory_Usage (%)",
        y="OS_Type",
        orientation="h",
        color="OS_Type",
        height=550
    )

    st.plotly_chart(fig4, use_container_width=True)

with col4:

    st.markdown('<div class="section-title">CPU vs Memory Usage by Operating System</div>', unsafe_allow_html=True)

    fig5 = px.scatter(
        df,
        x="CPU_Utilization (%)",
        y="Memory_Usage (%)",
        color="OS_Type",
        height=550
    )

    st.plotly_chart(fig5, use_container_width=True)

# ---------------------------------------------------
# DATA TABLE CENTERED AT BOTTOM
# ---------------------------------------------------
# ---------------------------------------------------
# DATA TABLE CENTERED AT BOTTOM
# ---------------------------------------------------

st.markdown('<div class="section-title">Server Performance Dataset</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([3,6,3])

with col2:
    st.dataframe(df, use_container_width=True, height=400)