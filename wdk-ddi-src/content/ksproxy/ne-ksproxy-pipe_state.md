---
UID : NE:ksproxy.PIPE_STATE
title : PIPE_STATE
author : windows-driver-content
description : .
old-location : stream\pipe_state.htm
old-project : stream
ms.assetid : A3053A39-5DB6-4DB8-89ED-63ABDB1CD16F
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : PIPE_STATE, PIPE_STATE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ksproxy.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : PIPE_STATE
req.alt-loc : Ksproxy.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : PIPE_STATE
---

# PIPE_STATE Enumeration


## Syntax
````
typedef enum  { 
  PipeState_DontCare,
  PipeState_RangeNotFixed,
  PipeState_RangeFixed,
  PipeState_CompressionUnknown,
  PipeState_Finalized
} PIPE_STATE;
````

## Constants

<table>

<tr>
<td>PipeState_CompressionUnknown</td>
<td></td>
</tr>

<tr>
<td>PipeState_DontCare</td>
<td></td>
</tr>

<tr>
<td>PipeState_Finalized</td>
<td></td>
</tr>

<tr>
<td>PipeState_RangeFixed</td>
<td></td>
</tr>

<tr>
<td>PipeState_RangeNotFixed</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ksproxy.h |