---
UID: NF.portcls.IPortWaveRTStream.FreePagesFromMdl
title: IPortWaveRTStream::FreePagesFromMdl
author: windows-driver-content
description: The FreePagesFromMdl method frees a memory descriptor list (MDL).
old-location: audio\iportwavertstream_freepagesfrommdl.htm
old-project: audio
ms.assetid: 8839c0ab-08c5-4cc7-a526-aa1ebe2fde15
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IPortWaveRTStream, FreePagesFromMdl, IPortWaveRTStream::FreePagesFromMdl
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
req.alt-api: IPortWaveRTStream.FreePagesFromMdl
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

# IPortWaveRTStream::FreePagesFromMdl method



## -description
<p>The <code>FreePagesFromMdl</code> method frees a memory descriptor list (<a href="..\wdm\ns-wdm--mdl.md">MDL</a>).</p>


## -syntax

````
VOID FreePagesFromMdl(
  [in] PMDL MemoryDescriptorList
);
````


## -parameters
<dl>

### -param <i>MemoryDescriptorList</i> [in]

<dd>
<p>Pointer to the MDL.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The miniport driver must call this method to free an MDL that was previously allocated by calling either <a href="audio.iportwavertstream_allocatepagesformdl">IPortWaveRTStream::AllocatePagesForMdl</a> or <a href="audio.iportwavertstream_allocatecontiguouspagesformdl">IPortWaveRTStream::AllocateContiguousPagesForMdl</a>.</p>

<p><code>FreePagesFromMdl</code> frees both the physical memory pages described in the MDL and the MDL itself. On return, the MDL pointer value in the <i>MemoryDescriptorList</i> parameter is no longer valid.</p>

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
<a href="audio.iportwavertstream_allocatepagesformdl">IPortWaveRTStream::AllocatePagesForMdl</a>
</dt>
<dt>
<a href="audio.iportwavertstream_allocatecontiguouspagesformdl">IPortWaveRTStream::AllocateContiguousPagesForMdl </a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPortWaveRTStream::FreePagesFromMdl method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
