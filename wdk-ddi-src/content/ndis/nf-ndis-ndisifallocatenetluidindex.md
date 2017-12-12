---
UID: NF.ndis.NdisIfAllocateNetLuidIndex
title: NdisIfAllocateNetLuidIndex function
author: windows-driver-content
description: The NdisIfAllocateNetLuidIndex function allocates a NET_LUID index for an NDIS network interface provider.
old-location: netvista\ndisifallocatenetluidindex.htm
old-project: netvista
ms.assetid: bc62da04-242a-4d9a-8a85-2342a1b3e628
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: NdisIfAllocateNetLuidIndex
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
req.alt-api: NdisIfAllocateNetLuidIndex
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

# NdisIfAllocateNetLuidIndex function



## -description
The 
  <b>NdisIfAllocateNetLuidIndex</b> function allocates a 
  <a href="netvista.net_luid">NET_LUID</a> index for an NDIS network interface
  provider.



## -syntax

````
NDIS_STATUS NdisIfAllocateNetLuidIndex(
  _In_  NET_IFTYPE IfType,
  _Out_ PUINT32    pNetLuidIndex
);
````


## -parameters

### -param IfType [in]

The Internet Assigned Numbers Authority (IANA) interface type for an index. For example,
     IF_TYPE_ETHERNET_CSMACD (6) is the value for 
     <i>IfType</i> that is assigned to any Ethernet-like interface. For a list of interface types, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff565767">NDIS Interface Types</a>.


### -param pNetLuidIndex [out]

A pointer to a caller-supplied 
     <a href="netvista.net_luid">NET_LUID</a> index variable. If allocation is
     successful, 
     <b>NdisIfAllocateNetLuidIndex</b> sets this variable to the allocated 24-bit NET_LUID index value.


## -returns
<b>NdisIfAllocateNetLuidIndex</b> returns one of the following values:
<dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl>The operation completed successfully.
<dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl>The operation failed because of insufficient resources.

 


## -remarks
NDIS interface providers call the 
    <b>NdisIfAllocateNetLuidIndex</b> function to allocate a 
    <a href="netvista.net_luid">NET_LUID</a> index. An interface provider must allocate
    a NET_LUID index before the interface provider can register an interface.

<b>NdisIfAllocateNetLuidIndex</b> attempts to allocate a 24-bit NET_LUID index that is unique to the local
    computer and is associated with the interface type that the 
    <i>IfType</i> parameter specifies. NDIS records the NET_LUID index in persistent storage so that the index
    can remain associated with the same interface even after the computer restarts. NDIS will not allocate
    the same NET_LUID index to future callers of 
    <b>NdisIfAllocateNetLuidIndex</b> until after the interface provider calls the 
    <a href="netvista.ndisiffreenetluidindex">NdisIfFreeNetLuidIndex</a> function to
    free the index.

To build a 
    <a href="netvista.net_luid">NET_LUID</a> value from the NET_LUID index and the
    interface type, an interface provider calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff565890">NDIS_MAKE_NET_LUID</a> macro.

The interface provider must store the NET_LUID values that it allocates in persistent storage. For
    example, if there is a loss of computer power, the provider should have stored the NET_LUID values in
    persistent storage so it can call 
    <a href="netvista.ndisiffreenetluidindex">NdisIfFreeNetLuidIndex</a> later to
    free any indexes that are no longer in use. Also, the provider should use the same NET_LUID value
    whenever it registers the same interface with the 
    <a href="netvista.ndisifregisterinterface">
    NdisIfRegisterInterface</a> function.


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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565890">NDIS_MAKE_NET_LUID</a>
</dt>
<dt>
<a href="netvista.ndisiffreenetluidindex">NdisIfFreeNetLuidIndex</a>
</dt>
<dt>
<a href="netvista.ndisifregisterinterface">NdisIfRegisterInterface</a>
</dt>
<dt>
<a href="netvista.net_luid">NET_LUID</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisIfAllocateNetLuidIndex function%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

