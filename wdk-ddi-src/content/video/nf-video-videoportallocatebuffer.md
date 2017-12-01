---
UID: NF.video.VideoPortAllocateBuffer
title: VideoPortAllocateBuffer
author: windows-driver-content
description: The VideoPortAllocateBuffer function is obsolete in Windows 2000 and later. In its place, video miniport drivers should instead use VideoPortAllocatePool. VideoPortAllocateBuffer allocates a buffer of paged pool memory.
old-location: display\videoportallocatebuffer.htm
old-project: display
ms.assetid: 87289ea8-f727-428d-93a1-2d3b0ab44e8b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortAllocateBuffer
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
req.alt-api: VideoPortAllocateBuffer
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

# VideoPortAllocateBuffer function



## -description
<p>The <b>VideoPortAllocateBuffer</b> function is <b>obsolete</b> in Windows 2000 and later. In its place, video miniport drivers should instead use <a href="..\video\nf-video-videoportallocatepool.md">VideoPortAllocatePool</a>. </p>
<p><b>VideoPortAllocateBuffer</b> allocates a buffer of paged pool memory.</p>


## -syntax

````
VP_STATUS VideoPortAllocateBuffer(
  _In_  PVOID HwDeviceExtension,
  _In_  ULONG Size,
  _Out_ PVOID *Buffer
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>Size</i> [in]

<dd>
<p>Specifies the size of the buffer to allocate, in bytes.</p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>Is the location in which the video port driver returns a pointer to a pointer to the allocated pool memory.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortAllocateBuffer</b> returns NO_ERROR when it successfully completes the allocation request, or ERROR_NOT_ENOUGH_MEMORY if it is unable to allocate a buffer of <i>Size</i> bytes. A return value of ERROR_INSUFFICIENT_BUFFER indicates that a miniport driver has exceeded its maximum allowable allocation of memory.</p>

## -remarks
<p>A miniport driver can use the return value of this function to determine whether the buffer allocation succeeded.</p>

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
<a href="..\video\nf-video-videoportreleasebuffer.md">VideoPortReleaseBuffer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortAllocateBuffer function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
