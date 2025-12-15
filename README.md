# 🌍 Aid Gap Analyzer

**Snowflake Native App for NGOs to collaboratively measure and reduce last-mile aid gaps using privacy-preserving data clean rooms**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io)

## 🎯 Problem Statement

Many NGOs, government departments, and social enterprises work on the same populations and regions, but their data is siloed due to privacy, compliance, and trust barriers. This leads to:

- **Aid over-served in some areas and under-served in others** - decisions made from incomplete data
- Smaller organizations cannot benefit from richer data and analytics of larger partners
- Teams spend limited time on reports instead of acting on insights in the field

## 💡 Solution

Aid Gap Analyzer is a **Streamlit-based prototype** demonstrating how NGOs can:

1. **Securely pool operational data** (deliveries, beneficiaries, stock levels, geolocation)
2. **Run AI models on combined datasets** without exposing raw, identified data
3. **Identify last-mile service gaps** through geospatial analysis and time-series modeling
4. **Make data-driven decisions** to reduce inequity in aid distribution

The prototype simulates the core concept that would be deployed as a **Snowflake Native App** using:
- Snowflake Data Clean Rooms
- Differential Privacy Policies
- Snowpark for ML workloads
- Native Apps Framework for marketplace distribution

## ✨ Features

- 📊 **Interactive Dashboard** - Visualize aid distribution patterns across regions
- 🗺️ **Geospatial Gap Map** - Identify underserved areas through heatmaps
- 📈 **Trend Analysis** - Time-series view of aid delivery vs demand
- 🤖 **AI-Powered Insights** - Automated gap detection using ML models
- 🔒 **Privacy-First Design** - Demonstrates clean room concepts
- 📱 **Field Worker Interface** - Simulated mobile data collection

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│         Streamlit Web Application           │
│  (Prototype of Snowflake Native App UI)    │
└────────────┬───────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────┐
│     Simulated Data Clean Room Layer         │
│  (Would use Snowflake Data Clean Rooms)    │
└────────────┬───────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────────┐
│    AI/ML Models (Pandas + NumPy + Plotly)   │
│   (Would use Snowpark ML in production)     │
└──────────────────────────────────────────────┘
```

## 🛠️ Technology Stack

**Current Prototype:**
- **Python 3.8+** - Core programming language
- **Streamlit** - Interactive web application framework
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Plotly** - Interactive visualizations
- **Folium** - Geospatial mapping

**Production Vision (Snowflake Native App):**
- Snowflake AI Data Cloud
- Snowflake Native Apps Framework
- Snowflake Data Clean Rooms
- Snowpark / Snowpark Container Services
- Differential Privacy Policies

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/chakreshkatari/aid-gap-analyzer.git
cd aid-gap-analyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser to `http://localhost:8501`

## 📦 Project Structure

```
aid-gap-analyzer/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── LICENSE               # MIT License
│
├── data/                 # Sample datasets
│   ├── organizations.csv # Simulated NGO data
│   └── deliveries.csv    # Simulated delivery records
│
├── models/               # ML model implementations
│   ├── gap_detector.py   # Gap detection algorithm
│   └── forecasting.py    # Demand forecasting
│
└── utils/                # Utility functions
    ├── data_gen.py       # Synthetic data generation
    └── viz.py            # Visualization helpers
```

## 📊 Sample Data

The prototype includes synthetic data representing:
- 5 fictional NGO organizations
- 1000+ delivery records across 20 regions
- Geolocation data for mapping
- Time-series data for trend analysis

## 🎥 Demo

[Link to demo video will be added]

## 🌟 Key Differentiators

1. **Privacy-First Collaboration** - Built on clean room principles
2. **Snowflake Native** - Leverages enterprise-grade data platform
3. **AI-Powered** - Automated gap detection, not manual reporting
4. **Field-Ready** - Designed for offline-first field workers
5. **Scalable** - Can expand to multiple countries/partners

## 📈 Impact Metrics

If deployed across a network of NGOs:
- Reduce last-mile aid gaps by identifying underserved micro-regions
- Improve equity by giving all partners the same aggregate insights
- Enable rapid scaling through Snowflake Marketplace
- Measure long-term reduction in service gaps as quantitative KPI

## 🔮 Future Enhancements

- [ ] Real Snowflake integration
- [ ] Mobile app for field workers
- [ ] Integration with external data (climate, satellite imagery)
- [ ] Advanced ML models (LLMs for beneficiary feedback analysis)
- [ ] Multi-language support
- [ ] API for third-party integrations

## 🤝 Contributing

This is a hackathon prototype. Contributions welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Team

Developed for the **AI for Good Hackathon 2024**

## 🙏 Acknowledgments

- Snowflake for the Native Apps Framework
- Streamlit for the amazing web framework
- All NGOs working tirelessly to close aid gaps worldwide

## 📧 Contact

For questions or collaboration opportunities, please open an issue on GitHub.

---

**Built with ❤️ for social impact**
