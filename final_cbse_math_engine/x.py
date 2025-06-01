import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Graph of y = √x")

# Generate values
x = np.linspace(0, 10, 100)
y = np.sqrt(x)

# Create plot
fig, ax = plt.subplots()
ax.plot(x, y, label='y = √x')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Plot of y = √x')
ax.legend()
ax.grid(True)

# Show in browser
st.pyplot(fig)

