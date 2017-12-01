---
UID: NF.dbgeng.IDebugDataSpaces.ReadBusData
title: IDebugDataSpaces::ReadBusData
author: windows-driver-content
description: The ReadBusData method reads data from a system bus.
old-location: debugger\readbusdata.htm
old-project: debugger
ms.assetid: 5790b133-dbdc-4f77-a70e-616b0902794e
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugDataSpaces, ReadBusData, IDebugDataSpaces::ReadBusData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugDataSpaces.ReadBusData,IDebugDataSpaces2.ReadBusData,IDebugDataSpaces3.ReadBusData,IDebugDataSpaces4.ReadBusData
req.alt-loc: dbgeng.h
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
req.iface: IDebugDataSpaces
---

# IDebugDataSpaces::ReadBusData method



## -description
<p>The <b>ReadBusData</b> method reads data from a system bus.</p>


## -syntax

````
HRESULT ReadBusData(
  [in]            ULONG  BusDataType,
  [in]            ULONG  BusNumber,
  [in]            ULONG  SlotNumber,
  [in]            ULONG  Offset,
  [out]           PVOID  Buffer,
  [in]            ULONG  BufferSize,
  [out, optional] PULONG BytesRead
);
````


## -parameters
<dl>

### -param <i>BusDataType</i> [in]

<dd>
<p>Specifies the bus data type to read from.  For details of allowed values see the documentation for the BUS_DATA_TYPE enumeration in the Microsoft Windows SDK.</p>
</dd>

### -param <i>BusNumber</i> [in]

<dd>
<p>Specifies the system-assigned number of the bus.  This is usually zero, unless the system has more than one bus of the same bus data type.</p>
</dd>

### -param <i>SlotNumber</i> [in]

<dd>
<p>Specifies the logical slot number on the bus.</p>
</dd>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies the offset in the bus data to start reading from.</p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>Receives the data from the bus.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size in bytes of the buffer <i>Buffer</i>.  This is the maximum number of bytes that will be returned.</p>
</dd>

### -param <i>BytesRead</i> [out, optional]

<dd>
<p>Receives the number of bytes read from the bus.  If <i>BytesRead</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p>

## -remarks
<p>This method is only available in kernel-mode debugging.</p>

<p>The nature of the data read from the bus is system, bus, and slot dependent.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>