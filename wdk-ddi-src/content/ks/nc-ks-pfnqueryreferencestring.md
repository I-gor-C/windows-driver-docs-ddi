---
UID: NC.ks.PFNQUERYREFERENCESTRING
title: PFNQUERYREFERENCESTRING
author: windows-driver-content
description: This routine creates a buffer from the paged pool and copies the reference string associated with the PDO into this buffer. It is the caller's responsibility to free the buffer using ExFreePool.
old-location: stream\kstrqueryreferencestring.htm
old-project: stream
ms.assetid: 08fd750f-19cc-4d78-a26b-9f790c5c3acf
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KStrQueryReferenceString
req.alt-loc: ks.h
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

# PFNQUERYREFERENCESTRING callback



## -description
<p>This routine creates a buffer from the paged pool and copies the reference string associated with the PDO into this buffer. It is the caller's responsibility to free the buffer using <a href="..\ntddk\nf-ntddk-exfreepool.md">ExFreePool</a>.</p>


## -prototype

````
PFNQUERYREFERENCESTRING KStrQueryReferenceString;

NTSTATUS KStrQueryReferenceString(
  _In_    PVOID  Context,
  _Inout_ PWCHAR *String
)
{ ... }
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>Pointer to a device extension of the device's PDO.</p>
</dd>

### -param <i>String</i> [in, out]

<dd>
<p>Pointer to a string containing the reference string associated with the PDO.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>The driver can access this method through the <b>QueryReferenceString</b> member of the <a href="stream.bus_interface_reference">BUS_INTERFACE_REFERENCE</a> structure.</p>

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
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>