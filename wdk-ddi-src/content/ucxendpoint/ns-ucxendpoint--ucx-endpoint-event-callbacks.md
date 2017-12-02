---
UID: NS.ucxendpoint._UCX_ENDPOINT_EVENT_CALLBACKS
title: UCX_ENDPOINT_EVENT_CALLBACKS
author: windows-driver-content
description: This structure provides a list of pointers to UCX endpoint event callback functions.
old-location: buses\_ucx_endpoint_event_callbacks.htm
old-project: usbref
ms.assetid: 93071B7B-74D8-44A2-984D-A6BABFC07BA3
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCX_ENDPOINT_EVENT_CALLBACKS, UCX_ENDPOINT_EVENT_CALLBACKS, *PUCX_ENDPOINT_EVENT_CALLBACKS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxendpoint.h
req.include-header: Ucxclass.h, Ucxendpoint.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UCX_ENDPOINT_EVENT_CALLBACKS
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

# UCX_ENDPOINT_EVENT_CALLBACKS structure



## -description
<p>This structure provides a list of  pointers to UCX endpoint event callback functions.</p>


## -syntax

````
typedef struct _UCX_ENDPOINT_EVENT_CALLBACKS {
  ULONG                                           Size;
  PEVT_UCX_ENDPOINT_PURGE                         EvtEndpointPurge;
  PEVT_UCX_ENDPOINT_START                         EvtEndpointStart;
  PEVT_UCX_ENDPOINT_ABORT                         EvtEndpointAbort;
  PEVT_UCX_ENDPOINT_RESET                         EvtEndpointReset;
  PEVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS        EvtEndpointOkToCancelTransfers;
  PEVT_UCX_ENDPOINT_STATIC_STREAMS_ADD            EvtEndpointStaticStreamsAdd;
  PEVT_UCX_ENDPOINT_STATIC_STREAMS_ENABLE         EvtEndpointStaticStreamsEnable;
  PEVT_UCX_ENDPOINT_STATIC_STREAMS_DISABLE        EvtEndpointStaticStreamsDisable;
  HANDLE                                          Reserved1;
  PFN_UCX_ENDPOINT_GET_ISOCH_TRANSFER_PATH_DELAYS EvtEndpointGetIsochTransferPathDelays;
  PFN_UCX_ENDPOINT_SET_CHARACTERISTIC             EvtEndpointSetCharacteristic;
} UCX_ENDPOINT_EVENT_CALLBACKS, *P_UCX_ENDPOINT_EVENT_CALLBACKS;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>The size in bytes of the structure.</p>
</dd>

### -field EvtEndpointPurge

<dd>
<p>A pointer to an <a href="..\ucxendpoint\nc-ucxendpoint-evt-ucx-endpoint-purge.md">EVT_UCX_ENDPOINT_PURGE</a> callback function.</p>
</dd>

### -field EvtEndpointStart

<dd>
<p>A pointer to an <a href="..\ucxendpoint\nc-ucxendpoint-evt-ucx-endpoint-start.md">EVT_UCX_ENDPOINT_START</a> callback function.</p>
</dd>

### -field EvtEndpointAbort

<dd>
<p>A pointer to an <a href="..\ucxendpoint\nc-ucxendpoint-evt-ucx-endpoint-abort.md">EVT_UCX_ENDPOINT_ABORT</a> callback function.</p>
</dd>

### -field EvtEndpointReset

<dd>
<p>A pointer to an <a href="..\ucxendpoint\nc-ucxendpoint-evt-ucx-endpoint-reset.md">EVT_UCX_ENDPOINT_RESET</a> callback function.</p>
</dd>

### -field EvtEndpointOkToCancelTransfers

<dd>
<p>A pointer to an <a href="..\ucxendpoint\nc-ucxendpoint-evt-ucx-endpoint-ok-to-cancel-transfers.md">EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS</a> callback function.</p>
</dd>

### -field EvtEndpointStaticStreamsAdd

<dd>
<p>A pointer to an <a href="..\ucxendpoint\nc-ucxendpoint-evt-ucx-endpoint-static-streams-add.md">EVT_UCX_ENDPOINT_STATIC_STREAMS_ADD</a> callback function.</p>
</dd>

### -field EvtEndpointStaticStreamsEnable

<dd>
<p>A pointer to an <a href="..\ucxendpoint\nc-ucxendpoint-evt-ucx-endpoint-static-streams-enable.md">EVT_UCX_ENDPOINT_STATIC_STREAMS_ENABLE</a> callback function.</p>
</dd>

### -field EvtEndpointStaticStreamsDisable

<dd>
<p>A pointer to an <a href="..\ucxendpoint\nc-ucxendpoint-evt-ucx-endpoint-static-streams-disable.md">EVT_UCX_ENDPOINT_STATIC_STREAMS_DISABLE</a> callback function.</p>
</dd>

### -field Reserved1

<dd>
<p>Do not use.</p>
</dd>

### -field EvtEndpointGetIsochTransferPathDelays

<dd>
<p>A pointer to an <a href="..\ucxendpoint\nc-ucxendpoint-evt-ucx-endpoint-get-isoch-transfer-path-delays.md">EVT_UCX_ENDPOINT_GET_ISOCH_TRANSFER_PATH_DELAYS</a> callback function.</p>
</dd>

### -field EvtEndpointSetCharacteristic

<dd>
<p>A pointer to an <a href="..\ucxendpoint\nc-ucxendpoint-evt-ucx-endpoint-set-characteristic.md">EVT_UCX_ENDPOINT_SET_CHARACTERISTIC</a> callback function.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\ucxendpoint\nf-ucxendpoint-ucx-endpoint-event-callbacks-init.md">UCX_ENDPOINT_EVENT_CALLBACKS_INIT</a>
</dt>
<dt>
<a href="..\ucxendpoint\nf-ucxendpoint-ucxendpointinitseteventcallbacks.md">UcxEndpointInitSetEventCallbacks</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCX_ENDPOINT_EVENT_CALLBACKS structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
