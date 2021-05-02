import pandas as pd
import streamlit as st
import hfapi

client = hfapi.Client()
st.write("# Hi Dad \n## Use an asterisk (exactly one) and hit enter.")
user_string = st.text_input("begin sentence...")
output = client.fill_mask(user_string.replace("*", "[MASK]"))


try:
    df_tmp = pd.DataFrame(output)
    st.write(df_tmp[["sequence", "score"]])
except Exception:
    st.write("No results for you ;)")


#
#
# headers = {"Authorization": "Bearer api_WUSJemMQEeAlhglFlnivQWCcSxZgIPROdX"}
# API_URL = "https://api-inference.huggingface.co/models/bert-base-uncased"
#
#
# def query(payload):
#     data = json.dumps(payload)
#     response = requests.request("POST", API_URL, headers=headers, data=data)
#     return json.loads(response.content.decode("utf-8"))
#
# user_string = st.text_input("begin sentence...")
# data = query({"inputs": f"The answer to the universe was [MASK]."})

# data = query({"inputs": f"{user_string} [MASK]."})

