---
UID: NE.ntddrilapitypes.RILPERSODEACTIVATIONSTATEPARAMMASK
title: RILPERSODEACTIVATIONSTATEPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpersodeactivationstateparammask.htm
old-project: netvista
ms.assetid: 11c4388b-5c0d-4133-9c68-059d1af5c2ca
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
req.alt-api: RILPERSODEACTIVATIONSTATEPARAMMASK
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

# RILPERSODEACTIVATIONSTATEPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILPERSODEACTIVATIONSTATEPARAMMASK { 
  RIL_PARAM_PDS_CK_ATTEMPTS,
  RIL_PARAM_PDS_PUK_ATTEMPTS,
  RIL_PARAM_PDS_ALL
} RILPERSODEACTIVATIONSTATEPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_PDS_CK_ATTEMPTS"></a><a id="ril_param_pds_ck_attempts"></a><b>RIL_PARAM_PDS_CK_ATTEMPTS</b>

<dd></dd>

### -field <a id="RIL_PARAM_PDS_PUK_ATTEMPTS"></a><a id="ril_param_pds_puk_attempts"></a><b>RIL_PARAM_PDS_PUK_ATTEMPTS</b>

<dd></dd>

### -field <a id="RIL_PARAM_PDS_ALL"></a><a id="ril_param_pds_all"></a><b>RIL_PARAM_PDS_ALL</b>

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