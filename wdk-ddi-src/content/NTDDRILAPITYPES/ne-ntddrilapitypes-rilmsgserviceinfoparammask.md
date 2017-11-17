---
UID: NE.ntddrilapitypes.RILMSGSERVICEINFOPARAMMASK
title: RILMSGSERVICEINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgserviceinfoparammask.htm
ms.assetid: 9314909a-4580-49f9-b587-4d5e70ff0d4f
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
req.alt-api: RILMSGSERVICEINFOPARAMMASK
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

# RILMSGSERVICEINFOPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILMSGSERVICEINFOPARAMMASK { 
  RIL_PARAM_MSI_STOREUSED,
  RIL_PARAM_MSI_STORETOTAL,
  RIL_PARAM_MSI_ALL
} RILMSGSERVICEINFOPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_MSI_STOREUSED"></a><a id="ril_param_msi_storeused"></a><b>RIL_PARAM_MSI_STOREUSED</b>

<dd></dd>

### -field <a id="RIL_PARAM_MSI_STORETOTAL"></a><a id="ril_param_msi_storetotal"></a><b>RIL_PARAM_MSI_STORETOTAL</b>

<dd></dd>

### -field <a id="RIL_PARAM_MSI_ALL"></a><a id="ril_param_msi_all"></a><b>RIL_PARAM_MSI_ALL</b>

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