---
UID: NS.ks.PKS_COMPRESSION
title: PKS_COMPRESSION
author: windows-driver-content
description: The KS_COMPRESSION structure defines the compression of frames on an output pin.
old-location: stream\ks_compression.htm
ms.assetid: 065f51c3-f476-4f04-880a-5c42e493d458
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_COMPRESSION
req.alt-loc: ks.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: PKS_COMPRESSION, KS_COMPRESSION, *PKS_COMPRESSION
req.iface: 
---

# PKS_COMPRESSION structure



## -description
<p>The KS_COMPRESSION structure defines the compression of frames on an output pin.</p>


## -syntax

````
typedef struct {
  ULONG RatioNumerator;
  ULONG RatioDenominator;
  ULONG RatioConstantMargin;
} KS_COMPRESSION, *PKS_COMPRESSION;
````


## -struct-fields
<dl>

### -field <b>RatioNumerator</b>

<dd>
<p>Specifies the numerator of the compression/expansion ratio.</p>
</dd>

### -field <b>RatioDenominator</b>

<dd>
<p>Specifies the denominator of the compression/expansion ratio.</p>
</dd>

### -field <b>RatioConstantMargin</b>

<dd>
<p>Specifies a scalar constant to apply to the compression ratio. Set this to zero for no compression.</p>
</dd>
</dl>

## -remarks
<p>For compression, specify a fraction less than 1. For decompression, specify a fraction greater than 1. For example, a compressor might specify 1:3. A decompressor could specify 3:1.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>