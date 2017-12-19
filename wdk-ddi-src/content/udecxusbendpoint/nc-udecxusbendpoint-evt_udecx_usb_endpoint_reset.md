---
UID: NC.udecxusbendpoint.EVT_UDECX_USB_ENDPOINT_RESET
title: EVT_UDECX_USB_ENDPOINT_RESET
author: windows-driver-content
description: The USB device emulation class extension (UdeCx) invokes this callback function to reset an endpoint of the virtual USB device.
old-location: buses\evt_udecx_usb_endpoint_reset.htm
old-project: UsbRef
ms.assetid: 4220509B-A378-47F4-8E71-0290EDED89EB
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _UDECX_USB_ENDPOINT_INIT_AND_METADATA, UDECX_USB_ENDPOINT_INIT_AND_METADATA, PUDECX_USB_ENDPOINT_INIT_AND_METADATA, *PUDECX_USB_ENDPOINT_INIT_AND_METADATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: udecxusbendpoint.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 
req.alt-api: EvtUsbEndpointReset
req.alt-loc: UdecxUsbEndpoint.h
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
req.product: Windows 10 or later.
---

# EVT_UDECX_USB_ENDPOINT_RESET callback



## -description
The USB device emulation class extension (UdeCx) invokes this callback function to reset an endpoint of the virtual USB device.



## -prototype

````
EVT_UDECX_USB_ENDPOINT_RESET EvtUsbEndpointReset;

void EvtUsbEndpointReset(
  _In_ UDECXUSBENDPOINT UdecxUsbEndpoint,
  _In_ WDFREQUEST       Request
)
{ ... }
````


## -parameters

### -param UdecxUsbEndpoint [in]

A handle to a UDE endpoint object that represents the endpoint to reset. The client driver retrieved this pointer in the previous call to <a href="buses.udecxusbendpointcreate">UdecxUsbEndpointCreate</a>.


### -param Request [in]

A handle to a framework request object that represents the request to reset the endpoint.


## -returns
This callback function does not return a value.


## -remarks
The client driver registered this callback function in a previous call to <a href="buses.udecxusbendpointinitsetcallbacks">UdecxUsbEndpointInitSetCallbacks</a> by supplying a function pointer to its implementation.

The reset request clears the error condition in the endpoint that causes failed I/O transfers. At that time, UdeCx can invoke the  <i>EVT_UDECX_USB_ENDPOINT_RESET</i> callback function. That call is asynchronous. The client driver completes the request and signals completion with status by calling <a href="wdf.wdfrequestcompletewithinformation">WdfRequestCompleteWithInformation</a> method .  (this is the only way the UDECX client uses the request parameter).



## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.15

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>UdecxUsbEndpoint.h (include Udecx.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;=DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.how_to_recover_from_usb_pipe_errors">How to recover from USB pipe errors</a>
</dt>
<dt>
<a href="wdf.managing_i_o_queues">Managing I/O Queues</a>
</dt>
<dt>
<a href="buses.usb_emulated_device__ude__architecture">Architecture: USB Device Emulation (UDE)</a>
</dt>
<dt>
<a href="buses.writing_a_ude_client_driver">Write a UDE client driver</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [UsbRef\buses]:%20EVT_UDECX_USB_ENDPOINT_RESET callback function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

