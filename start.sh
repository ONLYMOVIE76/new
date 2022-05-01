if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/rahulrahamanx/AutoFilter-Group.git /AutoFilter-Group
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /AutoFilter-Group
fi
cd /AutoFilter-Group
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
