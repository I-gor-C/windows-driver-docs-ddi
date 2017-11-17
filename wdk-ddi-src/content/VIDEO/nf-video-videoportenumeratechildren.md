---
UID: NF.video.VideoPortEnumerateChildren
title: VideoPortEnumerateChildren
author: windows-driver-content
description: The VideoPortEnumerateChildren function allows a video miniport driver to force a reenumeration of its child devices.
old-location: display\videoportenumeratechildren.htm
ms.assetid: 41f081f3-4079-46f8-9d22-76a2d9e992b5
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: display
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortEnumerateChildren
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
req.irql: <= DISPATCH_LEVEL
ms.keywords: VideoPortEnumerateChildren
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortEnumerateChildren function



## -description
<p>The <b>VideoPortEnumerateChildren</b> function allows a video miniport driver to force a reenumeration of its child devices.</p>


## -syntax

````
VP_STATUS VideoPortEnumerateChildren(
  _In_       PVOID HwDeviceExtension,
  _Reserved_ PVOID Reserved
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>Reserved</i> [in]

<dd>
<p>Must be set to <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortEnumerateChildren</b> returns NO_ERROR.</p>

## -remarks
<p>Some devices generate an interrupt when new hardware is connected to the system, or when existing hardware is disconnected from the system. For these devices, <b>VideoPortEnumerateChildren</b> can make such system changes as seamless as possible. The following is one possible scenario that forces the reenumeration of child devices through <b>VideoPortEnumerateChildren</b>:</p>

<p>New hardware is connected, which generates an interrupt.</p>

<p>The miniport driver's interrupt handler (<a href="https://msdn.microsoft.com/523471e3-cf1e-48d2-b5f0-2f8d19ad71e0">HwVidInterrupt</a>) queues a DPC routine (<a href="https://msdn.microsoft.com/d4b443a2-3665-4e7c-b84a-5388a8fe8681">HwVidDpcRoutine</a>) by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff570339">VideoPortQueueDpc</a>.</p>

<p>The asynchronously executed DPC contains a call to <b>VideoPortEnumerateChildren</b>.</p>

<p><b>VideoPortEnumerateChildren</b> causes <a href="https://msdn.microsoft.com/175030c1-95d9-4a3b-976c-16e04852cb91">HwVidGetVideoChildDescriptor</a> to be called, allowing the Plug and Play Manager to enumerate all of the adapter's child devices.</p>

<p>Some devices generate an interrupt when new hardware is connected to the system, or when existing hardware is disconnected from the system. For these devices, <b>VideoPortEnumerateChildren</b> can make such system changes as seamless as possible. The following is one possible scenario that forces the reenumeration of child devices through <b>VideoPortEnumerateChildren</b>:</p>

<p>New hardware is connected, which generates an interrupt.</p>

<p>The miniport driver's interrupt handler (<a href="https://msdn.microsoft.com/523471e3-cf1e-48d2-b5f0-2f8d19ad71e0">HwVidInterrupt</a>) queues a DPC routine (<a href="https://msdn.microsoft.com/d4b443a2-3665-4e7c-b84a-5388a8fe8681">HwVidDpcRoutine</a>) by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff570339">VideoPortQueueDpc</a>.</p>

<p>The asynchronously executed DPC contains a call to <b>VideoPortEnumerateChildren</b>.</p>

<p><b>VideoPortEnumerateChildren</b> causes <a href="https://msdn.microsoft.com/175030c1-95d9-4a3b-976c-16e04852cb91">HwVidGetVideoChildDescriptor</a> to be called, allowing the Plug and Play Manager to enumerate all of the adapter's child devices.</p>

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
<p>Available in Windows 2000 and later versions of the Windows operating systems.</p>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/175030c1-95d9-4a3b-976c-16e04852cb91">HwVidGetVideoChildDescriptor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/523471e3-cf1e-48d2-b5f0-2f8d19ad71e0">HwVidInterrupt</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/d4b443a2-3665-4e7c-b84a-5388a8fe8681">HwVidDpcRoutine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570339">VideoPortQueueDpc</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortEnumerateChildren function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
