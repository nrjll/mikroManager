import streamlit as st
import paramiko as pmk

st.title("Page 1")

col1, col2 = st.columns(2)
with col1:
    hostname = st.text_input("Input IP Address")
    username = st.text_input("Input Username")
with col2:
    port = st.text_input("Input Port", value="22")
    password = st.text_input("Input Password", type="password")

def connect_to_ssh(hostname, port, username, password):
    try:
        client = pmk.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(pmk.AutoAddPolicy)
        client.connect(hostname, port=int(port), username=username, password=password)
        stdin, stdout, stderr = client.exec_command("ip address print")
        output = stdout.read().decode()
        error = stderr.read().decode()
        client.close()
        if output:
            st.success("Koneksi Terhubung")
            st.text_area("Hasil", output)
        if error:
            st.error("Koneksi Gagal")
            st.text_area("Hasil", error)
    except Exception as e:
        st.error(f"Koneksi Gagal: {e}")

if st.button("connect"):
    if hostname and port and username and password:
        connect_to_ssh(hostname, port, username, password)
    else:
        st.warning("error")



