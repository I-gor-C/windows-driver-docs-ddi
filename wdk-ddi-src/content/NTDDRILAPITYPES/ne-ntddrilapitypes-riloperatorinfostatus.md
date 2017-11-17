---
UID: NE.ntddrilapitypes.RILOPERATORINFOSTATUS
title: RILOPERATORINFOSTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riloperatorinfostatus.htm
ms.assetid: 372d84da-600f-44db-ac76-b59ceac7321d
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
req.alt-api: RILOPERATORINFOSTATUS
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

# RILOPERATORINFOSTATUS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILOPERATORINFOSTATUS { 
  RIL_OPSTATUS_AVAILABLE,
  RIL_OPSTATUS_CURRENT,
  RIL_OPSTATUS_FORBIDDEN,
  RIL_OPSTATUS_MAX
} RILOPERATORINFOSTATUS;
````


## -enum-fields
<dl>

### -field <a id="RIL_OPSTATUS_AVAILABLE"></a><a id="ril_opstatus_available"></a><b>RIL_OPSTATUS_AVAILABLE</b>

<dd></dd>

### -field <a id="RIL_OPSTATUS_CURRENT"></a><a id="ril_opstatus_current"></a><b>RIL_OPSTATUS_CURRENT</b>

<dd></dd>

### -field <a id="RIL_OPSTATUS_FORBIDDEN"></a><a id="ril_opstatus_forbidden"></a><b>RIL_OPSTATUS_FORBIDDEN</b>

<dd></dd>

### -field <a id="RIL_OPSTATUS_MAX"></a><a id="ril_opstatus_max"></a><b>RIL_OPSTATUS_MAX</b>

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