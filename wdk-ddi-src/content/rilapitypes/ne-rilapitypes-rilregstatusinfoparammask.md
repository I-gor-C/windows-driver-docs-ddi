---
UID: NE.rilapitypes.RILREGSTATUSINFOPARAMMASK
title: RILREGSTATUSINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilregstatusinfoparammask_2.htm
old-project: netvista
ms.assetid: 22751b8b-f19c-4480-b8f4-6ee2322419ca
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
req.alt-api: RILREGSTATUSINFOPARAMMASK
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

# RILREGSTATUSINFOPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILREGSTATUSINFOPARAMMASK { 
  RIL_PARAM_REGSI_HUICCAPP,
  RIL_PARAM_REGSI_REGSTATUS,
  RIL_PARAM_REGSI_ACCESSTECHNOLOGY,
  RIL_PARAM_REGSI_SYSTEMCAPS,
  RIL_PARAM_REGSI_REGREJECTREASON,
  RIL_PARAM_REGSI_CURRENTOPERATOR,
  RIL_PARAM_REGSI_VOICEDOMAIN,
  RIL_PARAM_REGSI_NETWORKCODE,
  RIL_PARAM_REGSI_ALL
} RILREGSTATUSINFOPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_REGSI_HUICCAPP"></a><a id="ril_param_regsi_huiccapp"></a><b>RIL_PARAM_REGSI_HUICCAPP</b>

<dd></dd>

### -field <a id="RIL_PARAM_REGSI_REGSTATUS"></a><a id="ril_param_regsi_regstatus"></a><b>RIL_PARAM_REGSI_REGSTATUS</b>

<dd></dd>

### -field <a id="RIL_PARAM_REGSI_ACCESSTECHNOLOGY"></a><a id="ril_param_regsi_accesstechnology"></a><b>RIL_PARAM_REGSI_ACCESSTECHNOLOGY</b>

<dd></dd>

### -field <a id="RIL_PARAM_REGSI_SYSTEMCAPS"></a><a id="ril_param_regsi_systemcaps"></a><b>RIL_PARAM_REGSI_SYSTEMCAPS</b>

<dd></dd>

### -field <a id="RIL_PARAM_REGSI_REGREJECTREASON"></a><a id="ril_param_regsi_regrejectreason"></a><b>RIL_PARAM_REGSI_REGREJECTREASON</b>

<dd></dd>

### -field <a id="RIL_PARAM_REGSI_CURRENTOPERATOR"></a><a id="ril_param_regsi_currentoperator"></a><b>RIL_PARAM_REGSI_CURRENTOPERATOR</b>

<dd></dd>

### -field <a id="RIL_PARAM_REGSI_VOICEDOMAIN"></a><a id="ril_param_regsi_voicedomain"></a><b>RIL_PARAM_REGSI_VOICEDOMAIN</b>

<dd></dd>

### -field <a id="RIL_PARAM_REGSI_NETWORKCODE"></a><a id="ril_param_regsi_networkcode"></a><b>RIL_PARAM_REGSI_NETWORKCODE</b>

<dd></dd>

### -field <a id="RIL_PARAM_REGSI_ALL"></a><a id="ril_param_regsi_all"></a><b>RIL_PARAM_REGSI_ALL</b>

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