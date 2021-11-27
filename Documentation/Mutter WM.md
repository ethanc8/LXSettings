# <big>Mutter WM</big>
## Table of Contents
<!-- TOC -->

* [<big>Mutter WM</big>](#bigmutter-wmbig)
    * [Table of Contents](#table-of-contents)
* [Preferences](#preferences)
    * [Behavior](#behavior)
    * [Titlebar](#titlebar)
    * [Bells](#bells)
    * [New windows](#new-windows)
    * [Advanced](#advanced)
        * [mutter](#mutter)
        * [dwp](#dwp)

<!-- /TOC -->

# Preferences
## Behavior
| Section  | Pref name              | Description                                                           |
| -------- | ---------------------- | --------------------------------------------------------------------- |
| `mutter` | `attach-modal-dialogs` | Attach modal dialogs to the window which created them                 |
| `mutter` | `auto-maximize`        | Automatically maximize windows shich fill the whole screen            |
| `mutter` | `dynamic-workspaces`   | Allow creating workspaces at runtime                                  |
| `mutter` | `edge-tiling`          | Snap windows to one side of the screen when you drag them to the edge |
| dwp      | `auto-raise`           | Automatically raise the focused window                                |
|          |                        |                                                                       |

## Titlebar
| Section  | Pref name                      | Description                                                           |
| -------- | ------------------------------ | --------------------------------------------------------------------- |
| dwp      | `action-double-click-titlebar` | When I double-click the titlebar:                                     |
| dwp      | `action-middle-click-titlebar` | When I middle-click the titlebar:                                     |
| dwp      | `action-right-click-titlebar`  | When I right-click the titlebar:                                      |

## Bells
| Section | Pref name          | Description                                                                                        |
| ------- | ------------------ | -------------------------------------------------------------------------------------------------- |
| dwp     | `audible-bell`     | Play a sound when an app rings the "system bell"                                                   |
| dwp     | `visual-bell`      | Show something on the screen when an app rings the "system bell"                                   |
| dwp     | `visual-bell-type` | Show this on the screen when an app rings the "system bell"                                        |
| dwp     | `button-layout`    | Layout of buttons on the titlebar -- should be combined with the equivalent Gtk3 HeaderBar setting |
| dwp     |                    |                                                                                                    |

## New windows
| Section  | Pref name          | Description                                   |
| -------- | ------------------ | --------------------------------------------- |
| `mutter` | `center-windows`   | Place new windows in the middle of the screen |


## Advanced
### `mutter`
* `check-alive`
* `disable-override-redirect`
* `draggable-border-width`
* `experimental-features`
* `focus-change-on-pointer-rest`
* `locate-pointer-key`
* `no-tab-popup`
* `overlay-key`
* `workspaces-only-on-primary`
### dwp
* `auto-raise-delay`
* `disable-workarounds`
* 
