---
UID: NS.ndiswwan._NDIS_WWAN_BASE_STATIONS_INFO
title: NDIS_WWAN_BASE_STATIONS_INFO
author: windows-driver-content
description: The NDIS_WWAN_BASE_STATIONS_INFO structure contains information about both serving and neighboring base stations.
old-location: netvista\ndis_wwan_base_stations_info.htm
old-project: netvista
ms.assetid: 7C0E0903-F564-4F2B-95F9-FA8512FEF61B
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_WWAN_BASE_STATIONS_INFO, NDIS_WWAN_BASE_STATIONS_INFO, *PNDIS_WWAN_BASE_STATIONS_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndiswwan.h
req.include-header: Ndiswwan.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_WWAN_BASE_STATIONS_INFO
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

# NDIS_WWAN_BASE_STATIONS_INFO structure



## -description
<p>The <b>NDIS_WWAN_BASE_STATIONS_INFO</b> structure contains information about both serving and neighboring base stations. It is used in the <a href="https://docs.microsoft.com/windows-hardware/drivers/network/ndis-status-wwan-base-stations-info">NDIS_STATUS_WWAN_BASE_STATIONS_INFO</a> status notification in response to a previous <a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-base-stations-info">OID_WWAN_BASE_STATIONS_INFO</a> query request.</p>


## -syntax

````
typedef struct _NDIS_WWAN_BASE_STATIONS_INFO {
  NDIS_OBJECT_HEADER      Header;
  WWAN_STATUS             uStatus;
  WWAN_BASE_STATIONS_INFO BaseStationsInfo;
} NDIS_WWAN_BASE_STATIONS_INFO, *PNDIS_WWAN_BASE_STATIONS_INFO;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header with type, revision, and size information about the <b>NDIS_WWAN_BASE_STATIONS_INFO</b> structure.
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
<p>NDIS_WWAN_BASE_STATIONS_INFO_REVISION_1</p>
</td>
</tr>
<tr>
<td>
<p>Size</p>
</td>
<td>
<p>sizeof(NDIS_WWAN_BASE_STATIONS_INFO)</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information about these members, see 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>uStatus</b>

<dd>
<p>The status of system capability. The following table shows the possible values for
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
<p>WWAN_STATUS_NO_DEVICE_SUPPORT</p>
</td>
<td>
<p>The operation failed because the device does not support this OID.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>BaseStationsInfo</b>

<dd>
<p>A formatted <a href="..\wwan\ns-wwan--wwan-base-stations-info.md">WWAN_BASE_STATIONS_INFO</a> structure that represents information about both serving and neighboring base stations.</p>
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
<p>Windows 10, version 1709</p>
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
<a href="https://docs.microsoft.com/windows-hardware/drivers/network/ndis-status-wwan-base-stations-info">NDIS_STATUS_WWAN_BASE_STATIONS_INFO</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-base-stations-info">OID_WWAN_BASE_STATIONS_INFO</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-base-stations-info.md">WWAN_BASE_STATIONS_INFO</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/windows-hardware/drivers/network/mb-base-stations-information-query-support">MB base stations information query support</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WWAN_BASE_STATIONS_INFO structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
