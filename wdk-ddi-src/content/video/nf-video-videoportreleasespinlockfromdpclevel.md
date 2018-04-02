---
UID: NF:video.VideoPortReleaseSpinLockFromDpcLevel
title: VideoPortReleaseSpinLockFromDpcLevel function
author: windows-driver-content
description: The VideoPortReleaseSpinLockFromDpcLevel function releases the spin lock obtained by a previous call to VideoPortAcquireSpinLockAtDpcLevel.
old-location: display\videoportreleasespinlockfromdpclevel.htm
old-project: display
ms.assetid: 375158e7-3fb5-4e49-a7cf-ee9a1e5c07ca
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: VideoPortReleaseSpinLockFromDpcLevel, VideoPortReleaseSpinLockFromDpcLevel function [Display Devices], VideoPort_Functions_2c3a3aa1-4ef4-4b7f-8cdf-b658a1128c35.xml, display.videoportreleasespinlockfromdpclevel, video/VideoPortReleaseSpinLockFromDpcLevel
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
req.irql: DISPATCH_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	Videoprt.sys
api_name:
-	VideoPortReleaseSpinLockFromDpcLevel
product: Windows
targetos: Windows
req.typenames: VIDEO_PORT_SERVICES
req.product: Windows 10 or later.
---


# VideoPortReleaseSpinLockFromDpcLevel function
The <b>VideoPortReleaseSpinLockFromDpcLevel</b> function releases the spin lock obtained by a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff570176">VideoPortAcquireSpinLockAtDpcLevel</a>.

## Syntax

```
VIDEOPORT_API VOID VideoPortReleaseSpinLockFromDpcLevel(
  PVOID                                                                     HwDeviceExtension,
  _Requires_lock_held_(*_Curr_)_Releases_lock_(*_Curr_) PSPIN_LOCK SpinLock 
);
```

## Parameters

`HwDeviceExtension`

Pointer to the miniport driver's device extension.

`Arg1`




## Return Value

None

## Remarks

Miniport drivers call <b>VideoPortReleaseSpinLockFromDpcLevel</b> to release a spin lock acquired by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff570176">VideoPortAcquireSpinLockAtDpcLevel</a>.

It is an error to call <b>VideoPortReleaseSpinLockFromDpcLevel</b> if the given spin lock was acquired by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff570175">VideoPortAcquireSpinLock</a> because the caller's original IRQL is not restored, which can cause deadlocks or fatal page faults.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows XP and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | video.h (include Video.h) |
| **Library** | Videoprt.lib |
| **DLL** | Videoprt.sys |
| **IRQL** | DISPATCH_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff570175">VideoPortAcquireSpinLock</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff570176">VideoPortAcquireSpinLockAtDpcLevel</a>