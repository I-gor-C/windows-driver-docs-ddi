---
UID: NF.wdm.READ_PORT_BUFFER_ULONG~r2
title: READ_PORT_BUFFER_ULONG function
author: windows-driver-content
description: The READ_PORT_BUFFER_ULONG routine reads a number of ULONG values from the specified port address into a buffer.
old-location: kernel\read_port_buffer_ulong.htm
old-project: kernel
ms.assetid: a63028d8-f90e-4f86-81f5-27bc727ecad7
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: READ_PORT_BUFFER_ULONG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: READ_PORT_BUFFER_ULONG
req.alt-loc: Hal.lib,Hal.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hal.lib
req.dll: 
req.irql: Any level (see Remarks section)
req.product: Windows 10 or later.
---

# READ_PORT_BUFFER_ULONG function



## -description
The <b>READ_PORT_BUFFER_ULONG</b> routine reads a number of ULONG values from the specified port address into a buffer.



## -syntax

````
VOID READ_PORT_BUFFER_ULONG(
  _In_  PULONG Port,
  _Out_ PULONG Buffer,
  _In_  ULONG  Count
);
````


## -parameters

### -param Port [in]

Specifies the port address, which must be a mapped memory range in I/O space.


### -param Buffer [out]

Pointer to a buffer into which an array of ULONG values is read.


### -param Count [in]

Specifies the number of ULONG values to be read into the buffer. 


## -returns
None


## -remarks
The size of the buffer must be large enough to contain at least the specified number of ULONG values.

Callers of <b>READ_PORT_BUFFER_ULONG</b> can be running at any IRQL, assuming the <i>Buffer</i> is resident and the <i>Port</i> is resident, mapped device memory.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows 2000.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Hal.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level (see Remarks section)

</td>
</tr>
</table>