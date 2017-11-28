---
UID: NF.filterpipeline.IPrintReadStream.ReadBytes
title: IPrintReadStream::ReadBytes
author: windows-driver-content
description: The ReadBytes method reads a number of bytes into a buffer.
old-location: print\iprintreadstream_readbytes.htm
old-project: print
ms.assetid: 41ba600d-8b89-4e07-950a-a2518c2572a6
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintReadStream, ReadBytes, IPrintReadStream::ReadBytes
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
req.alt-api: IPrintReadStream.ReadBytes
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
req.iface: IPrintReadStream
---

# IPrintReadStream::ReadBytes method



## -description
<p>The <code>ReadBytes</code> method reads a number of bytes into a buffer.</p>


## -syntax

````
HRESULT ReadBytes(
  [out] void  *pvBuffer,
  [in]  ULONG cbRequested,
  [out] ULONG *pcbRead,
  [out] BOOL  *pbEndOfFile
);
````


## -parameters
<dl>

### -param <i>pvBuffer</i> [out]

<dd>
<p>A pointer to the buffer that the bytes will be read into..</p>
</dd>

### -param <i>cbRequested</i> [in]

<dd>
<p>The number of bytes that are requested for the read.</p>
</dd>

### -param <i>pcbRead</i> [out]

<dd>
<p>A pointer to the number of bytes actually read.</p>
</dd>

### -param <i>pbEndOfFile</i> [out]

<dd>
<p>A pointer to a <b>BOOL</b> value that indicates whether the end of file (EOF) was read.</p>
</dd>
</dl>

## -returns
<p><code>ReadBytes</code> returns an <b>HRESULT</b> value.</p>

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