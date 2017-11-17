---
UID: NE.rilapitypes.RILCALLHANDOVERSTATEPARAMMASK
title: RILCALLHANDOVERSTATEPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallhandoverstateparammask_2.htm
ms.assetid: a9a5c8dc-8ffa-4142-879c-3a782b45dbff
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
req.alt-api: RILCALLHANDOVERSTATEPARAMMASK
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

# RILCALLHANDOVERSTATEPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILCALLHANDOVERSTATEPARAMMASK { 
  RIL_PARAM_HANDOVER_OLD_TYPE,
  RIL_PARAM_HANDOVER_NEW_TYPE,
  RIL_PARAM_HANDOVER_3GPPCAUSE,
  RIL_PARAM_HANDOVER_ALL
} RILCALLHANDOVERSTATEPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_HANDOVER_OLD_TYPE"></a><a id="ril_param_handover_old_type"></a><b>RIL_PARAM_HANDOVER_OLD_TYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_HANDOVER_NEW_TYPE"></a><a id="ril_param_handover_new_type"></a><b>RIL_PARAM_HANDOVER_NEW_TYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_HANDOVER_3GPPCAUSE"></a><a id="ril_param_handover_3gppcause"></a><b>RIL_PARAM_HANDOVER_3GPPCAUSE</b>

<dd></dd>

### -field <a id="RIL_PARAM_HANDOVER_ALL"></a><a id="ril_param_handover_all"></a><b>RIL_PARAM_HANDOVER_ALL</b>

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