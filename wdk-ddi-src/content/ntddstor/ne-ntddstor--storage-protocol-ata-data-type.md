---
UID: NE.ntddstor._STORAGE_PROTOCOL_ATA_DATA_TYPE
title: STORAGE_PROTOCOL_ATA_DATA_TYPE
author: windows-driver-content
description: The ATA protocol data type.
old-location: storage\storage_protocol_ata_data_type.htm
old-project: storage
ms.assetid: 4B42E143-17F5-4841-A9EA-C225B167E242
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SERIALPERF_STATS, SERIALPERF_STATS, *PSERIALPERF_STATS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddstor.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_PROTOCOL_ATA_DATA_TYPE
req.alt-loc: ntddstor.h
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
---

# STORAGE_PROTOCOL_ATA_DATA_TYPE enumeration



## -description
<p>The ATA protocol data type.</p>


## -syntax

````
typedef enum _STORAGE_PROTOCOL_ATA_DATA_TYPE { 
  AtaDataTypeUnknown   = 0,
  AtaDataTypeIdentify,
  AtaDataTypeLogPage
} STORAGE_PROTOCOL_ATA_DATA_TYPE, *PSTORAGE_PROTOCOL_ATA_DATA_TYPE;
````


## -enum-fields
<dl>

### -field AtaDataTypeUnknown

<dd>
<p>Unknown data type.</p>
</dd>

### -field AtaDataTypeIdentify

<dd>
<p>Identify device data type.</p>
</dd>

### -field AtaDataTypeLogPage

<dd>
<p>Log page data type.</p>
</dd>
</dl>

## -remarks
<p>When using <a href="..\ntddstor\ni-ntddstor-ioctl-storage-query-property.md">IOCTL_STORAGE_QUERY_PROPERTY</a> to retrieve protocol-specific information in the <a href="..\ntddstor\ns-ntddstor--storage-protocol-data-descriptor.md">STORAGE_PROTOCOL_DATA_DESCRIPTOR</a>, configure the <a href="..\ntddstor\ns-ntddstor--storage-property-query.md">STORAGE_PROPERTY_QUERY</a> structure as follows:</p>

<p>Allocate a buffer that can contains both a <a href="..\ntddstor\ns-ntddstor--storage-property-query.md">STORAGE_PROPERTY_QUERY</a> and a <a href="..\ntddstor\ns-ntddstor--storage-protocol-specific-data.md">STORAGE_PROTOCOL_SPECIFIC_DATA</a> structure.</p>

<p>Set the <b>PropertyID</b>  field to <b>StorageAdapterProtocolSpecificProperty</b> or <b>StorageDeviceProtocolSpecificProperty</b> for a controller or device/namespace request, respectively.</p>

<p>Set the <b>QueryType</b>  field to <b>PropertyStandardQuery</b>.</p>

<p>Fill the <a href="..\ntddstor\ns-ntddstor--storage-protocol-specific-data.md">STORAGE_PROTOCOL_SPECIFIC_DATA</a> structure with the desired values. The start of the <b>STORAGE_PROTOCOL_SPECIFIC_DATA</b> is the <b>AdditionalParameters</b> field of <a href="..\ntddstor\ns-ntddstor--storage-property-query.md">STORAGE_PROPERTY_QUERY</a>.</p>

<p>To specify a type of ATA protocol-specific information,  configure the <a href="..\ntddstor\ns-ntddstor--storage-protocol-specific-data.md">STORAGE_PROTOCOL_SPECIFIC_DATA</a> structure as follows:</p>

<p>Set the <b>ProtocolType</b>  field to <b>ProtocolTypeAta</b>.</p>

<p>Set the <b>DataType</b>  field to an enumeration value defined by <b>STORAGE_PROTOCOL_ATA_DATA_TYPE</b>:<ul>
<li>Use <b>AtaDataTypeIdentify</b> to identify the ATA drive.</li>
<li>Use <b>AtaDataTypeLogPage</b> to get log pages from the ATA drive.</li>
</ul>
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Server</p>
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
<dt>Ntddstor.h</dt>
</dl>
</td>
</tr>
</table>