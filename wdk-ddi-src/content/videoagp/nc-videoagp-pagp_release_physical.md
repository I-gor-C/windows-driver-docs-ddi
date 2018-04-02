---
UID: NC:videoagp.PAGP_RELEASE_PHYSICAL
title: PAGP_RELEASE_PHYSICAL
author: windows-driver-content
description: The AgpReleasePhysical function frees a physical address range reserved by a previous call to AgpReservePhysical.
old-location: display\agpreleasephysical.htm
old-project: display
ms.assetid: 4da0f5cb-a017-4df5-958b-c76b7a08495a
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: AgpReleasePhysical, AgpReleasePhysical callback function [Display Devices], PAGP_RELEASE_PHYSICAL, VideoPort_Functions_427923a7-3205-41a7-a470-dbc7d531e47f.xml, display.agpreleasephysical, videoagp/AgpReleasePhysical
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
-	AgpReleasePhysical
product:
- Windows
targetos: Windows
req.typenames: VP_SCATTER_GATHER_LIST, *PVP_SCATTER_GATHER_LIST
req.product: Windows 10 or later.
---


# PAGP_RELEASE_PHYSICAL callback function
The <b>AgpReleasePhysical</b> function frees a physical address range reserved by a previous call to <a href="https://msdn.microsoft.com/b3e21c94-acd5-4767-8ba5-70b2dcfb2aaa">AgpReservePhysical</a>.

## Syntax

```
PAGP_RELEASE_PHYSICAL PagpReleasePhysical;

void PagpReleasePhysical(
  IN PVOID HwDeviceExtension,
  IN PVOID PhysicalReserveContext
)
{...}
```

## Parameters

`HwDeviceExtension`

Pointer to the miniport driver's device extension.

`PhysicalReserveContext`

Is the context handle that identifies the reserved physical address range to be released. This context was obtained from <a href="https://msdn.microsoft.com/b3e21c94-acd5-4767-8ba5-70b2dcfb2aaa">AgpReservePhysical</a>.


## Return Value

None

## Remarks

The miniport driver must call <a href="https://msdn.microsoft.com/bb0e3330-5601-47dd-afc6-94a70b42daaf">AgpFreePhysical</a> to unmap all committed memory within the address range identified by <b>PhysicalReserveContext</b> before calling <b>AgpReleasePhysical</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 2000 and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | videoagp.h (include Video.h) |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/bb0e3330-5601-47dd-afc6-94a70b42daaf">AgpFreePhysical</a>



<a href="https://msdn.microsoft.com/b3e21c94-acd5-4767-8ba5-70b2dcfb2aaa">AgpReservePhysical</a>