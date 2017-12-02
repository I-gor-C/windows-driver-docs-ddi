---
UID: NF.kcom.KoCreateInstance
title: KoCreateInstance
author: windows-driver-content
description: The KoCreateInstance function creates an object of the class with the specified CLSID.
old-location: stream\kocreateinstance.htm
old-project: stream
ms.assetid: ee719cbe-0933-4adc-b5c7-62b66f2bf4e1
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KoCreateInstance
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
req.alt-api: KoCreateInstance
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

# KoCreateInstance function



## -description
<p><i>This function is intended for internal use only.</i></p>
<p>The <b>KoCreateInstance</b> function creates an object of the class with the specified CLSID. </p>


## -syntax

````
NTSTATUS KoCreateInstance(
  _In_     REFCLSID ClassId,
  _In_opt_ IUnknown *UnkOuter,
  _In_     ULONG    ClsContext,
  _In_     REFIID   InterfaceId,
  _Out_    PVOID    *Interface
);
````


## -parameters
<dl>

### -param ClassId [in]

<dd>
<p>The CLSID of the object to create an instance of.</p>
</dd>

### -param UnkOuter [in, optional]

<dd>
<p>The outer unknown object to pass to the new instance.</p>
</dd>

### -param ClsContext [in]

<dd>
<p>The context in which to create the instance. This must be CLSCTX_KERNEL_SERVER.</p>
</dd>

### -param InterfaceId [in]

<dd>
<p>Reference to the identifier of the interface that will communicate with the object.</p>
</dd>

### -param Interface [out]

<dd>
<p>Address of the pointer variable that receives the new interface pointer specified in <i>InterfaceId</i>.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if the instance was successfully created. Otherwise, it returns an error.</p>

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