---
UID: NE.ntddrilapitypes.RILSUPSVCTYPE
title: RILSUPSVCTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsupsvctype.htm
ms.assetid: 3d9415f7-cc28-4e45-8d88-b8693aa57116
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILSUPSVCTYPE
req.alt-loc: ntddrilapitypes.h
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
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
req.iface: 
---

# RILSUPSVCTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILSUPSVCTYPE { 
  RIL_SUPSVCTYPE_CLIP,
  RIL_SUPSVCTYPE_CLIR,
  RIL_SUPSVCTYPE_COLP,
  RIL_SUPSVCTYPE_COLR,
  RIL_SUPSVCTYPE_CNAP,
  RIL_SUPSVCTYPE_MAX
} RILSUPSVCTYPE;
````


## -enum-fields
<dl>

### -field <a id="RIL_SUPSVCTYPE_CLIP"></a><a id="ril_supsvctype_clip"></a><b>RIL_SUPSVCTYPE_CLIP</b>

<dd></dd>

### -field <a id="RIL_SUPSVCTYPE_CLIR"></a><a id="ril_supsvctype_clir"></a><b>RIL_SUPSVCTYPE_CLIR</b>

<dd></dd>

### -field <a id="RIL_SUPSVCTYPE_COLP"></a><a id="ril_supsvctype_colp"></a><b>RIL_SUPSVCTYPE_COLP</b>

<dd></dd>

### -field <a id="RIL_SUPSVCTYPE_COLR"></a><a id="ril_supsvctype_colr"></a><b>RIL_SUPSVCTYPE_COLR</b>

<dd></dd>

### -field <a id="RIL_SUPSVCTYPE_CNAP"></a><a id="ril_supsvctype_cnap"></a><b>RIL_SUPSVCTYPE_CNAP</b>

<dd></dd>

### -field <a id="RIL_SUPSVCTYPE_MAX"></a><a id="ril_supsvctype_max"></a><b>RIL_SUPSVCTYPE_MAX</b>

<dd></dd>
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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>