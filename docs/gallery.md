# Bruno gallery

Previews below are rendered from the current packaged sprite sheets. GIFs demonstrate the artwork independently of app state switching.

## Bruno

![Bruno states](images/bruno/four-states.png)

| Idle | Working | Waiting | Review |
| :---: | :---: | :---: | :---: |
| ![Idle](images/bruno/idle.gif) | ![Typing](images/bruno/running.gif) | ![Waiting](images/bruno/waiting.gif) | ![Review](images/bruno/review.gif) |

[All-state GIF](images/bruno/all-states.gif) · [MP4](images/bruno/all-states.mp4) · [Jump and landing](images/bruno/idle-jump-idle.gif) · [Look loop](images/bruno/look-loop.gif)

![Bruno contact sheet](images/bruno/contact-sheet.png)

![Bruno look directions](images/bruno/directions.png)

## Judoka Bruno

![Judoka states](images/bruno-judoka/four-states.png)

| Idle | Working | Waiting | Review |
| :---: | :---: | :---: | :---: |
| ![Idle](images/bruno-judoka/idle.gif) | ![Uchi-mata](images/bruno-judoka/running.gif) | ![Waiting](images/bruno-judoka/waiting.gif) | ![Review](images/bruno-judoka/review.gif) |

[All-state GIF](images/bruno-judoka/all-states.gif) · [MP4](images/bruno-judoka/all-states.mp4) · [Jump and landing](images/bruno-judoka/idle-jump-idle.gif) · [Look loop](images/bruno-judoka/look-loop.gif)

[Medium-paced throw](images/bruno-judoka/partnered-throw-medium.gif) · [Slower throw](images/bruno-judoka/partnered-throw-slow.gif). These are timing comparisons; they do not set installed playback speed.

![Judoka look directions](images/bruno-judoka/directions-final-r2.png)

## Chef Bruno

![Chef states](images/bruno-chef/four-states.png)

| Idle | Working | Waiting | Review |
| :---: | :---: | :---: | :---: |
| ![Idle](images/bruno-chef/idle.gif) | ![Soup](images/bruno-chef/running.gif) | ![Waiting](images/bruno-chef/waiting.gif) | ![Review](images/bruno-chef/review.gif) |

[All-state GIF](images/bruno-chef/all-states.gif) · [MP4](images/bruno-chef/all-states.mp4) · [Jump and landing](images/bruno-chef/idle-jump-idle.gif) · [Look loop](images/bruno-chef/look-loop.gif)

![Chef contact sheet](images/bruno-chef/contact-sheet.png)

![Chef look directions](images/bruno-chef/directions.png)

## Padding improvements

The current coder and chef packages use one consistent scale adjustment across every state to reduce overhead padding while preserving jumps and landing alignment.

![Coder padding comparison](images/bruno/comparison.png)

![Chef padding comparison](images/bruno-chef/comparison.png)

## More animations

Each variant's image folder also contains `running-right.gif`, `running-left.gif`, `waving.gif`, `jumping.gif`, and `failed.gif`. See [the format guide](sprite-format.md) for their meaning.
