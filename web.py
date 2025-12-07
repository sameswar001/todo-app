import streamlit as st
from  modules import reusableFuncs as rf

todos = rf.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    rf.write_todos(todos)



st.title("Task Manager App")
st.subheader("Manage Your Tasks Efficiently")
st.write("Welcome to the Task Manager App! Here you can manage your tasks efficiently.")
for i, todo in enumerate(todos):
   checkbox =  st.checkbox(todo, key =f"todo_{i}")
   if checkbox:
        todos.pop(i)
        rf.write_todos(todos)
        del st.session_state[f"todo_{i}"]
        st.rerun()

st.text_input(label="", placeholder="Add a new todo...", key="new_todo",
              on_change=add_todo)

st.session_state
