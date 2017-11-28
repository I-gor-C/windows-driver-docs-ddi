---
UID: NE.ntddrilapitypes.RILCALLWAITINGINFOPARAMMASK
title: RILCALLWAITINGINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallwaitinginfoparammask.htm
old-project: netvista
ms.assetid: 18fa3b00-8da7-4c83-a340-1515caffda01
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
req.alt-api: RILCALLWAITINGINFOPARAMMASK
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

# RILCALLWAITINGINFOPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILCALLWAITINGINFOPARAMMASK { 
  RIL_PARAM_CWI_CALLTYPE,
  RIL_PARAM_CWI_CALLERINFO,
  RIL_PARAM_CWI_ALL
} RILCALLWAITINGINFOPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_CWI_CALLTYPE"></a><a id="ril_param_cwi_calltype"></a><b>RIL_PARAM_CWI_CALLTYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_CWI_CALLERINFO"></a><a id="ril_param_cwi_callerinfo"></a><b>RIL_PARAM_CWI_CALLERINFO</b>

<dd></dd>

### -field <a id="RIL_PARAM_CWI_ALL"></a><a id="ril_param_cwi_all"></a><b>RIL_PARAM_CWI_ALL</b>

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