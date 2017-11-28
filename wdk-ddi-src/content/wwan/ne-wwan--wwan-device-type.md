---
UID: NE.wwan._WWAN_DEVICE_TYPE
title: WWAN_DEVICE_TYPE
author: windows-driver-content
description: The WWAN_DEVICE_TYPE enumeration lists the different device types that describe the MB device.
old-location: netvista\wwan_device_type.htm
old-project: netvista
ms.assetid: ad99b2b0-d62a-4e3e-a368-b9109f0fefb4
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_DEVICE_TYPE
req.alt-loc: wwan.h
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

# WWAN_DEVICE_TYPE enumeration



## -description
<p>The WWAN_DEVICE_TYPE enumeration lists the different device types that describe the MB device.</p>


## -syntax

````
typedef enum _WWAN_DEVICE_TYPE { 
  WwanDeviceTypeUnknown    = 0,
  WwanDeviceTypeEmbedded,
  WwanDeviceTypeRemovable,
  WwanDeviceTypeRemote,
  WwanDeviceTypeMax
} WWAN_DEVICE_TYPE, *PWWAN_DEVICE_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WwanDeviceTypeUnknown"></a><a id="wwandevicetypeunknown"></a><a id="WWANDEVICETYPEUNKNOWN"></a><b>WwanDeviceTypeUnknown</b>

<dd>
<p>The device type is unknown.</p>
</dd>

### -field <a id="WwanDeviceTypeEmbedded"></a><a id="wwandevicetypeembedded"></a><a id="WWANDEVICETYPEEMBEDDED"></a><b>WwanDeviceTypeEmbedded</b>

<dd>
<p>The device type is embedded in the system.</p>
</dd>

### -field <a id="WwanDeviceTypeRemovable"></a><a id="wwandevicetyperemovable"></a><a id="WWANDEVICETYPEREMOVABLE"></a><b>WwanDeviceTypeRemovable</b>

<dd>
<p>The device type is removable.</p>
</dd>

### -field <a id="WwanDeviceTypeRemote"></a><a id="wwandevicetyperemote"></a><a id="WWANDEVICETYPEREMOTE"></a><b>WwanDeviceTypeRemote</b>

<dd>
<p>The device type is remote. For example, a tethered cellular phone modem.</p>
</dd>

### -field <a id="WwanDeviceTypeMax"></a><a id="wwandevicetypemax"></a><a id="WWANDEVICETYPEMAX"></a><b>WwanDeviceTypeMax</b>

<dd>
<p>The total number of supported device types.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571204">WWAN_DEVICE_CAPS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_DEVICE_TYPE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
