```
gsettings-desktop-schemas \
mutter-common \
python3-gi \
gir1.2-gtk-3.0 \
gir1.2-gnomedesktop-3.0 \
gir1.2-handy-0.0 \
gir1.2-soup-2.4  \
gir1.2-notify-0.7 \
gir1.2-glib-2.0 \
gir1.2-pango-1.0 \
gnome-shell-extension-prefs
```

```bash
sudo ninja -C builddir install
PYTHONPATH=/usr/local/lib/python3.9/site-packages gnome-tweaks
```

```
gnome-settings-daemon,
gnome-shell-common (>= 3.24),
```