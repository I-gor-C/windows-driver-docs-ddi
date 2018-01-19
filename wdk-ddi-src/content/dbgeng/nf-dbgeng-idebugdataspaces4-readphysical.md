---
UID : NF:dbgeng.IDebugDataSpaces4.ReadPhysical
title : IDebugDataSpaces4::ReadPhysical method
author : windows-driver-content
description : The ReadPhysical method reads the target's memory from the specified physical address.
old-location : debugger\readphysical3.htm
old-project : debugger
ms.assetid : 8df51985-9208-46ce-8802-6bc5ec707ab2
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IDebugDataSpaces4, IDebugDataSpaces4::ReadPhysical, ReadPhysical
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
req.alt-api : IDebugDataSpaces.ReadPhysical,IDebugDataSpaces2.ReadPhysical,IDebugDataSpaces3.ReadPhysical,IDebugDataSpaces4.ReadPhysical
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


# ReadPhysical method
The <b>ReadPhysical</b> method reads the target's memory from the specified physical address.

## Syntax

````
HRESULT ReadPhysical(
  [in]            ULONG64 Offset,
  [out]           PVOID   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  BytesRead
);
````

## Parameters

`Offset`

Specifies the physical address of the memory to read.

`Buffer`

Receives the memory that is read.

`BufferSize`

Specifies the size in bytes of the buffer <i>Buffer</i>.  This is the maximum number of bytes that will be read.

`BytesRead`

Receives the number of bytes read from the target's memory.  If <i>BytesRead</i> is <b>NULL</b>, this information is not returned.


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