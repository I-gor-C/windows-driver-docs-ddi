---
UID: NS.udecxusbendpoint._UDECX_USB_ENDPOINT_CALLBACKS
title: UDECX_USB_ENDPOINT_CALLBACKS
author: windows-driver-content
description: Contains function pointers to endpoint callback functions implemented by the UDE client driver. Initialize this structure by calling UDECX_USB_ENDPOINT_CALLBACKS_INIT.
old-location: buses\udecx_usb_endpoint_callbacks.htm
old-project: usbref
ms.assetid: 5AAB4474-9FDF-4ACF-AC38-F84D2682B5E0
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UDECX_USB_ENDPOINT_CALLBACKS, UDECX_USB_ENDPOINT_CALLBACKS, *PUDECX_USB_ENDPOINT_CALLBACKS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: udecxusbendpoint.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UDECX_USB_ENDPOINT_CALLBACKS
req.alt-loc: udecxusbendpoint.h
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

# UDECX_USB_ENDPOINT_CALLBACKS structure



## -description
<p>Contains function pointers to endpoint callback functions implemented by the UDE client driver. Initialize this structure by calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt628006">UDECX_USB_ENDPOINT_CALLBACKS_INIT</a>.</p>


## -syntax

````
typedef struct _UDECX_USB_ENDPOINT_CALLBACKS {
  ULONG                        Size;
  PFN_UDECX_USB_ENDPOINT_RESET EvtUsbEndpointReset;
  EVT_UDECX_USB_ENDPOINT_START EvtUsbEndpointStart;
  EVT_UDECX_USB_ENDPOINT_PURGE EvtUsbEndpointPurge;
} UDECX_USB_ENDPOINT_CALLBACKS, *PUDECX_USB_ENDPOINT_CALLBACKS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size of this structure.</p>
</dd>

### -field <b>EvtUsbEndpointReset</b>

<dd>
<p>Required. A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/mt595917">EVT_UDECX_USB_ENDPOINT_RESET</a> callback function implemented by a UDE client driver.</p>
</dd>

### -field <b>EvtUsbEndpointStart</b>

<dd>
<p>Optional. A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/mt595918">EVT_UDECX_USB_ENDPOINT_START</a> callback function implemented by a UDE client driver.</p>
</dd>

### -field <b>EvtUsbEndpointPurge</b>

<dd>
<p>Optional. A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/mt595916">EVT_UDECX_USB_ENDPOINT_PURGE</a> callback function implemented by a UDE client driver.</p>
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
<dt>Udecxusbendpoint.h (include Udecx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt627985">UdecxUsbEndpointInitSetCallbacks</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt627983">UdecxUsbEndpointCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UDECX_USB_ENDPOINT_CALLBACKS structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
