---
UID: NF.filterpipeline.IPrintWriteStream.WriteBytes
title: IPrintWriteStream::WriteBytes
author: windows-driver-content
description: The WriteBytes method writes a specified number of bytes to a stream.
old-location: print\iprintwritestream_writebytes.htm
old-project: print
ms.assetid: d47c836e-a291-4cc2-9688-82526f8bfb8b
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintWriteStream, WriteBytes, IPrintWriteStream::WriteBytes
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: filterpipeline.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintWriteStream.WriteBytes
req.alt-loc: filterpipeline.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: Filterpipeline.idl
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IPrintWriteStream
---

# IPrintWriteStream::WriteBytes method



## -description
<p>The <code>WriteBytes</code> method writes a specified number of bytes to a stream.</p>


## -syntax

````
HRESULT WriteBytes(
  [in]  void  pvBuffer,
  [in]  ULONG cbBuffer,
  [out] ULONG *pcbWritten
);
````


## -parameters
<dl>

### -param pvBuffer [in]

<dd>
<p>A pointer to the buffer that the bytes will be written from.</p>
</dd>

### -param cbBuffer [in]

<dd>
<p>The size of the buffer to be read from.</p>
</dd>

### -param pcbWritten [out]

<dd>
<p>A pointer to the number of bytes actually written. </p>
</dd>
</dl>

## -returns
<p><code>WriteBytes</code> returns an <b>HRESULT</b> value.</p>

## -remarks


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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Filterpipeline.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IDL</p>
</th>
<td width="70%">
<dl>
<dt>Filterpipeline.idl</dt>
</dl>
</td>
</tr>
</table>