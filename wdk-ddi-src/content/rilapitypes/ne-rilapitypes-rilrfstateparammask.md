---
UID: NE.rilapitypes.RILRFSTATEPARAMMASK
title: RILRFSTATEPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilrfstateparammask_2.htm
old-project: netvista
ms.assetid: 075c61aa-b091-4616-810b-f39ad40d2777
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
req.alt-api: RILRFSTATEPARAMMASK
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

# RILRFSTATEPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILRFSTATEPARAMMASK { 
  RIL_PARAM_RFSTATE_RFSTATE,
  RIL_PARAM_RFSTATE_RFDATASIZE,
  RIL_PARAM_RFSTATE_RFDATA,
  RIL_PARAM_RFSTATE_ALL
} RILRFSTATEPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_RFSTATE_RFSTATE"></a><a id="ril_param_rfstate_rfstate"></a><b>RIL_PARAM_RFSTATE_RFSTATE</b>

<dd></dd>

### -field <a id="RIL_PARAM_RFSTATE_RFDATASIZE"></a><a id="ril_param_rfstate_rfdatasize"></a><b>RIL_PARAM_RFSTATE_RFDATASIZE</b>

<dd></dd>

### -field <a id="RIL_PARAM_RFSTATE_RFDATA"></a><a id="ril_param_rfstate_rfdata"></a><b>RIL_PARAM_RFSTATE_RFDATA</b>

<dd></dd>

### -field <a id="RIL_PARAM_RFSTATE_ALL"></a><a id="ril_param_rfstate_all"></a><b>RIL_PARAM_RFSTATE_ALL</b>

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