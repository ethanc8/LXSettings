sudo rm -r /usr/local/lib/python3.9/site-packages/gtweak
meson builddir
ninja -C builddir
sudo ninja -C builddir install
PYTHONPATH=/usr/local/lib/python3.9/site-packages gnome-tweaks