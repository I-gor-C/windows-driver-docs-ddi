---
UID: NF:video.VideoPortReleaseSpinLock
title: VideoPortReleaseSpinLock function
author: windows-driver-content
description: The VideoPortReleaseSpinLock function releases ownership of a given spin lock and restores the original IRQL at which the caller was running.
old-location: display\videoportreleasespinlock.htm
old-project: display
ms.assetid: 8ce2006e-e66c-4b2d-8d26-2eba8d8e2864
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: VideoPortReleaseSpinLock, VideoPortReleaseSpinLock function [Display Devices], VideoPort_Functions_43cceda5-f5eb-4567-97f5-d53d0bf93c0b.xml, display.videoportreleasespinlock, video/VideoPortReleaseSpinLock
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
req.irql: DISPATCH_LEVEL (see Remarks section)
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	Videoprt.sys
api_name:
-	VideoPortReleaseSpinLock
product: Windows
targetos: Windows
req.typenames: VIDEO_PORT_SERVICES
req.product: Windows 10 or later.
---


# VideoPortReleaseSpinLock function
The <b>VideoPortReleaseSpinLock</b> function releases ownership of a given spin lock and restores the original IRQL at which the caller was running.

## Syntax

```
VIDEOPORT_API VOID VideoPortReleaseSpinLock(
  PVOID                                                                     HwDeviceExtension,
  _Requires_lock_held_(*_Curr_)_Releases_lock_(*_Curr_) PSPIN_LOCK SpinLock ,
  _IRQL_restores_ UCHAR                                                     NewIrql
);
```

## Parameters

`HwDeviceExtension`

Pointer to the miniport driver's device extension.

`Arg1`



`NewIrql`

Specifies the IRQL to be restored.


## Return Value

None

## Remarks

This call is the inverse of <a href="https://msdn.microsoft.com/library/windows/hardware/ff570175">VideoPortAcquireSpinLock</a>. The <i>NewIrql</i> value must be the same as the value pointed to by <i>OldIrql</i> when <b>VideoPortAcquireSpinLock </b>returned.

Callers of <b>VideoPortReleaseSpinLock</b> must be running at IRQL = DISPATCH_LEVEL. On return from this routine, IRQL is restored to the <i>NewIrql</i> value.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows XP and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | video.h (include Video.h) |
| **Library** | Videoprt.lib |
| **DLL** | Videoprt.sys |
| **IRQL** | DISPATCH_LEVEL (see Remarks section) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff570175">VideoPortAcquireSpinLock</a>