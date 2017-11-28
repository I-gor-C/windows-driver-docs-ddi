---
UID: NS.mpiowmi._MPIO_ADAPTER_INFORMATION
title: MPIO_ADAPTER_INFORMATION
author: windows-driver-content
description: The MPIO_ADAPTER_INFORMATION structure contains information that pertains to MPIO's view of a path.
old-location: storage\mpio_adapter_information.htm
old-project: storage
ms.assetid: bcf159a7-75a5-46aa-897a-2c5eb00f51d8
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MPIO_ADAPTER_INFORMATION, MPIO_ADAPTER_INFORMATION, *PMPIO_ADAPTER_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: mpiowmi.h
req.include-header: Mpiowmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MPIO_ADAPTER_INFORMATION
req.alt-loc: mpiowmi.h
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

# MPIO_ADAPTER_INFORMATION structure



## -description
<p>The MPIO_ADAPTER_INFORMATION structure contains information that pertains to MPIO's view of a path.</p>


## -syntax

````
typedef struct _MPIO_ADAPTER_INFORMATION {
  ULONGLONG PathId;
  UCHAR     BusNumber;
  UCHAR     DeviceNumber;
  UCHAR     FunctionNumber;
  UCHAR     Pad;
  WCHAR     AdapterName[63 + 1];
} MPIO_ADAPTER_INFORMATION, *PMPIO_ADAPTER_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>PathId</b>

<dd>
<p>An unsigned 64-bitfield that represents an identifier that is assigned to a particular path. This field will match the PathIdentifier field in the instance(s) of the PDO_INFORMATION class that represent device(s) exposed via this path.</p>
</dd>

### -field <b>BusNumber</b>

<dd>
<p>An unsigned 8-bitfield that corresponds to the bus number that is assigned by PCI to the host bus adapter through which this path is exposed.</p>
</dd>

### -field <b>DeviceNumber</b>

<dd>
<p>An unsigned 8-bitfield that corresponds to the device number that is assigned by PCI to the host bus adapter through which this path is exposed.</p>
</dd>

### -field <b>FunctionNumber</b>

<dd>
<p>An unsigned 8-bitfield that corresponds to the function number that is assigned by PCI to the host bus adapter through which this path is exposed.</p>
</dd>

### -field <b>Pad</b>

<dd>
<p>Should be zero.</p>
</dd>

### -field <b>AdapterName</b>

<dd>
<p>A string field that returns the friendly name of the host bus adapter through which this path is exposed.</p>
</dd>
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
<dt>Mpiowmi.h (include Mpiowmi.h)</dt>
</dl>
</td>
</tr>
</table>