---
UID: NF.ndis.NdisSetPhysicalAddressLow
title: NdisSetPhysicalAddressLow
author: windows-driver-content
description: NdisSetPhysicalAddressLow sets the low-order part of a given physical address to a given value.
old-location: netvista\ndissetphysicaladdresslow.htm
old-project: netvista
ms.assetid: 2454f923-15c5-43c8-8d62-eee000d89a10
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisSetPhysicalAddressLow
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisSetPhysicalAddressLow (NDIS
   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisSetPhysicalAddressLow (NDIS
   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisSetPhysicalAddressLow
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
req.iface: 
---

# NdisSetPhysicalAddressLow function



## -description
<p><b>NdisSetPhysicalAddressLow</b> sets the low-order part of a given physical address to a given
  value.</p>


## -syntax

````
VOID NdisSetPhysicalAddressLow(
  _In_ NDIS_PHYSICAL_ADDRESS PhysicalAddress,
  _In_ ULONG                 Value
);
````


## -parameters
<dl>

### -param <i>PhysicalAddress</i> [in]

<dd>
<p>Specifies a physical address of an OS-dependent size.</p>
</dd>

### -param <i>Value</i> [in]

<dd>
<p>Specifies the value to be written into the low-order part of the address.</p>
</dd>
</dl>

## -returns
<p>None</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/93b978a0-f259-4395-84e0-25031f578c03">NdisSetPhysicalAddressLow (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisSetPhysicalAddressLow (NDIS
   5.1)</b>) in Windows XP.</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562654">NdisGetPhysicalAddressLow</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557129">NDIS_PHYSICAL_ADDRESS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564551">NdisSetPhysicalAddressHigh</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisSetPhysicalAddressLow function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
