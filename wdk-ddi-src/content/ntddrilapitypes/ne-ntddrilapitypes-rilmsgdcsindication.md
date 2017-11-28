---
UID: NE.ntddrilapitypes.RILMSGDCSINDICATION
title: RILMSGDCSINDICATION
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgdcsindication.htm
old-project: netvista
ms.assetid: 709980c8-e13f-48a7-9af7-26f0bb79e699
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
req.alt-api: RILMSGDCSINDICATION
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

# RILMSGDCSINDICATION enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILMSGDCSINDICATION { 
  RIL_DCSINDICATION_FAX,
  RIL_DCSINDICATION_EMAIL,
  RIL_DCSINDICATION_OTHER,
  RIL_DCSINDICATION_MAX
} RILMSGDCSINDICATION;
````


## -enum-fields
<dl>

### -field <a id="RIL_DCSINDICATION_FAX"></a><a id="ril_dcsindication_fax"></a><b>RIL_DCSINDICATION_FAX</b>

<dd></dd>

### -field <a id="RIL_DCSINDICATION_EMAIL"></a><a id="ril_dcsindication_email"></a><b>RIL_DCSINDICATION_EMAIL</b>

<dd></dd>

### -field <a id="RIL_DCSINDICATION_OTHER"></a><a id="ril_dcsindication_other"></a><b>RIL_DCSINDICATION_OTHER</b>

<dd></dd>

### -field <a id="RIL_DCSINDICATION_MAX"></a><a id="ril_dcsindication_max"></a><b>RIL_DCSINDICATION_MAX</b>

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