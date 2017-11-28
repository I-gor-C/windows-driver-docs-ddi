---
UID: NE.ucxusbdevice._UCX_USBDEVICE_CHARACTERISTIC_TYPE
title: UCX_USBDEVICE_CHARACTERISTIC_TYPE
author: windows-driver-content
description: Defines values that indicates the type of device characteristic.
old-location: buses\ucx_usbdevice_characteristic_type.htm
old-project: usbref
ms.assetid: 86FA72CC-C23F-40B9-9FDD-80C3B0D5EA73
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: STREAM_INFO, STREAM_INFO, *PSTREAM_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ucxusbdevice.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UCX_USBDEVICE_CHARACTERISTIC_TYPE
req.alt-loc: ucxusbdevice.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# UCX_USBDEVICE_CHARACTERISTIC_TYPE enumeration



## -description
<p>Defines values that indicates the type of device characteristic.</p>


## -syntax

````
typedef enum _UCX_USBDEVICE_CHARACTERISTIC_TYPE { 
  UCX_USBDEVICE_CHARACTERISTIC_TYPE_PATH_DELAY  = 0x01
} UCX_USBDEVICE_CHARACTERISTIC_TYPE, *PUCX_USBDEVICE_CHARACTERISTIC_TYPE;
````


## -enum-fields
<dl>

### -field <a id="UCX_USBDEVICE_CHARACTERISTIC_TYPE_PATH_DELAY"></a><a id="ucx_usbdevice_characteristic_type_path_delay"></a><b>UCX_USBDEVICE_CHARACTERISTIC_TYPE_PATH_DELAY</b>

<dd>
<p>The type of characteristic of the device.</p>
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
<a href="buses.ucx_usbdevice_characteristic">UCX_USBDEVICE_CHARACTERISTIC</a>
</dt>
<dt>
<a href="buses.evt_ucx_usbdevice_get_characteristic">EVT_UCX_USBDEVICE_GET_CHARACTERISTIC</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCX_USBDEVICE_CHARACTERISTIC_TYPE enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
