---
UID: NF.netdma.NetDmaDeregisterProvider
title: NetDmaDeregisterProvider function
author: windows-driver-content
description: The NetDmaDeregisterProvider function deregisters a DMA provider.
old-location: netvista\netdmaderegisterprovider.htm
old-project: netvista
ms.assetid: 8832adbc-c2ab-4742-94a0-4e33d03eaaf1
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: NetDmaDeregisterProvider
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: netdma.h
req.include-header: Netdma.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NetDMA 1.0 drivers in Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NetDmaDeregisterProvider
req.alt-loc: netdma.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
---

# NetDmaDeregisterProvider function



## -description

## -syntax

````
VOID NetDmaDeregisterProvider(
  _In_ PVOID NetDmaProviderHandle
);
````


## -parameters

### -param NetDmaProviderHandle [in]

A handle that identifies a DMA provider. The DMA provider driver received this handle from the
     NetDMA interface in a call to the 
     <a href="netvista.netdmaregisterprovider">
     NetDmaRegisterProvider</a> function.

## -returns
None

## -remarks
DMA provider drivers call the 
    <b>NetDmaDeregisterProvider</b> function to deregister a DMA provider that was previously registered by
    calling the 
    <a href="netvista.netdmaregisterprovider">
    NetDmaRegisterProvider</a> function.

The DMA provider driver must call the 
    <a href="netvista.netdmaproviderstop">NetDmaProviderStop</a> function before it
    deregisters a DMA provider. The DMA provider driver calls 
    <b>NetDmaProviderStop</b> to notify the NetDMA interface that a previously started DMA provider is no
    longer available.

A DMA provider driver typically calls the 
    <b>NetDmaDeregisterProvider</b> function in the context of processing the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551738">IRP_MN_REMOVE_DEVICE</a> IRP for the DMA
    provider.

Call 
    <b>NetDmaDeregisterProvider</b> at IRQL = PASSIVE_LEVEL.

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
Supported for NetDMA 1.0 drivers in Windows Vista.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Netdma.h (include Netdma.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551738">IRP_MN_REMOVE_DEVICE</a>
</dt>
<dt>
<a href="netvista.netdmaproviderstop">NetDmaProviderStop</a>
</dt>
<dt>
<a href="netvista.netdmaregisterprovider">NetDmaRegisterProvider</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NetDmaDeregisterProvider function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
