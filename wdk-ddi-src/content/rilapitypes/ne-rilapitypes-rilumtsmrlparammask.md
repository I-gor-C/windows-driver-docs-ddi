---
UID: NE.rilapitypes.RILUMTSMRLPARAMMASK
title: RILUMTSMRLPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilumtsmrlparammask_2.htm
old-project: netvista
ms.assetid: d0450aeb-8b6e-4ab2-94b7-563503a83e76
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
req.alt-api: RILUMTSMRLPARAMMASK
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

# RILUMTSMRLPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILUMTSMRLPARAMMASK { 
  RIL_PARAM_UMTSMRL_MNC,
  RIL_PARAM_UMTSMRL_LAC,
  RIL_PARAM_UMTSMRL_CELLID,
  RIL_PARAM_UMTSMRL_UARFCN,
  RIL_PARAM_UMTSMRL_PRIMARY_SC,
  RIL_PARAM_UMTSMRL_RSCP,
  RIL_PARAM_UMTSMRL_ECNO,
  RIL_PARAM_UMTSMRL_PATHLOSS,
  RIL_PARAM_UMTSMRL_ALL
} RILUMTSMRLPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_UMTSMRL_MNC"></a><a id="ril_param_umtsmrl_mnc"></a><b>RIL_PARAM_UMTSMRL_MNC</b>

<dd></dd>

### -field <a id="RIL_PARAM_UMTSMRL_LAC"></a><a id="ril_param_umtsmrl_lac"></a><b>RIL_PARAM_UMTSMRL_LAC</b>

<dd></dd>

### -field <a id="RIL_PARAM_UMTSMRL_CELLID"></a><a id="ril_param_umtsmrl_cellid"></a><b>RIL_PARAM_UMTSMRL_CELLID</b>

<dd></dd>

### -field <a id="RIL_PARAM_UMTSMRL_UARFCN"></a><a id="ril_param_umtsmrl_uarfcn"></a><b>RIL_PARAM_UMTSMRL_UARFCN</b>

<dd></dd>

### -field <a id="RIL_PARAM_UMTSMRL_PRIMARY_SC"></a><a id="ril_param_umtsmrl_primary_sc"></a><b>RIL_PARAM_UMTSMRL_PRIMARY_SC</b>

<dd></dd>

### -field <a id="RIL_PARAM_UMTSMRL_RSCP"></a><a id="ril_param_umtsmrl_rscp"></a><b>RIL_PARAM_UMTSMRL_RSCP</b>

<dd></dd>

### -field <a id="RIL_PARAM_UMTSMRL_ECNO"></a><a id="ril_param_umtsmrl_ecno"></a><b>RIL_PARAM_UMTSMRL_ECNO</b>

<dd></dd>

### -field <a id="RIL_PARAM_UMTSMRL_PATHLOSS"></a><a id="ril_param_umtsmrl_pathloss"></a><b>RIL_PARAM_UMTSMRL_PATHLOSS</b>

<dd></dd>

### -field <a id="RIL_PARAM_UMTSMRL_ALL"></a><a id="ril_param_umtsmrl_all"></a><b>RIL_PARAM_UMTSMRL_ALL</b>

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