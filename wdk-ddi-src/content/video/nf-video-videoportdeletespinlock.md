---
UID: NF:video.VideoPortDeleteSpinLock
title: VideoPortDeleteSpinLock function
author: windows-driver-content
description: The VideoPortDeleteSpinLock function deletes a given spin lock.
old-location: display\videoportdeletespinlock.htm
old-project: display
ms.assetid: 74845e4d-0fa1-4625-96a7-2fddec8b901d
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: VideoPortDeleteSpinLock, VideoPortDeleteSpinLock function [Display Devices], VideoPort_Functions_d98d74d6-bf9c-441b-95e3-a3455927dd45.xml, display.videoportdeletespinlock, video/VideoPortDeleteSpinLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later versions of the Windows operating systems.
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
req.lib: Videoprt.lib
req.dll: Videoprt.sys
req.irql: "<=DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	Videoprt.sys
api_name:
-	VideoPortDeleteSpinLock
product: Windows
targetos: Windows
req.typenames: VIDEO_PORT_SERVICES
req.product: Windows 10 or later.
---


# VideoPortDeleteSpinLock function
The <b>VideoPortDeleteSpinLock</b> function deletes a given spin lock.

## Syntax

```
VIDEOPORT_API VP_STATUS VideoPortDeleteSpinLock(
  IN PVOID      HwDeviceExtension,
  IN PSPIN_LOCK SpinLock
);
```

## Parameters

`HwDeviceExtension`

Pointer to the miniport driver's device extension.

`SpinLock`

Pointer to the spin lock to delete.


## Return Value

If the spin lock is successfully deleted, <b>VideoPortDeleteSpinLock</b> returns NO_ERROR.

## Remarks

A miniport driver uses this function to delete a spin lock that was previously created in a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff570289">VideoPortCreateSpinLock</a>.

This routine cannot be called from an ISR or from a <a href="https://msdn.microsoft.com/library/windows/hardware/ff570372">VideoPortSynchronizeExecution</a> callback requested where the <i>Priority</i> parameter is set to either <b>VpMediumPriority</b> or <b>VpHighPriority</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows XP and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | video.h (include Video.h) |
| **Library** | Videoprt.lib |
| **DLL** | Videoprt.sys |
| **IRQL** | "<=DISPATCH_LEVEL" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff570289">VideoPortCreateSpinLock</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff570372">VideoPortSynchronizeExecution</a>