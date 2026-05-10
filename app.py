import os

# 告诉系统去运行真正的 webui.py，并指定 Hugging Face 必须的 7860 端口
os.system("streamlit run webui.py --server.port 7860 --server.address 0.0.0.0")
