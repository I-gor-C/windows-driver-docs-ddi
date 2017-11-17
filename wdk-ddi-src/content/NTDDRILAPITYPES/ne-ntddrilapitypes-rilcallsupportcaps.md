---
UID: NE.ntddrilapitypes.RILCALLSUPPORTCAPS
title: RILCALLSUPPORTCAPS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallsupportcaps.htm
ms.assetid: 1573a1bd-8c47-4fdc-89d1-242e91ff0e47
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
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
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

### -field <a id="RIL_CAPS_CALLSUPPORT_CD"></a><a id="ril_caps_callsupport_cd"></a><b>RIL_CAPS_CALLSUPPORT_CD</b>

<dd></dd>

### -field <a id="RIL_CAPS_CALLSUPPORT_CNAP"></a><a id="ril_caps_callsupport_cnap"></a><b>RIL_CAPS_CALLSUPPORT_CNAP</b>

<dd></dd>

### -field <a id="RIL_CAPS_CALLSUPPORT_CUG"></a><a id="ril_caps_callsupport_cug"></a><b>RIL_CAPS_CALLSUPPORT_CUG</b>

<dd></dd>

### -field <a id="RIL_CAPS_CALLSUPPORT_EMLPP"></a><a id="ril_caps_callsupport_emlpp"></a><b>RIL_CAPS_CALLSUPPORT_EMLPP</b>

<dd></dd>

### -field <a id="RIL_CAPS_CALLSUPPORT_FM"></a><a id="ril_caps_callsupport_fm"></a><b>RIL_CAPS_CALLSUPPORT_FM</b>

<dd></dd>

### -field <a id="RIL_CAPS_CALLSUPPORT_MSP"></a><a id="ril_caps_callsupport_msp"></a><b>RIL_CAPS_CALLSUPPORT_MSP</b>

<dd></dd>

### -field <a id="RIL_CAPS_CALLSUPPORT_USSD_PHASE2"></a><a id="ril_caps_callsupport_ussd_phase2"></a><b>RIL_CAPS_CALLSUPPORT_USSD_PHASE2</b>

<dd></dd>

### -field <a id="RIL_CAPS_CALLSUPPORT_USS"></a><a id="ril_caps_callsupport_uss"></a><b>RIL_CAPS_CALLSUPPORT_USS</b>

<dd></dd>

### -field <a id="RIL_CAPS_CALLSUPPORT_ALL"></a><a id="ril_caps_callsupport_all"></a><b>RIL_CAPS_CALLSUPPORT_ALL</b>

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