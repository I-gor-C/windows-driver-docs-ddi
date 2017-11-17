---
UID: NE.ntddrilapitypes.RILSENDMSGRESPONSEPARAMMASK
title: RILSENDMSGRESPONSEPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsendmsgresponseparammask.htm
ms.assetid: d3bf2b1a-22ac-4b37-a442-ecd8a2108b46
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
req.alt-api: RILSENDMSGRESPONSEPARAMMASK
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

# RILSENDMSGRESPONSEPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILSENDMSGRESPONSEPARAMMASK { 
  RIL_PARAM_MSGRES_CDMACAUSECODE,
  RIL_PARAM_MSGRES_CDMAERRORCLASS,
  RIL_PARAM_MSGRES_GWLTRANSPORTCODE,
  RIL_PARAM_MSGRES_GWLRELAYCODE,
  RIL_PARAM_MSGRES_MSGID,
  RIL_PARAM_MSGRES_ALL
} RILSENDMSGRESPONSEPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_MSGRES_CDMACAUSECODE"></a><a id="ril_param_msgres_cdmacausecode"></a><b>RIL_PARAM_MSGRES_CDMACAUSECODE</b>

<dd></dd>

### -field <a id="RIL_PARAM_MSGRES_CDMAERRORCLASS"></a><a id="ril_param_msgres_cdmaerrorclass"></a><b>RIL_PARAM_MSGRES_CDMAERRORCLASS</b>

<dd></dd>

### -field <a id="RIL_PARAM_MSGRES_GWLTRANSPORTCODE"></a><a id="ril_param_msgres_gwltransportcode"></a><b>RIL_PARAM_MSGRES_GWLTRANSPORTCODE</b>

<dd></dd>

### -field <a id="RIL_PARAM_MSGRES_GWLRELAYCODE"></a><a id="ril_param_msgres_gwlrelaycode"></a><b>RIL_PARAM_MSGRES_GWLRELAYCODE</b>

<dd></dd>

### -field <a id="RIL_PARAM_MSGRES_MSGID"></a><a id="ril_param_msgres_msgid"></a><b>RIL_PARAM_MSGRES_MSGID</b>

<dd></dd>

### -field <a id="RIL_PARAM_MSGRES_ALL"></a><a id="ril_param_msgres_all"></a><b>RIL_PARAM_MSGRES_ALL</b>

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