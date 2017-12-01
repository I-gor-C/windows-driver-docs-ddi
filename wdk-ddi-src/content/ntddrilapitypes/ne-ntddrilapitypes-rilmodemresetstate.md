---
UID: NE.ntddrilapitypes.RILMODEMRESETSTATE
title: RILMODEMRESETSTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmodemresetstate.htm
old-project: netvista
ms.assetid: 4069ded7-95d7-46c2-a4a7-a360482c7b7d
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
req.alt-api: RILMODEMRESETSTATE
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

# RILMODEMRESETSTATE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILMODEMRESETSTATE { 
  RIL_MODEMRESETSTATE_RECOVERED,
  RIL_MODEMRESETSTATE_FAILED,
  RIL_MODEMRESETSTATE_MAX
} RILMODEMRESETSTATE;
````


## -enum-fields
<dl>

### -field <a id="RIL_MODEMRESETSTATE_RECOVERED"></a><a id="ril_modemresetstate_recovered"></a><b>RIL_MODEMRESETSTATE_RECOVERED</b>

<dd></dd>

### -field <a id="RIL_MODEMRESETSTATE_FAILED"></a><a id="ril_modemresetstate_failed"></a><b>RIL_MODEMRESETSTATE_FAILED</b>

<dd></dd>

### -field <a id="RIL_MODEMRESETSTATE_MAX"></a><a id="ril_modemresetstate_max"></a><b>RIL_MODEMRESETSTATE_MAX</b>

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