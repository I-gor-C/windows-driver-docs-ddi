---
UID: NE.ntddrilapitypes.RILUICCCOMMAND
title: RILUICCCOMMAND
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluicccommand.htm
ms.assetid: 1c2ded31-9d2d-46e4-a23f-a48528fd448f
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
req.alt-api: RILUICCCOMMAND
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

# RILUICCCOMMAND enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILUICCCOMMAND { 
  RIL_UICCCMD_READRECORD,
  RIL_UICCCMD_UPDATEBINARY,
  RIL_UICCCMD_UPDATERECORD,
  RIL_UICCCMD_MAX
} RILUICCCOMMAND;
````


## -enum-fields
<dl>

### -field <a id="RIL_UICCCMD_READRECORD"></a><a id="ril_uicccmd_readrecord"></a><b>RIL_UICCCMD_READRECORD</b>

<dd></dd>

### -field <a id="RIL_UICCCMD_UPDATEBINARY"></a><a id="ril_uicccmd_updatebinary"></a><b>RIL_UICCCMD_UPDATEBINARY</b>

<dd></dd>

### -field <a id="RIL_UICCCMD_UPDATERECORD"></a><a id="ril_uicccmd_updaterecord"></a><b>RIL_UICCCMD_UPDATERECORD</b>

<dd></dd>

### -field <a id="RIL_UICCCMD_MAX"></a><a id="ril_uicccmd_max"></a><b>RIL_UICCCMD_MAX</b>

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