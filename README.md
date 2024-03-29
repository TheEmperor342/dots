# Dotfiles
My configuration for QTile and bspwm
<details>
  <summary>QTile</summary>

  ## Packages needed
  - Xorg: xorg-server xorg-xinit, xorg-xsetroot, xorg-xrandr
  - WM: QTile
      - Python3
      - QTile Extras
      - python-psutil
  - Wallpaper setter: QTile
  - Bar: QTile bar
  - Catppuccin
    - GTK Theme: catppuccin Mocha
    - Cursor Theme: catppuccin cursors
  - Gruvbox
    - gruvbox-dark-gtk
  - Browser: Firefox
  - Notif daemon: dunst
  - Compositor: picom
  - Terminal: kitty
  - Tray:
    - NetworkManager Applet
    - cbatticon
    - Blueman
  - Bluetooth: blueman
  - Font: JetBrainsMono nerd fonts
  - Editor: neovim (with [Lazy.nvim](https://github.com/folke/lazy.nvim))
    - `jq` and `tidy` for [rest.nvim](https://github.com/rest-nvim/rest.nvim)
    - xclip
  - lxsession, lxappearance, xdotool, unclutter


  Command to install dependencies in Arch Linux:
  ```
  yay -S --needed xorg-server xorg-xinit xorg-xsetroot xorg-xrandr qtile qtile-extras python-psutil network-manager-applet cbatticon firefox dunst picom kitty brightnessctl zsh zsh-autosuggestions zsh-syntax-highlighting blueman python ttf-jetbrains-mono-nerd lxsession-gtk3 lxappearance xdotool neovim jq tidy xclip rofi alsa-utils
  ```
  
  ## Gallery
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/f9efdd24-935b-480a-8c96-2e6db5cefbac)
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/dbd8e035-2a50-4b4f-94b2-867a136e6a69)
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/bd42305b-ecca-4c9d-9a51-62ed6d91e17a)
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/cb9ba538-619a-47de-be70-180c7caac994)


</details>

<details>
  <summary>bspwm</summary>

  ## Packages needed
  - Xorg: xorg-server xorg-xinit, xorg-xsetroot, xorg-xrandr
  - WM and Keybinds: [bspwm (rounded corners)](https://github.com/phuhl/bspwm-rounded) & [sxhkd](https://github.com/baskerville/sxhkd)
  - GTK Theme: catppuccin Mocha
  - Cursor Theme: catppuccin cursors
  - Browser: Firefox
  - Wallpaper setter: nitrogen
  - Notif daemon: dunst
  - Compositor: picom
  - Terminal: kitty
  - Bar: polybar OR eww (There are configs for both in `home/.config`)
  - Tray:
    - NetworkManager Applet
    - Blueman
  - Python3
  - Font: JetBrainsMono nerd fonts
  - Editor: neovim (with [Lazy.nvim](https://github.com/folke/lazy.nvim))
    - `jq` and `tidy` for [rest.nvim](https://github.com/rest-nvim/rest.nvim)
    - xclip
  - lxsession, lxappearance, xdotool

  Command to install dependencies in Arch Linux:
  ```
  yay -S --needed xorg-server xorg-xinit xorg-xsetroot xorg-xrandr bspwm-rounded-corners network-manager-applet catppuccin-gtk-theme-mocha catppuccin-cursors-mocha sxhkd firefox nitrogen dunst picom kitty brightnessctl zsh zsh-autosuggestions zsh-syntax-highlighting blueman python ttf-jetbrains-mono-nerd lxsession-gtk3 lxappearance xdotool neovim jq tidy xclip rofi alsa-utils
  ```
  ### Polybar
  ```
  sudo pacman -S polybar
  ```
  ### eww
  - Compile eww from source.
    - [Link to repo](https://github.com/elkowar/eww)
    
  After installation:
  ```
  yay -S playerctl python-colorthief
  ```
  ## Gallery (With eww)
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/c8868352-8616-4813-9bef-01b51be321cb)
  ## Gallery (With Polybar)
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/d4388466-34be-4ea5-a834-7d835f62fcdb)
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/76ee1867-b5ce-4478-b8d9-46b783259150)
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/484e7404-28c5-4426-9418-db872cb9cb8a)
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/fe5ca0e2-ed0e-4a44-9abe-b7012c922a11)
  
</details>

___
Optional: Install `fzf` for a script in `home/.local/bin/`

____
I have laptop so I also use [libinput-gestures](https://aur.archlinux.org/packages/libinput-gestures) and [auto-cpufreq](https://github.com/AdnanHodzic/auto-cpufreq)
  - Remove their autostarts from bspwmrc or qtile autostarts if you don't want to use them

Installing gestures stuff
```
yay -S libinput-gestures
sudo gpasswd -a $USER input
```
Reboot after adding your user to input group

If you don't have an nvidia GPU, I [envy](https://github.com/bayasdev/envycontrol) you (pun intended).
- remove xrandr commands from `.xinitrc` located at `home/.config/X11/`

