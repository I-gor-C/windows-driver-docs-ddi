---
UID : NF:dbgeng.IDebugSymbols3.ReadTypedDataVirtual
title : IDebugSymbols3::ReadTypedDataVirtual method
author : windows-driver-content
description : The ReadTypedDataVirtual method reads the value of a variable in the target's virtual memory.
old-location : debugger\readtypeddatavirtual.htm
old-project : debugger
ms.assetid : 526bebd8-95af-4f6f-a381-eb60273d1af5
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IDebugSymbols3, IDebugSymbols3::ReadTypedDataVirtual, ReadTypedDataVirtual
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
req.alt-api : IDebugSymbols.ReadTypedDataVirtual,IDebugSymbols2.ReadTypedDataVirtual,IDebugSymbols3.ReadTypedDataVirtual
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


# ReadTypedDataVirtual method
The <b>ReadTypedDataVirtual</b> method reads the value of a variable in the target's virtual memory.

## Syntax

````
HRESULT ReadTypedDataVirtual(
  [in]            ULONG64 Offset,
  [in]            ULONG64 Module,
  [in]            ULONG   TypeId,
  [out]           PVOID   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  BytesRead
);
````

## Parameters

`Offset`

Specifies the location in the target's virtual address space of the variable to read.

`Module`

Specifies the base address of the module containing the type of the variable.

`TypeId`

Specifies the type ID of the type.

`Buffer`

Receives the data that is read.

`BufferSize`

Specifies the size in bytes of the buffer <i>Buffer</i>.  This is the maximum number of bytes to be read.

`BytesRead`

Receives the number of bytes that were read.  If <i>BytesRead</i> is <b>NULL</b>, this information is not returned.


## Return Value

<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.
<dl>
<dt><b>S_FALSE</b></dt>
</dl>The method was successful.  However, the buffer <i>Buffer</i> was not large enough to hold all the data and it was truncated.

 

This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.

## Remarks

The number of bytes this method attempts to read is the smaller of the size of the buffer and the size of the variable.

This is a convenience method.  The same result can be obtained by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549457">GetTypeSize</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff554359">ReadVirtual</a>.

For more information about types, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558931">Types</a>.</p>

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