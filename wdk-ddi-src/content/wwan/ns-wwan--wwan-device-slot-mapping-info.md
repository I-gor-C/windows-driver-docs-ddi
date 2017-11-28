---
UID: NS.wwan._WWAN_DEVICE_SLOT_MAPPING_INFO
title: WWAN_DEVICE_SLOT_MAPPING_INFO
author: windows-driver-content
description: The WWAN_DEVICE_SLOT_MAPPING_INFO structure represents the executor-to-slot mapping relationship in the MB device.
old-location: netvista\wwan_device_slot_mappings.htm
old-project: netvista
ms.assetid: 48DD867C-1235-4955-A01E-FF46C850DA31
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WWAN_DEVICE_SLOT_MAPPING_INFO, WWAN_DEVICE_SLOT_MAPPING_INFO, *PWWAN_DEVICE_SLOT_MAPPING_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1703
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_DEVICE_SLOT_MAPPING_INFO
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

# WWAN_DEVICE_SLOT_MAPPING_INFO structure



## -description
<p>The WWAN_DEVICE_SLOT_MAPPING_INFO structure represents the executor-to-slot mapping relationship in the MB device.</p>


## -syntax

````
typedef struct _WWAN_DEVICE_SLOT_MAPPING_INFO {
  ULONG            MapCount;
  WWAN_LIST_HEADER SlotMapList;
} WWAN_DEVICE_SLOT_MAPPING_INFO, *PWWAN_DEVICE_SLOT_MAPPING_INFO;
````


## -struct-fields
<dl>

### -field <b>MapCount</b>

<dd>
<p>The number of mappings, which is always equal to the number of executors.</p>
</dd>

### -field <b>SlotMapList</b>

<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571208">WWAN_LIST_HEADER</a> has a new structure, <b>WwanStructSlotIndex</b>, which represents the slot index the <i>i-th</i> executor is mapped to (where 0 &lt;= i &lt;= (MapCount -1)).</p>
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
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndiswwan\ns-ndiswwan--ndis-wwan-set-device-slot-mapping-info.md">NDIS_WWAN_SET_DEVICE_SLOT_MAPPING_INFO</a>
</dt>
<dt>
<a href="..\ndiswwan\ns-ndiswwan--ndis-wwan-device-slot-mapping-info.md">NDIS_WWAN_DEVICE_SLOT_MAPPING_INFO</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_DEVICE_SLOT_MAPPING_INFO structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
