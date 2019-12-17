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

<h4>Installation Instructions for opencv</h4>
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

<h4>Installation Instructions for crazyflie</h4>
<h5>pynput<h/5>
  <code>pip3 install pynput</code>
<h5>cflib<h/5>
  <code>pip3 install cflib</code>
                              
                              
<h3>Use Example</h3>
<code>python3 image_collector.py</code>
<p>This program opens a video stream from a camera plugged into PC's USB port 1 (just guess and check if feed is blank initially). It discretely and quickly updates environment.png in the same directory.</p>
<code>python3 qr_scanner_image -i environment.png</code>
<p>Repeatedly checks environment.png for updates. Scans image for QR codes, decodes them, and stores relevant data in vector.txt.</p>
<p>The image collector needs to be running when you call the scanner. Both should run continuously throughout the demonstration, and should not exit on their own.</p>

<code>python3 autonomous_sequence_high_level.py</code>
<p>Running this program will result in:
   <p> 1) Drone takeoff to <code>HEIGHT</code> </p>
   <p> 2) Read the surveillance drone and adversary drone position from a text file and appropriately give the surveillance drone           trajectory </p>
   <p> 3) Land the drone </p>
</p>
