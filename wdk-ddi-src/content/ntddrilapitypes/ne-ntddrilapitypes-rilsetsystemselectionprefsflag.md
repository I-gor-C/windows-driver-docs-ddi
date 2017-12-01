---
UID: NE.ntddrilapitypes.RILSETSYSTEMSELECTIONPREFSFLAG
title: RILSETSYSTEMSELECTIONPREFSFLAG
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsetsystemselectionprefsflag.htm
old-project: netvista
ms.assetid: 081f4a23-43d8-4ad4-806c-1b6322e057d5
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
req.alt-api: RILSETSYSTEMSELECTIONPREFSFLAG
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

# RILSETSYSTEMSELECTIONPREFSFLAG enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILSETSYSTEMSELECTIONPREFSFLAG { 
  RIL_SSSPFLAG_APPLYIMMEDIATELY,
  RIL_SSSPFLAG_ENFORCESCAN,
  RIL_SSSPFLAG_ALL
} RILSETSYSTEMSELECTIONPREFSFLAG;
````


## -enum-fields
<dl>

### -field <a id="RIL_SSSPFLAG_APPLYIMMEDIATELY"></a><a id="ril_ssspflag_applyimmediately"></a><b>RIL_SSSPFLAG_APPLYIMMEDIATELY</b>

<dd></dd>

### -field <a id="RIL_SSSPFLAG_ENFORCESCAN"></a><a id="ril_ssspflag_enforcescan"></a><b>RIL_SSSPFLAG_ENFORCESCAN</b>

<dd></dd>

### -field <a id="RIL_SSSPFLAG_ALL"></a><a id="ril_ssspflag_all"></a><b>RIL_SSSPFLAG_ALL</b>

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