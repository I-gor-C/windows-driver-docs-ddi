---
UID: NF.ndis.NdisCompleteBindAdapterEx
title: NdisCompleteBindAdapterEx
author: windows-driver-content
description: A protocol driver calls the NdisCompleteBindAdapterEx function to complete a binding operation for which the driver's ProtocolBindAdapterEx function returned NDIS_STATUS_PENDING.
old-location: netvista\ndiscompletebindadapterex.htm
old-project: netvista
ms.assetid: e52c7aeb-bbd8-402e-94af-f74df6deb23c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisCompleteBindAdapterEx
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
req.alt-api: NdisCompleteBindAdapterEx
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Protocol_Driver_Function
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

# NdisCompleteBindAdapterEx function



## -description
<p>A protocol driver calls the 
  <b>NdisCompleteBindAdapterEx</b> function to complete a binding operation for which the driver's 
  <a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a> function
  returned NDIS_STATUS_PENDING.</p>


## -syntax

````
VOID NdisCompleteBindAdapterEx(
  _In_ NDIS_HANDLE BindContext,
  _In_ NDIS_STATUS Status
);
````


## -parameters
<dl>

### -param <i>BindContext</i> [in]

<dd>
<p>The handle that NDIS passed to the 
     <i>BindContext</i> parameter of the 
     <a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">
     ProtocolBindAdapterEx</a> function.</p>
</dd>

### -param <i>Status</i> [in]

<dd>
<p>The final status of the completed bind operation. This parameter can be one of the following
     values:
     </p>
<p></p>
<dl>

### -param <a id="NDIS_STATUS_SUCCESS"></a><a id="ndis_status_success"></a>NDIS_STATUS_SUCCESS

<dd>
<p>The driver successfully completed the binding to the underlying NIC.</p>
</dd>

### -param <a id="NDIS_STATUS_XXX_or_NTSTATUS_XXX"></a><a id="ndis_status_xxx_or_ntstatus_xxx"></a><a id="NDIS_STATUS_XXX_OR_NTSTATUS_XXX"></a>NDIS_STATUS_<i>XXX</i> or NTSTATUS_<i>XXX</i>

<dd>
<p>The protocol driver's attempt to set up a binding failed or the protocol driver could not
       allocate the resources it needed to carry out network I/O operations. Usually, such an error status is
       propagated from an 
       <b>Ndis<i>Xxx</i></b> function or a kernel-mode support routine.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If a protocol driver returns NDIS_STATUS_PENDING from its 
    <a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a> function,
    that driver must call 
    <b>NdisCompleteBindAdapterEx</b> after the binding operation is completed.</p>

<p>If the open operation was successful, the protocol driver is ready to accept receive indications from
    underlying drivers and to initiate send requests and OID requests on the binding. If the driver calls 
    <b>NdisCompleteBindAdapterEx</b> with an error status, the binding attempt failed and the driver has
    released any resources it allocated to establish the binding.</p>

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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.ndis_irql_protocol_driver_function">Irql_Protocol_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nf-ndis-ndisopenadapterex.md">NdisOpenAdapterEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisCompleteBindAdapterEx function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
