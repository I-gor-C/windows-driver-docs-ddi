---
UID: NF.dot11wdi.NdisMDeregisterWdiMiniportDriver
title: NdisMDeregisterWdiMiniportDriver
author: windows-driver-content
description: A miniport driver calls the NdisMDeregisterWdiMiniportDriver function to release resources that it allocated with a previous call to the NdisMRegisterWdiMiniportDriver function.
old-location: netvista\ndismderegisterwdiminiportdriver.htm
old-project: netvista
ms.assetid: 6B2B0A88-9F63-4A68-894B-38424FBE161E
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisMDeregisterWdiMiniportDriver
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMDeregisterWdiMiniportDriver
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
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

# NdisMDeregisterWdiMiniportDriver function



## -description
<p>A miniport driver calls the NdisMDeregisterWdiMiniportDriver function to release resources that it allocated with a previous call to the <a href="https://msdn.microsoft.com/library/windows/hardware/mt297596">NdisMRegisterWdiMiniportDriver</a> function.</p>


## -syntax

````
VOID NdisMDeregisterWdiMiniportDriver(
  _In_ NDIS_MINIPORT_DRIVER_HANDLE NdisMiniportDriverHandle
);
````


## -parameters
<dl>

### -param <i>NdisMiniportDriverHandle</i> [in]

<dd>
<p>The NDIS handle for a miniport driver.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dot11wdi.h</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt297596">NdisMRegisterWdiMiniportDriver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMDeregisterWdiMiniportDriver function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
