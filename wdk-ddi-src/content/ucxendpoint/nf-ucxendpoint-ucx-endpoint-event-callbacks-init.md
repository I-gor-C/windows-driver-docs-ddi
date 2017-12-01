---
UID: NF.ucxendpoint.UCX_ENDPOINT_EVENT_CALLBACKS_INIT
title: UCX_ENDPOINT_EVENT_CALLBACKS_INIT
author: windows-driver-content
description: Initializes a UCX_ENDPOINT_EVENT_CALLBACKS structure with client driver's callback functions. The client driver calls this function before calling UcxEndpointCreate method to create an endpoint and register its callback functions with UCX.
old-location: buses\_ucx_endpoint_event_callbacks_init.htm
old-project: usbref
ms.assetid: 1890052A-EE98-4749-ACF9-8321148F3828
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCX_ENDPOINT_EVENT_CALLBACKS_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ucxendpoint.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: UCX_ENDPOINT_EVENT_CALLBACKS_INIT
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
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# UCX_ENDPOINT_EVENT_CALLBACKS_INIT function



## -description
<p>Initializes a <a href="buses._ucx_endpoint_event_callbacks">UCX_ENDPOINT_EVENT_CALLBACKS</a> structure with client driver's callback functions. The client driver calls this function before calling <a href="buses._ucxendpointcreate">UcxEndpointCreate</a> method to create an endpoint and register its callback functions with UCX.</p>


## -syntax

````
void UCX_ENDPOINT_EVENT_CALLBACKS_INIT(
  _Out_ PUCX_ENDPOINT_EVENT_CALLBACKS                Callbacks,
  _In_  PEVT_UCX_ENDPOINT_PURGE                      EvtEndpointPurge,
  _In_  PEVT_UCX_ENDPOINT_START                      EvtEndpointStart,
  _In_  PEVT_UCX_ENDPOINT_ABORT                      EvtEndpointAbort,
  _In_  PEVT_UCX_ENDPOINT_RESET                      EvtEndpointReset,
  _In_  PEVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS     EvtEndpointOkToCancelTransfers,
  _In_  PEVT_UCX_ENDPOINT_STATIC_STREAMS_ADD         EvtEndpointStaticStreamsAdd,
  _In_  PEVT_UCX_ENDPOINT_STATIC_STREAMS_ENABLE      EvtEndpointStaticStreamsEnable,
  _In_  PEVT_UCX_ENDPOINT_STATIC_STREAMS_DISABLE     EvtEndpointStaticStreamsDisable
);
````


## -parameters
<dl>

### -param <i>Callbacks</i> [out]

<dd>
<p>A pointer to a <a href="buses._ucx_endpoint_event_callbacks">UCX_ENDPOINT_EVENT_CALLBACKS</a> structure that contains pointers to the client driver's event callback functions.</p>
</dd>

### -param <i>EvtEndpointPurge</i> [in]

<dd>
<p>A pointer to client driver's implementation of the <a href="buses.evt_ucx_endpoint_purge">EVT_UCX_ENDPOINT_PURGE</a>                     event callback function.</p>
</dd>

### -param <i>EvtEndpointStart</i> [in]

<dd>
<p>A pointer to client driver's implementation of the <a href="buses.evt_ucx_endpoint_start">EVT_UCX_ENDPOINT_START</a>                     event callback function.</p>
</dd>

### -param <i>EvtEndpointAbort</i> [in]

<dd>
<p>A pointer to client driver's implementation of the <a href="buses.evt_ucx_endpoint_abort">EVT_UCX_ENDPOINT_ABORT</a>                     event callback function.</p>
</dd>

### -param <i>EvtEndpointReset</i> [in]

<dd>
<p>A pointer to client driver's implementation of the <a href="buses.evt_ucx_endpoint_reset">EVT_UCX_ENDPOINT_RESET</a>                     event callback function.</p>
</dd>

### -param <i>EvtEndpointOkToCancelTransfers</i> [in]

<dd>
<p>A pointer to client driver's implementation of the <a href="buses.evt_ucx_endpoint_ok_to_cancel_transfers">EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS</a>    event callback function.</p>
</dd>

### -param <i>EvtEndpointStaticStreamsAdd</i> [in]

<dd>
<p>A pointer to client driver's implementation of the <a href="buses.evt_ucx_endpoint_static_streams_add">EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD</a>        event callback function.</p>
</dd>

### -param <i>EvtEndpointStaticStreamsEnable</i> [in]

<dd>
<p>A pointer to client driver's implementation of the <a href="buses.evt_ucx_endpoint_static_streams_enable">EVT_UCX_ENDPOINT_STATIC_STREAMS_ENABLE</a>     event callback function.</p>
</dd>

### -param <i>EvtEndpointStaticStreamsDisable</i> [in]

<dd>
<p>A pointer to client driver's implementation of the <a href="buses.evt_ucx_endpoint_static_streams_disable">EVT_UCX_ENDPOINT_STATIC_STREAMS_DISABLE</a>    event callback function.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum support</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
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
<dt>Ucxendpoint.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses._ucxendpointcreate">UcxEndpointCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCX_ENDPOINT_EVENT_CALLBACKS_INIT function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
