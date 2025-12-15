import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page config
st.set_page_config(
    page_title="Aid Gap Analyzer",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {font-size: 3rem; font-weight: bold; color: #1f77b4; margin-bottom: 1rem;}
    .sub-header {font-size: 1.5rem; color: #555; margin-bottom: 2rem;}
    .metric-card {background-color: #f0f2f6; padding: 1rem; border-radius: 0.5rem; margin: 0.5rem 0;}
</style>
""", unsafe_allow_html=True)

# Generate synthetic data
@st.cache_data
def generate_data():
    np.random.seed(42)
    regions = ['North', 'South', 'East', 'West', 'Central']
    organizations = ['Red Cross', 'UN WFP', 'Care International', 'Oxfam', 'Local NGO Network']
    
    # Generate delivery data
    n_records = 500
    data = {
        'date': [datetime.now() - timedelta(days=np.random.randint(0, 90)) for _ in range(n_records)],
        'region': np.random.choice(regions, n_records),
        'organization': np.random.choice(organizations, n_records),
        'deliveries': np.random.randint(10, 200, n_records),
        'beneficiaries': np.random.randint(50, 1000, n_records),
        'gap_score': np.random.uniform(0, 100, n_records)
    }
    df = pd.DataFrame(data)
    
    # Calculate regional statistics
    regional_stats = df.groupby('region').agg({
        'deliveries': 'sum',
        'beneficiaries': 'sum',
        'gap_score': 'mean'
    }).reset_index()
    
    return df, regional_stats

df, regional_stats = generate_data()

# Header
st.markdown('<div class="main-header">🌍 Aid Gap Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Privacy-Preserving Collaborative Analytics for NGOs</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/150x50/1f77b4/ffffff?text=Snowflake+Native+App", use_column_width=True)
    st.markdown("---")
    st.markdown("### Filters")
    
    selected_regions = st.multiselect(
        "Select Regions",
        options=df['region'].unique(),
        default=df['region'].unique()
    )
    
    selected_orgs = st.multiselect(
        "Select Organizations",
        options=df['organization'].unique(),
        default=df['organization'].unique()
    )
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("""
    This prototype demonstrates a **Snowflake Native App** for NGOs to:
    - Securely pool operational data
    - Identify last-mile aid gaps
    - Make data-driven decisions
    
    **Built with:**
    - Streamlit
    - Plotly
    - Pandas/NumPy
    """)

# Filter data
filtered_df = df[
    (df['region'].isin(selected_regions)) & 
    (df['organization'].isin(selected_orgs))
]

# Key Metrics
st.markdown("### 📊 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Deliveries",
        f"{filtered_df['deliveries'].sum():,}",
        delta=f"+{np.random.randint(5, 15)}%"
    )

with col2:
    st.metric(
        "Beneficiaries Reached",
        f"{filtered_df['beneficiaries'].sum():,}",
        delta=f"+{np.random.randint(8, 20)}%"
    )

with col3:
    st.metric(
        "Avg Gap Score",
        f"{filtered_df['gap_score'].mean():.1f}",
        delta=f"-{np.random.randint(3, 10)}%",
        delta_color="inverse"
    )

with col4:
    st.metric(
        "Active Organizations",
        len(selected_orgs),
        delta="Collaborating"
    )

st.markdown("---")

# Two column layout
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown("### 🗺️ Regional Aid Distribution")
    
    # Regional bar chart
    regional_filtered = filtered_df.groupby('region').agg({
        'deliveries': 'sum',
        'beneficiaries': 'sum'
    }).reset_index()
    
    fig_regional = go.Figure()
    fig_regional.add_trace(go.Bar(
        x=regional_filtered['region'],
        y=regional_filtered['deliveries'],
        name='Deliveries',
        marker_color='#1f77b4'
    ))
    fig_regional.add_trace(go.Bar(
        x=regional_filtered['region'],
        y=regional_filtered['beneficiaries'],
        name='Beneficiaries',
        marker_color='#ff7f0e',
        yaxis='y2'
    ))
    
    fig_regional.update_layout(
        yaxis=dict(title='Deliveries'),
        yaxis2=dict(title='Beneficiaries', overlaying='y', side='right'),
        hovermode='x unified',
        height=400
    )
    
    st.plotly_chart(fig_regional, use_container_width=True)

with col_right:
    st.markdown("### ⚠️ Gap Severity")
    
    # Gap scores by region
    gap_by_region = filtered_df.groupby('region')['gap_score'].mean().sort_values(ascending=False)
    
    fig_gap = go.Figure(go.Bar(
        x=gap_by_region.values,
        y=gap_by_region.index,
        orientation='h',
        marker_color=gap_by_region.values,
        marker_colorscale='Reds',
        text=[f"{v:.1f}" for v in gap_by_region.values],
        textposition='outside'
    ))
    fig_gap.update_layout(
        xaxis_title="Gap Score",
        yaxis_title="Region",
        height=400,
        showlegend=False
    )
    
    st.plotly_chart(fig_gap, use_container_width=True)

st.markdown("---")

# Time series
st.markdown("### 📈 Delivery Trends Over Time")

time_series = filtered_df.groupby(filtered_df['date'].dt.date)['deliveries'].sum().reset_index()
time_series.columns = ['date', 'deliveries']

fig_time = px.line(
    time_series,
    x='date',
    y='deliveries',
    title='Daily Deliveries',
    markers=True
)
fig_time.update_layout(height=300)
st.plotly_chart(fig_time, use_container_width=True)

# Organization breakdown
st.markdown("### 🤝 Organization Contributions")

col1, col2 = st.columns(2)

with col1:
    org_deliveries = filtered_df.groupby('organization')['deliveries'].sum().sort_values(ascending=False)
    
    fig_org = px.pie(
        values=org_deliveries.values,
        names=org_deliveries.index,
        title='Deliveries by Organization'
    )
    st.plotly_chart(fig_org, use_container_width=True)

with col2:
    org_beneficiaries = filtered_df.groupby('organization')['beneficiaries'].sum().sort_values(ascending=False)
    
    fig_ben = px.pie(
        values=org_beneficiaries.values,
        names=org_beneficiaries.index,
        title='Beneficiaries by Organization'
    )
    st.plotly_chart(fig_ben, use_container_width=True)

# Data table
st.markdown("---")
st.markdown("### 📄 Recent Delivery Records")
st.dataframe(
    filtered_df.sort_values('date', ascending=False).head(10)[[
        'date', 'region', 'organization', 'deliveries', 'beneficiaries', 'gap_score'
    ]],
    use_container_width=True
)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888;'>
    <p><strong>Aid Gap Analyzer</strong> - Powered by Snowflake Native Apps Framework</p>
    <p>Built with ❤️ for the AI for Good Hackathon 2024</p>
</div>
""", unsafe_allow_html=True)
