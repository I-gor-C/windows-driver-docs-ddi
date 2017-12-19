---
UID: NF.udecxwdfdevice.UdecxWdfDeviceTryHandleUserIoctl
title: UdecxWdfDeviceTryHandleUserIoctl function
author: windows-driver-content
description: Attempts to handle an IOCTL request sent by a user-mode software.
old-location: buses\udecxwdfdevicetryhandleuserioctl.htm
old-project: UsbRef
ms.assetid: CC199F5C-BF05-4F1F-BEE4-8693F9156D8A
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: UdecxWdfDeviceTryHandleUserIoctl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: udecxwdfdevice.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 
req.alt-api: UdecxWdfDeviceTryHandleUserIoctl
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

# UdecxWdfDeviceTryHandleUserIoctl function



## -description
Attempts to handle an IOCTL request sent by a user-mode software. 



## -syntax

````
FORCEINLINE BOOLEAN UdecxWdfDeviceTryHandleUserIoctl(
  _In_ WDFDEVICE  Device,
  _In_ WDFREQUEST Request
);
````


## -parameters

### -param Device [in]

A handle to a framework device object that represents the controller. The client driver initialized this object in the previous call to <a href="buses.udecxwdfdeviceaddusbdeviceemulation">UdecxWdfDeviceAddUsbDeviceEmulation</a>.


### -param Request [in]

A handle to a framework request object that represents the IOCTL request. 


## -returns
TRUE indicates that USB device emulation  class extension (UdeCx) recognized and completed the request (with success or failure). In this case, the client driver must
    not complete the request. FALSE otherwise; the driver must complete the request.


## -remarks
The UDE client driver presents itself to user-mode software as a host controller driver. The client driver registers and exposes the GUID_DEVINTERFACE_USB_HOST_CONTROLLER device interface GUID. User-mode software  can open a handle to the device by specifying that GUID. By using that handle, the software can send IOCTL requests. 

 The client driver does not need to process the received IOCTL. It can send the request to the class extension by calling <b>UdecxWdfDeviceTryHandleUserIoctl</b>. If the class extension recognizes the request as a standard request, it completes it. Otherwise, the call fails and the client driver is then expected to complete the request. For a list of IOCTLs that must be handled, see <a href="usb_interfaces.htm#um_ioctl">USB IOCTLs for applications and services</a>.


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
<dt>UdecxWdfDevice.h (include Udecx.h)</dt>
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
<a href="buses.usb_emulated_device__ude__architecture">Architecture: USB Device Emulation (UDE)</a>
</dt>
<dt>
<a href="buses.writing_a_ude_client_driver">Write a UDE client driver</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [UsbRef\buses]:%20UdecxWdfDeviceTryHandleUserIoctl function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

