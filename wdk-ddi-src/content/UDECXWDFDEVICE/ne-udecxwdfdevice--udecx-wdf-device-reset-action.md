---
UID: NE.udecxwdfdevice._UDECX_WDF_DEVICE_RESET_ACTION
title: UDECX_WDF_DEVICE_RESET_ACTION
author: windows-driver-content
description: Defines values that indicate the types of reset operation supported by an emulated USB host controller.
old-location: buses\udecx_wdf_device_reset_action.htm
ms.assetid: E3216F62-5506-4DA2-AD89-B2406D3E97C0
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: usbref
req.header: udecxwdfdevice.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UDECX_WDF_DEVICE_RESET_ACTION
req.alt-loc: UdecxWdfDevice.h
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
ms.keywords: UDECX_USB_ENDPOINT_INIT_AND_METADATA, UDECX_USB_ENDPOINT_INIT_AND_METADATA, *PUDECX_USB_ENDPOINT_INIT_AND_METADATA
req.iface: 
req.product: Windows 10 or later.
---

# UDECX_WDF_DEVICE_RESET_ACTION enumeration



## -description
<p>Defines values that indicate the types of reset operation supported by an emulated USB host controller.</p>


## -syntax

````
typedef enum _UDECX_WDF_DEVICE_RESET_ACTION { 
  UdecxWdfDeviceResetActionResetEachUsbDevice  = 0,
  UdecxWdfDeviceResetActionResetWdfDevice      = 
} UDECX_WDF_DEVICE_RESET_ACTION;
````


## -enum-fields
<dl>

### -field <a id="UdecxWdfDeviceResetActionResetEachUsbDevice"></a><a id="udecxwdfdeviceresetactionreseteachusbdevice"></a><a id="UDECXWDFDEVICERESETACTIONRESETEACHUSBDEVICE"></a><b>UdecxWdfDeviceResetActionResetEachUsbDevice</b>

<dd>
<p>Each device that is attached to the controller is reset.</p>
</dd>

### -field <a id="UdecxWdfDeviceResetActionResetWdfDevice"></a><a id="udecxwdfdeviceresetactionresetwdfdevice"></a><a id="UDECXWDFDEVICERESETACTIONRESETWDFDEVICE"></a><b>UdecxWdfDeviceResetActionResetWdfDevice</b>

<dd>
<p>The emulated host controller is reset.</p>
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
<dt>UdecxWdfDevice.h (include Udecx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt595920">EVT_UDECX_WDF_DEVICE_RESET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt628008">UDECX_WDF_DEVICE_CONFIG</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UDECX_WDF_DEVICE_RESET_ACTION enumeration%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
