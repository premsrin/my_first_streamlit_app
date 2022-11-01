import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd


st.header('Name: Premnath Srinivasan')
st.header('Homework 1')

st.markdown("**QUESTION 1**:")
x_limit = 100
# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(x_limit)
# Create a random array of data that we will use for our y values
y_data = abs(np.random.randn(100))  
df = pd.DataFrame({'x': x_axis,
                   'y': y_data})
st.write(df)

st.markdown("**QUESTION 2**:")
scatter = alt.Chart(df).mark_point().encode(x='x', y='y')
st.altair_chart(scatter, use_container_width=True)


st.markdown("**QUESTION 3**:")
st.write("The 5 changes I made were:")
st.markdown("- A scatter plot with filled circles.")
st.markdown("- Changed the property 'size' to match the x value")
st.markdown("- Changed the property 'color' to match the y value")
st.markdown("- Added tooltip to give values of x and y")
st.markdown("- Made the chart interactive so that we can zoom in and out")

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    padding-left:40px;
}
</style>
''', unsafe_allow_html=True)

scatter = alt.Chart(df).mark_circle().encode(x='x', y='y', size='x', color = 'y', 
tooltip=['x','y'] ).interactive()
st.altair_chart(scatter, use_container_width=True)

st.markdown("**QUESTION 4**:")
#cars = data.cars()
#st.write(data.cars.url)
cars = pd.read_json('cars.json')

st.write(cars)
st.write("Original Car chart - Horsepower vs MilesPerGallon")
carscatter = alt.Chart(cars).mark_circle(size=60).encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color='Origin'
)
st.altair_chart(carscatter, use_container_width=True)

st.write("The 2 changes I made were:")
st.markdown("- Made the chart interactive so that we can zoom in and out. Added tool tip")
st.markdown("- Added multi selection Legend so that we can select 'origin' country from the legend.  Once selected, the main scatter plot will be updated")

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    padding-left:40px;
}
</style>
''', unsafe_allow_html=True)

selection = alt.selection_multi(fields=['Origin', 'Cylinders'])
color = alt.condition(selection,
                      alt.Color('Origin:N', legend=None),
                      alt.value('lightgray'))

scatter = alt.Chart(cars).mark_circle().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=color,
    tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).interactive()

legend = alt.Chart(cars).mark_rect().encode(
    y=alt.Y('Origin:N', axis=alt.Axis(orient='right')),
    x='Cylinders:O',
    color=color
).add_selection(
    selection
)

scatter | legend
