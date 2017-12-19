---
UID: NS.WDFUSB._WDF_USB_DEVICE_INFORMATION
title: _WDF_USB_DEVICE_INFORMATION
author: windows-driver-content
description: The WDF_USB_DEVICE_INFORMATION structure contains version and capability information for a USB device.
old-location: wdf\wdf_usb_device_information.htm
old-project: wdf
ms.assetid: 5d212a29-22b9-408d-9562-b232fc91cc9f
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _WDF_USB_DEVICE_INFORMATION, PWDF_USB_DEVICE_INFORMATION, WDF_USB_DEVICE_INFORMATION, *PWDF_USB_DEVICE_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_USB_DEVICE_INFORMATION
req.alt-loc: wdfusb.h
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
req.product: Windows 10 or later.
---

# _WDF_USB_DEVICE_INFORMATION structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_USB_DEVICE_INFORMATION</b> structure contains version and capability information for a USB device.



## -syntax

````
typedef struct _WDF_USB_DEVICE_INFORMATION {
  ULONG                    Size;
  USBD_VERSION_INFORMATION UsbdVersionInformation;
  ULONG                    HcdPortCapabilities;
  ULONG                    Traits;
} WDF_USB_DEVICE_INFORMATION, *PWDF_USB_DEVICE_INFORMATION;
````


## -struct-fields

### -field Size

The size, in bytes, of this structure. 


### -field UsbdVersionInformation

A <a href="buses.usbd_version_information">USBD_VERSION_INFORMATION</a> structure that provides version information for the host controller driver (HCD) and the USB specification version that the device supports.


### -field HcdPortCapabilities

This member is reserved for system use.


### -field Traits

A set of bit flags that identify device traits. The flags are defined by the <a href="wdf.wdf_usb_device_traits">WDF_USB_DEVICE_TRAITS</a> enumeration.


## -remarks
The <b>WDF_USB_DEVICE_INFORMATION</b> structure is filled in by the <a href="wdf.wdfusbtargetdeviceretrieveinformation">WdfUsbTargetDeviceRetrieveInformation</a> method. Before calling <b>WdfUsbTargetDeviceRetrieveInformation</b>, the driver must call <a href="wdf.wdf_usb_device_information_init">WDF_USB_DEVICE_INFORMATION_INIT</a> to initialize the structure.


## -requirements
<table>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfusb.h (include Wdfusb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.usbd_version_information">USBD_VERSION_INFORMATION</a>
</dt>
<dt>
<a href="wdf.wdf_usb_device_information_init">WDF_USB_DEVICE_INFORMATION_INIT</a>
</dt>
<dt>
<a href="wdf.wdf_usb_device_traits">WDF_USB_DEVICE_TRAITS</a>
</dt>
<dt>
<a href="wdf.wdfusbtargetdeviceretrieveinformation">WdfUsbTargetDeviceRetrieveInformation</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_USB_DEVICE_INFORMATION structure%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

