---
UID: NE.ntddrilapitypes.RILSUPSERVICEDATASTATUS
title: RILSUPSERVICEDATASTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsupservicedatastatus.htm
old-project: netvista
ms.assetid: 60cecce7-9085-4cbd-b637-e24af51d1c22
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: RILSUPSERVICEDATASTATUS
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

# RILSUPSERVICEDATASTATUS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILSUPSERVICEDATASTATUS { 
  RIL_SUPSVCDATASTATUS_FURTHERINFOREQUIRED,
  RIL_SUPSVCDATASTATUS_TIMEOUT,
  RIL_SUPSVCDATASTATUS_ERROR,
  RIL_SUPSVCDATASTATUS_MAX
} RILSUPSERVICEDATASTATUS;
````


## -enum-fields
<dl>

### -field <a id="RIL_SUPSVCDATASTATUS_FURTHERINFOREQUIRED"></a><a id="ril_supsvcdatastatus_furtherinforequired"></a><b>RIL_SUPSVCDATASTATUS_FURTHERINFOREQUIRED</b>

<dd></dd>

### -field <a id="RIL_SUPSVCDATASTATUS_TIMEOUT"></a><a id="ril_supsvcdatastatus_timeout"></a><b>RIL_SUPSVCDATASTATUS_TIMEOUT</b>

<dd></dd>

### -field <a id="RIL_SUPSVCDATASTATUS_ERROR"></a><a id="ril_supsvcdatastatus_error"></a><b>RIL_SUPSVCDATASTATUS_ERROR</b>

<dd></dd>

### -field <a id="RIL_SUPSVCDATASTATUS_MAX"></a><a id="ril_supsvcdatastatus_max"></a><b>RIL_SUPSVCDATASTATUS_MAX</b>

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