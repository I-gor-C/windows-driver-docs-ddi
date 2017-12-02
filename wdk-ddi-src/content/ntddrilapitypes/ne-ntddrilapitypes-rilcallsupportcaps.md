---
UID: NE.ntddrilapitypes.RILCALLSUPPORTCAPS
title: RILCALLSUPPORTCAPS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallsupportcaps.htm
old-project: netvista
ms.assetid: 1573a1bd-8c47-4fdc-89d1-242e91ff0e47
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: RILCALLSUPPORTCAPS
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

# RILCALLSUPPORTCAPS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILCALLSUPPORTCAPS { 
  RIL_CAPS_CALLSUPPORT_CD,
  RIL_CAPS_CALLSUPPORT_CNAP,
  RIL_CAPS_CALLSUPPORT_CUG,
  RIL_CAPS_CALLSUPPORT_EMLPP,
  RIL_CAPS_CALLSUPPORT_FM,
  RIL_CAPS_CALLSUPPORT_MSP,
  RIL_CAPS_CALLSUPPORT_USSD_PHASE2,
  RIL_CAPS_CALLSUPPORT_USS,
  RIL_CAPS_CALLSUPPORT_ALL
} RILCALLSUPPORTCAPS;
````


## -enum-fields
<dl>

### -field RIL_CAPS_CALLSUPPORT_CD

<dd></dd>

### -field RIL_CAPS_CALLSUPPORT_CNAP

<dd></dd>

### -field RIL_CAPS_CALLSUPPORT_CUG

<dd></dd>

### -field RIL_CAPS_CALLSUPPORT_EMLPP

<dd></dd>

### -field RIL_CAPS_CALLSUPPORT_FM

<dd></dd>

### -field RIL_CAPS_CALLSUPPORT_MSP

<dd></dd>

### -field RIL_CAPS_CALLSUPPORT_USSD_PHASE2

<dd></dd>

### -field RIL_CAPS_CALLSUPPORT_USS

<dd></dd>

### -field RIL_CAPS_CALLSUPPORT_ALL

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