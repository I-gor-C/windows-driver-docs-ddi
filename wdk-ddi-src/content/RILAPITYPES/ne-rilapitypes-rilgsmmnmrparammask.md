---
UID: NE.rilapitypes.RILGSMMNMRPARAMMASK
title: RILGSMMNMRPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilgsmmnmrparammask_2.htm
ms.assetid: 9e58bd61-9cb7-40fb-a6e5-1e8a8d428774
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
req.alt-api: RILGSMMNMRPARAMMASK
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

# RILGSMMNMRPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILGSMMNMRPARAMMASK { 
  RIL_PARAM_GSMNMR_MNC,
  RIL_PARAM_GSMNMR_LAC,
  RIL_PARAM_GSMNMR_CELLID,
  RIL_PARAM_GSMNMR_ARFCN,
  RIL_PARAM_GSMNMR_BSID,
  RIL_PARAM_GSMNMR_RXLEVEL,
  RIL_PARAM_GSMNMR_ALL
} RILGSMMNMRPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_GSMNMR_MNC"></a><a id="ril_param_gsmnmr_mnc"></a><b>RIL_PARAM_GSMNMR_MNC</b>

<dd></dd>

### -field <a id="RIL_PARAM_GSMNMR_LAC"></a><a id="ril_param_gsmnmr_lac"></a><b>RIL_PARAM_GSMNMR_LAC</b>

<dd></dd>

### -field <a id="RIL_PARAM_GSMNMR_CELLID"></a><a id="ril_param_gsmnmr_cellid"></a><b>RIL_PARAM_GSMNMR_CELLID</b>

<dd></dd>

### -field <a id="RIL_PARAM_GSMNMR_ARFCN"></a><a id="ril_param_gsmnmr_arfcn"></a><b>RIL_PARAM_GSMNMR_ARFCN</b>

<dd></dd>

### -field <a id="RIL_PARAM_GSMNMR_BSID"></a><a id="ril_param_gsmnmr_bsid"></a><b>RIL_PARAM_GSMNMR_BSID</b>

<dd></dd>

### -field <a id="RIL_PARAM_GSMNMR_RXLEVEL"></a><a id="ril_param_gsmnmr_rxlevel"></a><b>RIL_PARAM_GSMNMR_RXLEVEL</b>

<dd></dd>

### -field <a id="RIL_PARAM_GSMNMR_ALL"></a><a id="ril_param_gsmnmr_all"></a><b>RIL_PARAM_GSMNMR_ALL</b>

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