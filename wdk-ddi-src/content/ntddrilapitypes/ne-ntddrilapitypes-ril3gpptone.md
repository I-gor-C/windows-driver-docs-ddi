---
UID: NE.ntddrilapitypes.RIL3GPPTONE
title: RIL3GPPTONE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\ril3gpptone.htm
old-project: netvista
ms.assetid: 3dd7c317-b77f-4cc1-8513-ed305418e76f
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
req.alt-api: RIL3GPPTONE
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

# RIL3GPPTONE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RIL3GPPTONE { 
  RIL_3GPPTONE_RINGBACK,
  RIL_3GPPTONE_BUSY,
  RIL_3GPPTONE_CONGESTION,
  RIL_3GPPTONE_AUTHENTICATIONFAILURE,
  RIL_3GPPTONE_NUMBERUNOBTAINABLE,
  RIL_3GPPTONE_CALLDROPPED,
  RIL_3GPPTONE_MAX
} RIL3GPPTONE;
````


## -enum-fields
<dl>

### -field <a id="RIL_3GPPTONE_RINGBACK"></a><a id="ril_3gpptone_ringback"></a><b>RIL_3GPPTONE_RINGBACK</b>

<dd></dd>

### -field <a id="RIL_3GPPTONE_BUSY"></a><a id="ril_3gpptone_busy"></a><b>RIL_3GPPTONE_BUSY</b>

<dd></dd>

### -field <a id="RIL_3GPPTONE_CONGESTION"></a><a id="ril_3gpptone_congestion"></a><b>RIL_3GPPTONE_CONGESTION</b>

<dd></dd>

### -field <a id="RIL_3GPPTONE_AUTHENTICATIONFAILURE"></a><a id="ril_3gpptone_authenticationfailure"></a><b>RIL_3GPPTONE_AUTHENTICATIONFAILURE</b>

<dd></dd>

### -field <a id="RIL_3GPPTONE_NUMBERUNOBTAINABLE"></a><a id="ril_3gpptone_numberunobtainable"></a><b>RIL_3GPPTONE_NUMBERUNOBTAINABLE</b>

<dd></dd>

### -field <a id="RIL_3GPPTONE_CALLDROPPED"></a><a id="ril_3gpptone_calldropped"></a><b>RIL_3GPPTONE_CALLDROPPED</b>

<dd></dd>

### -field <a id="RIL_3GPPTONE_MAX"></a><a id="ril_3gpptone_max"></a><b>RIL_3GPPTONE_MAX</b>

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