---
UID: NS.bdatypes._BDA_TUNER_TUNERSTATE
title: BDA_TUNER_TUNERSTATE
author: windows-driver-content
description: TBD.
old-location: stream\bda_tuner_tunerstate.htm
ms.assetid: 77B30ADC-27F2-4883-97FC-F6C29B539EE0
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: bdatypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDA_TUNER_TUNERSTATE
req.alt-loc: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: BDA_TUNER_TUNERSTATE, BDA_TUNER_TUNERSTATE, *PBDA_TUNER_TUNERSTATE
req.iface: 
---

# BDA_TUNER_TUNERSTATE structure



## -description
<p>TBD</p>


## -syntax

````
typedef struct _BDA_TUNER_TUNERSTATE {
  PBDARESULT lResult;
  ULONG      ulTuneLength;
  BYTE       argbTuneData[MIN_DIMENSION];
} BDA_TUNER_TUNERSTATE, *PBDA_TUNER_TUNERSTATE;
````


## -struct-fields
<dl>

### -field <b>lResult</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>ulTuneLength</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>argbTuneData</b>

<dd>
<p>TBD</p>
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
<dt>Bdatypes.h</dt>
</dl>
</td>
</tr>
</table>