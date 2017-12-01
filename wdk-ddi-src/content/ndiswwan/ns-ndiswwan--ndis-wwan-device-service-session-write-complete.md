---
UID: NS.ndiswwan._NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE
title: NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE
author: windows-driver-content
description: The NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE structure represents the status of a device service session write operation.
old-location: netvista\ndis_wwan_device_service_session_write_complete.htm
old-project: netvista
ms.assetid: 16A48882-BEA6-4F95-8E9F-572BFD102031
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE, NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE, *PNDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE
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
req.alt-api: NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE
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

# NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE structure



## -description
<p>The NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE structure represents the status of a device service session write operation.</p>


## -syntax

````
typedef struct _NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE {
  NDIS_OBJECT_HEADER Header;
  WWAN_STATUS        uStatus;
} NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE, *PNDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header with type, revision, and size information about the NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE
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
<p>NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE_REVISION_1</p>
</td>
</tr>
<tr>
<td>
<p>Size</p>
</td>
<td>
<p>sizeof(NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE)</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information about these members, see 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>uStatus</b>

<dd>
<p>The status of the completion of the write operation.</p>
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