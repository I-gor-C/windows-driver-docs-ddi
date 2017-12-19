---
UID: NC.udecxusbdevice.EVT_UDECX_USB_DEVICE_D0_EXIT
title: EVT_UDECX_USB_DEVICE_D0_EXIT
author: windows-driver-content
description: The USB device emulation class extension (UdeCx) invokes this callback function when it gets a request to send the virtual USB device to a low power state.
old-location: buses\evt_udecx_usb_device_d0_exit.htm
old-project: UsbRef
ms.assetid: CC2878DC-66EC-4493-8188-3B6BAEA928DF
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: UdecxUrbSetBytesCompleted
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: udecxusbdevice.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 
req.alt-api: EvtUsbDeviceLinkPowerExit
req.alt-loc: udecxusbdevice.h
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

# EVT_UDECX_USB_DEVICE_D0_EXIT callback



## -description
The USB device emulation class extension (UdeCx) invokes this callback function when it gets a request to send the virtual USB device to a low power state.



## -prototype

````
EVT_UDECX_USB_DEVICE_D0_EXIT EvtUsbDeviceLinkPowerExit;

NTSTATUS EvtUsbDeviceLinkPowerExit(
  _In_ WDFDEVICE                     UdecxWdfDevice,
  _In_ UDECXUSBDEVICE                UdecxUsbDevice,
  _In_ UDECX_USB_DEVICE_WAKE_SETTING WakeSetting
)
{ ... }
````


## -parameters

### -param UdecxWdfDevice [in]

A handle to a framework device object that represents the controller to which the USB device is attached. The client driver initialized this object in a previous call to <a href="buses.udecxwdfdeviceaddusbdeviceemulation">UdecxWdfDeviceAddUsbDeviceEmulation</a>.


### -param UdecxUsbDevice [in]

A handle to UDE device object. The client driver created this object in a previous call to <a href="buses.udecxusbdevicecreate">UdecxUsbDeviceCreate</a>.


### -param WakeSetting [in]

A <a href="buses.udecx_usb_device_wake_setting">UDECX_USB_DEVICE_WAKE_SETTING</a>-type value that indicates remote wake capability of the USB device.


## -returns
If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE.


## -remarks
The client driver registered the function in a previous call to <a href="buses.udecxusbdeviceinitsetstatechangecallbacks">UdecxUsbDeviceInitSetStateChangeCallbacks</a> by supplying a function pointer to its implementation.

In the callback implementation, the client driver for the USB device is expected to perform steps to send the device to a low power state. In this function, the driver can initiate its wake-up from a low link power state, function suspend, or both.
To do so, the driver for a USB 2.0 device must call the <a href="buses.udecxusbdevicesignalwake">UdecxUsbDeviceSignalWake</a> method.  USB 3.0 devices must use <a href="buses.udecxusbdevicesignalfunctionwake">UdecxUsbDeviceSignalFunctionWake</a>.

The power request may be completed asynchronously by returning STATUS_PENDING, and then later calling <a href="buses.udecxusbdevicelinkpowerexitcomplete">UdecxUsbDeviceLinkPowerExitComplete</a> with the actual completion code.



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
<dt>Udecxusbdevice.h (include Udecx.h)</dt>
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
<a href="buses.udecxusbdevicesignalwake">UdecxUsbDeviceSignalWake</a>
</dt>
<dt>
<a href="buses.udecxusbdevicelinkpowerexitcomplete">UdecxUsbDeviceLinkPowerExitComplete</a>
</dt>
<dt>
<a href="..\udecxusbdevice\nc-udecxusbdevice-evt_udecx_usb_device_d0_entry.md">EVT_UDECX_USB_DEVICE_D0_ENTRY</a>
</dt>
<dt>
<a href="buses.usb_emulated_device__ude__architecture">Architecture: USB Device Emulation (UDE)</a>
</dt>
<dt>
<a href="buses.writing_a_ude_client_driver">Write a UDE client driver</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [UsbRef\buses]:%20EVT_UDECX_USB_DEVICE_D0_EXIT callback function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

