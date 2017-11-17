---
UID: NE.rilapitypes.RILSETSYSTEMSELECTIONPREFSFLAG
title: RILSETSYSTEMSELECTIONPREFSFLAG
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsetsystemselectionprefsflag_2.htm
ms.assetid: d932f5c8-d6a6-4611-b6f2-12c501df1117
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILSETSYSTEMSELECTIONPREFSFLAG
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
ms.keywords: RIL_WritePhonebookEntry
req.iface: 
req.product: Windows 10 or later.
---

# RILSETSYSTEMSELECTIONPREFSFLAG enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>