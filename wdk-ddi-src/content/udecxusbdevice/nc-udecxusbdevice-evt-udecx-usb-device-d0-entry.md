---
UID: NC.udecxusbdevice.EVT_UDECX_USB_DEVICE_D0_ENTRY
title: EVT_UDECX_USB_DEVICE_D0_ENTRY
author: windows-driver-content
description: The USB device emulation class extension (UdeCx) invokes this callback function when it gets a request to bring the virtual USB device out of a low power state to working state.
old-location: buses\evt_udecx_usb_device_d0_entry.htm
old-project: usbref
ms.assetid: 92CEEAF3-BD70-4B1C-8385-00720A195E50
ms.author: windowsdriverdev
ms.date: 11/20/2017
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
req.alt-api: EvtUsbDeviceLinkPowerEntry
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
req.iface: 
req.product: Windows 10 or later.
---

# EVT_UDECX_USB_DEVICE_D0_ENTRY callback



## -description
<p>The USB device emulation class extension (UdeCx) invokes this callback function when it gets a request to bring the virtual USB device out of a low power state to working state.</p>


## -prototype

````
EVT_UDECX_USB_DEVICE_D0_ENTRY EvtUsbDeviceLinkPowerEntry;

NTSTATUS EvtUsbDeviceLinkPowerEntry(
  _In_ WDFDEVICE      UdecxWdfDevice,
  _In_ UDECXUSBDEVICE UdecxUsbDevice
)
{ ... }
````


## -parameters
<dl>

### -param <i>UdecxWdfDevice</i> [in]

<dd>
<p>A handle to a framework device object that represents the controller to which the USB device is attached. The client driver initialized this object in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/mt627990">UdecxWdfDeviceAddUsbDeviceEmulation</a>.</p>
</dd>

### -param <i>UdecxUsbDevice</i> [in]

<dd>
<p>A handle to UDE device object. The client driver created this object in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/mt595959">UdecxUsbDeviceCreate</a>.</p>
</dd>
</dl>

## -returns
<p>If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE.</p>

## -remarks
<p>The client driver registered the function in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/mt627972">UdecxUsbDeviceInitSetStateChangeCallbacks</a> by supplying a function pointer to its implementation.</p>

<p>In the callback implementation, the client driver for the USB device is expected to perform steps to enter working state. </p>

<p>The power request may be completed asynchronously by returning STATUS_PENDING, and then later completing it by calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt627974">UdecxUsbDeviceLinkPowerExitComplete</a> with the actual completion code.
</p>

<p>The client driver registered the function in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/mt627972">UdecxUsbDeviceInitSetStateChangeCallbacks</a> by supplying a function pointer to its implementation.</p>

<p>In the callback implementation, the client driver for the USB device is expected to perform steps to enter working state. </p>

<p>The power request may be completed asynchronously by returning STATUS_PENDING, and then later completing it by calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt627974">UdecxUsbDeviceLinkPowerExitComplete</a> with the actual completion code.
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
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
<p>1.15</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Udecxusbdevice.h (include Udecx.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt627982">UdecxUsbDeviceSignalWake</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt627974">UdecxUsbDeviceLinkPowerExitComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt595911">EVT_UDECX_USB_DEVICE_D0_EXIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt595932">Architecture: USB Device Emulation (UDE)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt595939">Write a UDE client driver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20EVT_UDECX_USB_DEVICE_D0_ENTRY callback function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
