---
UID: NC.ucxendpoint.EVT_UCX_ENDPOINT_GET_ISOCH_TRANSFER_PATH_DELAYS
title: EVT_UCX_ENDPOINT_GET_ISOCH_TRANSFER_PATH_DELAYS
author: windows-driver-content
description: UCX invokes this callback function to get information about transfer path delays for an isochronous endpoint.
old-location: buses\evt_ucx_endpoint_get_isoch_transfer_path_delays_.htm
old-project: usbref
ms.assetid: E400CCAE-8F0F-4814-8B63-EB4E116543A2
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCXUSBDEVICE_INFO,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ucxendpoint.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: EvtUcxEndpointGetIsochTransferPathDelays
req.alt-loc: Ucxendpoint.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# EVT_UCX_ENDPOINT_GET_ISOCH_TRANSFER_PATH_DELAYS callback



## -description
<p>UCX invokes this callback function to get information about transfer path delays for an isochronous endpoint. </p>


## -prototype

````
EVT_UCX_ENDPOINT_GET_ISOCH_TRANSFER_PATH_DELAYS EvtUcxEndpointGetIsochTransferPathDelays;

NTSTATUS EvtUcxEndpointGetIsochTransferPathDelays(
  _In_    UCXENDPOINT                              Endpoint,
  _Inout_ PUCX_ENDPOINT_ISOCH_TRANSFER_PATH_DELAYS UcxEndpointTransferPathDelays
)
{ ... }
````


## -parameters
<dl>

### -param <i>Endpoint</i> [in]

<dd>
<p>A handle to a UCXENDPOINT object that represents the isochronous endpoint for which the client driver receives the transfer path delays.</p>
</dd>

### -param <i>UcxEndpointTransferPathDelays</i> [in, out]

<dd>
<p>A pointer to a <a href="buses.ucx_endpoint_isoch_transfer_path_delays">UCX_ENDPOINT_ISOCH_TRANSFER_PATH_DELAYS</a> structure that contains transfer path delay values.</p>
</dd>
</dl>

## -returns
<p>If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it must return a status value for which NT_SUCCESS(status) equals FALSE.</p>

## -remarks
<p>The UCX client driver registers this callback function with the USB host controller extension (UCX) by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188039">UcxEndpointCreate</a>
 method.</p>

<p>The UCX client driver registers this callback function with the USB host controller extension (UCX) by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188039">UcxEndpointCreate</a>
 method.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses._urb_get_isoch_pipe_transfer_path_delays">_URB_GET_ISOCH_PIPE_TRANSFER_PATH_DELAYS</a>
</dt>
<dt><a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/usbcon/usb-client-drivers-for-ma-usb">USB client drivers for Media-Agnostic (MA-USB)</a></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20EVT_UCX_ENDPOINT_GET_ISOCH_TRANSFER_PATH_DELAYS callback function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
