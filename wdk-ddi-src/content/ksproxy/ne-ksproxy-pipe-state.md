---
UID: NE.ksproxy.PIPE_STATE
title: PIPE_STATE
author: windows-driver-content
description: .
old-location: stream\pipe_state.htm
old-project: stream
ms.assetid: A3053A39-5DB6-4DB8-89ED-63ABDB1CD16F
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagTRANSPORTVIDEOPARMS, TRANSPORTVIDEOPARMS, *PTRANSPORTVIDEOPARMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ksproxy.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PIPE_STATE
req.alt-loc: Ksproxy.h
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

# PIPE_STATE enumeration



## -description
<p></p>


## -syntax

````
typedef enum  { 
  PipeState_DontCare,
  PipeState_RangeNotFixed,
  PipeState_RangeFixed,
  PipeState_CompressionUnknown,
  PipeState_Finalized
} PIPE_STATE;
````


## -enum-fields
<dl>

### -field <a id="PipeState_DontCare"></a><a id="pipestate_dontcare"></a><a id="PIPESTATE_DONTCARE"></a><b>PipeState_DontCare</b>

<dd></dd>

### -field <a id="PipeState_RangeNotFixed"></a><a id="pipestate_rangenotfixed"></a><a id="PIPESTATE_RANGENOTFIXED"></a><b>PipeState_RangeNotFixed</b>

<dd></dd>

### -field <a id="PipeState_RangeFixed"></a><a id="pipestate_rangefixed"></a><a id="PIPESTATE_RANGEFIXED"></a><b>PipeState_RangeFixed</b>

<dd></dd>

### -field <a id="PipeState_CompressionUnknown"></a><a id="pipestate_compressionunknown"></a><a id="PIPESTATE_COMPRESSIONUNKNOWN"></a><b>PipeState_CompressionUnknown</b>

<dd></dd>

### -field <a id="PipeState_Finalized"></a><a id="pipestate_finalized"></a><a id="PIPESTATE_FINALIZED"></a><b>PipeState_Finalized</b>

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
<dt>Ksproxy.h</dt>
</dl>
</td>
</tr>
</table>