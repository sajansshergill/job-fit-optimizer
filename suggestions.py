# suggestions.py

# Predefined dictionary mapping skills to suggested portfolio projects
project_ideas = {
    "machine learning": "Build a model to predict house prices using scikit-learn and regression techniques.",
    "a/b testing": "Run simulated A/B testing on website conversion rates using Python and statsmodels.",
    "customer segmentation": "Use K-Means clustering on e-commerce customer data to segment user personas.",
    "sql": "Analyze sales and inventory trends using SQL queries on a sample retail dataset.",
    "tableau": "Create an interactive dashboard showing product performance across regions.",
    "data visualization": "Build a visual analytics dashboard in Streamlit using COVID-19 data.",
    "nlp": "Create a sentiment analysis model for product reviews using NLTK or spaCy.",
    "deep learning": "Build an image classifier with TensorFlow or PyTorch using CIFAR-10.",
    "time series": "Forecast monthly energy consumption using Facebook Prophet or ARIMA.",
    "python": "Build a web scraper using BeautifulSoup and display results in a dashboard.",
    "excel": "Perform profitability and cost analysis using pivot tables and Excel formulas.",
}

def suggest_projects(missing_skills):
    """
    Takes a list of missing skills and returns personalized project ideas.
    """
    suggestions = []

    for skill in missing_skills:
        skill_lower = skill.lower()
        for key in project_ideas:
            if key in skill_lower:
                suggestions.append((skill, project_ideas[key]))
                break

    return suggestions
