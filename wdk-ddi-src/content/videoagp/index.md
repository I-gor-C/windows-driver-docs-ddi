---
UID: NA:videoagp
---

# Videoagp.h header

## -description

This header is used by Display. For more information, see
- [Display](../_display/index.md)

Videoagp.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [VideoPortGetAgpServices function](nf-videoagp-videoportgetagpservices.md) | The VideoPortGetAgpServices function is obsolete and is supported only for backward compatibility with existing drivers. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [PAGP_COMMIT_PHYSICAL callback](nc-videoagp-pagp_commit_physical.md) | The AgpCommitPhysical function maps system (physical) memory to the specified range of AGP-decodable physical addresses. |
| [PAGP_COMMIT_VIRTUAL callback](nc-videoagp-pagp_commit_virtual.md) | The AgpCommitVirtual function maps reserved virtual memory to an associated range of AGP-decodable physical addresses. |
| [PAGP_FREE_PHYSICAL callback](nc-videoagp-pagp_free_physical.md) | The AgpFreePhysical function frees system memory that was committed by a previous call to AgpCommitPhysical. |
| [PAGP_FREE_VIRTUAL callback](nc-videoagp-pagp_free_virtual.md) | The AgpFreeVirtual function frees virtual memory committed by a previous call to AgpCommitVirtual. |
| [PAGP_RELEASE_PHYSICAL callback](nc-videoagp-pagp_release_physical.md) | The AgpReleasePhysical function frees a physical address range reserved by a previous call to AgpReservePhysical. |
| [PAGP_RELEASE_VIRTUAL callback](nc-videoagp-pagp_release_virtual.md) | The AgpReleaseVirtual function frees system memory reserved by a previous call to AgpReserveVirtual. |
| [PAGP_RESERVE_PHYSICAL callback](nc-videoagp-pagp_reserve_physical.md) | The AgpReservePhysical function reserves a range of physical addresses on the system bus to which the AGP controller can respond. |
| [PAGP_RESERVE_VIRTUAL callback](nc-videoagp-pagp_reserve_virtual.md) | The AgpReserveVirtual function reserves a range of virtual addresses for AGP. |
| [PAGP_SET_RATE callback](nc-videoagp-pagp_set_rate.md) | The AgpSetRate function reprograms the data transfer rate of the AGP chipset. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_VIDEO_PORT_AGP_SERVICES structure](ns-videoagp-_video_port_agp_services.md) | The VIDEO_PORT_AGP_SERVICES structure is obsolete and is supported only for backward compatibility with existing drivers. In its place, driver writers should use VIDEO_PORT_AGP_INTERFACE. |
