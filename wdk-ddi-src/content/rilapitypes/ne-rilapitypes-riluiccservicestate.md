---
UID: NE.rilapitypes.RILUICCSERVICESTATE
title: RILUICCSERVICESTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccservicestate_2.htm
old-project: netvista
ms.assetid: f817db6b-bda4-45cd-953b-fd3d81bafa8f
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
req.alt-api: RILUICCSERVICESTATE
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

# RILUICCSERVICESTATE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>