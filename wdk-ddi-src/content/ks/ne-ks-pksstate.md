---
UID: NE.ks.PKSSTATE
title: PKSSTATE
author: windows-driver-content
description: The KSSTATE enumeration lists possible states of a kernel streaming object.
old-location: stream\ksstate.htm
old-project: stream
ms.assetid: 6f5a3c65-9d6c-4d5f-af99-71aba16eb254
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSSTATE
req.alt-loc: ks.h
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

# PKSSTATE enumeration



## -description
<p>The KSSTATE enumeration lists possible states of a kernel streaming object.</p>


## -syntax

````
typedef enum  { 
  KSSTATE_STOP     = 0,
  KSSTATE_ACQUIRE  = 1,
  KSSTATE_PAUSE    = 2,
  KSSTATE_RUN      = 3
} KSSTATE, *PKSSTATE;
````


## -enum-fields
<dl>

### -field <a id="KSSTATE_STOP"></a><a id="ksstate_stop"></a><b>KSSTATE_STOP</b>

<dd>
<p>Indicates that the object is in minimum resource consumption mode.</p>
</dd>

### -field <a id="KSSTATE_ACQUIRE"></a><a id="ksstate_acquire"></a><b>KSSTATE_ACQUIRE</b>

<dd>
<p>Indicates that the object is acquiring resources.</p>
</dd>

### -field <a id="KSSTATE_PAUSE"></a><a id="ksstate_pause"></a><b>KSSTATE_PAUSE</b>

<dd>
<p>Indicates that the object is preparing to make instant transition to Run state.</p>
</dd>

### -field <a id="KSSTATE_RUN"></a><a id="ksstate_run"></a><b>KSSTATE_RUN</b>

<dd>
<p>Indicates that the object is actively streaming.</p>
</dd>
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
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>