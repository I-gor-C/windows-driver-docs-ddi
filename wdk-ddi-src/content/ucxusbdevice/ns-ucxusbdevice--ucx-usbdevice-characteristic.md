---
UID: NS.ucxusbdevice._UCX_USBDEVICE_CHARACTERISTIC
title: UCX_USBDEVICE_CHARACTERISTIC
author: windows-driver-content
description: Stores the characteristics of an device.
old-location: buses\ucx_usbdevice_characteristic.htm
old-project: usbref
ms.assetid: 31BF5607-51EA-4FBF-A754-872FBD45915D
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCX_USBDEVICE_CHARACTERISTIC, UCX_USBDEVICE_CHARACTERISTIC, *PUCX_USBDEVICE_CHARACTERISTIC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxusbdevice.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UCX_USBDEVICE_CHARACTERISTIC
req.alt-loc: Ucxusbdevice.h
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

# UCX_USBDEVICE_CHARACTERISTIC structure



## -description
<p>Stores the characteristics of an device. </p>


## -syntax

````
typedef struct _UCX_USBDEVICE_CHARACTERISTIC {
  ULONG                             Size;
  UCX_USBDEVICE_CHARACTERISTIC_TYPE CharacteristicType;
  union {
    UCX_USBDEVICE_CHARACTERISTIC_PATH_DELAY PathDelay;
  };
} UCX_USBDEVICE_CHARACTERISTIC, *PUCX_USBDEVICE_CHARACTERISTIC;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Size of this structure.</p>
</dd>

### -field <b>CharacteristicType</b>

<dd>
<p>A <a href="buses.ucx_usbdevice_characteristic_type">UCX_USBDEVICE_CHARACTERISTIC_TYPE</a>-type value that indicates the type of device characteristic.</p>
</dd>

### -field <b>PathDelay</b>

<dd>
<p>A <a href="buses.ucx_usbdevice_characteristic_path_delay">UCX_USBDEVICE_CHARACTERISTIC_PATH_DELAY</a>-typed value that indicates the path delay values for the endpoint.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ucxusbdevice.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.evt_ucx_usbdevice_get_characteristic">EVT_UCX_USBDEVICE_GET_CHARACTERISTIC</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCX_USBDEVICE_CHARACTERISTIC structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
