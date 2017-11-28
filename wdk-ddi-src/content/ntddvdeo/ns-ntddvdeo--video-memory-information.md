---
UID: NS.ntddvdeo._VIDEO_MEMORY_INFORMATION
title: VIDEO_MEMORY_INFORMATION
author: windows-driver-content
description: The VIDEO_MEMORY_INFORMATION structure contains information about a mapping of video memory into system space or the private virtual address space of a user-mode process.
old-location: display\video_memory_information.htm
old-project: display
ms.assetid: 7d580d5c-b97f-4d26-9eec-165c5db66a0b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VIDEO_MEMORY_INFORMATION, VIDEO_MEMORY_INFORMATION, *PVIDEO_MEMORY_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddvdeo.h
req.include-header: Ntddvdeo.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VIDEO_MEMORY_INFORMATION
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
req.iface: 
---

# VIDEO_MEMORY_INFORMATION structure



## -description
<p>The VIDEO_MEMORY_INFORMATION structure contains information about a mapping of video memory into system space or the private virtual address space of a user-mode process. The mapping is created when an <a href="https://msdn.microsoft.com/library/windows/hardware/ff567812">IOCTL_VIDEO_MAP_VIDEO_MEMORY</a> request is sent to the video miniport driver.</p>


## -syntax

````
typedef struct _VIDEO_MEMORY_INFORMATION {
  PVOID VideoRamBase;
  ULONG VideoRamLength;
  PVOID FrameBufferBase;
  ULONG FrameBufferLength;
} VIDEO_MEMORY_INFORMATION, *PVIDEO_MEMORY_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>VideoRamBase</b>

<dd>
<p>Virtual address of the video RAM in system space or in the address space of the user-mode process that initiated the request.</p>
</dd>

### -field <b>VideoRamLength</b>

<dd>
<p>The size, in bytes, of the virtual address range that is mapped to video RAM. Memory accessible through a bank switch mechanism is not described by this value.</p>
<p>This value must be equal to the product <b>VideoMemoryBitmapHeight</b> * <b>ScreenStride</b>, where each factor in the product is a member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570521">VIDEO_MODE_INFORMATION</a> structure.</p>
</dd>

### -field <b>FrameBufferBase</b>

<dd>
<p>Pointer to the virtual address of the <a href="wdkgloss.f#wdkgloss.frame_buffer#wdkgloss.frame_buffer"><i>frame buffer</i></a> in the caller's address space. The frame buffer is the actively displayed part of video RAM.</p>
</dd>

### -field <b>FrameBufferLength</b>

<dd>
<p>Specifies the linear length of the frame buffer in the caller's virtual address space. Memory accessible through a bank switch mechanism is not described by this value.</p>
<p>This value must be equal to the product <b>VisScreenWidth</b> * <b>ScreenStride</b>, where each term in this product is a member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570521">VIDEO_MODE_INFORMATION</a> structure.</p>
</dd>
</dl>

## -remarks
<p>In the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567812">IOCTL_VIDEO_MAP_VIDEO_MEMORY</a> request, <a href="https://msdn.microsoft.com/library/windows/hardware/ff570506">VIDEO_MEMORY</a> serves as an input structure, while VIDEO_MEMORY_INFORMATION serves as an output structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570506">VIDEO_MEMORY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570521">VIDEO_MODE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567812">IOCTL_VIDEO_MAP_VIDEO_MEMORY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568153">IOCTL_VIDEO_UNMAP_VIDEO_MEMORY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VIDEO_MEMORY_INFORMATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
