# Directing from a long script

Use the 5,000–20,000-character draft as the source for a shot list. Mark story turns, the action that communicates each turn, and any dialogue that must survive the edit. Divide the shot list into jobs of 4–30 seconds and cut at a natural change of location, angle, or sound.

## Shot syntax

Use clip-local timestamps with adjoining ranges. Start at 00:00 and stop at the requested runtime. For each shot specify framing, camera movement, action, and the exact moment when sound begins or ends. Name reference slots consistently across clips.

```text
CLIP 04 | 12 seconds | Keep coat, envelope, and hallway lighting from CLIP 03.
[00:00–00:05] WIDE, static. Courier crosses left to right and reaches for the latch.
SOUND: Footsteps at 00:01–00:03; latch click at 00:04.8.
[00:05–00:12] CUT ON ACTION to medium close-up on the same side of the axis.
Courier holds the envelope in the right hand. At 00:07 say: "I brought the original."
SOUND: Keep hallway tone across the cut. End dialogue by 00:10; hold room tone to 00:12.
```

## Camera and transition controls

Choose one primary movement per shot. Give it a start, a direction, and an endpoint. For a cut on action, repeat the final pose, prop hand, and direction in the following shot. For a reveal, define which object occludes the subject and when the camera clears it. Use a short hold before and after important actions to give the editor room to trim.

## Sound cues

Label dialogue, effects, ambience, and music separately. Put dialogue in quotes and identify the speaker and timing. Map effects to on-screen contact. For a sound bridge, name the incoming sound and its overlap with the next shot. Read dialogue aloud before rendering and shorten it if the take leaves too little room for the reaction.

## Revision pass

Make a continuity sheet with the approved reference IDs, wardrobe, lens cues, prop positions, and room tone. Validate each job against the repository's JSON schema. Compare the rendered take with the shot list and revise one failed cue at a time. Keep neighbouring clips intact while testing an edit to a single shot.

magi-2-ai.com is an independent third-party web workspace and community resource for Sand.ai MAGI-2 and is not officially affiliated with Sand.ai.
