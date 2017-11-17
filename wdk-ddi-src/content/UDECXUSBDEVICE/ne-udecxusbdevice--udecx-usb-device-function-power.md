---
UID: NE.udecxusbdevice._UDECX_USB_DEVICE_FUNCTION_POWER
title: UDECX_USB_DEVICE_FUNCTION_POWER
author: windows-driver-content
description: Defines values for function wake capability of a virtual USB 3.0 device.
old-location: buses\udecx_usb_device_function_power.htm
ms.assetid: 7EE6D8AE-E001-4BC9-A617-682202A297E7
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: usbref
req.header: udecxusbdevice.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UDECX_USB_DEVICE_FUNCTION_POWER
req.alt-loc: UdecxUsbDevice.h
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
ms.keywords: UdecxUrbSetBytesCompleted
req.iface: 
req.product: Windows 10 or later.
---

# UDECX_USB_DEVICE_FUNCTION_POWER enumeration



## -description
<p>Defines values for function wake capability of a virtual USB 3.0  device.</p>


## -syntax

````
typedef enum _UDECX_USB_DEVICE_FUNCTION_POWER { 
  UdecxUsbDeviceFunctionNotSuspended         = 0,
  UdecxUsbDeviceFunctionSuspendedCannotWake  = ,
  UdecxUsbDeviceFunctionSuspendedCanWake     = 
} UDECX_USB_DEVICE_FUNCTION_POWER, *PUDECX_USB_DEVICE_FUNCTION_POWER;
````


## -enum-fields
<dl>

### -field <a id="UdecxUsbDeviceFunctionNotSuspended"></a><a id="udecxusbdevicefunctionnotsuspended"></a><a id="UDECXUSBDEVICEFUNCTIONNOTSUSPENDED"></a><b>UdecxUsbDeviceFunctionNotSuspended</b>

<dd>
<p>The USB interface cannot enter function suspend. </p>
</dd>

### -field <a id="UdecxUsbDeviceFunctionSuspendedCannotWake"></a><a id="udecxusbdevicefunctionsuspendedcannotwake"></a><a id="UDECXUSBDEVICEFUNCTIONSUSPENDEDCANNOTWAKE"></a><b>UdecxUsbDeviceFunctionSuspendedCannotWake</b>

<dd>
<p>The USB interface cannot send a wake signal to the host controller.</p>
</dd>

### -field <a id="UdecxUsbDeviceFunctionSuspendedCanWake"></a><a id="udecxusbdevicefunctionsuspendedcanwake"></a><a id="UDECXUSBDEVICEFUNCTIONSUSPENDEDCANWAKE"></a><b>UdecxUsbDeviceFunctionSuspendedCanWake</b>

<dd>
<p>The USB interface can send a wake signal to the host controller when the function is in suspend state.</p>
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
<dt>UdecxUsbDevice.h (include Udecx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt595915">EVT_UDECX_USB_DEVICE_SET_FUNCTION_SUSPEND_AND_WAKE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UDECX_USB_DEVICE_FUNCTION_POWER enumeration%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
