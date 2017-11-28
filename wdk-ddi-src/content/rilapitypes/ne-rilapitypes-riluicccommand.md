---
UID: NE.rilapitypes.RILUICCCOMMAND
title: RILUICCCOMMAND
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluicccommand_2.htm
old-project: netvista
ms.assetid: 13861810-91a6-4027-81a0-297b049e3ee4
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.alt-api: RILUICCCOMMAND
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

# RILUICCCOMMAND enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>