---
UID: NF.portcls.IPortWaveRTStream.MapAllocatedPages
title: IPortWaveRTStream::MapAllocatedPages
author: windows-driver-content
description: The MapAllocatedPages method maps a list of previously allocated physical pages into a contiguous block of virtual memory that is accessible from kernel-mode.
old-location: audio\iportwavertstream_mapallocatedpages.htm
old-project: audio
ms.assetid: 90f412de-073f-4889-adf3-898cde0206b7
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: IPortWaveRTStream, MapAllocatedPages, IPortWaveRTStream::MapAllocatedPages
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
req.alt-api: IPortWaveRTStream.MapAllocatedPages
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
req.irql: Passive level.
req.iface: IPortWaveRTStream
---

# IPortWaveRTStream::MapAllocatedPages method



## -description
<p>The <code>MapAllocatedPages</code> method maps a list of previously allocated physical pages into a contiguous block of virtual memory that is accessible from kernel-mode.</p>


## -syntax

````
PVOID MapAllocatedPages(
  [in] PMDL                MemoryDescriptorList,
  [in] MEMORY_CACHING_TYPE CacheType
);
````


## -parameters
<dl>

### -param <i>MemoryDescriptorList</i> [in]

<dd>
<p>Pointer to the memory descriptor list (<a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a>) that will be mapped. The MDL can be allocated by calling either <a href="audio.iportwavertstream_allocatepagesformdl">IPortWaveRTStream::AllocatePagesForMdl </a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff536924">IPortWaveRTStream::AllocateContiguousPagesForMdl</a>.</p>
</dd>

### -param <i>CacheType</i> [in]

<dd>
<p>Specifies the cache type. Set this parameter to one of the following <a href="https://msdn.microsoft.com/library/windows/hardware/ff554430">MEMORY_CACHING_TYPE</a> enumeration values: <b>MmNonCached</b>, <b>MmCached</b>, or <b>MmWriteCombined</b>.</p>
</dd>
</dl>

## -returns
<p><code>MapAllocatedPages</code> returns the starting address of the mapped buffer in virtual memory. If the method is unable to map the buffer, it returns <b>NULL</b>.</p>

## -remarks
<p>Since the Windows audio stack does not support a mechanism to express memory access alignment requirements for buffers, audio drivers must select a caching type for mapped memory buffers that does not impose platform-specific alignment requirements. In other words, the caching type used by the audio driver for mapped memory buffers, must not make assumptions about the memory alignment requirements for any specific platform.</p>

<p>This method maps the physical memory pages in the MDL  into kernel-mode virtual memory. Typically, the miniport driver calls this method if it requires software access to the scatter-gather list for an audio buffer. In this case, the storage for the scatter-gather list must have been allocated by the <b>IPortWaveRTStream::AllocatePagesForMdl</b> or <b>IPortWaveRTStream::AllocateContiguousPagesForMdl</b> method. </p>

<p>A WaveRT miniport driver should not require software access to the audio buffer itself.</p>

<p><code>MapAllocatedPages</code> is similar in operation to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554629">MmMapLockedPagesSpecifyCache</a> function. The miniport driver is responsible for unmapping the memory prior to freeing it. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536934">IPortWaveRTStream::UnmapAllocatedPages</a>.</p>

<p>Since the Windows audio stack does not support a mechanism to express memory access alignment requirements for buffers, audio drivers must select a caching type for mapped memory buffers that does not impose platform-specific alignment requirements. In other words, the caching type used by the audio driver for mapped memory buffers, must not make assumptions about the memory alignment requirements for any specific platform.</p>

<p>This method maps the physical memory pages in the MDL  into kernel-mode virtual memory. Typically, the miniport driver calls this method if it requires software access to the scatter-gather list for an audio buffer. In this case, the storage for the scatter-gather list must have been allocated by the <b>IPortWaveRTStream::AllocatePagesForMdl</b> or <b>IPortWaveRTStream::AllocateContiguousPagesForMdl</b> method. </p>

<p>A WaveRT miniport driver should not require software access to the audio buffer itself.</p>

<p><code>MapAllocatedPages</code> is similar in operation to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554629">MmMapLockedPagesSpecifyCache</a> function. The miniport driver is responsible for unmapping the memory prior to freeing it. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536934">IPortWaveRTStream::UnmapAllocatedPages</a>.</p>

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
<p>Passive level.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536922">IPortWaveRTStream</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536925">IPortWaveRTStream::AllocatePagesForMdl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536924">IPortWaveRTStream::AllocateContiguousPagesForMdl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536934">IPortWaveRTStream::UnmapAllocatedPages</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554629">MmMapLockedPagesSpecifyCache</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554430">MEMORY_CACHING_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPortWaveRTStream::MapAllocatedPages method%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
