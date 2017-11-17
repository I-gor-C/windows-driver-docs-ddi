---
UID: NF.ksproxy.KsOpenDefaultDevice
title: KsOpenDefaultDevice
author: windows-driver-content
description: The KsOpenDefaultDevice function opens a handle to the first device that is listed in the specified Plug and Play (PnP) category.
old-location: stream\ksopendefaultdevice.htm
ms.assetid: a017f0b7-8f4f-4797-96de-10137cb3443e
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ksproxy.h
req.include-header: Ksproxy.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsOpenDefaultDevice
req.alt-loc: Ksproxy.lib,Ksproxy.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ksproxy.lib
req.dll: 
req.irql: 
ms.keywords: KsOpenDefaultDevice
req.iface: 
---

# KsOpenDefaultDevice function



## -description
<p>The <b>KsOpenDefaultDevice</b> function opens a handle to the first device that is listed in the specified Plug and Play (PnP) category. </p>


## -syntax

````
HRESULT KsOpenDefaultDevice(
  _In_  REFGUID     Category,
  _In_  ACCESS_MASK Access,
  _Out_ PHANDLE     DeviceHandle
);
````


## -parameters
<dl>

### -param <i>Category</i> [in]

<dd>
<p>Identifier of the PnP category to enumerate.</p>
</dd>

### -param <i>Access</i> [in]

<dd>
<p>An ACCESS_MASK bitmask specifying how to access the default device.</p>
</dd>

### -param <i>DeviceHandle</i> [out]

<dd>
<p>Pointer to a variable that receives the handle to the default device that is opened.</p>
</dd>
</dl>

## -returns
<p>Returns NOERROR if successful; otherwise, returns an error code.</p>

## -remarks
<p>The <b>KsOpenDefaultDevice</b> function passes a pointer to <i>Category</i> in a call to the <b>SetupDiGetClassDevs</b> function to obtain a handle to the list of PnP devices. For more information about the ACCESS_MASK bitmask and <b>SetupDiGetClassDevs</b>, see the Microsoft Windows SDK documentation.</p>

<p>The <b>KsOpenDefaultDevice</b> function passes a pointer to <i>Category</i> in a call to the <b>SetupDiGetClassDevs</b> function to obtain a handle to the list of PnP devices. For more information about the ACCESS_MASK bitmask and <b>SetupDiGetClassDevs</b>, see the Microsoft Windows SDK documentation.</p>

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
<dt>Ksproxy.h (include Ksproxy.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ksproxy.lib</dt>
</dl>
</td>
</tr>
</table>