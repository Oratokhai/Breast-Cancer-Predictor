# breast-cancer-streamlit
This is a Streamlit web application I built as a project I undertook during my time in Covenant University in a course CSC 442 taught beautifully by the delectable Dr Dami Osufoye.
This application predicts the likelihood of breast cancer using machine learning, built with a trained classification model and designed for easy use by medical practitioners, researchers and anyone interested in early detection insights

 [Live App](https://breast-cancer-predictor-oratokhai.streamlit.app/)

# Features
- Simple and intuitive interface
- Real-time prediction based on user input
- Powered by scikit-learn and Streamlit
- Easily deployable on Streamlit Cloud

# Tech Stack
- Python
- Scikit-learn
- Streamlit
- Pandas

## How to Use
1. Go to the live app.
2. Input the tumor features.
3. Hit "Predict" and see the result!

## Tumor features
- radius_mean: Directly reflects the average size of the cell nuclei. Malignant tumors often have larger, more irregular nuclei.
- texture_mean: Indicates the variation in gray-scale intensity—basically the "roughness" of the tumor. Malignant tumors usually show higher texture variation.
- perimeter_mean: Strongly correlated with radius and area, this captures the shape irregularity of tumors.
- area_mean: One of the most predictive features in the dataset. Malignant tumors tend to cover more area due to uncontrolled growth.
- smoothness_mean: Captures how jagged or smooth the tumor edges are. Benign tumors tend to be smoother, while malignant ones appear rougher

## Preview
![screenshot](breastcancerscreenshor.png)
