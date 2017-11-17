---
UID: NS.usbioctl._HUB_DEVICE_CONFIG_INFO_V1
title: HUB_DEVICE_CONFIG_INFO_V1
author: windows-driver-content
description: The HUB_DEVICE_CONFIG_INFO structure is used in conjunction with the kernel-mode IOCTL, IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO to request to report information about a USB device and the hub to which the device is attached.
old-location: buses\hub_device_config_info.htm
ms.assetid: 2e94cf01-6edf-40ca-b25e-ce7c125e4686
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: usbref
req.header: usbioctl.h
req.include-header: Usbioctl.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows XP and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HUB_DEVICE_CONFIG_INFO
req.alt-loc: usbioctl.h
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
ms.keywords: HUB_DEVICE_CONFIG_INFO_V1, HUB_DEVICE_CONFIG_INFO, *PHUB_DEVICE_CONFIG_INFO
req.iface: 
req.product: Windows 10 or later.
---

# HUB_DEVICE_CONFIG_INFO_V1 structure



## -description
<p>The <b>HUB_DEVICE_CONFIG_INFO</b> structure is used in conjunction with the kernel-mode IOCTL, <a href="https://msdn.microsoft.com/library/windows/hardware/ff537252">IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO</a> to request to report information about a USB device and the hub to which the device is attached. </p>


## -syntax

````
typedef struct _HUB_DEVICE_CONFIG_INFO {
  ULONG              Version;
  ULONG              Length;
  USB_HUB_CAP_FLAGS  HubFlags;
  USB_ID_STRING      HardwareIds;
  USB_ID_STRING      CompatibleIds;
  USB_ID_STRING      DeviceDescription;
} HUB_DEVICE_CONFIG_INFO, *PHUB_DEVICE_CONFIG_INFO;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>Specifies the version number.  Must be set to 1. </p>
</dd>

### -field <b>Length</b>

<dd>
<p>Specifies the size of the <b>HUB_DEVICE_CONFIG_INFO</b> structure. Must be set by the caller.</p>
</dd>

### -field <b>HubFlags</b>

<dd>
<p>Specifies the hub capabilities in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff539330">USB_HUB_CAP_FLAGS</a> structure.  </p>
</dd>

### -field <b>HardwareIds</b>

<dd>
<p>The PnP hardware ID multi-string for the USB device in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540043">USB_ID_STRING</a> structure. </p>
</dd>

### -field <b>CompatibleIds</b>

<dd>
<p> PnP compatible ID multi-string for the USB device in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540043">USB_ID_STRING</a> structure. </p>
</dd>

### -field <b>DeviceDescription</b>

<dd>
<p>Description of the device in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540043">USB_ID_STRING</a> structure. This may be set to <b>NULL</b>.</p>
</dd>
</dl>

## -remarks
<p>
 The <b>Buffer</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540043">USB_ID_STRING</a> structure points to a string that contains <b>HardwareIds</b>, <b>CompatibleIds</b>, and <b>DeviceDescription</b> values.
The caller is responsible for releasing this string buffer, which is allocated by the hub driver.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows XP and later operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbioctl.h (include Usbioctl.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537252">IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539330">USB_HUB_CAP_FLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540043">USB_ID_STRING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540160">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20HUB_DEVICE_CONFIG_INFO structure%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
