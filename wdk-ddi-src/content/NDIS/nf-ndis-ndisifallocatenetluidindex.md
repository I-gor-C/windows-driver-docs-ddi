---
UID: NF.ndis.NdisIfAllocateNetLuidIndex
title: NdisIfAllocateNetLuidIndex
author: windows-driver-content
description: The NdisIfAllocateNetLuidIndex function allocates a NET_LUID index for an NDIS network interface provider.
old-location: netvista\ndisifallocatenetluidindex.htm
ms.assetid: bc62da04-242a-4d9a-8a85-2342a1b3e628
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
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
ms.keywords: NdisIfAllocateNetLuidIndex
req.iface: 
---

# NdisIfAllocateNetLuidIndex function



## -description
<p>The 
  <b>NdisIfAllocateNetLuidIndex</b> function allocates a 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568747">NET_LUID</a> index for an NDIS network interface
  provider.</p>


## -syntax

````
NDIS_STATUS NdisIfAllocateNetLuidIndex(
  _In_  NET_IFTYPE IfType,
  _Out_ PUINT32    pNetLuidIndex
);
````


## -parameters
<dl>

### -param <i>IfType</i> [in]

<dd>
<p>The Internet Assigned Numbers Authority (IANA) interface type for an index. For example,
     IF_TYPE_ETHERNET_CSMACD (6) is the value for 
     <i>IfType</i> that is assigned to any Ethernet-like interface. For a list of interface types, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff565767">NDIS Interface Types</a>.</p>
</dd>

### -param <i>pNetLuidIndex</i> [out]

<dd>
<p>A pointer to a caller-supplied 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568747">NET_LUID</a> index variable. If allocation is
     successful, 
     <b>NdisIfAllocateNetLuidIndex</b> sets this variable to the allocated 24-bit NET_LUID index value.</p>
</dd>
</dl>

## -returns
<p><b>NdisIfAllocateNetLuidIndex</b> returns one of the following values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>The operation completed successfully.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>The operation failed because of insufficient resources.</p>

<p> </p>

## -remarks
<p>NDIS interface providers call the 
    <b>NdisIfAllocateNetLuidIndex</b> function to allocate a 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568747">NET_LUID</a> index. An interface provider must allocate
    a NET_LUID index before the interface provider can register an interface.</p>

<p><b>NdisIfAllocateNetLuidIndex</b> attempts to allocate a 24-bit NET_LUID index that is unique to the local
    computer and is associated with the interface type that the 
    <i>IfType</i> parameter specifies. NDIS records the NET_LUID index in persistent storage so that the index
    can remain associated with the same interface even after the computer restarts. NDIS will not allocate
    the same NET_LUID index to future callers of 
    <b>NdisIfAllocateNetLuidIndex</b> until after the interface provider calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562706">NdisIfFreeNetLuidIndex</a> function to
    free the index.</p>

<p>To build a 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568747">NET_LUID</a> value from the NET_LUID index and the
    interface type, an interface provider calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff565890">NDIS_MAKE_NET_LUID</a> macro.</p>

<p>The interface provider must store the NET_LUID values that it allocates in persistent storage. For
    example, if there is a loss of computer power, the provider should have stored the NET_LUID values in
    persistent storage so it can call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562706">NdisIfFreeNetLuidIndex</a> later to
    free any indexes that are no longer in use. Also, the provider should use the same NET_LUID value
    whenever it registers the same interface with the 
    <a href="https://msdn.microsoft.com/d0b0ada7-afb1-4cb7-ada6-7c5c7abe7d19">
    NdisIfRegisterInterface</a> function.</p>

<p>NDIS interface providers call the 
    <b>NdisIfAllocateNetLuidIndex</b> function to allocate a 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568747">NET_LUID</a> index. An interface provider must allocate
    a NET_LUID index before the interface provider can register an interface.</p>

<p><b>NdisIfAllocateNetLuidIndex</b> attempts to allocate a 24-bit NET_LUID index that is unique to the local
    computer and is associated with the interface type that the 
    <i>IfType</i> parameter specifies. NDIS records the NET_LUID index in persistent storage so that the index
    can remain associated with the same interface even after the computer restarts. NDIS will not allocate
    the same NET_LUID index to future callers of 
    <b>NdisIfAllocateNetLuidIndex</b> until after the interface provider calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562706">NdisIfFreeNetLuidIndex</a> function to
    free the index.</p>

<p>To build a 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568747">NET_LUID</a> value from the NET_LUID index and the
    interface type, an interface provider calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff565890">NDIS_MAKE_NET_LUID</a> macro.</p>

<p>The interface provider must store the NET_LUID values that it allocates in persistent storage. For
    example, if there is a loss of computer power, the provider should have stored the NET_LUID values in
    persistent storage so it can call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562706">NdisIfFreeNetLuidIndex</a> later to
    free any indexes that are no longer in use. Also, the provider should use the same NET_LUID value
    whenever it registers the same interface with the 
    <a href="https://msdn.microsoft.com/d0b0ada7-afb1-4cb7-ada6-7c5c7abe7d19">
    NdisIfRegisterInterface</a> function.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547949">Irql_Interfaces_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565890">NDIS_MAKE_NET_LUID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562706">NdisIfFreeNetLuidIndex</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562715">NdisIfRegisterInterface</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568747">NET_LUID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisIfAllocateNetLuidIndex function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
