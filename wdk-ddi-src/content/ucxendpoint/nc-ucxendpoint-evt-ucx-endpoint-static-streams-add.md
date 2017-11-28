---
UID: NC.ucxendpoint.EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD
title: EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD
author: windows-driver-content
description: The client driver's implementation that UCX calls to create static streams.
old-location: buses\evt_ucx_endpoint_static_streams_add.htm
old-project: usbref
ms.assetid: 76f94f19-894a-47af-a407-8e14263f1143
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCXUSBDEVICE_INFO,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ucxendpoint.h
req.include-header: Ucxclass.h, Ucxendpoint.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: PEVT_UCX_ENDPOINT_STATIC_STREAMS_ADD
req.alt-loc: ucxendpoint.h
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
req.iface: 
req.product: Windows 10 or later.
---

# EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD callback



## -description
<p>The client driver's implementation that UCX calls to create static streams.</p>


## -prototype

````
EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD EvtUcxEndpointStaticStreamsAdd;

NTSTATUS EvtUcxEndpointStaticStreamsAdd(
  _In_ UCXENDPOINT       Endpoint,
  _In_ ULONG             NumberOfStreams,
  _In_ PUCXSSTREAMS_INIT UcxStaticStreamsInit
)
{ ... }

typedef EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD PEVT_UCX_ENDPOINT_STATIC_STREAMS_ADD;
````


## -parameters
<dl>

### -param <i>Endpoint</i> [in]

<dd>
<p>A handle to a UCXENDPOINT object that represents the endpoint.</p>
</dd>

### -param <i>NumberOfStreams</i> [in]

<dd>
<p>The number of non-default streams to create.</p>
</dd>

### -param <i>UcxStaticStreamsInit</i> [in]

<dd>
<p>A pointer to an opaque structure containing
        initialization information.  This structure is managed by UCX.</p>
</dd>
</dl>

## -returns
<p>If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it must return a status value for which NT_SUCCESS(status) equals FALSE.</p>

## -remarks
<p>The UCX client driver registers this callback function with the USB host controller extension (UCX) by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188039">UcxEndpointCreate</a>
 method.</p>

<p>This callback function creates a UCX static streams object by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188050">UcxStaticStreamsCreate</a>
 method. Only one UCX static streams object can be associated with a single endpoint.  The driver then calls <a href="https://msdn.microsoft.com/library/windows/hardware/mt188051">UcxStaticStreamsSetStreamInfo</a>
 once per stream to create a queue for each stream.</p>

<p>A static streams object is not enabled
    until UCX calls the client driver's <a href="https://msdn.microsoft.com/library/windows/hardware/mt187832">EVT_UCX_ENDPOINT_STATIC_STREAMS_ENABLE</a> callback function.</p>

<p>The UCX client driver registers this callback function with the USB host controller extension (UCX) by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188039">UcxEndpointCreate</a>
 method.</p>

<p>This callback function creates a UCX static streams object by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188050">UcxStaticStreamsCreate</a>
 method. Only one UCX static streams object can be associated with a single endpoint.  The driver then calls <a href="https://msdn.microsoft.com/library/windows/hardware/mt188051">UcxStaticStreamsSetStreamInfo</a>
 once per stream to create a queue for each stream.</p>

<p>A static streams object is not enabled
    until UCX calls the client driver's <a href="https://msdn.microsoft.com/library/windows/hardware/mt187832">EVT_UCX_ENDPOINT_STATIC_STREAMS_ENABLE</a> callback function.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ucxendpoint.h (include Ucxclass.h or Ucxendpoint.h)</dt>
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
</table>