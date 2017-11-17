---
UID: NS.smclib._T0_DATA
title: T0_DATA
author: windows-driver-content
description: The T0_DATA structure is used by the smart card driver library to process T0 I/O.
old-location: smartcrd\t0_data.htm
ms.assetid: CC827018-F6B2-48DF-BF0A-36654F866BD9
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: smartcrd
req.header: smclib.h
req.include-header: Smclib.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: T0_DATA
req.alt-loc: Smclib.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: T0_DATA, T0_DATA, *PT0_DATA
req.iface: 
req.product: Windows 10 or later.
---

# T0_DATA structure



## -description
<p>The T0_DATA structure is used by the smart card driver library to process T0 I/O. </p>


## -syntax

````
typedef struct _T0_DATA {
  ULONG Lc;
  ULONG Le;
} T0_DATA, *PT0_DATA;
````


## -struct-fields
<dl>

### -field <b>Lc</b>

<dd>
<p>Number of data bytes in the request.</p>
</dd>

### -field <b>Le</b>

<dd>
<p>Number of expected bytes from the card.</p>
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
<dt>Smclib.h (include Smclib.h)</dt>
</dl>
</td>
</tr>
</table>