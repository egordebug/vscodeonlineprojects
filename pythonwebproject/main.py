import webview
import os
import subprocess

def run():
    out = subprocess.check_output("ls", shell=True, text=True)
    return out

if __name__ == "__main__":
    file_path = os.path.abspath("web/index.html")
    api = Api()
    window = webview.create_window("web", file_path, js_api=api)
    webview.start()
    main()
