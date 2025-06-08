https://developer.apple.com/forums/thread/669678
https://download.developer.apple.com/Developer_Tools/Xcode_10.1/Xcode_10.1.xip

sudo xcode-select --install 

# sudo apt update
# sudo apt install pandoc -y
# sudo apt install build-essential -y

dnf update
sudo dnf grouplist
sudo dnf group install "Development Tools"
cat /etc/yum.repos.d/google-chrome.repo
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch
enabled=1
gpgcheck=1
gpgkey=https://dl.google.com/linux/linux_signing_key.pub

sudo dnf install google-chrome-stable -y
google-chrome --version
Google Chrome 134.0.6998.88

# 1. Download the Google Chrome package
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb  #for 64-bit systems
#For 32-bit systems( less likely on bioinformatics tasks)
#wget https://dl.google.com/linux/direct/google-chrome-stable_current_i386.deb

# 2. Install the package (this will automatically configure the Google repository)
sudo apt install ./google-chrome-stable_current_amd64.deb #replace with the i386 file if required

# 3. Update your package lists to ensure everything is synchronized
sudo apt update

which google-chrome
google-chrome --version

export PATH="$PATH:/opt/google/chrome/"  # Or wherever `which google-chrome` points

sudo apt install python3.12-venv -y
python3 -m venv seleniumbase
cd seleniumbase
source bin/activate
# deactivate
pip install seleniumbase
pip install datasets huggingface_hub
google-chrome-stable --version
Google Chrome 134.0.6998.88
/home/sw7v6/py312/lib/python3.12/site-packages/seleniumbase/drivers/chromedriver --version
ChromeDriver 134.0.6998.88

/Users/sw7v6/git/tmp/py311/lib/python3.13/site-packages/seleniumbase/drivers/chromedriver --version
ChromeDriver 134.0.6998.88

conda create -n playwright python=3.12 -y
# conda create -n playwright python=3.11 -y
# conda remove --all -y --name playwright
conda activate playwright
pip install pytest-playwright
playwright install
playwright install-deps

# git clone https://github.com/seleniumbase/SeleniumBase.git
# cd SeleniumBase/
# pip install -e .
pip install seleniumbase

Example 0001.md:

# Chapter 1: The Beginning

This is the first paragraph of Chapter 1.

It continues with more text.

## Section 1.1:  An Interesting Detail

More details here.


python scrape_data.py data1.csv
cat 0*.md > book.md

pandoc -s --metadata title="ข้านี่แหละขันทีอันดับหนึ่งในใต้หล้า" -o "ข้านี่แหละขันทีอันดับหนึ่งในใต้หล้า.epub" book.md
