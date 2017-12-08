---
UID: NF.portcls.IPortWaveRTStream.AllocatePagesForMdl
title: IPortWaveRTStream::AllocatePagesForMdl
author: windows-driver-content
description: The AllocatePagesForMdl method allocates a list of nonpaged physical memory pages and returns a pointer to a memory descriptor list (MDL) that describes them.
old-location: audio\iportwavertstream_allocatepagesformdl.htm
old-project: audio
ms.assetid: 44839b9e-f206-49e6-a9f6-14e79d1e0ae2
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IPortWaveRTStream, AllocatePagesForMdl, IPortWaveRTStream::AllocatePagesForMdl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPortWaveRTStream.AllocatePagesForMdl
req.alt-loc: Portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Passive level
req.iface: IPortWaveRTStream
---

# IPortWaveRTStream::AllocatePagesForMdl method



## -description
<p>The <code>AllocatePagesForMdl</code> method allocates a list of nonpaged physical memory pages and returns a pointer to a memory descriptor list (<a href="..\wdm\ns-wdm--mdl.md">MDL</a>) that describes them.</p>


## -syntax

````
PMDL AllocatePagesForMdl(
  [in] PHYSICAL_ADDRESS HighAddress,
  [in] SIZE_T           TotalBytes
);
````


## -parameters
<dl>

### -param HighAddress [in]

<dd>
<p>Specifies the high end of the address range from which the storage for the MDL can be allocated. The low end of the address range is implicitly zero.</p>
</dd>

### -param TotalBytes [in]

<dd>
<p>Specifies the total number of bytes to allocate for the MDL. This method always allocates an integral number of memory pages.</p>
</dd>
</dl>

## -returns
<p><code>AllocatePagesforMdl</code> returns a pointer to an MDL that describes a list of physical memory pages. If the method is unable to allocate the requested buffer, it returns <b>NULL</b>.</p>

## -remarks
<p>Since the Windows audio stack does not support a mechanism to express memory access alignment requirements for buffers, audio drivers must select a caching type for mapped memory buffers that does not impose platform-specific alignment requirements. In other words, the caching type used by the audio driver for mapped memory buffers, must not make assumptions about the memory alignment requirements for any specific platform.</p>

<p>The driver calls this method to allocate memory that can be mapped to user or kernel mode. The physical memory pages in the MDL are not necessarily contiguous in physical memory, but they all fall within the specified address range.</p>

<p>The method always allocates an integral number of pages. If sufficient memory is available, the memory allocation is the requested size rounded up to the next page. Otherwise, the memory allocation can be less than the requested size. The caller must verify how many bytes are actually allocated.</p>

<p>If the DMA controller of the audio device requires the physical memory pages in the buffer to be contiguous, the driver must call <a href="audio.iportwavertstream_allocatecontiguouspagesformdl">IPortWaveRTStream::AllocateContiguousPagesForMdl </a> instead.</p>

<p>Like the <a href="..\wdm\nf-wdm-mmallocatepagesformdl.md">MmAllocatePagesForMdl </a> function, the <code>AllocatePagesforMdl</code> method allocates memory pages that are locked (nonpaged) but unmapped. If the miniport driver wants to set up software access to this memory, the miniport driver must make a subsequent call to <a href="audio.iportwavertstream_mapallocatedpages">IPortWaveRTStream::MapAllocatedPages </a> to map the pages into kernel-mode address space. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Passive level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\portcls\nn-portcls-iportwavertstream.md">IPortWaveRTStream</a>
</dt>
<dt>
<a href="audio.iportwavertstream_allocatecontiguouspagesformdl">IPortWaveRTStream::AllocateContiguousPagesForMdl</a>
</dt>
<dt>
<a href="audio.iportwavertstream_mapallocatedpages">IPortWaveRTStream::MapAllocatedPages</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPortWaveRTStream::AllocatePagesForMdl method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
