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
ms.keywords : PIPE_STATE, PipeState_CompressionUnknown, ksproxy/PipeState_Finalized, ksproxy/PipeState_RangeFixed, PipeState_DontCare, stream.pipe_state, PipeState_RangeFixed, PIPE_STATE enumeration [Streaming Media Devices], PipeState_RangeNotFixed, ksproxy/PIPE_STATE, PipeState_Finalized, ksproxy/PipeState_DontCare, ksproxy/PipeState_RangeNotFixed, ksproxy/PipeState_CompressionUnknown
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
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