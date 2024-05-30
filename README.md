 <h1>Real-time Barcode Detection with Flask and YOLO</h1>

  <p>This project utilizes Flask, OpenCV, and YOLO (You Only Look Once) to implement real-time barcode detection from a live camera feed. The application continuously processes frames from the camera, detecting and annotating barcodes in the video stream.</p>

  <h2>Key Features:</h2>
  <ul>
    <li><strong>Real-time Detection:</strong> Detects barcodes in real-time from a live camera feed.</li>
    <li><strong>Bounding Box Annotation:</strong> Draws bounding boxes around detected barcodes for easy visualization.</li>
    <li><strong>Total Count Display:</strong> Displays the total count of detected barcodes on the video stream.</li>
    <li><strong>Web Interface:</strong> Provides a web interface for starting and stopping the barcode detection process.</li>
  </ul>

  <h2>Dependencies:</h2>
  <ul>
    <li>Flask: Lightweight web framework for Python.</li>
    <li>OpenCV: Open Source Computer Vision Library for image processing tasks.</li>
    <li>Ultralytics YOLO: State-of-the-art object detection model for real-time detection tasks.</li>
  </ul>

  <h2>Installation:</h2>
  <ol>
    <li>Clone the repository:
      <pre><code>git clone https://github.com/yourusername/your-repository.git</code></pre></li>
    <li>Navigate to the project directory:
      <pre><code>cd your-repository</code></li></pre>
    <li>Install dependencies using pip:
      <pre><code>pip install -r requirements.txt</code></li></pre>
  </ol>

  <h2>Running the Application:</h2>
  <ol>
    <li>Run the Flask application:
      <pre><code>python app.py</code></pre></li>
    <li>Open a web browser and navigate to <pre><code>http://localhost:5000</code></pre> to access the application.</li>
    <li>Click on the "Start Detection" button to begin barcode detection from the live camera feed.</li>
    <li>To stop detection, click on the "Stop Detection" button.</li>
  </ol>

  <p>Make sure to replace <code>yourusername</code> and <code>your-repository</code> with your GitHub username and repository name, respectively. Additionally, ensure that you have Python installed on your system and that the necessary dependencies are installed using the provided <code>requirements.txt</code> file.</p>
  For installung the Dependencies
  <pre><code>pip install -r requirements.txt</code></pre>

  <h2>Contributions:</h2>
  <p>Contributions are welcome! If you have suggestions for improvements, bug fixes, or additional features, feel free to open an issue or create a pull request.</p>

