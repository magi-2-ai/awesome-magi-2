# Awesome MAGI-2

A prompt cookbook, directing guide, and local JSON validator for Sand.ai MAGI-2 workflows.

> Try MAGI-2 directly in your browser (4–30s 1080p, native audio sync, up to 20 multimodal references): https://magi-2-ai.com

The open MAGI-2 Preview release offers unified audio-video generation from text or a still image. Its 114B checkpoint generates 10-second clips and uses a separate refiner for 1080p. Find the upstream [inference code](https://github.com/SandAI-org/MAGI-2-preview) and [preview weights](https://huggingface.co/sand-ai/MAGI-2-preview).

## Contents

- [Omni-reference prompt templates](prompts/omni-reference-templates.md)
- [Long-script directing guide](prompts/long-script-directing-guide.md)
- [Sample JSON job](examples/sample_job.json)
- [Python validator](scripts/validate_magi2_payload.py)

## Workflow comparison

| Model or workflow | Clip duration | Native audio-video sync | Multimodal references | Script length |
| --- | --- | --- | --- | --- |
| MAGI-2 (480B) workspace workflow | 4–30 s | Yes | Up to 20 in this cookbook schema | 20,000 characters in the local schema |
| Seedance 2.5 | Up to 30 s | Yes | Up to 30 images, 10 video clips, and 10 audio clips | Check the serving interface |
| Kling 3.0 | Check the selected mode | Available in supported modes | Depends on mode and interface | Check the serving interface |

[ByteDance Seedance 2.5 release notes](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) · [Kling AI](https://klingai.com/)

## Quick start

1. Copy a template and replace its slot names with your own asset identifiers. Give each asset one job, such as product identity or camera motion.
2. Copy the sample JSON. Set duration in seconds and list references under images, videos, and audio.
3. Run the offline check with Python 3.

```sh
python scripts/validate_magi2_payload.py examples/sample_job.json
```

4. Enter the script and attach assets in your generation interface. Review the rendered clip against the timestamps, especially spoken lines and cut points. For repeatable comparisons, hold duration and assets fixed, change one prompt instruction per run, and record cut timing, visible identity drift, and dialogue sync.

## FAQ

**Do I need a GPU?** The browser workspace and offline validator work without a local GPU. For self-hosting Preview, consult Sand.ai's inference instructions.

**Does the validator submit jobs?** It only reads local JSON, checks the schema, and reports errors. It needs no API credentials or network access.

**How do I fit a long script into 30 seconds?** Convert the script into a shot plan. Keep only the beats that fit the clip, and render the remaining shots in separate jobs.

## Affiliation

magi-2-ai.com is an independent third-party web workspace and community resource for Sand.ai MAGI-2 and is not officially affiliated with Sand.ai.
