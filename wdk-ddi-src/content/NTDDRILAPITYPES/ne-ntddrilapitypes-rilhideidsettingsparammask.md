---
UID: NE.ntddrilapitypes.RILHIDEIDSETTINGSPARAMMASK
title: RILHIDEIDSETTINGSPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilhideidsettingsparammask.htm
ms.assetid: 3ac34302-f56f-424d-b627-f977c4aabfba
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
req.alt-api: RILHIDEIDSETTINGSPARAMMASK
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

# RILHIDEIDSETTINGSPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILHIDEIDSETTINGSPARAMMASK { 
  RIL_PARAM_HIDS_STATUS,
  RIL_PARAM_HIDS_PROVISIONING,
  RIL_PARAM_HIDS_ALL
} RILHIDEIDSETTINGSPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_HIDS_STATUS"></a><a id="ril_param_hids_status"></a><b>RIL_PARAM_HIDS_STATUS</b>

<dd></dd>

### -field <a id="RIL_PARAM_HIDS_PROVISIONING"></a><a id="ril_param_hids_provisioning"></a><b>RIL_PARAM_HIDS_PROVISIONING</b>

<dd></dd>

### -field <a id="RIL_PARAM_HIDS_ALL"></a><a id="ril_param_hids_all"></a><b>RIL_PARAM_HIDS_ALL</b>

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