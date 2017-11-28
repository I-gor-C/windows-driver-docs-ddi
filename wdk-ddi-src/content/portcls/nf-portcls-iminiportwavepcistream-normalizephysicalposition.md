---
UID: NF.portcls.IMiniportWavePciStream.NormalizePhysicalPosition
title: IMiniportWavePciStream::NormalizePhysicalPosition
author: windows-driver-content
description: The NormalizePhysicalPosition method converts a physical buffer position to a time-based value.
old-location: audio\iminiportwavepcistream_normalizephysicalposition.htm
old-project: audio
ms.assetid: 4ae4dc8d-3502-40c1-8109-6935990a7091
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: IMiniportWavePciStream, NormalizePhysicalPosition, IMiniportWavePciStream::NormalizePhysicalPosition
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
req.alt-api: IMiniportWavePciStream.NormalizePhysicalPosition
req.alt-loc: portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
req.iface: IMiniportWavePciStream
---

# IMiniportWavePciStream::NormalizePhysicalPosition method



## -description
<p>The <code>NormalizePhysicalPosition</code> method converts a physical buffer position to a time-based value.</p>


## -syntax

````
NTSTATUS NormalizePhysicalPosition(
  [in, out] PLONGLONG PhysicalPosition
);
````


## -parameters
<dl>

### -param <i>PhysicalPosition</i> [in, out]

<dd>
<p>Pointer to a caller-allocated buffer that contains either the physical position or time-based value. On entry, this buffer contains the physical-position value that is to be converted. On return, the buffer contains the converted value, which is time-based.</p>
</dd>
</dl>

## -returns
<p><code>NormalizePhysicalPosition</code> returns STATUS_SUCCESS if the call was successful. Otherwise, the method returns an appropriate error code.</p>

## -remarks
<p>Given a physical position based on the actual number of bytes transferred, the <code>NormalizePhysicalPosition</code> method converts the position to a time-based value that is expressed in 100-nanosecond units.</p>

<p>Given a physical position based on the actual number of bytes transferred, the <code>NormalizePhysicalPosition</code> method converts the position to a time-based value that is expressed in 100-nanosecond units.</p>

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
<p>Any level</p>
</td>
</tr>
</table>