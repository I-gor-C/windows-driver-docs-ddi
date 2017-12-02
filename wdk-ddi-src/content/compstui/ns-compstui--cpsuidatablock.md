---
UID: NS.compstui._CPSUIDATABLOCK
title: CPSUIDATABLOCK
author: windows-driver-content
description: The CPSUIDATABLOCK structure is used as a parameter for the ComPropSheet function, if the function code is CPSFUNC_SET_DATABLOCK or CPSFUNC_QUERY_DATABLOCK.
old-location: print\cpsuidatablock.htm
old-project: print
ms.assetid: c5b488ac-dd8d-4484-81ca-b64fdf517100
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: CPSUIDATABLOCK, CPSUIDATABLOCK, *PCPSUIDATABLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: compstui.h
req.include-header: Compstui.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CPSUIDATABLOCK
req.alt-loc: compstui.h
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
req.iface: 
---

# CPSUIDATABLOCK structure



## -description
<p>The CPSUIDATABLOCK structure is used as a parameter for the <a href="print.compropsheet">ComPropSheet</a> function, if the function code is <a href="print.cpsfunc_set_datablock">CPSFUNC_SET_DATABLOCK</a> or <a href="print.cpsfunc_query_datablock">CPSFUNC_QUERY_DATABLOCK</a>.</p>


## -syntax

````
typedef struct _CPSUIDATABLOCK {
  DWORD  cbData;
  LPBYTE pbData;
} CPSUIDATABLOCK, *PCPSUIDATABLOCK;
````


## -struct-fields
<dl>

### -field cbData

<dd>
<p>Size, in bytes of the buffer pointed to by <b>pbData</b>.</p>
</dd>

### -field pbData

<dd>
<p>Pointer to a caller-allocated buffer.</p>
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
<dt>Compstui.h (include Compstui.h)</dt>
</dl>
</td>
</tr>
</table>