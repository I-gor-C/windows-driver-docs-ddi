---
UID: NF.ndis.NdisQueryAdapterInstanceName
title: NdisQueryAdapterInstanceName
author: windows-driver-content
description: The NdisQueryAdapterInstanceName function retrieves the friendly name of a physical NIC or a virtual adapter that the calling protocol driver is bound to.
old-location: netvista\ndisqueryadapterinstancename.htm
old-project: netvista
ms.assetid: bd6fade6-9b9b-4b38-8e53-c70c40c1165f
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisQueryAdapterInstanceName
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisQueryAdapterInstanceName
   (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisQueryAdapterInstanceName
   (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisQueryAdapterInstanceName
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NdisQueryAdapterInstanceName function



## -description
<p>The 
  <b>NdisQueryAdapterInstanceName</b> function retrieves the friendly name of a physical NIC or a virtual
  adapter that the calling protocol driver is bound to.</p>


## -syntax

````
NDIS_STATUS NdisQueryAdapterInstanceName(
  _Out_ PNDIS_STRING AdapterInstanceName,
  _In_  NDIS_HANDLE  NdisBindingHandle
);
````


## -parameters
<dl>

### -param <i>AdapterInstanceName</i> [out]

<dd>
<p>A pointer to a caller-supplied NDIS_STRING type that receives a counted Unicode string. This
     string specifies the friendly name of the interface to which the binding refers. This interface is
     either a physical NIC or a virtual adapter. For Windows 2000 and later, NDIS defines the NDIS_STRING
     type as a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> type.</p>
</dd>

### -param <i>NdisBindingHandle</i> [in]

<dd>
<p>A handle that identifies the binding to the target physical NIC or virtual adapter of the
     next-lower driver to which the caller is bound. Typically, 
     <i>NdisBindingHandle</i> was returned by the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a> function.</p>
</dd>
</dl>

## -returns
<p><b>NdisQueryAdapterInstanceName</b> returns NDIS_STATUS_SUCCESS if memory for the string at 
     <i>AdapterInstanceName</i> was successfully allocated; otherwise, it returns
     NDIS_STATUS_RESOURCES.</p>

## -remarks
<p>A protocol driver uses 
    <b>NdisQueryAdapterInstanceName</b> to retrieve the friendly name of a physical NIC or a virtual adapter
    to which the protocol driver is bound. The protocol driver specifies the handle to such a NIC or virtual
    adapter in 
    <i>NdisBindingHandle</i> . The protocol driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a> function to retrieve
    this handle.</p>

<p><b>NdisQueryAdapterInstanceName</b> allocates memory for the string that specifies the friendly name.
    After the caller finishes using this memory, the caller must call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562577">NdisFreeMemory</a> function to release the
    memory.</p>

<p>Friendly names are intended to help the user quickly and accurately identify a physical NIC or virtual
    adapter--for example, "PCI Ethernet Adapter" and "Virtual Private Networking Adapter" are considered
    friendly names.</p>

<p>A protocol driver uses 
    <b>NdisQueryAdapterInstanceName</b> to retrieve the friendly name of a physical NIC or a virtual adapter
    to which the protocol driver is bound. The protocol driver specifies the handle to such a NIC or virtual
    adapter in 
    <i>NdisBindingHandle</i> . The protocol driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a> function to retrieve
    this handle.</p>

<p><b>NdisQueryAdapterInstanceName</b> allocates memory for the string that specifies the friendly name.
    After the caller finishes using this memory, the caller must call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562577">NdisFreeMemory</a> function to release the
    memory.</p>

<p>Friendly names are intended to help the user quickly and accurately identify a physical NIC or virtual
    adapter--for example, "PCI Ethernet Adapter" and "Virtual Private Networking Adapter" are considered
    friendly names.</p>

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
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/946aa523-5543-464d-a037-d05adb25428d">NdisQueryAdapterInstanceName
   (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisQueryAdapterInstanceName
   (NDIS 5.1)</b>) in Windows XP.</p>
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
<p>&lt;= DISPATCH_LEVEL</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562577">NdisFreeMemory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisQueryAdapterInstanceName function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
