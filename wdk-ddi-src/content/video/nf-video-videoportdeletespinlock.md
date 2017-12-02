---
UID: NF.video.VideoPortDeleteSpinLock
title: VideoPortDeleteSpinLock
author: windows-driver-content
description: The VideoPortDeleteSpinLock function deletes a given spin lock.
old-location: display\videoportdeletespinlock.htm
old-project: display
ms.assetid: 74845e4d-0fa1-4625-96a7-2fddec8b901d
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortDeleteSpinLock
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
req.alt-api: VideoPortDeleteSpinLock
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortDeleteSpinLock function



## -description
<p>The <b>VideoPortDeleteSpinLock</b> function deletes a given spin lock.</p>


## -syntax

````
VP_STATUS VideoPortDeleteSpinLock(
  _In_ PVOID      HwDeviceExtension,
  _In_ PSPIN_LOCK SpinLock
);
````


## -parameters
<dl>

### -param HwDeviceExtension [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param SpinLock [in]

<dd>
<p>Pointer to the spin lock to delete.</p>
</dd>
</dl>

## -returns
<p>If the spin lock is successfully deleted, <b>VideoPortDeleteSpinLock</b> returns NO_ERROR.</p>

## -remarks
<p>A miniport driver uses this function to delete a spin lock that was previously created in a call to <a href="..\video\nf-video-videoportcreatespinlock.md">VideoPortCreateSpinLock</a>.</p>

<p>This routine cannot be called from an ISR or from a <a href="..\video\nf-video-videoportsynchronizeexecution.md">VideoPortSynchronizeExecution</a> callback requested where the <i>Priority</i> parameter is set to either <b>VpMediumPriority</b> or <b>VpHighPriority</b>.</p>

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
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\video\nf-video-videoportcreatespinlock.md">VideoPortCreateSpinLock</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportsynchronizeexecution.md">VideoPortSynchronizeExecution</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortDeleteSpinLock function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
