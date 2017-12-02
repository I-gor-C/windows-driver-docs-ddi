---
UID: NF.portcls.IPortWaveRTStream.GetPhysicalPageAddress
title: IPortWaveRTStream::GetPhysicalPageAddress
author: windows-driver-content
description: The GetPhysicalPageAddress method returns the physical address for a page within a memory descriptor list (MDL).
old-location: audio\iportwavertstream_getphysicalpageaddress.htm
old-project: audio
ms.assetid: 24c22102-f91d-4ea1-81fb-98052b8d0153
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IPortWaveRTStream, GetPhysicalPageAddress, IPortWaveRTStream::GetPhysicalPageAddress
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
req.alt-api: IPortWaveRTStream.GetPhysicalPageAddress
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

# IPortWaveRTStream::GetPhysicalPageAddress method



## -description
<p>The <code>GetPhysicalPageAddress</code> method returns the physical address for a page within a memory descriptor list (<a href="..\wdm\ns-wdm--mdl.md">MDL</a>).</p>


## -syntax

````
PHYSICAL_ADDRESS GetPhysicalPageAddress(
  [in] PMDL  MemoryDescriptorList,
  [in] ULONG Index
);
````


## -parameters
<dl>

### -param MemoryDescriptorList [in]

<dd>
<p>Pointer to the MDL.</p>
</dd>

### -param Index [in]

<dd>
<p>Index to the target page within the MDL.</p>
</dd>
</dl>

## -returns
<p>The <code>GetPhysicalPageAddress</code> method returns the physical address for a page within an MDL.</p>

## -remarks
<p>The miniport driver calls this method to determine the physical memory address for pages within an MDL that was previously allocated by calling either <a href="audio.iportwavertstream_allocatepagesformdl">IPortWaveRTStream::AllocatePagesForMdl</a> or <b>IPortWaveRTStream::AllocateContiguousPagesForMdl</b>.</p>

<p>The miniport typically calls this for each page in the MDL in order to program the physical address into the DMA.  The <i>Index</i> parameter is used to select the desired page, and can range from zero to the count returned by <a href="audio.iportwavertstream_getphysicalpagescount">GetPhysicalPagesCount</a>.</p>

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
<a href="audio.iportwavertstream_allocatepagesformdl">IPortWaveRTStream::AllocatePagesForMdl</a>
</dt>
<dt>
<a href="audio.iportwavertstream_allocatecontiguouspagesformdl">IPortWaveRTStream::AllocateContiguousPagesForMdl</a>
</dt>
<dt>
<a href="audio.iportwavertstream_getphysicalpagescount">IPortWaveRTStream::GetPhysicalPagesCount </a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPortWaveRTStream::GetPhysicalPageAddress method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
