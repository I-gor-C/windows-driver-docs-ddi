---
UID: NF.ndis.NdisSetPhysicalAddressLow
title: NdisSetPhysicalAddressLow macro
author: windows-driver-content
description: NdisSetPhysicalAddressLow sets the low-order part of a given physical address to a given value.
old-location: netvista\ndissetphysicaladdresslow.htm
old-project: NetVista
ms.assetid: 2454f923-15c5-43c8-8d62-eee000d89a10
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: NdisSetPhysicalAddressLow
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisSetPhysicalAddressLow (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisSetPhysicalAddressLow (NDIS   5.1)) in Windows XP.
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
---

# NdisSetPhysicalAddressLow macro



## -description
<b>NdisSetPhysicalAddressLow</b> sets the low-order part of a given physical address to a given
  value.



## -syntax

````
VOID NdisSetPhysicalAddressLow(
  [in] NDIS_PHYSICAL_ADDRESS PhysicalAddress,
  [in] ULONG                 Value
);
````


## -parameters

### -param PhysicalAddress [in]

Specifies a physical address of an OS-dependent size.


### -param Value [in]

Specifies the value to be written into the low-order part of the address.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/93b978a0-f259-4395-84e0-25031f578c03">NdisSetPhysicalAddressLow (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisSetPhysicalAddressLow (NDIS
   5.1)</b>) in Windows XP.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.ndisgetphysicaladdresslow">NdisGetPhysicalAddressLow</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557129">NDIS_PHYSICAL_ADDRESS</a>
</dt>
<dt>
<a href="netvista.ndissetphysicaladdresshigh">NdisSetPhysicalAddressHigh</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NdisSetPhysicalAddressLow macro%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

