---
UID: NE.ntddrilapitypes.RILUNSOLICITEDSSINFOPARAMMASK
title: RILUNSOLICITEDSSINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilunsolicitedssinfoparammask.htm
ms.assetid: 41cf5add-4cad-41ed-ba9c-6bfba56a9f65
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
req.alt-api: RILUNSOLICITEDSSINFOPARAMMASK
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

# RILUNSOLICITEDSSINFOPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILUNSOLICITEDSSINFOPARAMMASK { 
  RIL_PARAM_UNSSS_ID,
  RIL_PARAM_UNSSS_NOTIFICATIONCODE,
  RIL_PARAM_UNSSS_ADDRESS,
  RIL_PARAM_UNSSS_SUBADDR,
  RIL_PARAM_UNSSS_CUGINDEX,
  RIL_PARAM_UNSSS_HISTLENGTH,
  RIL_PARAM_UNSSS_HISTINFO,
  RIL_PARAM_UNSSS_ALL
} RILUNSOLICITEDSSINFOPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_UNSSS_ID"></a><a id="ril_param_unsss_id"></a><b>RIL_PARAM_UNSSS_ID</b>

<dd></dd>

### -field <a id="RIL_PARAM_UNSSS_NOTIFICATIONCODE"></a><a id="ril_param_unsss_notificationcode"></a><b>RIL_PARAM_UNSSS_NOTIFICATIONCODE</b>

<dd></dd>

### -field <a id="RIL_PARAM_UNSSS_ADDRESS"></a><a id="ril_param_unsss_address"></a><b>RIL_PARAM_UNSSS_ADDRESS</b>

<dd></dd>

### -field <a id="RIL_PARAM_UNSSS_SUBADDR"></a><a id="ril_param_unsss_subaddr"></a><b>RIL_PARAM_UNSSS_SUBADDR</b>

<dd></dd>

### -field <a id="RIL_PARAM_UNSSS_CUGINDEX"></a><a id="ril_param_unsss_cugindex"></a><b>RIL_PARAM_UNSSS_CUGINDEX</b>

<dd></dd>

### -field <a id="RIL_PARAM_UNSSS_HISTLENGTH"></a><a id="ril_param_unsss_histlength"></a><b>RIL_PARAM_UNSSS_HISTLENGTH</b>

<dd></dd>

### -field <a id="RIL_PARAM_UNSSS_HISTINFO"></a><a id="ril_param_unsss_histinfo"></a><b>RIL_PARAM_UNSSS_HISTINFO</b>

<dd></dd>

### -field <a id="RIL_PARAM_UNSSS_ALL"></a><a id="ril_param_unsss_all"></a><b>RIL_PARAM_UNSSS_ALL</b>

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