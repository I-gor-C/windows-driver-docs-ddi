---
UID: NF.ndis.NdisIfGetInterfaceIndexFromNetLuid
title: NdisIfGetInterfaceIndexFromNetLuid
author: windows-driver-content
description: The NdisIfGetInterfaceIndexFromNetLuid function gets the network interface index that is associated with a NET_LUID value.
old-location: netvista\ndisifgetinterfaceindexfromnetluid.htm
old-project: netvista
ms.assetid: 6aaa4ae9-fd3c-4cdd-ac37-0533c45143af
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisIfGetInterfaceIndexFromNetLuid
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
req.alt-api: NdisIfGetInterfaceIndexFromNetLuid
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
req.iface: 
---

# NdisIfGetInterfaceIndexFromNetLuid function



## -description
<p>The 
  <b>NdisIfGetInterfaceIndexFromNetLuid</b> function gets the network interface index that is associated with
  a 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568747">NET_LUID</a> value.</p>


## -syntax

````
NDIS_STATUS NdisIfGetInterfaceIndexFromNetLuid(
  _In_  NET_LUID     NetLuid,
  _Out_ PNET_IFINDEX pIfIndex
);
````


## -parameters
<dl>

### -param <i>NetLuid</i> [in]

<dd>
<p>A 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568747">NET_LUID</a> value that identifies a network
     interface.</p>
</dd>

### -param <i>pIfIndex</i> [out]

<dd>
<p>A pointer to a caller-supplied interface index variable. If 
     <b>NdisIfGetInterfaceIndexFromNetLuid</b> succeeds, NDIS writes the network interface index that is
     associated with the specified NET_LUID to this variable.</p>
</dd>
</dl>

## -returns
<p><b>NdisIfGetInterfaceIndexFromNetLuid</b> returns one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>The operation completed successfully.</p><dl>
<dt><b>NDIS_STATUS_INTERFACE_NOT_FOUND</b></dt>
</dl><p><b>NdisIfGetInterfaceIndexFromNetLuid</b> failed because the specified NET_LUID was not present in the
       list of registered interfaces.</p>

<p> </p>

## -remarks
<p>NDIS drivers can call the 
    <b>NdisIfGetInterfaceIndexFromNetLuid</b> function to get the network interface index that is associated
    with a 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568747">NET_LUID</a> value.</p>

<p>For the interfaces that the NDIS proxy provider service manages, NDIS provides the interface index and
    NET_LUID in various driver initialization structures:</p>

<p>Miniport drivers can obtain the interface index and NET_LUID for a miniport adapter in the 
      <a href="..\ndis\ns-ndis--ndis-miniport-init-parameters.md">
      NDIS_MINIPORT_INIT_PARAMETERS</a> structure.</p>

<p>Filter drivers can obtain the interface index and NET_LUID for a filter module in the 
      <a href="..\ndis\ns-ndis--ndis-filter-attach-parameters.md">
      NDIS_FILTER_ATTACH_PARAMETERS</a> structure.</p>

<p>Protocol drivers can obtain the interface index and NET_LUID of the highest and the lowest
      interfaces on a driver stack in the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff564832">NDIS_BIND_PARAMETERS</a> structure.</p>

<p>NDIS assigns an interface index to a network interface when the interface provider calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562715">NdisIfRegisterInterface</a> function.
    An interface provider calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff565890">NDIS_MAKE_NET_LUID</a> macro to create the
    NET_LUID value before it registers an interface.</p>

<p>The interface index value can change without a computer restart. Deregistering and re-registering an
    interface that is associated with a NET_LUID value might result in different interface index values. Do
    not confuse the interface index with the NET_LUID index that persists after a computer restarts.</p>

<p>NDIS provides the 
    <a href="..\ndis\nf-ndis-ndisifgetnetluidfrominterfaceindex.md">
    NdisIfGetNetLuidFromInterfaceIndex</a> function to get the NET_LUID value that is associated with a
    specified interface index.</p>

<p>NDIS drivers can call the 
    <b>NdisIfGetInterfaceIndexFromNetLuid</b> function to get the network interface index that is associated
    with a 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568747">NET_LUID</a> value.</p>

<p>For the interfaces that the NDIS proxy provider service manages, NDIS provides the interface index and
    NET_LUID in various driver initialization structures:</p>

<p>Miniport drivers can obtain the interface index and NET_LUID for a miniport adapter in the 
      <a href="..\ndis\ns-ndis--ndis-miniport-init-parameters.md">
      NDIS_MINIPORT_INIT_PARAMETERS</a> structure.</p>

<p>Filter drivers can obtain the interface index and NET_LUID for a filter module in the 
      <a href="..\ndis\ns-ndis--ndis-filter-attach-parameters.md">
      NDIS_FILTER_ATTACH_PARAMETERS</a> structure.</p>

<p>Protocol drivers can obtain the interface index and NET_LUID of the highest and the lowest
      interfaces on a driver stack in the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff564832">NDIS_BIND_PARAMETERS</a> structure.</p>

<p>NDIS assigns an interface index to a network interface when the interface provider calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562715">NdisIfRegisterInterface</a> function.
    An interface provider calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff565890">NDIS_MAKE_NET_LUID</a> macro to create the
    NET_LUID value before it registers an interface.</p>

<p>The interface index value can change without a computer restart. Deregistering and re-registering an
    interface that is associated with a NET_LUID value might result in different interface index values. Do
    not confuse the interface index with the NET_LUID index that persists after a computer restarts.</p>

<p>NDIS provides the 
    <a href="..\ndis\nf-ndis-ndisifgetnetluidfrominterfaceindex.md">
    NdisIfGetNetLuidFromInterfaceIndex</a> function to get the NET_LUID value that is associated with a
    specified interface index.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564832">NDIS_BIND_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565481">NDIS_FILTER_ATTACH_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565890">NDIS_MAKE_NET_LUID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565972">NDIS_MINIPORT_INIT_PARAMETERS</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisifgetnetluidfrominterfaceindex.md">
   NdisIfGetNetLuidFromInterfaceIndex</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisIfGetInterfaceIndexFromNetLuid function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
