---
UID: NC.ks.PFNREFERENCEDEVICEOBJECT
title: PFNREFERENCEDEVICEOBJECT
author: windows-driver-content
description: The driver can use this routine to increment the reference count of the PDO.
old-location: stream\kstrreferencedeviceobject.htm
old-project: stream
ms.assetid: f4bf38eb-5028-4fcb-9752-8dab88db5904
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
req.alt-api: KStrReferenceDeviceObject
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

# PFNREFERENCEDEVICEOBJECT callback



## -description
<p>The driver can use this routine to increment the reference count of the PDO.</p>


## -prototype

````
PFNREFERENCEDEVICEOBJECT KStrReferenceDeviceObject;

VOID KStrReferenceDeviceObject(
  _In_ PVOID Context
)
{ ... }
````


## -parameters
<dl>

### -param Context [in]

<dd>
<p>Pointer to a device extension of the device's PDO.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>The driver can access this method through the <b>ReferenceDeviceObject</b> member of the <a href="stream.bus_interface_reference">BUS_INTERFACE_REFERENCE</a> structure.</p>

<p>The device object remains active and enumerated until the reference count returns to 0.</p>

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