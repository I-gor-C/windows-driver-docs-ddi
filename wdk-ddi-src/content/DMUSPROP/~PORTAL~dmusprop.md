# Declarations in the dmusprop header
This header Dmusprop contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [SYNTH_PORTPARAMS structure](ns-dmusprop--synth-portparams.md) | The SYNTH_PORTPARAMS structure contains the configuration parameters for a DirectMusic port, which is a DirectMusic term for a device that sends or receives music data. |
| [SYNTH_STATS structure](ns-dmusprop--synth-stats.md) | The SYNTH_STATS structure specifies synthesizer performance statistics such as the number of voices playing, CPU usage, number of notes lost, amount of free memory, and peak volume level. |
| [SYNTH_BUFFER structure](ns-dmusprop--synth-buffer.md) | The SYNTH_BUFFER structure specifies DLS data that is being downloaded to a synthesizer. |
| [SYNTHVOICEPRIORITY_INSTANCE structure](ns-dmusprop--synthvoicepriority-instance.md) | The SYNTHVOICEPRIORITY_INSTANCE structure identifies a voice in a MIDI synthesizer by specifying the voice's channel group (set of 16 MIDI channels) and its channel number within that group. |
| [SYNTHDOWNLOAD structure](ns-dmusprop--synthdownload.md) | The SYNTHDOWNLOAD structure specifies a handle for downloaded DLS data. It also specifies whether the buffer containing the DLS data can be freed. |
| [SYNTH_REVERB_PARAMS structure](ns-dmusprop--synth-reverb-params.md) | The SYNTH_REVERB_PARAMS structure contains configuration parameters. |
| [SYNTHCAPS structure](ns-dmusprop--synthcaps.md) | The SYNTHCAPS structure specifies the capabilities of a synthesizer. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [KSPROPERTY_SYNTHCLOCK enumeration](ne-dmusprop-ksproperty-synthclock.md) | TBD |
| [KSPROPERTY_SYNTH enumeration](ne-dmusprop-ksproperty-synth.md) | TBD |
| [KSPROPERTY_SYNTH_DLS enumeration](ne-dmusprop-ksproperty-synth-dls.md) | TBD |

This header is used in these topics:

- [audio](..content/_audio)
