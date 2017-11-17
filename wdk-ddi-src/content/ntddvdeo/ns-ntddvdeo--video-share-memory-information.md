---
UID: NS.ntddvdeo._VIDEO_SHARE_MEMORY_INFORMATION
title: VIDEO_SHARE_MEMORY_INFORMATION
author: windows-driver-content
description: The VIDEO_SHARE_MEMORY_INFORMATION structure is used to communicate to the display driver that a request for a block of user-mode memory has been fulfilled.
old-location: display\video_share_memory_information.htm
ms.assetid: 004ecb65-a462-45e5-a647-9655727b202b
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: ntddvdeo.h
req.include-header: Ntddvdeo.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VIDEO_SHARE_MEMORY_INFORMATION
req.alt-loc: ntddvdeo.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: VIDEO_SHARE_MEMORY_INFORMATION, VIDEO_SHARE_MEMORY_INFORMATION, *PVIDEO_SHARE_MEMORY_INFORMATION
req.iface: 
---

# VIDEO_SHARE_MEMORY_INFORMATION structure



## -description
<p>The VIDEO_SHARE_MEMORY_INFORMATION structure is used to communicate to the display driver that a request for a block of user-mode memory has been fulfilled.</p>


## -syntax

````
typedef struct _VIDEO_SHARE_MEMORY_INFORMATION {
  ULONG SharedViewOffset;
  ULONG SharedViewSize;
  PVOID VirtualAddress;
} VIDEO_SHARE_MEMORY_INFORMATION, *PVIDEO_SHARE_MEMORY_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>SharedViewOffset</b>

<dd>
<p>Indicates the offset, in bytes, from the beginning of the <a href="wdkgloss.f#wdkgloss.frame_buffer#wdkgloss.frame_buffer"><i>frame buffer</i></a>.</p>
</dd>

### -field <b>SharedViewSize</b>

<dd>
<p>Indicates the size, in bytes, of the frame buffer. The value of this member will always be a multiple of 64 KB.</p>
</dd>

### -field <b>VirtualAddress</b>

<dd>
<p>Indicates the address in virtual memory at which the requested memory was mapped.</p>
</dd>
</dl>

## -remarks
<p>When an application must have access to user-mode video memory, the display driver can call into the video miniport driver by sending it an <a href="https://msdn.microsoft.com/library/windows/hardware/ff568149">IOCTL_VIDEO_SHARE_VIDEO_MEMORY</a> request. The miniport driver uses a <a href="https://msdn.microsoft.com/library/windows/hardware/ff570548">VIDEO_SHARE_MEMORY</a> structure as an input buffer, and communicates back to the display driver a VIDEO_SHARE_MEMORY_INFORMATION structure. </p>

<p>The video miniport driver fills out a VIDEO_SHARE_MEMORY_INFORMATION structure based on information in a VIDEO_SHARE_MEMORY structure. The following table summarizes how the information is used:</p>

<p><b>ProcessHandle</b></p>

<p>Is not used.</p>

<p><b>ViewOffset</b></p>

<p>Copied directly to <b>SharedViewOffset</b>.</p>

<p><b>ViewSize</b></p>

<p>Values that are multiples of 64 KB are copied directly to <b>SharedViewSize</b>. Other values are rounded up to the next larger multiple of 64 KB. </p>

<p><b>RequestedVirtualAddress</b></p>

<p>If <b>NULL</b>, the miniport driver determines the address of a frame buffer to assign to <b>VirtualAddress</b>. If non-<b>NULL</b>, the miniport driver attempts to assign that value to <b>VirtualAddress</b>.</p>

<p> </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddvdeo.h (include Ntddvdeo.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570548">VIDEO_SHARE_MEMORY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568149">IOCTL_VIDEO_SHARE_VIDEO_MEMORY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VIDEO_SHARE_MEMORY_INFORMATION structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
