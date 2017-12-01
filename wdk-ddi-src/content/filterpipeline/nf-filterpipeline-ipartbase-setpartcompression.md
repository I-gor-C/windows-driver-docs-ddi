---
UID: NF.filterpipeline.IPartBase.SetPartCompression
title: IPartBase::SetPartCompression
author: windows-driver-content
description: The SetPartCompression method sets the compression of the part.
old-location: print\ipartbase_setpartcompression.htm
old-project: print
ms.assetid: 4e407266-4789-4de7-bcc8-7e9bb54804ed
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPartBase, SetPartCompression, IPartBase::SetPartCompression
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
req.alt-api: IPartBase.SetPartCompression
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
req.iface: IPartBase
---

# IPartBase::SetPartCompression method



## -description
<p>The <b>SetPartCompression</b> method sets the compression of the part.</p>


## -syntax

````
HRESULT SetPartCompression(
  [in] EXpsCompressionOptions compression
);
````


## -parameters
<dl>

### -param <i>compression</i> [in]

<dd>
<p>A <a href="print.expscompressionoptions">ExpsCompressionOptions</a>-typed value that describes the compression option for the part.</p>
</dd>
</dl>

## -returns
<p><b>SetPartCompression</b> returns an <b>HRESULT</b> value.</p>

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