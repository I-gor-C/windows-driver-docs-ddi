---
UID: NE.rilapitypes.RILUICCKEYREF
title: RILUICCKEYREF
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluicckeyref_2.htm
old-project: netvista
ms.assetid: 98edfbc2-cc45-4618-9c7c-020a20955dbd
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
req.alt-api: RILUICCKEYREF
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

# RILUICCKEYREF enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILUICCKEYREF { 
  RIL_UICCKEYREF_PIN1,
  RIL_UICCKEYREF_UPIN,
  RIL_UICCKEYREF_PIN2,
  RIL_UICCKEYREF_NEV
} RILUICCKEYREF;
````


## -enum-fields
<dl>

### -field <a id="RIL_UICCKEYREF_PIN1"></a><a id="ril_uicckeyref_pin1"></a><b>RIL_UICCKEYREF_PIN1</b>

<dd></dd>

### -field <a id="RIL_UICCKEYREF_UPIN"></a><a id="ril_uicckeyref_upin"></a><b>RIL_UICCKEYREF_UPIN</b>

<dd></dd>

### -field <a id="RIL_UICCKEYREF_PIN2"></a><a id="ril_uicckeyref_pin2"></a><b>RIL_UICCKEYREF_PIN2</b>

<dd></dd>

### -field <a id="RIL_UICCKEYREF_NEV"></a><a id="ril_uicckeyref_nev"></a><b>RIL_UICCKEYREF_NEV</b>

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