---
UID: NS.ksmedia.PTRANSPORT_STATE
title: PTRANSPORT_STATE
author: windows-driver-content
description: The TRANSPORT_STATE structure
old-location: stream\transport_state.htm
ms.assetid: 373fb91d-e469-4136-b2e3-bf57016c0fd6
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TRANSPORT_STATE
req.alt-loc: ksmedia.h
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
ms.keywords: PTRANSPORT_STATE, TRANSPORT_STATE, *PTRANSPORT_STATE
req.iface: 
---

# PTRANSPORT_STATE structure



## -description
<p>The TRANSPORT_STATE structure </p>


## -syntax

````
typedef struct {
  ULONG Mode;
  ULONG State;
} TRANSPORT_STATE, *PTRANSPORT_STATE;
````


## -struct-fields
<dl>

### -field <b>Mode</b>

<dd>
<p>Specifies the mode of the external device transport.</p>
</dd>

### -field <b>State</b>

<dd>
<p>Specifies the state of the external device transport mode.</p>
</dd>
</dl>

## -remarks
<p>Any ED_Xxx tokens are defined in <i>xprtdefs.h</i> in the Microsoft DirectX SDK.</p>

<p>The following modes and states are used by <i>msdv.sys </i>and <i>mstape.sys</i>:</p>

<p>When <b>Mode</b> equals ED_MODE_RECORD, <b>State</b> may be:</p><dl>
<dd>
<p>ED_MODE_RECORD</p>
</dd>
<dd>
<p>ED_MODE_RECORD_FREEZE.</p>
</dd>
</dl><p>ED_MODE_RECORD</p>

<p>ED_MODE_RECORD_FREEZE.</p>

<p>When <b>Mode</b> equals ED_MODE_PLAY, <b>State</b> may be:</p><dl>
<dd>
<p>ED_MODE_PLAY</p>
</dd>
<dd>
<p>ED_MODE_REV_PLAY</p>
</dd>
<dd>
<p>ED_MODE_STEP_FWD</p>
</dd>
<dd>
<p>ED_MODE_STEP_REV</p>
</dd>
<dd>
<p>ED_MODE_PLAY_SLOWEST_FWD</p>
</dd>
<dd>
<p>ED_MODE_PLAY_FASTEST_FWD</p>
</dd>
<dd>
<p>ED_MODE_PLAY_SLOWEST_REV</p>
</dd>
<dd>
<p>ED_MODE_PLAY_FASTEST_REV</p>
</dd>
<dd>
<p>ED_MODE_FREEZE</p>
</dd>
</dl><p>ED_MODE_PLAY</p>

<p>ED_MODE_REV_PLAY</p>

<p>ED_MODE_STEP_FWD</p>

<p>ED_MODE_STEP_REV</p>

<p>ED_MODE_PLAY_SLOWEST_FWD</p>

<p>ED_MODE_PLAY_FASTEST_FWD</p>

<p>ED_MODE_PLAY_SLOWEST_REV</p>

<p>ED_MODE_PLAY_FASTEST_REV</p>

<p>ED_MODE_FREEZE</p>

<p><b>Mode</b> equals <b>State</b> in the cases of:</p><dl>
<dd>
<p>ED_MODE_REW_FASTEST</p>
</dd>
<dd>
<p>ED_MODE_STOP</p>
</dd>
<dd>
<p>ED_MODE_PLAY</p>
</dd>
<dd>
<p>ED_MODE_FF</p>
</dd>
</dl><p>ED_MODE_REW_FASTEST</p>

<p>ED_MODE_STOP</p>

<p>ED_MODE_PLAY</p>

<p>ED_MODE_FF</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>