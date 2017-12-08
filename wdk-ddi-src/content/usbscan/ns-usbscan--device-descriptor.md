---
UID: NS.usbscan._DEVICE_DESCRIPTOR
title: DEVICE_DESCRIPTOR
author: windows-driver-content
description: The DEVICE_DESCRIPTOR structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_GET_DEVICE_DESCRIPTOR.
old-location: image\device_descriptor.htm
old-project: image
ms.assetid: 15ad337a-0b33-48ba-98cf-6aff2698e2ba
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DEVICE_DESCRIPTOR, DEVICE_DESCRIPTOR, *PDEVICE_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbscan.h
req.include-header: Usbscan.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEVICE_DESCRIPTOR
req.alt-loc: usbscan.h
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

# DEVICE_DESCRIPTOR structure



## -description
<p>The DEVICE_DESCRIPTOR structure is used as a parameter to <a href="base.deviceiocontrol">DeviceIoControl</a>, when the specified I/O control code is <a href="..\usbscan\ni-usbscan-ioctl-get-device-descriptor.md">IOCTL_GET_DEVICE_DESCRIPTOR</a>.</p>


## -syntax

````
typedef struct _DEVICE_DESCRIPTOR {
  USHORT usVendorId;
  USHORT usProductId;
  USHORT usBcdDevice;
  USHORT usLanguageId;
} DEVICE_DESCRIPTOR, *PDEVICE_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field usVendorId

<dd>
<p>Vendor identifier.</p>
</dd>

### -field usProductId

<dd>
<p>Device product identifier.</p>
</dd>

### -field usBcdDevice

<dd>
<p>BCD-encoded device version number.</p>
</dd>

### -field usLanguageId

<dd>
<p><i>Not used</i>.</p>
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
<dt>Usbscan.h (include Usbscan.h)</dt>
</dl>
</td>
</tr>
</table>