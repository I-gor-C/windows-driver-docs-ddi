---
UID: NE.rilapitypes.RILSUPSVCTYPE
title: RILSUPSVCTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsupsvctype_2.htm
old-project: netvista
ms.assetid: 4aec39d6-3e12-4393-b477-24ea2036c227
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RIL_WritePhonebookEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILSUPSVCTYPE
req.alt-loc: rilapitypes.h
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
req.product: Windows 10 or later.
---

# RILSUPSVCTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>