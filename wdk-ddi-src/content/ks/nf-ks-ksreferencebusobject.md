---
UID: NF.ks.KsReferenceBusObject
title: KsReferenceBusObject
author: windows-driver-content
description: References the bus Physical device object.
old-location: stream\ksreferencebusobject.htm
old-project: stream
ms.assetid: 96297c0a-a3ba-4f16-befb-ee6a55d2fb25
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsReferenceBusObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsReferenceBusObject
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

# KsReferenceBusObject function



## -description
<p>References the bus Physical device object.</p>


## -syntax

````
NTSTATUS KsReferenceBusObject(
  _In_ KSDEVICE_HEADER Header
);
````


## -parameters
<dl>

### -param <i>Header</i> [in]

<dd>
<p>Points to a header previously allocated by <b>KsAllocateDeviceHeader</b> that also contains the PnP device stack object.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if the reference was successful, else an error such as STATUS_INSUFFICIENT_RESOURCES.</p>

## -remarks
<p>This function is used by filters that use the device header to keep track of their PnP object stack. This is normally called on a successful Open of the filter when the bus for this device requires such a reference (such as software devices), and is matched by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff561676">KsDereferenceBusObject</a> on a close of that filter instance. The caller must have previously also called KsSetDevicePnpAndBaseObject in order to set the PnP device stack object. This would have been done in the PnP AddDevice function. If the object has not been previously referenced, interface space is allocated and the function uses the PnP device object to acquire the bus referencing interface. It then calls the ReferenceDeviceObject method on that interface. The interface itself is released and freed when the device header is freed.</p>

<p>This function is used by filters that use the device header to keep track of their PnP object stack. This is normally called on a successful Open of the filter when the bus for this device requires such a reference (such as software devices), and is matched by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff561676">KsDereferenceBusObject</a> on a close of that filter instance. The caller must have previously also called KsSetDevicePnpAndBaseObject in order to set the PnP device stack object. This would have been done in the PnP AddDevice function. If the object has not been previously referenced, interface space is allocated and the function uses the PnP device object to acquire the bus referencing interface. It then calls the ReferenceDeviceObject method on that interface. The interface itself is released and freed when the device header is freed.</p>

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
<dt>Ks.h (include Ks.h)</dt>
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