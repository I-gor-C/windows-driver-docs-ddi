---
UID: NE.ntddrilapitypes.RILUICCSERVICESTATE
title: RILUICCSERVICESTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccservicestate.htm
old-project: netvista
ms.assetid: 01d64333-3f49-45e1-bd2b-dda0aeb6a083
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
req.alt-api: RILUICCSERVICESTATE
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

# RILUICCSERVICESTATE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILUICCSERVICESTATE { 
  RIL_UICCSERVICESTATE_DISABLED,
  RIL_UICCSERVICESTATE_ENABLED,
  RIL_UICCSERVICESTATE_MAX
} RILUICCSERVICESTATE;
````


## -enum-fields
<dl>

### -field <a id="RIL_UICCSERVICESTATE_DISABLED"></a><a id="ril_uiccservicestate_disabled"></a><b>RIL_UICCSERVICESTATE_DISABLED</b>

<dd></dd>

### -field <a id="RIL_UICCSERVICESTATE_ENABLED"></a><a id="ril_uiccservicestate_enabled"></a><b>RIL_UICCSERVICESTATE_ENABLED</b>

<dd></dd>

### -field <a id="RIL_UICCSERVICESTATE_MAX"></a><a id="ril_uiccservicestate_max"></a><b>RIL_UICCSERVICESTATE_MAX</b>

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