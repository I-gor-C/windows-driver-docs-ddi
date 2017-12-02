---
UID: NF.video.VideoPortCreateSpinLock
title: VideoPortCreateSpinLock
author: windows-driver-content
description: The VideoPortCreateSpinLock function creates a spin lock.
old-location: display\videoportcreatespinlock.htm
old-project: display
ms.assetid: bb5f3b3e-3358-4181-9c4d-1871be1a7b7b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortCreateSpinLock
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
req.alt-api: VideoPortCreateSpinLock
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
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortCreateSpinLock function



## -description
<p>The <b>VideoPortCreateSpinLock</b> function creates a spin lock.</p>


## -syntax

````
VP_STATUS VideoPortCreateSpinLock(
  _In_  PVOID      HwDeviceExtension,
  _Out_ PSPIN_LOCK *SpinLock
);
````


## -parameters
<dl>

### -param HwDeviceExtension [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param SpinLock [out]

<dd>
<p>Pointer to a memory location that will receive a pointer to the newly created spin lock.</p>
</dd>
</dl>

## -returns
<p>On success the function returns NO_ERROR. If an error occurs, the function returns an appropriate error code.</p>

## -remarks
<p>This routine must be called before an initial call to <a href="..\video\nf-video-videoportacquirespinlock.md">VideoPortAcquireSpinLock</a> or to any other support routine that requires a spin lock as an argument. </p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\video\nf-video-videoportdeletespinlock.md">VideoPortDeleteSpinLock</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportacquirespinlock.md">VideoPortAcquireSpinLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortCreateSpinLock function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
