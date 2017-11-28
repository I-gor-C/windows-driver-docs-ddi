---
UID: NE.ntddrilapitypes.RILMSGDCSTYPE
title: RILMSGDCSTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgdcstype.htm
old-project: netvista
ms.assetid: 557fc92e-6550-44ea-ac09-bb0b74e1275f
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
req.alt-api: RILMSGDCSTYPE
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

# RILMSGDCSTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILMSGDCSTYPE { 
  RIL_DCSTYPE_MSGWAIT,
  RIL_DCSTYPE_MSGCLASS,
  RIL_DCSTYPE_LANGUAGE,
  RIL_DCSTYPE_MAX
} RILMSGDCSTYPE;
````


## -enum-fields
<dl>

### -field <a id="RIL_DCSTYPE_MSGWAIT"></a><a id="ril_dcstype_msgwait"></a><b>RIL_DCSTYPE_MSGWAIT</b>

<dd></dd>

### -field <a id="RIL_DCSTYPE_MSGCLASS"></a><a id="ril_dcstype_msgclass"></a><b>RIL_DCSTYPE_MSGCLASS</b>

<dd></dd>

### -field <a id="RIL_DCSTYPE_LANGUAGE"></a><a id="ril_dcstype_language"></a><b>RIL_DCSTYPE_LANGUAGE</b>

<dd></dd>

### -field <a id="RIL_DCSTYPE_MAX"></a><a id="ril_dcstype_max"></a><b>RIL_DCSTYPE_MAX</b>

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