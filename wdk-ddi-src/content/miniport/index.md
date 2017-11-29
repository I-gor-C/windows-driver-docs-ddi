# Miniport.h header


This header is used by Display, Windows kernel. For more information, see
- [Display](../_display/index.md)
- [Windows kernel](../_kernel/index.md)

Miniport.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [EMULATOR_ACCESS_ENTRY structure](ns-miniport--emulator-access-entry.md) | The EMULATOR_ACCESS_ENTRY structure specifies an element in the EmulatorAccessEntries array set up in the VIDEO_PORT_CONFIG_INFO structure by drivers of VGA-compatible (SVGA) adapters on x86-based NT-based operating system platforms. |
| [GROUP_AFFINITY structure](ns-miniport--group-affinity.md) | The GROUP_AFFINITY structure specifies a group number and the processor affinity within that group. |
| [PROCESSOR_NUMBER structure](ns-miniport--processor-number.md) | The PROCESSOR_NUMBER structure identifies a processor by its group number and group-relative processor number. |
