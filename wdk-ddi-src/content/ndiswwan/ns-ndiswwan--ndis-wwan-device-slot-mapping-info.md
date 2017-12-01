---
UID: NS.ndiswwan._NDIS_WWAN_DEVICE_SLOT_MAPPING_INFO
title: NDIS_WWAN_DEVICE_SLOT_MAPPING_INFO
author: windows-driver-content
description: The NDIS_WWAN_DEVICE_SLOT_MAPPING_INFO structure represents the executor-to-slot mapping relationship of the MB device.
old-location: netvista\ndis_wwan_device_slot_mappings.htm
old-project: netvista
ms.assetid: 18437B56-B84C-499B-8D4F-F65B5B8221A6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_WWAN_DEVICE_SLOT_MAPPING_INFO, NDIS_WWAN_DEVICE_SLOT_MAPPING_INFO, *PNDIS_WWAN_DEVICE_SLOT_MAPPING_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndiswwan.h
req.include-header: Ndiswwan.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1703
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_WWAN_DEVICE_SLOT_MAPPING_INFO
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

# NDIS_WWAN_DEVICE_SLOT_MAPPING_INFO structure



## -description
<p>The <b>NDIS_WWAN_DEVICE_SLOT_MAPPING_INFO</b> structure represents the executor-to-slot mapping relationship of the MB device.</p>


## -syntax

````
typedef struct _NDIS_WWAN_DEVICE_SLOT_MAPPING_INFO {
  NDIS_OBJECT_HEADER            Header;
  WWAN_STATUS                   uStatus;
  WWAN_DEVICE_SLOT_MAPPING_INFO DeviceSlotMappings;
} NDIS_WWAN_DEVICE_SLOT_MAPPING_INFO, *PNDIS_WWAN_DEVICE_SLOT_MAPPING_INFO;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header with type, revision, and size information about the <b>NDIS_WWAN_DEVICE_SLOT_MAPPING_INFO</b> structure.
     The MB Service sets the header with the values that are shown in the following table when it sends the
     data structure to the miniport driver for 
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
<p>NDIS_WWAN_DEVICE_SLOT_MAPPING_INFO_REVISION_1</p>
</td>
</tr>
<tr>
<td>
<p>Size</p>
</td>
<td>
<p>sizeof(NDIS_WWAN_DEVICE_SLOT_MAPPING_INFO)</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information about these members, see 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>uStatus</b>

<dd>
<p>The system capability status. The following table shows the possible values for
     this member.
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WWAN_STATUS_SUCCESS</p>
</td>
<td>
<p>The operation succeeded.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_BUSY</p>
</td>
<td>
<p>The operation failed because the device was busy. In the absence of any explicit information from the function to clear this condition, the host can use subsequent actions by the function (e.g. notifications or command completions) as a hint to retry the failed operation.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_FAILURE</p>
</td>
<td>
<p>The operation failed.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_INVALID_PARAMETERS</p>
</td>
<td>
<p>The operation failed because of invalid parameters (e.g. slot numbers out of range or duplicated values in the mapping).</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_NO_DEVICE_SUPPORT</p>
</td>
<td>
<p>The operation failed because the device does not support this OID.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>DeviceSlotMappings</b>

<dd>
<p>A formatted <a href="..\wwan\ns-wwan--wwan-device-slot-mapping-info.md">WWAN_DEVICE_SLOT_MAPPING_INFO</a> structure that represents the executor-to-slot mapping relationship of the MB device.</p>
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
<p>Windows 10, version 1703</p>
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
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-device-slot-mapping-info.md">WWAN_DEVICE_SLOT_MAPPING_INFO</a>
</dt>
<dt>
<a href="netvista.oid_wwan_device_slot_mappings">OID_WWAN_DEVICE_SLOT_MAPPING_INFO</a>
</dt>
<dt>
<a href="netvista.ndis_status_wwan_device_slot_mappings">NDIS_STATUS_WWAN_DEVICE_SLOT_MAPPING_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WWAN_DEVICE_SLOT_MAPPING_INFO structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
