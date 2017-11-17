---
UID: NE.ntddrilapitypes.RILTONESIGNALINFOPARAMMASK
title: RILTONESIGNALINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riltonesignalinfoparammask.htm
ms.assetid: 5ebacb12-4ccd-4e92-ba73-b79c1969eb4f
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
req.alt-api: RILTONESIGNALINFOPARAMMASK
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

# RILTONESIGNALINFOPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILTONESIGNALINFOPARAMMASK { 
  RIL_PARAM_TONESIGNAL_GPP2TONE,
  RIL_PARAM_TONESIGNAL_GPP2ISDNALERTING,
  RIL_PARAM_TONESIGNAL_EXECUTOR,
  RIL_PARAM_TONESIGNAL_All
} RILTONESIGNALINFOPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_TONESIGNAL_GPP2TONE"></a><a id="ril_param_tonesignal_gpp2tone"></a><b>RIL_PARAM_TONESIGNAL_GPP2TONE</b>

<dd></dd>

### -field <a id="RIL_PARAM_TONESIGNAL_GPP2ISDNALERTING"></a><a id="ril_param_tonesignal_gpp2isdnalerting"></a><b>RIL_PARAM_TONESIGNAL_GPP2ISDNALERTING</b>

<dd></dd>

### -field <a id="RIL_PARAM_TONESIGNAL_EXECUTOR"></a><a id="ril_param_tonesignal_executor"></a><b>RIL_PARAM_TONESIGNAL_EXECUTOR</b>

<dd></dd>

### -field <a id="RIL_PARAM_TONESIGNAL_All"></a><a id="ril_param_tonesignal_all"></a><a id="RIL_PARAM_TONESIGNAL_ALL"></a><b>RIL_PARAM_TONESIGNAL_All</b>

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