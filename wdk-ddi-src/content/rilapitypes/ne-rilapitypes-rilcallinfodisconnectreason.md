---
UID: NE.rilapitypes.RILCALLINFODISCONNECTREASON
title: RILCALLINFODISCONNECTREASON
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallinfodisconnectreason_2.htm
old-project: netvista
ms.assetid: b0cc8ecb-fa13-414a-b08a-de0d60724f25
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.alt-api: RILCALLINFODISCONNECTREASON
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

# RILCALLINFODISCONNECTREASON enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILCALLINFODISCONNECTREASON { 
  RIL_DISCREASON_BUSY,
  RIL_DISCREASON_NETWORKERROR,
  RIL_DISCREASON_RADIOFADE,
  RIL_DISCREASON_CONGESTION,
  RIL_DISCREASON_EMERGENCYONLY,
  RIL_DISCREASON_NOSERVICE,
  RIL_DISCREASON_OTHEREXECUTORBUSY,
  RIL_DISCREASON_EMERGENCYFAILOVER,
  RIL_DISCREASON_HANDOVER_MERGE,
  RIL_DISCREASON_MAX
} RILCALLINFODISCONNECTREASON;
````


## -enum-fields
<dl>

### -field <a id="RIL_DISCREASON_BUSY"></a><a id="ril_discreason_busy"></a><b>RIL_DISCREASON_BUSY</b>

<dd></dd>

### -field <a id="RIL_DISCREASON_NETWORKERROR"></a><a id="ril_discreason_networkerror"></a><b>RIL_DISCREASON_NETWORKERROR</b>

<dd></dd>

### -field <a id="RIL_DISCREASON_RADIOFADE"></a><a id="ril_discreason_radiofade"></a><b>RIL_DISCREASON_RADIOFADE</b>

<dd></dd>

### -field <a id="RIL_DISCREASON_CONGESTION"></a><a id="ril_discreason_congestion"></a><b>RIL_DISCREASON_CONGESTION</b>

<dd></dd>

### -field <a id="RIL_DISCREASON_EMERGENCYONLY"></a><a id="ril_discreason_emergencyonly"></a><b>RIL_DISCREASON_EMERGENCYONLY</b>

<dd></dd>

### -field <a id="RIL_DISCREASON_NOSERVICE"></a><a id="ril_discreason_noservice"></a><b>RIL_DISCREASON_NOSERVICE</b>

<dd></dd>

### -field <a id="RIL_DISCREASON_OTHEREXECUTORBUSY"></a><a id="ril_discreason_otherexecutorbusy"></a><b>RIL_DISCREASON_OTHEREXECUTORBUSY</b>

<dd></dd>

### -field <a id="RIL_DISCREASON_EMERGENCYFAILOVER"></a><a id="ril_discreason_emergencyfailover"></a><b>RIL_DISCREASON_EMERGENCYFAILOVER</b>

<dd></dd>

### -field <a id="RIL_DISCREASON_HANDOVER_MERGE"></a><a id="ril_discreason_handover_merge"></a><b>RIL_DISCREASON_HANDOVER_MERGE</b>

<dd></dd>

### -field <a id="RIL_DISCREASON_MAX"></a><a id="ril_discreason_max"></a><b>RIL_DISCREASON_MAX</b>

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