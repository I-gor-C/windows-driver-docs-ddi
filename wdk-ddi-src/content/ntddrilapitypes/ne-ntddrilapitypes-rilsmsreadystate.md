---
UID: NE.ntddrilapitypes.RILSMSREADYSTATE
title: RILSMSREADYSTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsmsreadystate.htm
old-project: netvista
ms.assetid: f37b1e31-d0fa-4b0a-bab6-131b3bf1bdcd
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILSMSREADYSTATE
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
req.iface: 
---

# RILSMSREADYSTATE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILSMSREADYSTATE { 
  RIL_SMSREADY_SERVICEREADY_3GPP2,
  RIL_SMSREADY_UICCREADY,
  RIL_SMSREADYSTATE_ALL
} RILSMSREADYSTATE;
````


## -enum-fields
<dl>

### -field <a id="RIL_SMSREADY_SERVICEREADY_3GPP2"></a><a id="ril_smsready_serviceready_3gpp2"></a><b>RIL_SMSREADY_SERVICEREADY_3GPP2</b>

<dd></dd>

### -field <a id="RIL_SMSREADY_UICCREADY"></a><a id="ril_smsready_uiccready"></a><b>RIL_SMSREADY_UICCREADY</b>

<dd></dd>

### -field <a id="RIL_SMSREADYSTATE_ALL"></a><a id="ril_smsreadystate_all"></a><b>RIL_SMSREADYSTATE_ALL</b>

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