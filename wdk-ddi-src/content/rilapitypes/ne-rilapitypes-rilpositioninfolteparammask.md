---
UID: NE.rilapitypes.RILPOSITIONINFOLTEPARAMMASK
title: RILPOSITIONINFOLTEPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpositioninfolteparammask_2.htm
old-project: netvista
ms.assetid: 9c71420f-8b85-4f31-9a08-7f363be75cc0
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
req.alt-api: RILPOSITIONINFOLTEPARAMMASK
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

# RILPOSITIONINFOLTEPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILPOSITIONINFOLTEPARAMMASK { 
  RIL_PARAM_POSITION_LTE_MNC,
  RIL_PARAM_POSITION_LTE_CELLID,
  RIL_PARAM_POSITION_LTE_EARFCN,
  RIL_PARAM_POSITION_LTE_PHYSCELLID,
  RIL_PARAM_POSITION_LTE_TAC,
  RIL_PARAM_POSITION_LTE_RSRP,
  RIL_PARAM_POSITION_LTE_RSRQ,
  RIL_PARAM_POSITION_LTE_TA,
  RIL_PARAM_POSITION_LTE_ALL
} RILPOSITIONINFOLTEPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_POSITION_LTE_MNC"></a><a id="ril_param_position_lte_mnc"></a><b>RIL_PARAM_POSITION_LTE_MNC</b>

<dd></dd>

### -field <a id="RIL_PARAM_POSITION_LTE_CELLID"></a><a id="ril_param_position_lte_cellid"></a><b>RIL_PARAM_POSITION_LTE_CELLID</b>

<dd></dd>

### -field <a id="RIL_PARAM_POSITION_LTE_EARFCN"></a><a id="ril_param_position_lte_earfcn"></a><b>RIL_PARAM_POSITION_LTE_EARFCN</b>

<dd></dd>

### -field <a id="RIL_PARAM_POSITION_LTE_PHYSCELLID"></a><a id="ril_param_position_lte_physcellid"></a><b>RIL_PARAM_POSITION_LTE_PHYSCELLID</b>

<dd></dd>

### -field <a id="RIL_PARAM_POSITION_LTE_TAC"></a><a id="ril_param_position_lte_tac"></a><b>RIL_PARAM_POSITION_LTE_TAC</b>

<dd></dd>

### -field <a id="RIL_PARAM_POSITION_LTE_RSRP"></a><a id="ril_param_position_lte_rsrp"></a><b>RIL_PARAM_POSITION_LTE_RSRP</b>

<dd></dd>

### -field <a id="RIL_PARAM_POSITION_LTE_RSRQ"></a><a id="ril_param_position_lte_rsrq"></a><b>RIL_PARAM_POSITION_LTE_RSRQ</b>

<dd></dd>

### -field <a id="RIL_PARAM_POSITION_LTE_TA"></a><a id="ril_param_position_lte_ta"></a><b>RIL_PARAM_POSITION_LTE_TA</b>

<dd></dd>

### -field <a id="RIL_PARAM_POSITION_LTE_ALL"></a><a id="ril_param_position_lte_all"></a><b>RIL_PARAM_POSITION_LTE_ALL</b>

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