# Known issues

## Working animation stops

In the desktop app build inspected on 21 October 2026 (`26.1013.40934`), the shared animation selector plays a non-idle action three times, then loops idle unless the caller explicitly enables looping. The floating mascot wrapper omits that option. Cursor-looking poses can override the work animation, and hovering can temporarily trigger jumping.

This affects all three Bruno variants. Their work frames are present and animate correctly in the independent previews. Installing a sprite sheet cannot change the app's looping or gaze rules.

The runtime needs to loop the work state for as long as work is active and resolve work ahead of hover/gaze. This repository does not patch the signed application. Behavior may differ in later builds.

## Space above the head

The fixed sprite frame also holds raised limbs, jumps, and the partnered throw. Resting poses leave space above their heads. The current coder and chef sheets reduce this padding with uniform fits of 1.19× and 1.08× respectively.

Judoka's jump reaches within two pixels of the top of his frame, and the throw uses 182 of its 192 horizontal pixels. Further enlargement would clip action poses. Fully tightening the status-bubble placement requires a runtime layout change.

## Preview speed

The medium and slow uchi-mata GIFs demonstrate different speeds. They do not change installed playback timing. The app decides the sheet's frame durations.

## Missing animation or missing pet

Check operating-system reduced-motion settings if the pet uses a still frame. Verify that each installed folder contains both `pet.json` and `spritesheet.png`, and that the manifest retains `spriteVersionNumber: 2`. Refresh the list or reopen the app after copying packages. [Official Pets documentation](https://learn.chatgpt.com/docs/pets).
