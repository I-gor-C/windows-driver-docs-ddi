---
UID: NF.ndis.NdisDeregisterDeviceEx
title: NdisDeregisterDeviceEx
author: windows-driver-content
description: The NdisDeregisterDeviceEx function removes, from the system, a device object that was created by the NdisRegisterDeviceEx function.
old-location: netvista\ndisderegisterdeviceex.htm
old-project: netvista
ms.assetid: bca1ef90-b574-4ed5-a9ec-c553372490b1
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisDeregisterDeviceEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisDeregisterDeviceEx
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miscellaneous_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NdisDeregisterDeviceEx function



## -description
<p>The 
  <b>NdisDeregisterDeviceEx</b> function removes, from the system, a device object that was created by the 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff564518">NdisRegisterDeviceEx</a> function.</p>


## -syntax

````
VOID NdisDeregisterDeviceEx(
  _In_ NDIS_HANDLE NdisDeviceHandle
);
````


## -parameters
<dl>

### -param <i>NdisDeviceHandle</i> [in]

<dd>
<p>The handle returned by 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff564518">NdisRegisterDeviceEx</a> that identifies
     the device object to be deregistered.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The 
    <b>NdisDeregisterDeviceEx</b> function removes a device object that was created by the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564518">NdisRegisterDeviceEx</a> function. 
    <b>NdisDeregisterDeviceEx</b> also removes the symbolic link that is associated with this device
    object.</p>

<p>The 
    <b>NdisDeregisterDeviceEx</b> function removes a device object that was created by the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564518">NdisRegisterDeviceEx</a> function. 
    <b>NdisDeregisterDeviceEx</b> also removes the symbolic link that is associated with this device
    object.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547982">Irql_Miscellaneous_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564518">NdisRegisterDeviceEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisDeregisterDeviceEx function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
