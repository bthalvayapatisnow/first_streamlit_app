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
streamlit.dataframe(my_fruit_list)

