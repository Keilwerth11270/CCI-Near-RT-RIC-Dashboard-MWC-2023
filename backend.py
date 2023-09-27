from flask import Flask, jsonify, send_from_directory, redirect
from flask_cors import CORS
import subprocess
import os
import paramiko

app = Flask(__name__)
CORS(app)  # Allow requests from any origin for all routes

# Serve the index.html file, which redirects to other HTML files
@app.route('/', methods=['GET'])
def serve_frontend():
    return redirect('/index.html')

# Serve the other HTML files
@app.route('/<filename>', methods=['GET'])
def serve_html(filename):
    return send_from_directory(os.path.dirname(__file__), filename)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.dirname(__file__), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/getOnboarded', methods=['GET'])
def get_onboarded():
    try:
        # THIS IS THE COMMAND
        curl_process = subprocess.Popen(['dms_cli', 'get_charts_list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        # Capture the output of the command
        result, error = curl_process.communicate()

        # Check for errors in the command
        if curl_process.returncode != 0:
            return jsonify({'error': error}), 500

        return result, 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/getDeployed', methods=['GET'])
def get_deployed():
    try:
        # THIS IS THE COMMAND
        curl_process = subprocess.Popen(['kubectl', 'get', 'pods', '-A'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        # Capture the output of the command
        result, error = curl_process.communicate()

        # Check for errors in the command
        if curl_process.returncode != 0:
            return jsonify({'error': error}), 500

        return result, 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/getE2Nodes', methods=['GET'])
def get_e2nodes():
    try:
        # THIS IS THE COMMAND --THE URL MAY CHANGE, YOU CAN CHECK WITH: kubectl get pods -A -o wide | grep submgr
        curl_process = subprocess.Popen(['curl', '-X', 'GET', 'http://10.244.0.15:8080/ric/v1/get_all_e2nodes'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        # Capture the output of the command
        result, error = curl_process.communicate()

        # Check for errors
        if curl_process.returncode != 0:
            return jsonify({'error': error}), 500

        return result, 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/getxAppUE', methods=['GET'])
def get_xAppUE():
    try:
        # THIS IS THE COMMAND
        curl_process = subprocess.Popen(['curl', '-X', 'GET', 'http://10.244.0.15:8080/ric/v1/get_all_e2nodes'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        # Capture the output of the command
        result, error = curl_process.communicate()

        # Check for errors
        if curl_process.returncode != 0:
            return jsonify({'error': error}), 500

        return result, 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1555)



# @app.route('/getSchedulerData', methods=['GET'])
# def get_SchedulerData():
#     try:
#         # SSH connection parameters
#         ssh_host = '10.147.20.164'
#         ssh_port = 22  # Default SSH port
#         ssh_username = 'ccinrt'
#         ssh_password = 'coolpass'

#         # Create an SSH client
#         ssh_client = paramiko.SSHClient()
#         ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#         print("set up ssh client")


#         # Connect to the remote server
#         try:
#             ssh_client.connect(ssh_host, ssh_port, ssh_username, ssh_password)
#             print("SSH connection successful\n")  # Print a success message
#         except Exception as ssh_error:
#             print(f"SSH connection failed: {str(ssh_error)}\n")


#         # Define the commands as a list
#         commands = [
#             'ls',
#             'ls',
#             'ls'
#         ]

#         retval = ["returnvalue"]

#         print("commands: ")
#         print(commands)
#         print("\n")

#         for command in commands:
#             stdin, stdout, stderr = ssh_client.exec_command(command)
#             result = stdout.read().decode()
#             retval = result

#         # Close the SSH connection
#         ssh_client.close()

#         # Return the result
#         print("new return value:")
#         print(retval)
#         print("\n")

#         return result

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

