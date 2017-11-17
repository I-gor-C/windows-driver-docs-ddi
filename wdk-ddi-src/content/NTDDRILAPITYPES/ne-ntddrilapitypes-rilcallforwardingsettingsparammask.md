---
UID: NE.ntddrilapitypes.RILCALLFORWARDINGSETTINGSPARAMMASK
title: RILCALLFORWARDINGSETTINGSPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallforwardingsettingsparammask.htm
ms.assetid: 0da4e19f-9e7b-4986-bdb1-fc59e177f3fa
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
req.alt-api: RILCALLFORWARDINGSETTINGSPARAMMASK
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

# RILCALLFORWARDINGSETTINGSPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILCALLFORWARDINGSETTINGSPARAMMASK { 
  RIL_PARAM_CFS_INFOCLASSES,
  RIL_PARAM_CFS_ADDRESS,
  RIL_PARAM_CFS_SUBADDRESS,
  RIL_PARAM_CFS_DELAYTIME,
  RIL_PARAM_CFS_ALL
} RILCALLFORWARDINGSETTINGSPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_CFS_INFOCLASSES"></a><a id="ril_param_cfs_infoclasses"></a><b>RIL_PARAM_CFS_INFOCLASSES</b>

<dd></dd>

### -field <a id="RIL_PARAM_CFS_ADDRESS"></a><a id="ril_param_cfs_address"></a><b>RIL_PARAM_CFS_ADDRESS</b>

<dd></dd>

### -field <a id="RIL_PARAM_CFS_SUBADDRESS"></a><a id="ril_param_cfs_subaddress"></a><b>RIL_PARAM_CFS_SUBADDRESS</b>

<dd></dd>

### -field <a id="RIL_PARAM_CFS_DELAYTIME"></a><a id="ril_param_cfs_delaytime"></a><b>RIL_PARAM_CFS_DELAYTIME</b>

<dd></dd>

### -field <a id="RIL_PARAM_CFS_ALL"></a><a id="ril_param_cfs_all"></a><b>RIL_PARAM_CFS_ALL</b>

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