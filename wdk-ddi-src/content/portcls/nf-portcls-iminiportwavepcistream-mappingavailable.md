---
UID: NF.portcls.IMiniportWavePciStream.MappingAvailable
title: IMiniportWavePciStream::MappingAvailable
author: windows-driver-content
description: The MappingAvailable method indicates that a new mapping is available.
old-location: audio\iminiportwavepcistream_mappingavailable.htm
old-project: audio
ms.assetid: 11126cc9-43a1-41b1-adc9-13af57157d74
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: IMiniportWavePciStream, MappingAvailable, IMiniportWavePciStream::MappingAvailable
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IMiniportWavePciStream.MappingAvailable
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
req.irql: <= DISPATCH_LEVEL (see Remarks section)
req.iface: IMiniportWavePciStream
---

# IMiniportWavePciStream::MappingAvailable method



## -description
<p>The <code>MappingAvailable</code> method indicates that a new mapping is available.</p>


## -syntax

````
VOID MappingAvailable(
    None
);
````


## -parameters
<dl>

### -param <i>None</i> 

<dd></dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The port driver calls the <code>MappingAvailable</code> method to notify the miniport driver that a new mapping has become available, but it does so only when the miniport driver's previous request for mapping through <a href="https://msdn.microsoft.com/library/windows/hardware/ff536909">IPortWavePciStream::GetMapping</a> has been refused.</p>

<p>The port driver (Portcls.sys) can call the <code>MappingAvailable</code> method at any level equal to or below DISPATCH_LEVEL, depending on the circumstances under which the call is made. As a result, the <code>MappingAvailable</code> method must be in a non-paged code segment and can only touch non-paged code.</p>

<p>See the discussion of allocator framing in <a href="NULL">WavePci Latency</a>.</p>

<p>The port driver calls the <code>MappingAvailable</code> method to notify the miniport driver that a new mapping has become available, but it does so only when the miniport driver's previous request for mapping through <a href="https://msdn.microsoft.com/library/windows/hardware/ff536909">IPortWavePciStream::GetMapping</a> has been refused.</p>

<p>The port driver (Portcls.sys) can call the <code>MappingAvailable</code> method at any level equal to or below DISPATCH_LEVEL, depending on the circumstances under which the call is made. As a result, the <code>MappingAvailable</code> method must be in a non-paged code segment and can only touch non-paged code.</p>

<p>See the discussion of allocator framing in <a href="NULL">WavePci Latency</a>.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536725">IMiniportWavePciStream</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536909">IPortWavePciStream::GetMapping</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportWavePciStream::MappingAvailable method%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
