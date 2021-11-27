# <big>Dependencies</big>
## 

# APT dependencies

```
blueman
dconf-editor
wpagui
gnome-system-tools
mugshot
xfce4-notifyd
pavucontrol
```

> **Note**: `xfce4-notifyd` will install a notification daemon. I chose this because it's lightweight and has a log.

# Pi-Apps dependencies

```
Timeshift
Autostar
```

# Allowing login environment variables

```bash
touch ~/.xprofile
touch ~/.xinitrc
touch ~/EnvironmentVariables

cat ~/.xprofile >> ~/EnvironmentVariables
cat ~/.xinitrc >>~/EnvironmentVariables

cat <<EOL >~/.xprofile
#!/bin/bash
source ~/EnvironmentVariables
EOL

cat <<EOL >~/.xinitrc
#!/bin/bash
source ~/EnvironmentVariables
EOL
```