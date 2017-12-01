---
UID: NF.dbgeng.IDebugDataSpaces2.WriteBusData
title: IDebugDataSpaces2::WriteBusData
author: windows-driver-content
description: The WriteBusData method writes data to a system bus.
old-location: debugger\writebusdata.htm
old-project: debugger
ms.assetid: bd4e762d-b3d5-4a4c-bdeb-998cd72783b4
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugDataSpaces2, WriteBusData, IDebugDataSpaces2::WriteBusData
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
req.alt-api: IDebugDataSpaces.WriteBusData,IDebugDataSpaces2.WriteBusData,IDebugDataSpaces3.WriteBusData,IDebugDataSpaces4.WriteBusData
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
req.iface: IDebugDataSpaces2
---

# IDebugDataSpaces2::WriteBusData method



## -description
<p>The <b>WriteBusData</b> method writes data to a system bus.</p>


## -syntax

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


## -parameters
<dl>

### -param <i>BusDataType</i> [in]

<dd>
<p>Specifies the bus data type of the bus to write to.  For details of allowed values see the documentation for the BUS_DATA_TYPE enumeration in the Microsoft Windows SDK.</p>
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
<p>Specifies the offset in the bus data to start writing to.</p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>Specifies the data to write to the bus.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size in bytes of the buffer <i>Buffer</i>.  This is the maximum number of bytes that will be written.</p>
</dd>

### -param <i>BytesWritten</i> [out, optional]

<dd>
<p>Receives the number of bytes written to the bus.  If <i>BytesWritten</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

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