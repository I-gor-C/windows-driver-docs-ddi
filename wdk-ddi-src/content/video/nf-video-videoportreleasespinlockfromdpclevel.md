---
UID: NF.video.VideoPortReleaseSpinLockFromDpcLevel
title: VideoPortReleaseSpinLockFromDpcLevel
author: windows-driver-content
description: The VideoPortReleaseSpinLockFromDpcLevel function releases the spin lock obtained by a previous call to VideoPortAcquireSpinLockAtDpcLevel.
old-location: display\videoportreleasespinlockfromdpclevel.htm
old-project: display
ms.assetid: 375158e7-3fb5-4e49-a7cf-ee9a1e5c07ca
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortReleaseSpinLockFromDpcLevel
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
req.alt-api: VideoPortReleaseSpinLockFromDpcLevel
req.alt-loc: Videoprt.sys
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
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortReleaseSpinLockFromDpcLevel function



## -description
<p>The <b>VideoPortReleaseSpinLockFromDpcLevel</b> function releases the spin lock obtained by a previous call to <a href="..\video\nf-video-videoportacquirespinlockatdpclevel.md">VideoPortAcquireSpinLockAtDpcLevel</a>.</p>


## -syntax

````
VOID VideoPortReleaseSpinLockFromDpcLevel(
  _In_    PVOID      HwDeviceExtension,
  _Inout_ PSPIN_LOCK SpinLock
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>SpinLock</i> [in, out]

<dd>
<p>Pointer to a memory location that contains the spin lock to be released.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Miniport drivers call <b>VideoPortReleaseSpinLockFromDpcLevel</b> to release a spin lock acquired by calling <a href="..\video\nf-video-videoportacquirespinlockatdpclevel.md">VideoPortAcquireSpinLockAtDpcLevel</a>.</p>

<p>It is an error to call <b>VideoPortReleaseSpinLockFromDpcLevel</b> if the given spin lock was acquired by calling <a href="..\video\nf-video-videoportacquirespinlock.md">VideoPortAcquireSpinLock</a> because the caller's original IRQL is not restored, which can cause deadlocks or fatal page faults. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows XP and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\video\nf-video-videoportacquirespinlockatdpclevel.md">VideoPortAcquireSpinLockAtDpcLevel</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportacquirespinlock.md">VideoPortAcquireSpinLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortReleaseSpinLockFromDpcLevel function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
