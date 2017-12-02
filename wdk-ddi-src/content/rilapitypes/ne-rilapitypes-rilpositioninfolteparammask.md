---
UID: NE.rilapitypes.RILPOSITIONINFOLTEPARAMMASK
title: RILPOSITIONINFOLTEPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpositioninfolteparammask_2.htm
old-project: netvista
ms.assetid: 9c71420f-8b85-4f31-9a08-7f363be75cc0
ms.author: windowsdriverdev
ms.date: 11/30/2017
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

### -field RIL_PARAM_POSITION_LTE_MNC

<dd></dd>

### -field RIL_PARAM_POSITION_LTE_CELLID

<dd></dd>

### -field RIL_PARAM_POSITION_LTE_EARFCN

<dd></dd>

### -field RIL_PARAM_POSITION_LTE_PHYSCELLID

<dd></dd>

### -field RIL_PARAM_POSITION_LTE_TAC

<dd></dd>

### -field RIL_PARAM_POSITION_LTE_RSRP

<dd></dd>

### -field RIL_PARAM_POSITION_LTE_RSRQ

<dd></dd>

### -field RIL_PARAM_POSITION_LTE_TA

<dd></dd>

### -field RIL_PARAM_POSITION_LTE_ALL

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