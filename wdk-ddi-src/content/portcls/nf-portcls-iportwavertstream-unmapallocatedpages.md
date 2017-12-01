---
UID: NF.portcls.IPortWaveRTStream.UnmapAllocatedPages
title: IPortWaveRTStream::UnmapAllocatedPages
author: windows-driver-content
description: The UnmapAllocatedPages method releases a mapping.
old-location: audio\iportwavertstream_unmapallocatedpages.htm
old-project: audio
ms.assetid: 558636ed-4bab-42bc-8925-df01e032439a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IPortWaveRTStream, UnmapAllocatedPages, IPortWaveRTStream::UnmapAllocatedPages
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
req.alt-api: IPortWaveRTStream.UnmapAllocatedPages
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

# IPortWaveRTStream::UnmapAllocatedPages method



## -description
<p>The <code>UnmapAllocatedPages</code> method releases a mapping.</p>


## -syntax

````
VOID UnmapAllocatedPages(
  [in] PVOID BaseAddress,
  [in] PMDL  MemoryDescriptorList
);
````


## -parameters
<dl>

### -param <i>BaseAddress</i> [in]

<dd>
<p>Pointer to the base virtual address to which the physical pages were mapped.</p>
</dd>

### -param <i>MemoryDescriptorList</i> [in]

<dd>
<p>Pointer to a memory descriptor list (<a href="..\wdm\ns-wdm--mdl.md">MDL</a>) that describes the physical pages.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The miniport driver must call this method to release a mapping that was set up by a previous call to <a href="audio.iportwavertstream_mapallocatedpages">IPortWaveRTStream::MapAllocatedPages</a>. The driver must release the mapping before calling <a href="audio.iportwavertstream_freepagesfrommdl">IPortWaveRTStream::FreePagesFromMdl </a> to free the MDL.</p>

<p>This method is similar in operation to the <a href="..\wdm\nf-wdm-mmunmaplockedpages.md">MmUnmapLockedPages</a> function. </p>

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
<a href="..\portcls\nn-portcls-iportwavertstream.md">IPortWaveRTStream</a>
</dt>
<dt>
<a href="audio.iportwavertstream_mapallocatedpages">IPortWaveRTStream::MapAllocatedPages</a>
</dt>
<dt>
<a href="audio.iportwavertstream_freepagesfrommdl">IPortWaveRTStream::FreePagesFromMdl</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-mmunmaplockedpages.md">MmUnmapLockedPages</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPortWaveRTStream::UnmapAllocatedPages method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
