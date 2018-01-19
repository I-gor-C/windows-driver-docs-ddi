---
UID : NF:dbgeng.IDebugDataSpaces4.WriteBusData
title : IDebugDataSpaces4::WriteBusData method
author : windows-driver-content
description : The WriteBusData method writes data to a system bus.
old-location : debugger\writebusdata.htm
old-project : debugger
ms.assetid : bd4e762d-b3d5-4a4c-bdeb-998cd72783b4
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IDebugDataSpaces4, IDebugDataSpaces4::WriteBusData, WriteBusData
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
req.alt-api : IDebugDataSpaces.WriteBusData,IDebugDataSpaces2.WriteBusData,IDebugDataSpaces3.WriteBusData,IDebugDataSpaces4.WriteBusData
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


# WriteBusData method
The <b>WriteBusData</b> method writes data to a system bus.

## Syntax

````
HRESULT WriteBusData(
  [in]            ULONG  BusDataType,
  [in]            ULONG  BusNumber,
  [in]            ULONG  SlotNumber,
  [in]            ULONG  Offset,
  [in]            PVOID  Buffer,
  [in]            ULONG  BufferSize,
  [out, optional] PULONG BytesWritten
);
````

## Parameters

`BusDataType`

Specifies the bus data type of the bus to write to.  For details of allowed values see the documentation for the BUS_DATA_TYPE enumeration in the Microsoft Windows SDK.

`BusNumber`

Specifies the system-assigned number of the bus.  This is usually zero, unless the system has more than one bus of the same bus data type.

`SlotNumber`

Specifies the logical slot number on the bus.

`Offset`

Specifies the offset in the bus data to start writing to.

`Buffer`

Specifies the data to write to the bus.

`BufferSize`

Specifies the size in bytes of the buffer <i>Buffer</i>.  This is the maximum number of bytes that will be written.

`BytesWritten`

Receives the number of bytes written to the bus.  If <i>BytesWritten</i> is <b>NULL</b>, this information is not returned.


## Return Value

This method can also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.

## Remarks

This method is only available in kernel-mode debugging.

The nature of the data read from the bus is system, bus, and slot dependent.</p>

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