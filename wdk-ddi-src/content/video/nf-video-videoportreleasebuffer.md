---
UID: NF.video.VideoPortReleaseBuffer
title: VideoPortReleaseBuffer
author: windows-driver-content
description: The VideoPortReleaseBuffer function is obsolete in Windows 2000 and later. In its place, video miniport drivers should instead use VideoPortFreePool. VideoPortReleaseBuffer deallocates a block of paged pool memory.
old-location: display\videoportreleasebuffer.htm
old-project: display
ms.assetid: 627f43e7-1561-4822-b2b6-a49b54550bf5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortReleaseBuffer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortReleaseBuffer
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

# VideoPortReleaseBuffer function



## -description
<p>The <b>VideoPortReleaseBuffer</b> function is <b>obsolete</b> in Windows 2000 and later. In its place, video miniport drivers should instead use <a href="..\video\nf-video-videoportfreepool.md">VideoPortFreePool</a>. </p>
<p><b>VideoPortReleaseBuffer</b> deallocates a block of paged pool memory.</p>


## -syntax

````
VOID VideoPortReleaseBuffer(
  _In_ PVOID HwDeviceExtension,
  _In_ PVOID Buffer
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>Specifies the address of the block of pool memory being deallocated.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>This function releases memory allocated by <a href="..\video\nf-video-videoportallocatebuffer.md">VideoPortAllocateBuffer</a>. A miniport driver must not access the memory block to which <i>Buffer</i> points after it has been freed. </p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\video\nf-video-videoportallocatebuffer.md">VideoPortAllocateBuffer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortReleaseBuffer function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
