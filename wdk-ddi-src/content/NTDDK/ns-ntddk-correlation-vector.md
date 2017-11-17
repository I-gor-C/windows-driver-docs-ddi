---
UID: NS.ntddk.CORRELATION_VECTOR
title: CORRELATION_VECTOR
author: windows-driver-content
description: Store the correlation vector that is used to reference events and the generated logs for diagnostic purposes.
old-location: kernel\correlation_vector.htm
ms.assetid: 35c1799f-2012-42b0-95e6-6902c818a094
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CORRELATION_VECTOR
req.alt-loc: Ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: CORRELATION_VECTOR, CORRELATION_VECTOR
req.iface: 
---

# CORRELATION_VECTOR structure



## -description
<p>Store the correlation vector that is used to reference events and the generated logs
    for diagnostic purposes.</p>


## -syntax

````
typedef struct _CORRELATION_VECTOR {
  CHAR  Version;
  CHAR  Vector[RTL_CORRELATION_VECTOR_STRING_LENGTH];
} CORRELATION_VECTOR;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of the correlation vector. Possible values are: </p>
<ul>
<li>RTL_CORRELATION_VECTOR_VERSION_1</li>
<li>RTL_CORRELATION_VECTOR_VERSION_2</li>
<li>RTL_CORRELATION_VECTOR_VERSION_CURRENT</li>
</ul>
</dd>

### -field <b>Vector</b>

<dd>
<p>An array CHARs that represents the correlation vector.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h</dt>
</dl>
</td>
</tr>
</table>