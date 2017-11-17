---
UID: NE.rilapitypes.RILLOCATIONINFOPARAMMASK
title: RILLOCATIONINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rillocationinfoparammask_2.htm
ms.assetid: a7ce7aaf-fd98-4ba6-8c9e-d15419c658f1
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILLOCATIONINFOPARAMMASK
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
ms.keywords: RIL_WritePhonebookEntry
req.iface: 
req.product: Windows 10 or later.
---

# RILLOCATIONINFOPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILLOCATIONINFOPARAMMASK { 
  RIL_PARAM_LU_HUICCAPP,
  RIL_PARAM_LU_LAC,
  RIL_PARAM_LU_TAC,
  RIL_PARAM_LU_CELLID,
  RIL_PARAM_LU_ALL
} RILLOCATIONINFOPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_LU_HUICCAPP"></a><a id="ril_param_lu_huiccapp"></a><b>RIL_PARAM_LU_HUICCAPP</b>

<dd></dd>

### -field <a id="RIL_PARAM_LU_LAC"></a><a id="ril_param_lu_lac"></a><b>RIL_PARAM_LU_LAC</b>

<dd></dd>

### -field <a id="RIL_PARAM_LU_TAC"></a><a id="ril_param_lu_tac"></a><b>RIL_PARAM_LU_TAC</b>

<dd></dd>

### -field <a id="RIL_PARAM_LU_CELLID"></a><a id="ril_param_lu_cellid"></a><b>RIL_PARAM_LU_CELLID</b>

<dd></dd>

### -field <a id="RIL_PARAM_LU_ALL"></a><a id="ril_param_lu_all"></a><b>RIL_PARAM_LU_ALL</b>

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