# IBLIS - Ideal Battery Life Indicator Script

Basically serves you reminders to plug in your laptop when it's at 40% charge capacity and unplug it when it reaches 80%. This habit can help extend the longevity and charge capacity of your laptop.

## Pre-requisites

You need Python 3 installed on your machine.

## Setup

Clone this repository (or download it as a zip and extract it to a directory).
Within this directory, execute

```bash
pip install -r requirements.txt
```

## Usage

To test out the script, open your command line interface and run

```bash
pythonw indicator.pyw
```

To run it as a background process at startup,

1. Create a shortcut to the batch file.
2. Once the shortcut is created, right-click the shortcut file and select Cut.
3. Open the Run command window using <kbd>Ctrl</kbd>+<kbd>R</kbd>, and type ```shell:startup``` to open the Startup folder.
4. Once the Startup folder is opened, click the Home tab at the top of the folder and select Paste to paste the shortcut file into the Startup folder.
