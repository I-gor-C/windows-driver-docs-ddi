---
UID: NS.ntddvdeo._VIDEO_PUBLIC_ACCESS_RANGES
title: VIDEO_PUBLIC_ACCESS_RANGES
author: windows-driver-content
description: The VIDEO_PUBLIC_ACCESS_RANGES structure contains information about video resources other than frame buffers and video RAM, such as memory-mapped I/O registers or ports.
old-location: display\video_public_access_ranges.htm
old-project: display
ms.assetid: 78912da9-ab02-459c-97b0-477949d4a71d
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VIDEO_PUBLIC_ACCESS_RANGES, VIDEO_PUBLIC_ACCESS_RANGES, *PVIDEO_PUBLIC_ACCESS_RANGES
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
req.alt-api: VIDEO_PUBLIC_ACCESS_RANGES
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

# VIDEO_PUBLIC_ACCESS_RANGES structure



## -description
<p>The VIDEO_PUBLIC_ACCESS_RANGES structure contains information about video resources other than <a href="wdkgloss.f#wdkgloss.frame_buffer#wdkgloss.frame_buffer"><i>frame buffers</i></a> and video RAM, such as memory-mapped I/O registers or ports.</p>


## -syntax

````
typedef struct _VIDEO_PUBLIC_ACCESS_RANGES {
  ULONG InIoSpace;
  ULONG MappedInIoSpace;
  PVOID VirtualAddress;
} VIDEO_PUBLIC_ACCESS_RANGES, *PVIDEO_PUBLIC_ACCESS_RANGES;
````


## -struct-fields
<dl>

### -field <b>InIoSpace</b>

<dd>
<p>Indicates the location of the range. This parameter can be one of the following values, or certain bitwise combinations of these values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>VIDEO_MEMORY_SPACE_DENSE</p>
</td>
<td>
<p>Obsolete.</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MEMORY_SPACE_IO</p>
</td>
<td>
<p>The indicated address ranges are in system I/O space rather than in memory space.</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MEMORY_SPACE_MEMORY</p>
</td>
<td>
<p>The indicated address ranges are in memory space rather than in system I/O space. </p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MEMORY_SPACE_P6CACHE</p>
</td>
<td>
<p>The processor aggregates a sequence of write operations and sends them to a given cache line. The processor then flushes the cache. This flag is meaningful only when VIDEO_MEMORY_SPACE_IO is not set.</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MEMORY_SPACE_USER_MODE</p>
</td>
<td>
<p>Indicates that the address range specified should be mapped into user mode rather than kernel mode. This flag is meaningful only when VIDEO_MEMORY_SPACE_IO is not set.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>MappedInIoSpace</b>

<dd>
<p>Indicates, on the current platform, whether the registers or ports are mapped in I/O space or in memory space. A value of <b>TRUE</b> (1) indicates that the registers or ports are mapped in I/O space; a value of <b>FALSE</b> (0) indicates that the registers or ports are mapped in memory space.</p>
</dd>

### -field <b>VirtualAddress</b>

<dd>
<p>Pointer to the location of the registers or I/O ports as mapped under the current architecture.</p>
</dd>
</dl>

## -remarks
<p>VIDEO_PUBLIC_ACCESS_RANGES is similar to <a href="https://msdn.microsoft.com/library/windows/hardware/ff570498">VIDEO_ACCESS_RANGE</a> in that both are used by miniport drivers to obtain information about display resources. The principal difference is that VIDEO_PUBLIC_ACCESS_RANGES contains information about control and accelerator registers for an adapter, while VIDEO_ACCESS_RANGE is used to hold frame buffer and video RAM addresses.</p>

<p>VIDEO_PUBLIC_ACCESS_RANGES is used as an input buffer with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567829">IOCTL_VIDEO_QUERY_PUBLIC_ACCESS_RANGES</a> request.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570498">VIDEO_ACCESS_RANGE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567829">IOCTL_VIDEO_QUERY_PUBLIC_ACCESS_RANGES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VIDEO_PUBLIC_ACCESS_RANGES structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
