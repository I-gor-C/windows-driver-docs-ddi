---
UID: NF.kcom.KoDriverInitialize
title: KoDriverInitialize
author: windows-driver-content
description: The KoDriverInitialize function initializes a driver object to handle the kernel streaming interface.
old-location: stream\kodriverinitialize.htm
old-project: stream
ms.assetid: ed61d135-967d-4e7c-b437-09c9e0e6f3c2
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KoDriverInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: kcom.h
req.include-header: Kcom.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KoDriverInitialize
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
req.iface: 
---

# KoDriverInitialize function



## -description
<p><i>This function is intended for internal use only.</i></p>
<p>The <b>KoDriverInitialize</b> function initializes a driver object to handle the kernel streaming interface. </p>


## -syntax

````
NTSTATUS KoDriverInitialize(
  _In_ PDRIVER_OBJECT        DriverObject,
  _In_ PUNICODE_STRING       RegistryPathName,
  _In_ KoCreateObjectHandler CreateObjectHandler
);
````


## -parameters
<dl>

### -param DriverObject [in]

<dd>
<p>Pointer to a driver object to initialize that handles the kernel streaming interface.</p>
</dd>

### -param RegistryPathName [in]

<dd>
<p>Pointer to the registry path that is associated with the driver object.</p>
</dd>

### -param CreateObjectHandler [in]

<dd>
<p>Pointer to a function used to create new objects.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if successful. Otherwise, it returns a memory allocation error.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Kcom.h (include Kcom.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>