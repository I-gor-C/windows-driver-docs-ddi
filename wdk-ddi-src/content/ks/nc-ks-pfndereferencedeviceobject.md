---
UID: NC.ks.PFNDEREFERENCEDEVICEOBJECT
title: PFNDEREFERENCEDEVICEOBJECT
author: windows-driver-content
description: The driver can use this routine to decrement the reference count of the PDO.
old-location: stream\kstrdereferencedeviceobject.htm
old-project: stream
ms.assetid: 8d220b69-122c-4019-9c70-4c744503481d
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.alt-api: KStrDereferenceDeviceObject
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

# PFNDEREFERENCEDEVICEOBJECT callback



## -description
<p>The driver can use this routine to decrement the reference count of the PDO.</p>


## -prototype

````
PFNDEREFERENCEDEVICEOBJECT KStrDereferenceDeviceObject;

VOID KStrDereferenceDeviceObject(
  _In_ PVOID Context
)
{ ... }
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>Pointer to a device extension of the device's PDO.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if the request is handled. Otherwise returns an appropriate error code.</p>

## -remarks
<p>Minidrivers access this method through the <b>DereferenceDeviceObject</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557584">BUS_INTERFACE_REFERENCE</a> structure.</p>

<p>When the PDO's reference count is 0, it becomes eligible for removal. Note that this condition does not guarantee removal.</p>

<p>Minidrivers access this method through the <b>DereferenceDeviceObject</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557584">BUS_INTERFACE_REFERENCE</a> structure.</p>

<p>When the PDO's reference count is 0, it becomes eligible for removal. Note that this condition does not guarantee removal.</p>

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