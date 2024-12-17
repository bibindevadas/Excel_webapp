# Survey Results Dashboard 2023

This project is an interactive **Streamlit app** that visualizes survey results from an Excel file. It allows users to filter data dynamically, explore visualizations, and display results for analysis.

---

## **Table of Contents**
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Requirements](#requirements)
4. [Folder Structure](#folder-structure)
5. [Setup and Installation](#setup-and-installation)
6. [How to Run the App](#how-to-run-the-app)
7. [Acknowledgments](#acknowledgments)

---

## **Features**

- Interactive **bar charts** to visualize survey ratings.  
- **Pie charts** to show the number of participants per department.  
- Dynamic filters for:
   - Age Range
   - Departments  
- Displays filtered data in a table for easy reference.  
- Excel file (`Survey_Results.xlsx`) as a data source.  

---

## **Technologies Used**

- **Python 3.x**  
- **Streamlit**: For building the interactive web app.  
- **Pandas**: For reading and manipulating the Excel data.  
- **Plotly**: For creating interactive visualizations.  
- **Pillow**: For displaying images.  

---

## **Requirements**

Ensure you have the following installed:

- Python 3.x  
- Streamlit  
- Pandas  
- Plotly  
- Pillow  
- OpenPyXL  

You can install the required libraries using:
```
bash
pip install streamlit pandas plotly pillow openpyxl
```

## **Folder Structure**

Your project folder should look like this:
```
/Survey_App
    ├── survey_app.py           # The main Streamlit script
    ├── Survey_Results.xlsx     # Excel file with survey data
    └── images/
        └── survey.jpg          # Image displayed in the app
```

## **Setup and Installation**

1. Clone the repository to your local machine:

```
git clone https://github.com/your-username/survey-app.git
cd survey-app
```

2. Install the dependencies:

```
pip install streamlit pandas plotly pillow openpyxl
```

3. Ensure your Excel file (Survey_Results.xlsx) and the image file (survey.jpg) are in the correct folders.


## **How to Run the App**

1. Open the terminal or command prompt.

2. Navigate to your project folder:

```
  cd path/to/survey-app
```

3. Run the Streamlit app:

```
streamlit run survey_app.py
```

4. The app will open in your browser at:

  ```
  http://localhost:8501
```

## **Acknowledgments**

1. Streamlit: For creating interactive dashboards.
2. Pandas & Plotly: For data processing and visualizations.
