# EECS149-Final-Project
TANDEM- Tactical Anti-Stealth Necessary Drone Evasive Maneuvers

<h3>Localization Dependencies</h3>
<ul type="square">
  <li>python 3.x</li>
          <li>imutils</li>
          <li>OpenCV</li>
          <li>numpy</li>
          <li>pyzbar</li>
</ul>

<h4>Installation Instructions</h4>
<h5>imutils</h5>
<code>pip3 install imutils</code>
<h5>OpenCV</h5>
<code>cd ~/work_dir;
  git clone https://github.com/opencv/opencv.git
</code>
<code>
mkdir build;
cd build
</code>
<code>make -j7</code>

<code>sudo make install</code>
<h5>numpy</h5>
<code>pip3 install numpy</code>
<h5>pyzbar</h5>
<code>pip3 install pyzbar</code>


<h3>Use Example</h3>
<code>python3 localizer.py</code>
<p>This will open a video stream on USB port 1 (if feed is blank, try moving camera to different port), scan individual frames for QR codes, decode them, and finally process and write the relevant data to vector.txt. It should run continuously unless interrupted with ctrl-C on the CLI or by pressing q inside the video stream display.</p>
