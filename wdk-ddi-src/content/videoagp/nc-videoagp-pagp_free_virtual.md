---
UID: NC:videoagp.PAGP_FREE_VIRTUAL
title: PAGP_FREE_VIRTUAL
author: windows-driver-content
description: The AgpFreeVirtual function frees virtual memory committed by a previous call to AgpCommitVirtual.
old-location: display\agpfreevirtual.htm
old-project: display
ms.assetid: a6f689ab-8cf1-4207-af2b-30957500c190
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: AgpFreeVirtual, AgpFreeVirtual callback function [Display Devices], PAGP_FREE_VIRTUAL, VideoPort_Functions_49eabd30-2590-466f-b9d4-f2577a7e78e4.xml, display.agpfreevirtual, videoagp/AgpFreeVirtual
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: videoagp.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	videoagp.h
api_name:
-	AgpFreeVirtual
product: Windows
targetos: Windows
req.typenames: VP_SCATTER_GATHER_LIST, *PVP_SCATTER_GATHER_LIST
req.product: Windows 10 or later.
---


# PAGP_FREE_VIRTUAL callback function
The <b>AgpFreeVirtual</b> function frees virtual memory committed by a previous call to <a href="..\videoagp\nc-videoagp-pagp_commit_virtual.md">AgpCommitVirtual</a>.

## Syntax

```
PAGP_FREE_VIRTUAL PagpFreeVirtual;

void PagpFreeVirtual(
  IN PVOID HwDeviceExtension,
  IN PVOID VirtualReserveContext,
  IN ULONG Pages,
  IN ULONG Offset
)
{...}
```

## Parameters

`HwDeviceExtension`

Pointer to the miniport driver's device extension.

`VirtualReserveContext`

Identifies a reserved virtual address range. This context handle was obtained from <a href="..\videoagp\nc-videoagp-pagp_reserve_virtual.md">AgpReserveVirtual</a>.

`Pages`

Specifies the number of pages of virtual memory that the video port driver should unmap.

`Offset`

Specifies the page offset into the reserved virtual address range identified by <b>VirtualReserveContext</b> that indicates the actual base address at which to unmap virtual memory.


## Return Value

None

## Remarks

When a miniport driver calls <b>AgpFreeVirtual</b>, <i>Pages</i> pages of virtual addresses are unmapped. The unmapped range begins <b>Offset</b> pages into the range associated with <b>VirtualReserveContext</b>. The miniport driver must specify that the exact offset and number of pages be freed as were committed in a prior call to <a href="..\videoagp\nc-videoagp-pagp_commit_virtual.md">AgpCommitVirtual</a>. 

A call to <b>AgpFreeVirtual</b> must be paired with a previous call to <a href="..\videoagp\nc-videoagp-pagp_commit_virtual.md">AgpCommitVirtual</a>, and that call to <b>AgpCommitVirtual</b> must be preceded by a successful call to <a href="..\videoagp\nc-videoagp-pagp_reserve_virtual.md">AgpReserveVirtual</a>. If <b>AgpReserveVirtual</b> fails (returns <b>NULL</b>), you must not call <b>AgpCommitVirtual</b> or <b>AgpFreeVirtual</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 2000 and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | videoagp.h (include Video.h) |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="..\videoagp\nc-videoagp-pagp_commit_virtual.md">AgpCommitVirtual</a>