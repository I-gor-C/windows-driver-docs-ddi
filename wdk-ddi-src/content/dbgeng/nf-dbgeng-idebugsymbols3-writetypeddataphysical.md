---
UID : NF:dbgeng.IDebugSymbols3.WriteTypedDataPhysical
title : IDebugSymbols3::WriteTypedDataPhysical method
author : windows-driver-content
description : The WriteTypedDataPhysical method writes the value of a variable in the target computer's physical memory.
old-location : debugger\writetypeddataphysical.htm
old-project : debugger
ms.assetid : 5f29249f-bb62-45d1-aa0e-108db1d7f906
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IDebugSymbols3, IDebugSymbols3::WriteTypedDataPhysical, WriteTypedDataPhysical
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
req.alt-api : IDebugSymbols.WriteTypedDataPhysical,IDebugSymbols2.WriteTypedDataPhysical,IDebugSymbols3.WriteTypedDataPhysical
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


# WriteTypedDataPhysical method
The <b>WriteTypedDataPhysical</b> method writes the value of a variable in the target computer's physical memory.

## Syntax

````
HRESULT WriteTypedDataPhysical(
  [in]            ULONG64 Offset,
  [in]            ULONG64 Module,
  [in]            ULONG   TypeId,
  [in]            PVOID   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  BytesWritten
);
````

## Parameters

`Offset`

Specifies the physical address in the target computer's memory of the variable.

`Module`

Specifies the base address of the module containing the type of the variable.

`TypeId`

Specifies the type ID of the type of the variable.

`Buffer`

Specifies the buffer containing the data to be written.

`BufferSize`

Specifies the size in bytes of the buffer <i>Buffer</i>.  This is the maximum number of bytes to be written.

`BytesWritten`

Receives the number of bytes that were written.  If <i>BytesWritten</i> is <b>NULL</b>, this information is not returned.


## Return Value

This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.
<dl>
<dt><b>S_FALSE</b></dt>
</dl>The method was successful.  All the bytes in the buffer <i>Buffer</i> were written.  However, the buffer was smaller than the size of the specified type.

## Remarks

This method is only available in kernel mode debugging.

The number of bytes this method attempts to write is the smaller of the size of the buffer and the size of the variable.

This is a convenience method.  The same result can be obtained by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549457">GetTypeSize</a> and <a href="..\dbgeng\nf-dbgeng-idebugdataspaces-writephysical.md">WritePhysical</a>.

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