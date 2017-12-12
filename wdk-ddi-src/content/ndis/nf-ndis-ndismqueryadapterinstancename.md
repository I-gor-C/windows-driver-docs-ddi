---
UID: NF.ndis.NdisMQueryAdapterInstanceName
title: NdisMQueryAdapterInstanceName function
author: windows-driver-content
description: The NdisMQueryAdapterInstanceName function retrieves the friendly name of a miniport adapter.
old-location: netvista\ndismqueryadapterinstancename.htm
old-project: netvista
ms.assetid: 7af6ee73-814b-49f8-8641-d3e8dc672ee5
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: NdisMQueryAdapterInstanceName
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 5.1, and NDIS 6.0 and later. For NDIS 5.1 drivers, see       NdisMQueryAdapterInstanceName (NDIS 5.1).
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMQueryAdapterInstanceName
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miniport_Driver_Function
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

# NdisMQueryAdapterInstanceName function



## -description
The
  <b>NdisMQueryAdapterInstanceName</b> function retrieves the friendly name of a miniport adapter.



## -syntax

````
NDIS_STATUS NdisMQueryAdapterInstanceName(
  _Out_ PNDIS_STRING AdapterInstanceName,
  _In_  NDIS_HANDLE  MiniportAdapterHandle
);
````


## -parameters

### -param AdapterInstanceName [out]

A pointer to a caller-supplied NDIS_STRING type that receives a counted Unicode string. This
     string specifies the friendly name of the interface for the given miniport adapter. For Windows Vista
     and later versions of the Windows operating system, NDIS defines the NDIS_STRING type as a 
     <a href="kernel.unicode_string">UNICODE_STRING</a> type.


### -param MiniportAdapterHandle [in]

The handle to the miniport adapter that was previously input to the 
     <a href="..\ndis\nc-ndis-miniport_initialize.md">
     MiniportInitializeEx</a> function.


## -returns
Returns NDIS_STATUS_SUCCESS if memory for the string at 
     <i>AdapterInstanceName</i> was successfully allocated; otherwise, it returns
     NDIS_STATUS_RESOURCES.


## -remarks
A miniport driver uses 
    <b>NdisMQueryAdapterInstanceName</b> to retrieve the friendly name of an interface that the miniport
    driver controls. This interface is either a physical NIC or a virtual adapter and is called a 
    <i>miniport adapter</i>. The miniport driver specifies the handle to a miniport adapter in 
    <i>MiniportAdapterHandle</i> . This handle to the miniport adapter is passed to the miniport driver's 
    <a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a> function to
    set up the miniport adapter for network I/O operations.

<b>NdisMQueryAdapterInstanceName</b> allocates memory for the string that specifies the friendly name.
    After the caller finishes using this memory, the caller must call the 
    <a href="netvista.ndisfreememory">NdisFreeMemory</a> function to release the
    memory.

Friendly names are intended to help the user quickly and accurately identify a physical NIC or virtual
    adapter--for example, "PCI Ethernet Adapter" and "Virtual Private Networking Adapter" are considered
    friendly names.


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
Supported in NDIS 5.1, and NDIS 6.0 and later. For NDIS 5.1 drivers, see 
   <a href="https://msdn.microsoft.com/4d02f652-ec7a-46c3-bfe2-a1e5b187ad66">
   NdisMQueryAdapterInstanceName (NDIS 5.1)</a>.

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
<a href="devtest.ndis_irql_miniport_driver_function">Irql_Miniport_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="netvista.ndisfreememory">NdisFreeMemory</a>
</dt>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMQueryAdapterInstanceName function%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

