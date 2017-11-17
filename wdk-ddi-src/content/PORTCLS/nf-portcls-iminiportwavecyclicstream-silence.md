---
UID: NF.portcls.IMiniportWaveCyclicStream.Silence
title: IMiniportWaveCyclicStream::Silence
author: windows-driver-content
description: The Silence method is used to copy silence samples to a specified buffer.
old-location: audio\iminiportwavecyclicstream_silence.htm
ms.assetid: e2acf3f5-d054-44c4-8ab9-ffd1b934f700
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: audio
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IMiniportWaveCyclicStream.Silence
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
ms.keywords: IMiniportWaveCyclicStream, Silence, IMiniportWaveCyclicStream::Silence
req.iface: IMiniportWaveCyclicStream
---

# IMiniportWaveCyclicStream::Silence method



## -description
<p>The <code>Silence</code> method is used to copy silence samples to a specified buffer.</p>


## -syntax

````
void Silence(
  [in] PVOID Buffer,
  [in] ULONG ByteCount
);
````


## -parameters
<dl>

### -param <i>Buffer</i> [in]

<dd>
<p>Pointer in kernel virtual-address space to the start of the buffer to which the silence samples are to be written. The buffer must be large enough to contain at least the number of bytes specified in <i>ByteCount</i>.</p>
</dd>

### -param <i>ByteCount</i> [in]

<dd>
<p>Specifies the number of bytes of silence to be written to the buffer.</p>
</dd>
</dl>

## -returns
<p><code>Silence</code> returns STATUS_SUCCESS if the call was successful. Otherwise, the method returns an appropriate error code.</p>

## -remarks
<p>Windows treats 8-bit PCM values as unsigned, and it treats 16-bit and larger PCM values as signed. When filling a portion of an 8-bit PCM buffer with silence, the <code>Silence</code> method sets each byte to the value 0x80. When writing silence to a buffer containing 16-bit or larger PCM values, the method fills the specified portion of the buffer with zeros.</p>

<p>Windows treats 8-bit PCM values as unsigned, and it treats 16-bit and larger PCM values as signed. When filling a portion of an 8-bit PCM buffer with silence, the <code>Silence</code> method sets each byte to the value 0x80. When writing silence to a buffer containing 16-bit or larger PCM values, the method fills the specified portion of the buffer with zeros.</p>

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