---
UID: NE.rilapitypes.RILUICCSLOTSTATE
title: RILUICCSLOTSTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccslotstate_2.htm
old-project: netvista
ms.assetid: 472f7354-4b51-4fac-857e-d93083f160e8
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
req.alt-api: RILUICCSLOTSTATE
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

# RILUICCSLOTSTATE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILUICCSLOTSTATE { 
  RIL_UICCSLOT_OFF,
  RIL_UICCSLOT_EMPTY,
  RIL_UICCSLOT_NOT_READY,
  RIL_UICCSLOT_ACTIVE,
  RIL_UICCSLOT_ERROR,
  RIL_UICCSLOT_MAX
} RILUICCSLOTSTATE;
````


## -enum-fields
<dl>

### -field <a id="RIL_UICCSLOT_OFF"></a><a id="ril_uiccslot_off"></a><b>RIL_UICCSLOT_OFF</b>

<dd></dd>

### -field <a id="RIL_UICCSLOT_EMPTY"></a><a id="ril_uiccslot_empty"></a><b>RIL_UICCSLOT_EMPTY</b>

<dd></dd>

### -field <a id="RIL_UICCSLOT_NOT_READY"></a><a id="ril_uiccslot_not_ready"></a><b>RIL_UICCSLOT_NOT_READY</b>

<dd></dd>

### -field <a id="RIL_UICCSLOT_ACTIVE"></a><a id="ril_uiccslot_active"></a><b>RIL_UICCSLOT_ACTIVE</b>

<dd></dd>

### -field <a id="RIL_UICCSLOT_ERROR"></a><a id="ril_uiccslot_error"></a><b>RIL_UICCSLOT_ERROR</b>

<dd></dd>

### -field <a id="RIL_UICCSLOT_MAX"></a><a id="ril_uiccslot_max"></a><b>RIL_UICCSLOT_MAX</b>

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