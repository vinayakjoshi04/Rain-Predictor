# 🌧️ Rainfall Prediction System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![XGBoost](https://img.shields.io/badge/XGBoost-Latest-orange.svg)](https://xgboost.readthedocs.io/)

> A sophisticated machine learning web application that predicts daily rainfall probability using advanced weather parameters and XGBoost algorithm.

![Uploading image.png…]()


## 🎯 Overview

This project implements a robust rainfall prediction system that combines meteorological data analysis with machine learning to forecast whether it will rain on a given day. The system achieves **82.43% accuracy** using XGBoost classification and provides predictions through an intuitive web interface.

## ✨ Key Features

- 🤖 **Machine Learning Powered** - Utilizes XGBoost algorithm for high-accuracy predictions
- 🌐 **Web Interface** - Clean, responsive HTML form for easy interaction
- 📊 **Real-time Predictions** - Instant rainfall probability based on weather inputs
- 🎯 **High Accuracy** - Achieves 83.37% testing accuracy
- 🔧 **Easy Deployment** - Ready for cloud deployment with minimal configuration
- 📱 **Responsive Design** - Works seamlessly across desktop and mobile devices

## 🏗️ Project Architecture

```
Rainfall-Prediction/
├── 📁 templates/
│   └── index.html              # Frontend interface
├── 📓 rainfall-predictor.ipynb # Model development notebook
├── 🤖 xgboost_rain_model.pkl   # Trained ML model
├── 🌐 app.py                   # Flask web application
├── 📋 requirements.txt         # Python dependencies
├── 📄 README.md               # Project documentation
```

## 🧠 Model Specifications

| Component | Details |
|-----------|---------|
| **Algorithm** | XGBoost Classifier |
| **Accuracy** | 83.37% on test dataset |
| **Training Data** | Historical weather patterns |
| **Validation** | Cross-validation with time-series split |

### 📊 Input Features

The model processes the following meteorological parameters:

- 🌡️ **Temperature Metrics**: Current, Maximum, Minimum temperatures
- 💨 **Atmospheric Pressure**: Barometric pressure readings
- 💧 **Humidity Levels**: Relative humidity percentage
- ☁️ **Cloud Coverage**: Cloud density measurements
- ☀️ **Sunshine Duration**: Hours of direct sunlight
- 🌪️ **Wind Parameters**: Speed and direction
- 💎 **Dew Point**: Temperature at which condensation occurs

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vinayakjoshi04/Rain-Predictor.git
   cd Rain-Predictor
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv rainfall_env
   
   # On Windows
   rainfall_env\Scripts\activate
   
   # On macOS/Linux
   source rainfall_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the application**
   ```bash
   python app.py
   ```

5. **Access the web interface**
   
   Open your browser and navigate to: `http://127.0.0.1:5000`

## 🔮 Usage Example

### Sample Input Data

```json
{
  "pressure": 1013.25,
  "temperature": 25.5,
  "max_temp": 28.0,
  "min_temp": 22.0,
  "dew_point": 18.5,
  "humidity": 75,
  "cloud_coverage": 60,
  "sunshine_hours": 6.5,
  "wind_speed": 12.3,
  "wind_direction": 180
}
```

### Expected Output

```json
{
  "prediction": "Rain Expected",
  "confidence": 0.76,
  "weather_summary": "High probability of rainfall based on current conditions"
}
```

## 📈 Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 83.37% |
| Precision | 81.2% |
| Recall | 78.9% |
| F1-Score | 80.0% |
| AUC-ROC | 0.85 |

## 🌐 Deployment Options

### Option 1: Render (Recommended)

1. Push your code to GitHub
2. Create a new Web Service on [Render](https://render.com)
3. Connect your GitHub repository
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn app:app`

### Option 2: Heroku

1. Install Heroku CLI
2. Create a `Procfile` with: `web: gunicorn app:app`
3. Deploy using:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Option 3: Docker

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["python", "app.py"]
```

## 🛠️ Development

### Setting Up Development Environment

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Format code
black app.py

# Lint code
flake8 app.py
```

### Contributing Guidelines

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Run the test suite: `pytest`
5. Submit a pull request

## 🔄 Future Enhancements

- [ ] **Rainfall Amount Prediction** - Implement regression model for precipitation quantity
- [ ] **Real-time Weather API Integration** - Automatic data fetching from weather services
- [ ] **Mobile Application** - React Native or Flutter mobile app
- [ ] **Advanced Visualizations** - Interactive charts and weather maps
- [ ] **Multi-location Support** - Predictions for multiple geographical areas
- [ ] **Ensemble Methods** - Combine multiple ML algorithms for better accuracy
- [ ] **Time Series Forecasting** - Extended forecast periods (7-day, 14-day)

## 📊 Technology Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?style=for-the-badge&logo=xgboost&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 👨‍💻 Author

**Vinayak Joshi**
- GitHub: [@vinayakjoshi04](https://github.com/vinayakjoshi04)

## 🙏 Acknowledgments

- Weather data providers for training datasets
- XGBoost community for the excellent ML library
- Flask team for the lightweight web framework
- Open source community for continuous inspiration

## 📧 Support

If you have any questions or run into issues, please open an issue on GitHub or contact me directly.

---

⭐ **Star this repository if you found it helpful!**

Made with ❤️ by [Vinayak Joshi](https://github.com/vinayakjoshi04)
