---
UID: NF.udecxusbendpoint.UdecxUsbEndpointSetWdfIoQueue
title: UdecxUsbEndpointSetWdfIoQueue function
author: windows-driver-content
description: Sets a framework queue object with a UDE endpoint.
old-location: buses\udecxusbendpointsetwdfioqueue.htm
old-project: usbref
ms.assetid: 48744342-9137-48F5-9071-528974DE6AD5
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: UdecxUsbEndpointSetWdfIoQueue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: udecxusbendpoint.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 
req.alt-api: UdecxUsbEndpointSetWdfIoQueue
req.alt-loc: Udecxstub.lib,Udecxstub.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Udecxstub.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# UdecxUsbEndpointSetWdfIoQueue function



## -description
Sets a framework queue object with a UDE endpoint.


## -syntax

````
FORCEINLINE void UdecxUsbEndpointSetWdfIoQueue(
  _In_ UDECXUSBENDPOINT UdecxUsbEndpoint,
  _In_ WDFQUEUE         WdfQueue
);
````


## -parameters

### -param UdecxUsbEndpoint [in]

A handle to a UDE endpoint object. The client driver retrieved this pointer in the previous call to <a href="buses.udecxusbendpointcreate">UdecxUsbEndpointCreate</a>.

### -param WdfQueue [in]

A handle to a framework queue object that will handle requests sent to the endpoint. The client driver retrieved this pointer in the previous call to <a href="wdf.wdfioqueuecreate">WdfIoQueueCreate</a>. 

## -returns
This function does not return a value.

## -remarks


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
<dt>Udecxusbendpoint.h (include Udecx.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Udecxstub.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.creating_i_o_queues">Creating I/O Queues</a>
</dt>
<dt>
<a href="buses.usb_emulated_device__ude__architecture">Architecture: USB Device Emulation (UDE)</a>
</dt>
<dt>
<a href="buses.writing_a_ude_client_driver">Write a UDE client driver</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UdecxUsbEndpointSetWdfIoQueue function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
