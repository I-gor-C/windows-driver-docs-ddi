---
UID: NF.video.VideoPortAllocateContiguousMemory
title: VideoPortAllocateContiguousMemory
author: windows-driver-content
description: The VideoPortAllocateContiguousMemory function is obsolete in Windows 2000 and later.
old-location: display\videoportallocatecontiguousmemory.htm
old-project: display
ms.assetid: ba23f4d4-7e3d-4bfc-acf7-68dab01d2f61
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortAllocateContiguousMemory
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
req.alt-api: VideoPortAllocateContiguousMemory
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

# VideoPortAllocateContiguousMemory function



## -description
<p>The <b>VideoPortAllocateContiguousMemory</b> function is <b>obsolete</b> in Windows 2000 and later. Video miniport drivers should use <a href="..\video\nf-video-videoportallocatecommonbuffer.md">VideoPortAllocateCommonBuffer</a> in its place.</p>
<p><b>VideoPortAllocateContiguousMemory</b> allocates a range of physically contiguous, cache-aligned memory from the nonpaged pool.</p>


## -syntax

````
PVOID VideoPortAllocateContiguousMemory(
  _In_ PVOID            HwDeviceExtension,
  _In_ ULONG            NumberOfBytes,
  _In_ PHYSICAL_ADDRESS HighestAcceptableAddress
);
````


## -parameters
<dl>

### -param HwDeviceExtension [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param NumberOfBytes [in]

<dd>
<p>Specifies the size in bytes of the block of contiguous memory to be allocated. </p>
</dd>

### -param HighestAcceptableAddress [in]

<dd>
<p>Specifies the highest valid physical address the miniport driver can use. For example, if a device can only reference physical memory in the lower 16MB, this value would be set to 0x00000000FFFFFF.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortAllocateContiguousMemory</b> returns the base virtual address for the allocated memory, if the call is successful. If the request cannot be satisfied, <b>NULL</b> is returned.</p>

## -remarks
<p><b>VideoPortAllocateContiguousMemory</b> can be called to allocate a contiguous block of physical memory for a long-term internal buffer.</p>

<p>A miniport driver that must use contiguous memory should allocate only what it needs during driver initialization because nonpaged pool is likely to become fragmented as the system runs. If the miniport driver is unloaded, it must deallocate the memory. Contiguous allocations are aligned on an integral multiple of the processor's data-cache-line size to prevent cache and coherency problems.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortAllocateContiguousMemory function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
