---
UID: NS.ndiswwan._NDIS_WWAN_SUPPORTED_DEVICE_SERVICES
title: NDIS_WWAN_SUPPORTED_DEVICE_SERVICES
author: windows-driver-content
description: The NDIS_WWAN_SUPPORTED_DEVICE_SERVICES structure describes a list of supported device services.
old-location: netvista\ndis_wwan_supported_device_services.htm
old-project: netvista
ms.assetid: C94C4426-A487-422D-B84E-B29C2AD7BF0C
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_WWAN_SUPPORTED_DEVICE_SERVICES, NDIS_WWAN_SUPPORTED_DEVICE_SERVICES, *PNDIS_WWAN_SUPPORTED_DEVICE_SERVICES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndiswwan.h
req.include-header: Ndiswwan.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_WWAN_SUPPORTED_DEVICE_SERVICES
req.alt-loc: ndiswwan.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NDIS_WWAN_SUPPORTED_DEVICE_SERVICES structure



## -description
<p>The NDIS_WWAN_SUPPORTED_DEVICE_SERVICES structure describes a list of supported device services.</p>


## -syntax

````
typedef struct _NDIS_WWAN_SUPPORTED_DEVICE_SERVICES {
  NDIS_OBJECT_HEADER             Header;
  WWAN_STATUS                    uStatus;
  WWAN_SUPPORTED_DEVICE_SERVICES DeviceServices;
} NDIS_WWAN_SUPPORTED_DEVICE_SERVICES, *PNDIS_WWAN_SUPPORTED_DEVICE_SERVICES;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header with type, revision, and size information about the NDIS_WWAN_SUPPORTED_DEVICE_SERVICES
     structure. The MB Service sets the header with the values that are shown in the following table when it
     sends the data structure to the miniport driver for 
     <i>set</i> operations. Miniport drivers must set the header with the same values when they send the data
     structure to the MB service.
     </p>
<table>
<tr>
<th>Header submember</th>
<th>Value</th>
</tr>
<tr>
<td>
<p>Type</p>
</td>
<td>
<p>NDIS_OBJECT_TYPE_DEFAULT</p>
</td>
</tr>
<tr>
<td>
<p>Revision</p>
</td>
<td>
<p>NDIS_WWAN_SUPPORTED_DEVICE_SERVICES_REVISION_1</p>
</td>
</tr>
<tr>
<td>
<p>Size</p>
</td>
<td>
<p>sizeof(NDIS_WWAN_SUPPORTED_DEVICE_SERVICES)</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information about these members, see 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>uStatus</b>

<dd>
<p>The status of the device services query operation.</p>
</dd>

### -field <b>DeviceServices</b>

<dd>
<p>This member points to the list of the <a href="..\wwan\ns-wwan--wwan-supported-device-services.md">WWAN_SUPPORTED_DEVICE_SERVICES</a> structure that represents the list of supported device services and information about themby using the WWAN_LIST_HEADER structure</p>
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
<p>Supported starting with  Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndiswwan.h (include Ndiswwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wwan\ns-wwan--wwan-supported-device-services.md">WWAN_SUPPORTED_DEVICE_SERVICES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WWAN_SUPPORTED_DEVICE_SERVICES structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
