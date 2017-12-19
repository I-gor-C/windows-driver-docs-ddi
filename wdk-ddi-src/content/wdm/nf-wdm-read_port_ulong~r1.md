---
UID: NF.wdm.READ_PORT_ULONG~r1
title: READ_PORT_ULONG function
author: windows-driver-content
description: The READ_PORT_ULONG routine reads a ULONG value from the specified port address.
old-location: kernel\read_port_ulong.htm
old-project: kernel
ms.assetid: 8a2f4429-b805-4a36-afdf-8b9c9a886951
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: READ_PORT_ULONG
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
req.alt-api: READ_PORT_ULONG
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

# READ_PORT_ULONG function



## -description
The <b>READ_PORT_ULONG</b> routine reads a ULONG value from the specified port address.



## -syntax

````
ULONG READ_PORT_ULONG(
  _In_ PULONG Port
);
````


## -parameters

### -param Port [in]

Specifies the port address, which must be a mapped range in I/O space. 


## -returns
<b>READ_PORT_ULONG</b> returns the ULONG value that is read from the specified port address.


## -remarks
Callers of <b>READ_PORT_ULONG</b> can be running at any IRQL, assuming the <i>Port</i> is resident, mapped device memory.


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