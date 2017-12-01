---
UID: NE.rilapitypes.RILCALLFORWARDINGSETTINGSPARAMMASK
title: RILCALLFORWARDINGSETTINGSPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallforwardingsettingsparammask_2.htm
old-project: netvista
ms.assetid: 4db4e6fe-1faf-4109-95aa-e2e5bf3b0dd6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RIL_WritePhonebookEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILCALLFORWARDINGSETTINGSPARAMMASK
req.alt-loc: rilapitypes.h
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
req.product: Windows 10 or later.
---

# RILCALLFORWARDINGSETTINGSPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>