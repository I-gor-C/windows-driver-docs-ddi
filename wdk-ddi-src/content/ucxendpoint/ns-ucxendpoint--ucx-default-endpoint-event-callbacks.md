---
UID: NS.ucxendpoint._UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS
title: UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS
author: windows-driver-content
description: This structure provides a list of UCX default endpoint event callback functions.
old-location: buses\_ucx_default_endpoint_event_callbacks.htm
old-project: usbref
ms.assetid: A22E96FC-E219-4F6C-B8AF-AC86FAD89543
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS, UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS, *PUCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS
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
req.alt-api: UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS
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

# UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS structure



## -description
<p>This structure provides a list of UCX default endpoint event callback functions.</p>


## -syntax

````
typedef struct _UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS {
  ULONG                                    Size;
  PEVT_UCX_ENDPOINT_PURGE                  EvtEndpointPurge;
  PEVT_UCX_ENDPOINT_START                  EvtEndpointStart;
  PEVT_UCX_ENDPOINT_ABORT                  EvtEndpointAbort;
  PEVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS EvtEndpointOkToCancelTransfers;
  PEVT_UCX_DEFAULT_ENDPOINT_UPDATE         EvtDefaultEndpointUpdate;
  HANDLE                                   Reserved1;
} UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS, *P_UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size in bytes of this structure.</p>
</dd>

### -field <b>EvtEndpointPurge</b>

<dd>
<p>A pointer to a EVT_UCX_ENDPOINT_PURGE callback function.</p>
</dd>

### -field <b>EvtEndpointStart</b>

<dd>
<p>A pointer to a EVT_UCX_ENDPOINT_START callback function.</p>
</dd>

### -field <b>EvtEndpointAbort</b>

<dd>
<p>A pointer to a EVT_UCX_ENDPOINT_ABORT callback function.</p>
</dd>

### -field <b>EvtEndpointOkToCancelTransfers</b>

<dd>
<p>A pointer to a EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS callback function.</p>
</dd>

### -field <b>EvtDefaultEndpointUpdate</b>

<dd>
<p>A pointer to a EVT_UCX_DEFAULT_ENDPOINT_UPDATE callback function.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Do not use.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt187950">UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt188037">UcxDefaultEndpointInitSetEventCallbacks</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
