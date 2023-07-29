# Dotfiles
My configuration for bspwm

# Packages needed
- Xorg: xorg-server xorg-xinit, xorg-xsetroot, xorg-xrandr
- WM and Keybinds: [bspwm (rounded corners)](https://github.com/phuhl/bspwm-rounded) & [sxhkd](https://github.com/baskerville/sxhkd)
- GTK Theme: catppuccin Mocha
- Browser: Firefox
- Wallpaper setter: nitrogen
- Notif daemon: dunst
- Compositor: xcompmgr
- Terminal: kitty
- Bar: polybar
- Bluetooth: blueman
- Python3
- Font: JetBrainsMono nerd fonts
- Editor: neovim (with [Lazy.nvim](https://github.com/folke/lazy.nvim))
  - `jq` and `tidy` for [rest.nvim](https://github.com/rest-nvim/rest.nvim)
- lxsession, lxappearance, xdotool
- I have laptop so I also use [gestures](https://aur.archlinux.org/packages/libinput-gestures) and [tlp](https://archlinux.org/packages/extra/any/tlp)
  - Remove their autostarts from bspwmrc if you don't want to use them

___
Command to install dependencies in arch linux:
```
yay -S --needed xorg-server xorg-xinit xorg-xsetroot xorg-xrandr bspwm-rounded-corners catppuccin-gtk-theme-mocha polybar sxhkd firefox nitrogen dunst xcompmgr kitty brightnessctl zsh zsh-autosuggestions zsh-syntax-highlighting blueman python ttf-jetbrains-mono-nerd lxsession-gtk3 lxappearance xdotool neovim jq tidy rofi alsa-utils
```
Installing gestures stuff
```
yay -S libinput-gestures
sudo gpasswd -a $USER input
```
Reboot after adding your user to input group

TLP
```
sudo pacman -S tlp
```

If you don't have an nvidia GPU, I [envy](https://github.com/bayasdev/envycontrol) you (pun intended).
- remove xrandr commands from `.xinitrc` located at `home/.config/X11/`

![image](https://github.com/TheEmperor342/dots/assets/83999665/d4388466-34be-4ea5-a834-7d835f62fcdb)
![image](https://github.com/TheEmperor342/dots/assets/83999665/76ee1867-b5ce-4478-b8d9-46b783259150)
![image](https://github.com/TheEmperor342/dots/assets/83999665/484e7404-28c5-4426-9418-db872cb9cb8a)
![image](https://github.com/TheEmperor342/dots/assets/83999665/fe5ca0e2-ed0e-4a44-9abe-b7012c922a11)
