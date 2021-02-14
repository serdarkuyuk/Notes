# CLI applicaiton
heroku login

heroku create your-app-name --buildpack heroku/python

git clone remote-repo-url

pip install pipreqs

run pipreqs

touch setup.sh
put
```
mkdir -p ~/.streamlit

echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
```

Procfile
web: sh setup.sh && streamlit run your-script.py

create runtime.txt file
put
```
python-3.9.0
```

git add .
git commit -m "message"
git push heroku master



# Manual application

goto heroku open new app...
then github linked
manually deploy..






```python
import os
import base64
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

st.markdown(get_binary_file_downloader_html('photo.jpg', 'Picture'), unsafe_allow_html=True)
st.markdown(get_binary_file_downloader_html('data.csv', 'My Data'), unsafe_allow_html=True)
st.markdown(get_binary_file_downloader_html('2g1c.mp4', 'Video'), unsafe_allow_html=True)
```

# Pandas Profiling in Streamlit
pip install streamlit-pandas-profiling
```python
import pandas as pd
import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
pr = df.profile_report()

st.title("Pandas Profiling in Streamlit")
st.write(df)
st_profile_report(pr)
```
