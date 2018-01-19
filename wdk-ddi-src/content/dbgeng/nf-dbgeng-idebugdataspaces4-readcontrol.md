---
UID : NF:dbgeng.IDebugDataSpaces4.ReadControl
title : IDebugDataSpaces4::ReadControl method
author : windows-driver-content
description : The ReadControl method reads implementation-specific system data.
old-location : debugger\readcontrol.htm
old-project : debugger
ms.assetid : 52f65e2a-97a7-4c1c-a021-208bc2520b7d
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IDebugDataSpaces4, IDebugDataSpaces4::ReadControl, ReadControl
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : dbgeng.h
req.include-header : Dbgeng.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IDebugDataSpaces.ReadControl,IDebugDataSpaces2.ReadControl,IDebugDataSpaces3.ReadControl,IDebugDataSpaces4.ReadControl
req.alt-loc : dbgeng.h
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
req.typenames : "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
---


# ReadControl method
The <b>ReadControl</b> method reads implementation-specific system data.

## Syntax

````
HRESULT ReadControl(
  [in]            ULONG   Processor,
  [in]            ULONG64 Offset,
  [out]           PVOID   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  BytesRead
);
````

## Parameters

`Processor`

Specifies the processor whose information is to be read.

`Offset`

Specifies the offset in the control space of the memory to read.

`Buffer`

Receives the data read from the control-space memory.

`BufferSize`

Specifies the size in bytes of the buffer <i>Buffer</i>.  This is the maximum number of bytes that will be read.

`BytesRead`

Receives the number of bytes returned in the buffer <i>Buffer</i>.  If <i>BytesRead</i> is <b>NULL</b>, this information is not returned.


## Return Value

<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.

 

This method can also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.

## Remarks

This method is only available in kernel-mode debugging.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h (include Dbgeng.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |