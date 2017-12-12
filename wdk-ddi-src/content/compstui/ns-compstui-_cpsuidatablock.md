---
UID: NS.COMPSTUI._CPSUIDATABLOCK
title: _CPSUIDATABLOCK
author: windows-driver-content
description: The CPSUIDATABLOCK structure is used as a parameter for the ComPropSheet function, if the function code is CPSFUNC_SET_DATABLOCK or CPSFUNC_QUERY_DATABLOCK.
old-location: print\cpsuidatablock.htm
old-project: print
ms.assetid: c5b488ac-dd8d-4484-81ca-b64fdf517100
ms.author: windowsdriverdev
ms.date: 12/9/2017
ms.keywords: _CPSUIDATABLOCK, *PCPSUIDATABLOCK, CPSUIDATABLOCK
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
---

# _CPSUIDATABLOCK structure



## -description
The CPSUIDATABLOCK structure is used as a parameter for the <a href="print.compropsheet">ComPropSheet</a> function, if the function code is <a href="print.cpsfunc_set_datablock">CPSFUNC_SET_DATABLOCK</a> or <a href="print.cpsfunc_query_datablock">CPSFUNC_QUERY_DATABLOCK</a>.



## -syntax

````
typedef struct _CPSUIDATABLOCK {
  DWORD  cbData;
  LPBYTE pbData;
} CPSUIDATABLOCK, *PCPSUIDATABLOCK;
````


## -struct-fields

### -field cbData

Size, in bytes of the buffer pointed to by <b>pbData</b>.


### -field pbData

Pointer to a caller-allocated buffer.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Compstui.h (include Compstui.h)</dt>
</dl>
</td>
</tr>
</table>