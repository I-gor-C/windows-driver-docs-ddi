---
UID: NF.ndis.NdisQueryBindInstanceName
title: NdisQueryBindInstanceName
author: windows-driver-content
description: The NdisQueryBindInstanceName function retrieves the friendly name of a physical NIC or a virtual adapter that the calling protocol driver will bind to.
old-location: netvista\ndisquerybindinstancename.htm
ms.assetid: bbba8be8-aa7e-455f-a591-e9d915f137f4
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisQueryBindInstanceName (NDIS
   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisQueryBindInstanceName (NDIS
   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisQueryBindInstanceName
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: NdisQueryBindInstanceName
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: NdisQueryBindInstanceName
req.iface: 
---

# NdisQueryBindInstanceName function



## -description
<p>The 
  <b>NdisQueryBindInstanceName</b> function retrieves the friendly name of a physical NIC or a virtual adapter
  that the calling protocol driver will bind to.</p>


## -syntax

````
NDIS_STATUS NdisQueryBindInstanceName(
  _Out_ PNDIS_STRING pAdapterInstanceName,
  _In_  NDIS_HANDLE  BindingContext
);
````


## -parameters
<dl>

### -param <i>pAdapterInstanceName</i> [out]

<dd>
<p>A pointer to a caller-supplied NDIS_STRING type that receives a counted Unicode string. This
     string specifies the friendly name of the interface to which the binding refers. This interface is
     either a physical NIC or a virtual adapter. For Microsoft Windows 2000 and later operating systems, NDIS
     defines the NDIS_STRING type as a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> type.</p>
</dd>

### -param <i>BindingContext</i> [in]

<dd>
<p>A handle that identifies the NDIS context area for the bind operation. NDIS passed this handle to
     the 
     <i>BindContext</i> parameter of the 
     <a href="https://msdn.microsoft.com/1958722e-012e-4110-a82c-751744bcf9b5">
     ProtocolBindAdapterEx</a> function.</p>
</dd>
</dl>

## -returns
<p><b>NdisQueryBindInstanceName</b> returns NDIS_STATUS_SUCCESS if memory for the string at 
     <i>pAdapterInstanceName</i> was successfully allocated; otherwise, it returns
     NDIS_STATUS_RESOURCES.</p>

## -remarks
<p>A protocol driver uses 
    <b>NdisQueryBindInstanceName</b> to retrieve the friendly name of a physical NIC or a virtual adapter to
    which the protocol driver will be bound. The protocol driver specifies the binding context that NDIS
    provided in the 
    <a href="https://msdn.microsoft.com/1958722e-012e-4110-a82c-751744bcf9b5">
    ProtocolBindAdapterEx</a> function.</p>

<p>Protocol drivers can use 
    <b>NdisQueryBindInstanceName</b> to obtain the friendly name before they bind to the adapter.</p>

<p><b>NdisQueryBindInstanceName</b> allocates memory for the string that specifies the friendly name. After
    the caller finishes using this memory, the caller must call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562577">NdisFreeMemory</a> function to release the
    memory.</p>

<p>Friendly names are intended to help the user quickly and accurately identify a physical NIC or virtual
    adapter--for example, "PCI Ethernet Adapter" and "Virtual Private Networking Adapter" are considered
    friendly names.</p>

<p>A protocol driver uses 
    <b>NdisQueryBindInstanceName</b> to retrieve the friendly name of a physical NIC or a virtual adapter to
    which the protocol driver will be bound. The protocol driver specifies the binding context that NDIS
    provided in the 
    <a href="https://msdn.microsoft.com/1958722e-012e-4110-a82c-751744bcf9b5">
    ProtocolBindAdapterEx</a> function.</p>

<p>Protocol drivers can use 
    <b>NdisQueryBindInstanceName</b> to obtain the friendly name before they bind to the adapter.</p>

<p><b>NdisQueryBindInstanceName</b> allocates memory for the string that specifies the friendly name. After
    the caller finishes using this memory, the caller must call the 
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
   <a href="https://msdn.microsoft.com/e514efa3-d800-4702-ab9f-babed4fb4858">NdisQueryBindInstanceName (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisQueryBindInstanceName (NDIS
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975123">NdisQueryBindInstanceName</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562577">NdisFreeMemory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1958722e-012e-4110-a82c-751744bcf9b5">ProtocolBindAdapterEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisQueryBindInstanceName function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
