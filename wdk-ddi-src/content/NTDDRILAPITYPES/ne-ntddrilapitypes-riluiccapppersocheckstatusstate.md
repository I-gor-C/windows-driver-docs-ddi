---
UID: NE.ntddrilapitypes.RILUICCAPPPERSOCHECKSTATUSSTATE
title: RILUICCAPPPERSOCHECKSTATUSSTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccapppersocheckstatusstate.htm
ms.assetid: d41d5559-b9ec-4ae5-b658-8f75e8af13e4
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
req.alt-api: RILUICCAPPPERSOCHECKSTATUSSTATE
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

# RILUICCAPPPERSOCHECKSTATUSSTATE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILUICCAPPPERSOCHECKSTATUSSTATE { 
  RIL_PERSOCHECKSTATE_PASS,
  RIL_PERSOCHECKSTATE_FAIL,
  RIL_PERSOCHECKSTATE_MAX
} RILUICCAPPPERSOCHECKSTATUSSTATE;
````


## -enum-fields
<dl>

### -field <a id="RIL_PERSOCHECKSTATE_PASS"></a><a id="ril_persocheckstate_pass"></a><b>RIL_PERSOCHECKSTATE_PASS</b>

<dd></dd>

### -field <a id="RIL_PERSOCHECKSTATE_FAIL"></a><a id="ril_persocheckstate_fail"></a><b>RIL_PERSOCHECKSTATE_FAIL</b>

<dd></dd>

### -field <a id="RIL_PERSOCHECKSTATE_MAX"></a><a id="ril_persocheckstate_max"></a><b>RIL_PERSOCHECKSTATE_MAX</b>

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