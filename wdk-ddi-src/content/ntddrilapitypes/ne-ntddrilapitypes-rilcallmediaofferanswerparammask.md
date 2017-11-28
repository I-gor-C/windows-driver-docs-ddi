---
UID: NE.ntddrilapitypes.RILCALLMEDIAOFFERANSWERPARAMMASK
title: RILCALLMEDIAOFFERANSWERPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmediaofferanswerparammask.htm
old-project: netvista
ms.assetid: d11eb8f7-b670-45f3-8f90-6ea4db19bb20
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
req.alt-api: RILCALLMEDIAOFFERANSWERPARAMMASK
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

# RILCALLMEDIAOFFERANSWERPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILCALLMEDIAOFFERANSWERPARAMMASK { 
  RIL_PARAM_CMOA_CHANGE,
  RIL_PARAM_CMOA_ACTION,
  RIL_PARAM_CMOA_OLD_STATE,
  RIL_PARAM_CMOA_NEW_STATE,
  RIL_PARAM_CMOA_ALL
} RILCALLMEDIAOFFERANSWERPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_CMOA_CHANGE"></a><a id="ril_param_cmoa_change"></a><b>RIL_PARAM_CMOA_CHANGE</b>

<dd></dd>

### -field <a id="RIL_PARAM_CMOA_ACTION"></a><a id="ril_param_cmoa_action"></a><b>RIL_PARAM_CMOA_ACTION</b>

<dd></dd>

### -field <a id="RIL_PARAM_CMOA_OLD_STATE"></a><a id="ril_param_cmoa_old_state"></a><b>RIL_PARAM_CMOA_OLD_STATE</b>

<dd></dd>

### -field <a id="RIL_PARAM_CMOA_NEW_STATE"></a><a id="ril_param_cmoa_new_state"></a><b>RIL_PARAM_CMOA_NEW_STATE</b>

<dd></dd>

### -field <a id="RIL_PARAM_CMOA_ALL"></a><a id="ril_param_cmoa_all"></a><b>RIL_PARAM_CMOA_ALL</b>

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