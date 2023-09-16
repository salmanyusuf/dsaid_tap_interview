import streamlit as st
from salary_dataset import data
import plotly.express as px

st.set_page_config(page_title="Data Visualisation", page_icon="📰", layout="wide")

st.title("💰 Poly Graduates Salary - Data Visualisation")
st.markdown("""---""")

st.markdown(
    """
    #### On this page, you can access key analytics from the salary dataset based on recent poly graduates in a specific course of study highly subsidised by the government.
    """
)
st.markdown("""---""")

st.markdown(
    """
    ## Key Metrics:
    """
)

salary_data = data
student_count = salary_data.groupby('Student Group')['Count'].sum().reset_index()
total_X_students = student_count.loc[student_count['Student Group'] == 'Student Group X']['Count'].values[0]
total_Y_students = student_count.loc[student_count['Student Group'] == 'Student Group Y']['Count'].values[0]
total_students = total_X_students + total_Y_students

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Students in Group X", value=total_X_students)

with col2:
    st.metric(label="Total Students in Group Y", value=total_Y_students)

with col3:
    st.metric(label="Total Students", value=total_students)

fig1= px.bar(salary_data, x="Industry", y="Count", color='Student Group', title="Student Count by Industry", barmode="group")
st.plotly_chart(fig1, use_container_width=True)
fig2= px.bar(salary_data, x="Job Nature", y="Count", color='Student Group', title="Student Count by Job Nature", barmode="group")
st.plotly_chart(fig2, use_container_width=True)

# Average median salary based on student group
avg_median_salary = data.groupby('Student Group')['Median Salary'].mean().reset_index()
avg_X_median_salary = round(avg_median_salary.loc[avg_median_salary['Student Group'] == 'Student Group X']['Median Salary'].values[0], 2)
avg_Y_median_salary = round(avg_median_salary.loc[avg_median_salary['Student Group'] == 'Student Group Y']['Median Salary'].values[0], 2)
total_avg_median_salary = round(avg_median_salary['Median Salary'].mean(), 2)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Average Median Salary of Students in Group X", value=avg_X_median_salary)

with col2:
    st.metric(label="Average Median Salary of Students in Group Y", value=avg_Y_median_salary)

with col3:
    st.metric(label="Average Median Salary across both Student Groups", value=total_avg_median_salary)

fig3 = px.line(salary_data, x="Industry", y="Median Salary", color='Student Group', hover_data='Count', symbol="Student Group")
st.plotly_chart(fig3, use_container_width=True)

st.markdown("""---""")

st.markdown(
    """
    ## Dataset:
    """
)

st.dataframe(salary_data, use_container_width=True)