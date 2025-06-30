import streamlit as st
import requests

API_BASE = "http://127.0.0.1:8000"

st.set_page_config(page_title="Automation Dashboard", layout="wide")
st.title("🧪 Process Automation Dashboard")


col1, col2 = st.columns(2)


with col1:
    st.subheader("➕ Log New Test Result")
    with st.form("log_form"):
        module_name = st.text_input("Module Name")
        status = st.selectbox("Status", ["pass", "fail"])
        submitted = st.form_submit_button("Submit")
        if submitted:
            res = requests.post(f"{API_BASE}/log_test_result", json={
                "module_name": module_name,
                "status": status
            })
            if res.status_code == 200:
                st.success(f"✅ Logged (ID: {res.json()['id']})")
            else:
                st.error("Failed to log test result")

    st.subheader("📊 Summary Stats")
    try:
        summary = requests.get(f"{API_BASE}/get_summary").json()
        col_pass, col_fail = st.columns(2)
        col_pass.metric("✅ Passed", summary["passed"])
        col_fail.metric("❌ Failed", summary["failed"])
        st.metric("🧪 Total Tests", summary["total"])
    except:
        st.warning("API is not running")


with col2:
    st.subheader("📋 All Test Results")
    try:
        data = requests.get(f"{API_BASE}/get_all_results").json()["results"]
        if data:
            st.dataframe(
                data,
                column_config={
                    0: "ID",
                    1: "Module Name",
                    2: "Status",
                    3: "Timestamp"
                },
                use_container_width=True
            )
        else:
            st.info("No results found.")
    except:
        st.warning("API is not available")

    st.subheader("🔁 Update Test Result")
    with st.form("update_form"):
        test_id = st.number_input("Test ID", min_value=1, step=1)
        new_status = st.selectbox("New Status", ["pass", "fail"])
        update = st.form_submit_button("Update")
        if update:
            res = requests.put(f"{API_BASE}/update_test_status/{test_id}", json={"status": new_status})
            if res.status_code == 200:
                st.success("✅ Status updated!")
            else:
                st.error("Update failed. Check the ID.")
