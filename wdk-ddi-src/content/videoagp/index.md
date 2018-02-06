---
UID: NA:videoagp
ms.assetid: 0fc9df98-c623-3890-a8d0-1ec564589343
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# videoagp.h header



videoagp.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [PAGP_COMMIT_PHYSICAL](nc-videoagp-pagp_commit_physical.md) | The AgpCommitPhysical function maps system (physical) memory to the specified range of AGP-decodable physical addresses. |
| [PAGP_COMMIT_VIRTUAL](nc-videoagp-pagp_commit_virtual.md) | The AgpCommitVirtual function maps reserved virtual memory to an associated range of AGP-decodable physical addresses. |
| [PAGP_FREE_PHYSICAL](nc-videoagp-pagp_free_physical.md) | The AgpFreePhysical function frees system memory that was committed by a previous call to AgpCommitPhysical. |
| [PAGP_FREE_VIRTUAL](nc-videoagp-pagp_free_virtual.md) | The AgpFreeVirtual function frees virtual memory committed by a previous call to AgpCommitVirtual. |
| [PAGP_RELEASE_PHYSICAL](nc-videoagp-pagp_release_physical.md) | The AgpReleasePhysical function frees a physical address range reserved by a previous call to AgpReservePhysical. |
| [PAGP_RELEASE_VIRTUAL](nc-videoagp-pagp_release_virtual.md) | The AgpReleaseVirtual function frees system memory reserved by a previous call to AgpReserveVirtual. |
| [PAGP_RESERVE_PHYSICAL](nc-videoagp-pagp_reserve_physical.md) | The AgpReservePhysical function reserves a range of physical addresses on the system bus to which the AGP controller can respond. |
| [PAGP_RESERVE_VIRTUAL](nc-videoagp-pagp_reserve_virtual.md) | The AgpReserveVirtual function reserves a range of virtual addresses for AGP. |
| [PAGP_SET_RATE](nc-videoagp-pagp_set_rate.md) | The AgpSetRate function reprograms the data transfer rate of the AGP chipset. |
| [VideoPortGetAgpServices](nf-videoagp-videoportgetagpservices.md) | The VideoPortGetAgpServices function is obsolete and is supported only for backward compatibility with existing drivers. |



## Structures
| Title | Description |
| ---- |:---- |
| [_VIDEO_PORT_AGP_SERVICES](ns-videoagp-_video_port_agp_services.md) | The VIDEO_PORT_AGP_SERVICES structure is obsolete and is supported only for backward compatibility with existing drivers. In its place, driver writers should use VIDEO_PORT_AGP_INTERFACE. |