---
UID: NS.strmini._STREAM_METHOD_DESCRIPTOR
title: STREAM_METHOD_DESCRIPTOR
author: windows-driver-content
description: TBD.
old-location: stream\stream_method_descriptor.htm
ms.assetid: 2C35EF9F-143C-4DE2-93D0-5BCF8AADF11B
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: strmini.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STREAM_METHOD_DESCRIPTOR
req.alt-loc: 
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
ms.keywords: STREAM_METHOD_DESCRIPTOR, STREAM_METHOD_DESCRIPTOR, *PSTREAM_METHOD_DESCRIPTOR
req.iface: 
req.product: Windows 10 or later.
---

# STREAM_METHOD_DESCRIPTOR structure



## -description
<p>TBD</p>


## -syntax

````
typedef struct _STREAM_METHOD_DESCRIPTOR {
  ULONG     MethodSetID;
  PKSMETHOD Method;
  PVOID     MethodInfo;
  LONG      MethodInputSize;
  LONG      MethodOutputSize;
} STREAM_METHOD_DESCRIPTOR, *PSTREAM_METHOD_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>MethodSetID</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>Method</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>MethodInfo</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>MethodInputSize</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>MethodOutputSize</b>

<dd>
<p>TBD</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Strmini.h</dt>
</dl>
</td>
</tr>
</table>