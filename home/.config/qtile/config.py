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
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile import hook, qtile
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras.resources import wallpapers

import os
import subprocess

HOME = os.path.expanduser("~")
WALLPAPER = "~/.config/Wallpapers/catppuccin/astronaut.png"
LOGO = "~/.config/qtile/logos/catppuccin-logo.png"
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
solarized = {
    "crust": "#001e26",
    "mantle": "#002b36",
    "base": "#073642",
    "surface0": "#586e75",
    "surface1": "#657b83",
    "surface2": "#839496",
    "overlay0": "#93a1a1",
    "overlay1": "#eee8d5",
    "overlay2": "#eee8d5",
    "subtext0": "#eee8d5",
    "subtext1": "#eee8d5",
    "text": "#fdf6e3",
    "lavender": "#2aa198",
    "blue": "#268bd2",
    "sapphire": "#268bd2",
    "sky": "#6c71c4",
    "teal": "#6c71c4",
    "green": "#859900",
    "yellow": "#b58900",
    "peach": "#cb4b16",
    "red": "#dc322f",
    "maroon": "#dc322f",
    "muave": "#d33682",
}
gruvbox = {
    "crust": "#282828",
    "mantle": "#282828",
    "base": "#282828",
    "surface0": "#3c3836",
    "surface1": "#504945",
    "surface2": "#665c54",
    "overlay0": "#a89984",
    "overlay1": "#bdae93",
    "overlay2": "#d5c4a1",
    "subtext0": "#ebdbb2",
    "subtext1": "#fbf1c7",
    "text": "#ebdbb2",
    "lavender": "#8ec07c",
    "blue": "#458588",
    "sapphire": "#076678",
    "sky": "#83a598",
    "teal": "#83a598",
    "green": "#98971a",
    "yellow": "#fabd2f",
    "peach": "#d79921",
    "red": "#cc241d",
    "maroon": "#fb4934",
    "muave": "#b16286",
}
everblush = {
    "crust": "#141b1e",
    "mantle": "#141b1e",
    "base": "#232a2d",
    "surface0": "#3c3836",
    "surface1": "#232a2d",
    "surface2": "#232a2d",
    "overlay0": "#b3b9b8",
    "overlay1": "#b3b9b8",
    "overlay2": "#b3b9b8",
    "subtext0": "#b3b9b8",
    "subtext1": "#b3b9b8",
    "text": "#dadada",
    "lavender": "#c47fd5",
    "blue": "#67b0e8",
    "sapphire": "#67b0e8",
    "sky": "#6cbfbf",
    "teal": "#6cbfbf",
    "green": "#8ccf7e",
    "yellow": "#e5c76b",
    "peach": "#e5c76b",
    "red": "#e57474",
    "maroon": "#e57474",
    "muave": "#c47fd5",
}

colors = catppuccin
DEFAULT_LAYOUTS = {
    "margin": 5,
    "font": "JetBrainsMono Nerd Font",
    "fontsize": 9,
    "border_width": 1,
    "border_focus": colors["surface0"],
    "border_normal": colors["base"],
}


def DEFAULT_DECORATIONS(color: str = colors["mantle"]) -> dict:
    return {
        "background": color,
        "decorations": [
            PowerLineDecoration(
                path="forward_slash"
                # radius=4,
                # filled=True,
                # padding_y=4,
                # group=True
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
    Key([mod], "s", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Screenshot"),
    Key([mod], 'i', lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod, "shift"], 'f', lazy.spawn("firefox")),
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

groups.extend([
    ScratchPad("scratchpad", [
        DropDown("term", "kitty", opacity=0.9, height=0.8, y=0.1),
    ]),
])
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
        widget.Image(
            filename=LOGO,
            **DEFAULT_DECORATIONS(colors["subtext0"]),
            margin_x=15
        ),
        widget.Sep(**DEFAULT_DECORATIONS(colors["text"]), linewidth=0, padding=5),
        widget.GroupBox(
            fontsize=10,
            margin_y=3,
            margin_x=4,
            padding_y=2,
            padding_x=3,
            borderwidth=2,
            active=colors["crust"],
            inactive=colors["surface1"],
            highlight_method="block",
            this_current_screen_border=colors["overlay2"],
            **DEFAULT_DECORATIONS(colors["text"])
        ),
        widget.Sep(**DEFAULT_DECORATIONS(colors["text"]), linewidth=0, padding=5),
        widget.Spacer(),
        widget.Sep(
            **DEFAULT_DECORATIONS(colors["crust"]),
            linewidth=0,
            padding=1
        ),
        widget.Sep(**DEFAULT_DECORATIONS(colors["teal"]), linewidth=0, padding=2),
        widget.GenPollText(
            update_interval=10,
            func=lambda: subprocess.check_output(
                f"{HOME}/.local/bin/getram").decode("utf-8"),
            fmt=" 󰍛 {}%",
            foreground=colors["crust"],
            **DEFAULT_DECORATIONS(colors["teal"])
        ),
        widget.Sep(**DEFAULT_DECORATIONS(colors["teal"]), linewidth=0, padding=2),
        # widget.GenPollText(
        #     update_interval=10,
        #     func=lambda: subprocess.check_output(
        #         f"{HOME}/.local/bin/battery").decode("utf-8"),
        #     fmt=" {} ",
        #     foreground=colors["text"],
        #     **DEFAULT_DECORATIONS
        # ),
        widget.Sep(**DEFAULT_DECORATIONS(colors["sky"]), linewidth=0, padding=2),
        widget.Volume(
            fmt=" 󰕾 {}",
            font='JetBrainsMono Nerd Font',
            foreground=colors["crust"],
            padding=15,
            **DEFAULT_DECORATIONS(colors["sky"])
        ),
        widget.Sep(**DEFAULT_DECORATIONS(colors["sky"]), linewidth=0, padding=2),
        widget.Sep(**DEFAULT_DECORATIONS(colors["sapphire"]), linewidth=0, padding=2),
        widget.Backlight(
            fmt=" 󰃠  {} ",
            foreground=colors["crust"],
            change_command="brightnessctl s {0}",
            brightness_file="/sys/class/backlight/intel_backlight/brightness",
            max_brightness_file="/sys/class/backlight/intel_backlight/max_brightness",
            backlight_name="intel_backlight",
            mouse_callbacks={
                "Button4": lambda: qtile.cmd_spawn("brightnessctl set +5%"),
                "Button5": lambda: qtile.cmd_spawn("brightnessctl set 5%-"),
            },
            **DEFAULT_DECORATIONS(colors["sapphire"])
        ),
        widget.Sep(**DEFAULT_DECORATIONS(colors["sapphire"]), linewidth=0, padding=2),
        # widget.Sep(
        #    linewidth=0,
        #    padding=15
        # ),
        widget.Sep(**DEFAULT_DECORATIONS(colors["blue"]), linewidth=0, padding=2),
        widget.Clock(
            foreground=colors["crust"],
            format="   %I:%M %p ",
            **DEFAULT_DECORATIONS(colors["blue"])
        ),
        widget.Sep(**DEFAULT_DECORATIONS(colors["blue"]), linewidth=0, padding=2),
        # widget.Sep(
        #    linewidth=0,
        #    padding=5
        # ),
        widget.Systray(),
        widget.Sep(
            linewidth=0,
            padding=15
        ),
    ],
    24,
    background=colors["crust"]
)


@hook.subscribe.startup
def _():
    bar.window.window.set_property("QTILE_BAR", 1, "CARDINAL", 32)


screens = [
    Screen(
        wallpaper=WALLPAPER,
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
