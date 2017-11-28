---
UID: NS.ucxcontroller._UCXUSBDEVICE_INFO
title: UCXUSBDEVICE_INFO
author: windows-driver-content
description: Contains information about the USB device. This structure is passed by UCX in the EVT_UCX_CONTROLLER_USBDEVICE_ADD event callback function.
old-location: buses\_ucxusbdevice_info.htm
old-project: usbref
ms.assetid: E6875195-D6C4-4CEB-8381-8CBA732223A5
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCXUSBDEVICE_INFO,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxcontroller.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UCXUSBDEVICE_INFO
req.alt-loc: Ucxcontroller.h
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
req.iface: 
req.product: Windows 10 or later.
---

# UCXUSBDEVICE_INFO structure



## -description
<p>Contains information about the USB device. This structure is passed by UCX in the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187823">EVT_UCX_CONTROLLER_USBDEVICE_ADD</a> event callback function.</p>


## -syntax

````
typedef struct _UCXUSBDEVICE_INFO {
  ULONG                Size;
  USB_DEVICE_SPEED     DeviceSpeed;
  UCXUSBDEVICE         TtHub;
  USB_DEVICE_PORT_PATH PortPath;
} UCXUSBDEVICE_INFO, *P_UCXUSBDEVICE_INFO;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size in bytes of this structure.</p>
</dd>

### -field <b>DeviceSpeed</b>

<dd>
<p>Defines the device speed of the USB device or hub.</p>
</dd>

### -field <b>TtHub</b>

<dd>
<p>A handle to the USB  device object that represents the TT hub.</p>
</dd>

### -field <b>PortPath</b>

<dd>
<p>The port path for the USB device or hub.</p>
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
<dt>Ucxcontroller.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt187823">EVT_UCX_CONTROLLER_USBDEVICE_ADD</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCXUSBDEVICE_INFO structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
