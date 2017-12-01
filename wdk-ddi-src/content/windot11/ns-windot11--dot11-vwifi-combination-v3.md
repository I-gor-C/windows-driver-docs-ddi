---
UID: NS.windot11._DOT11_VWIFI_COMBINATION_V3
title: DOT11_VWIFI_COMBINATION_V3
author: windows-driver-content
description: The DOT11_VWIFI_COMBINATION_V3 structure contains the combination of MAC entities that an 802.11 wireless miniport driver simultaneously supports when virtualized.
old-location: netvista\dot11_vwifi_combination_v3.htm
old-project: netvista
ms.assetid: 65A397AE-B835-4043-9A81-24055901310B
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: DOT11_VWIFI_COMBINATION_V3,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Windot11.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with   Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_VWIFI_COMBINATION_V3
req.alt-loc: Windot11.h
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

# DOT11_VWIFI_COMBINATION_V3 structure



## -description

## -syntax

````
typedef struct _DOT11_VWIFI_COMBINATION_V3 {
  NDIS_OBJECT_HEADER Header;
  ULONG              uNumInfrastructure;
  ULONG              uNumAdhoc;
  ULONG              uNumSoftAP;
  ULONG              uNumVirtualStation;
  ULONG              uNumWFDGroup;
} DOT11_VWIFI_COMBINATION_V3, *PDOT11_VWIFI_COMBINATION_V3;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>DOT11_VWIFI_COMBINATION_V3</b> structure. The required settings for the members of <b>Header</b> are the following.</p>
<table>
<tr>
<th>Member</th>
<th>Setting</th>
</tr>
<tr>
<td><b>Type</b></td>
<td>NDIS_OBJECT_TYPE_DEFAULT</td>
</tr>
<tr>
<td><b>Revision</b></td>
<td>DOT11_VWIFI_COMBINATION_REVISION_3</td>
</tr>
<tr>
<td><b>Size</b></td>
<td>DOT11_SIZEOF_VWIFI_COMBINATION_REVISION_3</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>uNumInfrastructure</b>

<dd>
<p>The number of 802.11 infrastructure stations supported.</p>
</dd>

### -field <b>uNumAdhoc</b>

<dd>
<p>The number of adhoc stations supported.</p>
</dd>

### -field <b>uNumSoftAP</b>

<dd>
<p>The number of soft access point stations supported.</p>
</dd>

### -field <b>uNumVirtualStation</b>

<dd>
<p>The number of virtual stations supported.</p>
</dd>

### -field <b>uNumWFDGroup</b>

<dd>
<p>The number of simultaneous operational Wi-Fi Direct (WFD) groups supported.</p>
</dd>
</dl>

## -remarks
<p>When <b>uNumWFDGroup</b> &gt; 0, the miniport driver is required to support one more 802.11 MAC entity in addition to the number in <b>uNumWFDGroup</b>. This additional entity is used for WFD device functionality and is the only entity configured as <b>DOT11_OPERATION_MODE_WFD_DEVICE</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p> Supported starting with   Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Windot11.h (include Windot11.h)</dt>
</dl>
</td>
</tr>
</table>