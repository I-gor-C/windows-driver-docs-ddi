---
UID: NF.ucxendpoint.UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS_INIT
title: UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS_INIT
author: windows-driver-content
description: Initializes a UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS structure with client driver's callback functions. The client driver calls this function before calling UcxEndpointCreate method to create an endpoint and register its callback functions with UCX.
old-location: buses\ucx_default_endpoint_event_callbacks_init.htm
old-project: usbref
ms.assetid: EE7ABC3D-948B-481B-B254-40A05EDEB83D
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ucxendpoint.h
req.include-header: Ucxclass.h, Ucxendpoint.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS_INIT
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

# UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS_INIT function



## -description
<p>Initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/mt188062">UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS</a> structure with client driver's callback functions. The client driver calls this function before calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt188039">UcxEndpointCreate</a> method to create an endpoint and register its callback functions with UCX.</p>


## -syntax

````
FORCEINLINE void UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS_INIT(
  _Out_ PUCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS        Callbacks,
  _In_  PEVT_UCX_ENDPOINT_PURGE                      EvtEndpointPurge,
  _In_  PEVT_UCX_ENDPOINT_START                      EvtEndpointStart,
  _In_  PEVT_UCX_ENDPOINT_ABORT                      EvtEndpointAbort,
  _In_  PEVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS     EvtEndpointOkToCancelTransfers,
  _In_  PEVT_UCX_DEFAULT_ENDPOINT_UPDATE             EvtDefaultEndpointUpdate
);
````


## -parameters
<dl>

### -param <i>Callbacks</i> [out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/mt188062">UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS</a> structure that contains pointers to the client driver's event callback functions.</p>
</dd>

### -param <i>EvtEndpointPurge</i> [in]

<dd>
<p>A pointer to client driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187827">EVT_UCX_ENDPOINT_PURGE</a>                     event callback function.</p>
</dd>

### -param <i>EvtEndpointStart</i> [in]

<dd>
<p>A pointer to client driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187829">EVT_UCX_ENDPOINT_START</a>                     event callback function.</p>
</dd>

### -param <i>EvtEndpointAbort</i> [in]

<dd>
<p>A pointer to client driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187825">EVT_UCX_ENDPOINT_ABORT</a>                     event callback function.</p>
</dd>

### -param <i>EvtEndpointOkToCancelTransfers</i> [in]

<dd>
<p>A pointer to client driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187826">EVT_UCX_ENDPOINT_OK_TO_CANCEL_TRANSFERS</a>    event callback function.</p>
</dd>

### -param <i>EvtDefaultEndpointUpdate</i> [in]

<dd>
<p>A pointer to client driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187824">EVT_UCX_DEFAULT_ENDPOINT_UPDATE</a>    event callback function.</p>
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
<dt>Ucxendpoint.h (include Ucxclass.h or Ucxendpoint.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt188039">UcxEndpointCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCX_DEFAULT_ENDPOINT_EVENT_CALLBACKS_INIT function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
