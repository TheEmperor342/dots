# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout
from qtile_extras import widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile import hook, qtile
from qtile_extras.widget.decorations import RectDecoration

import os
import subprocess

HOME = os.path.expanduser("~")
catppuccin = {
    "crust": "#11111B",
    "mantle": "#181825",
    "base": "#1E1E2E",
    "surface0": "#313244",
    "surface1": "#45475a",
    "surface2": "#585b70",
    "overlay0": "#6c7086",
    "overlay1": "#7f849c",
    "overlay2": "#9399b2",
    "subtext0": "#a6adc8",
    "subtext1": "#bac2de",
    "text": "#cdd6f4",
    "lavender": "#b4befe",
    "blue": "#89b4fa",
    "sapphire": "#74c7ec",
    "sky": "#89dceb",
    "teal": "#94e2d5",
    "green": "#a6e3a1",
    "yellow": "#f9e2af",
    "peach": "#fab387",
    "red": "#f38ba8",
    "maroon": "#eba0ac",
    "muave": "#cba6f7",
}

DEFAULT_LAYOUTS = {
    "margin": 7,
    "font": "JetBrainsMono Nerd Font",
    "fontsize": 9,
    "border_width": 1,
    "border_focus": catppuccin["surface1"],
    "border_normal": catppuccin["surface0"],
}
DEFAULT_DECORATIONS = {
    "decorations": [
        RectDecoration(
            colour=catppuccin["base"],
            radius=5,
            filled=True,
            padding_y=4,
            group=True
        )
    ]
}

mod = "mod4"
terminal = "kitty"

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),

    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),

    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),

    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),

    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),

    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawn("rofi -show drun"),
        desc="rofi"),
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Reset all window sizes"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
        ]
    )

layouts = [
    # layout.Bsp(**DEFAULT_LAYOUTS),
    layout.MonadTall(**DEFAULT_LAYOUTS),
    # layout.Columns(**DEFAULT_LAYOUTS),
    # layout.Max(**DEFAULT_LAYOUTS),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=12,
    padding=3,
)
bar = bar.Bar(
    [
        widget.Sep(
            linewidth=0,
            padding=15
        ),
        widget.Image(
            filename="~/.config/qtile/logo.png"
        ),
        widget.Sep(
            linewidth=0,
            padding=15
        ),
        widget.GroupBox(
            fontsize=10,
            margin_y=3,
            margin_x=4,
            padding_y=2,
            padding_x=3,
            borderwidth=3,
            active=catppuccin["blue"],
            inactive=catppuccin["subtext1"],
            highlight_method="block",
            this_current_screen_border=catppuccin["surface0"],
            **DEFAULT_DECORATIONS
        ),
        widget.Sep(
            linewidth=0,
            padding=15
        ),
        widget.GenPollText(
            update_interval=10,
            func=lambda: subprocess.check_output(
                f"{HOME}/.local/bin/getram").decode("utf-8"),
            fmt=" 󰍛 {}% ",
            foreground=catppuccin["text"],
            **DEFAULT_DECORATIONS
        ),
        widget.Spacer(),
        widget.Sep(
            linewidth=0,
            padding=15
        ),
        widget.GenPollText(
            update_interval=10,
            func=lambda: subprocess.check_output(
                f"{HOME}/.local/bin/battery").decode("utf-8"),
            fmt=" {} ",
            foreground=catppuccin["text"],
            **DEFAULT_DECORATIONS
        ),
        widget.Sep(
            linewidth=0,
            padding=15
        ),
        widget.Volume(
            fmt=" 󰕾 {} ",
            font='JetBrainsMono Nerd Font',
            foreground=catppuccin["text"],
            **DEFAULT_DECORATIONS
        ),
        widget.Sep(
            linewidth=0,
            padding=15
        ),
        widget.Backlight(
            fmt=" 󰃠  {} ",
            foreground=catppuccin["text"],
            change_command="brightnessctl s {0}",
            brightness_file="/sys/class/backlight/intel_backlight/brightness",
            max_brightness_file="/sys/class/backlight/intel_backlight/max_brightness",
            backlight_name="intel_backlight",
            mouse_callbacks={
                "Button4": lambda: qtile.cmd_spawn("brightnessctl set +5%"),
                "Button5": lambda: qtile.cmd_spawn("brightnessctl set 5%-"),
            },
            **DEFAULT_DECORATIONS
        ),
        widget.Sep(
            linewidth=0,
            padding=15
        ),
        widget.Clock(
            foreground=catppuccin["text"],
            format="   %I:%M %p ",
            **DEFAULT_DECORATIONS
        ),
        widget.Sep(
            linewidth=0,
            padding=15
        ),
        widget.Systray(),
        widget.Sep(
            linewidth=0,
            padding=15
        ),
    ],
    32,
    background=catppuccin["crust"]
)


@hook.subscribe.startup
def _():
    bar.window.window.set_property("QTILE_BAR", 1, "CARDINAL", 32)


screens = [
    Screen(
        wallpaper="~/.config/Wallpapers/leafs.png",
        wallpaper_mode="fill",
        top=bar,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    **DEFAULT_LAYOUTS
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"


@hook.subscribe.startup_once
def autostart() -> None:
    subprocess.Popen([f"{HOME}/.config/qtile/autostart-once"])
