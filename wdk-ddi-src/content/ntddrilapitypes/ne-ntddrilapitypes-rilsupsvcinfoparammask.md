---
UID: NE.ntddrilapitypes.RILSUPSVCINFOPARAMMASK
title: RILSUPSVCINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsupsvcinfoparammask.htm
old-project: netvista
ms.assetid: d3a4780f-6fd4-40d3-a629-5dad31720506
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: RILSUPSVCINFOPARAMMASK
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

# RILSUPSVCINFOPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILSUPSVCINFOPARAMMASK { 
  RIL_PARAM_SSI_FROM_NETWORK,
  RIL_PARAM_SSI_FAILURE_REASON,
  RIL_PARAM_SSI_SUPSVC_ACTION,
  RIL_PARAM_SSI_SUPSVC_TYPE,
  RIL_PARAM_SSI_CALL_FORWARDING_REASON,
  RIL_PARAM_SSI_CALL_BARRING_TYPE,
  RIL_PARAM_SSI_INFOCLASSES,
  RIL_PARAM_SSI_ALPHA_IDENTIFIER,
  RIL_PARAM_SSI_CALL_BARRING_PASSWORD,
  RIL_PARAM_SSI_NEW_CALL_BARRING_PASSWORD,
  RIL_PARAM_SSI_CALL_FORWARDING_SETTINGS,
  RIL_PARAM_SSI_CALLER_ID_SETTINGS,
  RIL_PARAM_SSI_DIALED_ID_SETTINGS,
  RIL_PARAM_SSI_HIDE_ID_SETTINGS,
  RIL_PARAM_SSI_CONNECTED_ID_SETTINGS,
  RIL_PARAM_SSI_SUPSERVICE_DATA,
  RIL_PARAM_SSI_ALL
} RILSUPSVCINFOPARAMMASK;
````


## -enum-fields
<dl>

### -field RIL_PARAM_SSI_FROM_NETWORK

<dd></dd>

### -field RIL_PARAM_SSI_FAILURE_REASON

<dd></dd>

### -field RIL_PARAM_SSI_SUPSVC_ACTION

<dd></dd>

### -field RIL_PARAM_SSI_SUPSVC_TYPE

<dd></dd>

### -field RIL_PARAM_SSI_CALL_FORWARDING_REASON

<dd></dd>

### -field RIL_PARAM_SSI_CALL_BARRING_TYPE

<dd></dd>

### -field RIL_PARAM_SSI_INFOCLASSES

<dd></dd>

### -field RIL_PARAM_SSI_ALPHA_IDENTIFIER

<dd></dd>

### -field RIL_PARAM_SSI_CALL_BARRING_PASSWORD

<dd></dd>

### -field RIL_PARAM_SSI_NEW_CALL_BARRING_PASSWORD

<dd></dd>

### -field RIL_PARAM_SSI_CALL_FORWARDING_SETTINGS

<dd></dd>

### -field RIL_PARAM_SSI_CALLER_ID_SETTINGS

<dd></dd>

### -field RIL_PARAM_SSI_DIALED_ID_SETTINGS

<dd></dd>

### -field RIL_PARAM_SSI_HIDE_ID_SETTINGS

<dd></dd>

### -field RIL_PARAM_SSI_CONNECTED_ID_SETTINGS

<dd></dd>

### -field RIL_PARAM_SSI_SUPSERVICE_DATA

<dd></dd>

### -field RIL_PARAM_SSI_ALL

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