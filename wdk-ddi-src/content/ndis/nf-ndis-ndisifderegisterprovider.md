---
UID: NF.ndis.NdisIfDeregisterProvider
title: NdisIfDeregisterProvider function
author: windows-driver-content
description: The NdisIfDeregisterProvider function deregisters an interface provider that was previously registered by a call to the NdisIfRegisterProvider function.
old-location: netvista\ndisifderegisterprovider.htm
old-project: netvista
ms.assetid: 90e921e3-b384-495b-8cb6-74596d060ec0
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: NdisIfDeregisterProvider
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisIfDeregisterProvider
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Interfaces_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
---

# NdisIfDeregisterProvider function



## -description
The 
  <b>NdisIfDeregisterProvider</b> function deregisters an interface provider that was previously registered by
  a call to the 
  <a href="netvista.ndisifregisterprovider">
  NdisIfRegisterProvider</a> function.



## -syntax

````
VOID NdisIfDeregisterProvider(
  _In_ NDIS_HANDLE NdisProviderHandle
);
````


## -parameters

### -param NdisProviderHandle [in]

A handle that identifies the network interface provider. The caller obtained this handle from a
     previous call to the 
     <a href="netvista.ndisifregisterprovider">
     NdisIfRegisterProvider</a> function.


## -returns
None


## -remarks
NDIS drivers call the 
    <b>NdisIfDeregisterProvider</b> function to deregister as a network interface provider. NDIS drivers
    should deregister as interface providers when they are unloaded.

The interface provider must ensure that it does not have any interfaces registered when it calls 
    <b>NdisIfDeregisterProvider</b>. To deregister interfaces, the provider must call the 
    <a href="netvista.ndisifderegisterinterface">
    NdisIfDeregisterInterface</a> function once for each registered interface.

The provider must not use the provider handle that it passed at the 
    <i>NdisProviderHandle</i> parameter after it calls 
    <b>NdisIfDeregisterProvider</b>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported in NDIS 6.0 and later.

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
Library

</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.ndis_irql_interfaces_function">Irql_Interfaces_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.ndisifderegisterinterface">NdisIfDeregisterInterface</a>
</dt>
<dt>
<a href="netvista.ndisifregisterprovider">NdisIfRegisterProvider</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisIfDeregisterProvider function%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

