import streamlit;
import pandas;

streamlit.title('I love Labrodar dogs')

streamlit.header('Available dog breeds')
streamlit.text('We love puppies')
streamlit.text('Dogs eat lot of food')
streamlit.text('We have to take them out periodically')

streamlit.title('🥣 🥗 🐔 🥑🍞 adding emojis')

streamlit.header('🥣 🥗 🐔 🥑🍞 adding emojis')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Add user to pick the friuts they want in the smoothies
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

#Display the table on the page
streamlit.dataframe(my_fruit_list)

