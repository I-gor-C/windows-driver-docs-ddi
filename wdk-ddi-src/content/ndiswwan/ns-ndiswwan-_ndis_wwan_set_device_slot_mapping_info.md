---
UID: NS.NDISWWAN._NDIS_WWAN_SET_DEVICE_SLOT_MAPPING_INFO
title: _NDIS_WWAN_SET_DEVICE_SLOT_MAPPING_INFO
author: windows-driver-content
description: The NDIS_WWAN_SET_DEVICE_SLOT_MAPPING_INFO structure sets the executor-to-slot mapping relationship of the MB device.
old-location: netvista\ndis_wwan_set_device_slot_mappings.htm
old-project: netvista
ms.assetid: 5DAE5A36-1A2B-46DF-8CF1-FAC8B98460A8
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _NDIS_WWAN_SET_DEVICE_SLOT_MAPPING_INFO, NDIS_WWAN_SET_DEVICE_SLOT_MAPPING_INFO, *PNDIS_WWAN_SET_DEVICE_SLOT_MAPPING_INFO
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
req.alt-api: NDIS_WWAN_SET_DEVICE_SLOT_MAPPING_INFO
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
---

# _NDIS_WWAN_SET_DEVICE_SLOT_MAPPING_INFO structure



## -description
The <b>NDIS_WWAN_SET_DEVICE_SLOT_MAPPING_INFO</b> structure sets the executor-to-slot mapping relationship of the MB device.



## -syntax

````
typedef struct _NDIS_WWAN_SET_DEVICE_SLOT_MAPPING_INFO {
  NDIS_OBJECT_HEADER            Header;
  WWAN_DEVICE_SLOT_MAPPING_INFO DeviceSlotMappings;
} NDIS_WWAN_SET_DEVICE_SLOT_MAPPING_INFO, *PNDIS_WWAN_SET_DEVICE_SLOT_MAPPING_INFO;
````


## -struct-fields

### -field Header

The header with type, revision, and size information about the <b>NDIS_WWAN_SET_DEVICE_SLOT_MAPPINGS</b> structure.
     The MB Service sets the header with the values that are shown in the following table when it sends the
     data structure to the miniport driver for 
     <i>set</i> operations. Miniport drivers must set the header with the same values when they send the data
     structure to the MB service.
     

<table>
<tr>
<th>Header submember</th>
<th>Value</th>
</tr>
<tr>
<td>
Type

</td>
<td>
NDIS_OBJECT_TYPE_DEFAULT

</td>
</tr>
<tr>
<td>
Revision

</td>
<td>
NDIS_WWAN_SET_DEVICE_SLOT_MAPPING_INFO_REVISION_1

</td>
</tr>
<tr>
<td>
Size

</td>
<td>
sizeof(NDIS_WWAN_SET_DEVICE_SLOT_MAPPING_INFO)

</td>
</tr>
</table>
 

For more information about these members, see 
     <a href="netvista.ndis_object_header">NDIS_OBJECT_HEADER</a>.


### -field DeviceSlotMappings

A formatted <a href="netvista.wwan_device_slot_mappings">WWAN_DEVICE_SLOT_MAPPING_INFO</a> structure that represents the executor-to-slot mapping relationship of the MB device.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Windows 10, version 1703

</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="netvista.ndis_object_header">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="netvista.wwan_device_slot_mappings">WWAN_DEVICE_SLOT_MAPPING_INFO</a>
</dt>
<dt>
<a href="netvista.oid_wwan_device_slot_mappings">OID_WWAN_DEVICE_SLOT_MAPPING_INFO</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WWAN_SET_DEVICE_SLOT_MAPPING_INFO structure%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

