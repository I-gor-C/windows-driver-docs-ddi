---
UID : NE:ntddstor._STORAGE_PROTOCOL_ATA_DATA_TYPE
title : _STORAGE_PROTOCOL_ATA_DATA_TYPE
author : windows-driver-content
description : The ATA protocol data type.
old-location : storage\storage_protocol_ata_data_type.htm
old-project : storage
ms.assetid : 4B42E143-17F5-4841-A9EA-C225B167E242
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _STORAGE_PROTOCOL_ATA_DATA_TYPE, *PSTORAGE_PROTOCOL_ATA_DATA_TYPE, STORAGE_PROTOCOL_ATA_DATA_TYPE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ntddstor.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : STORAGE_PROTOCOL_ATA_DATA_TYPE
req.alt-loc : ntddstor.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PSTORAGE_PROTOCOL_ATA_DATA_TYPE, STORAGE_PROTOCOL_ATA_DATA_TYPE"
---

# _STORAGE_PROTOCOL_ATA_DATA_TYPE Enumeration
The ATA protocol data type.

## Syntax
````
typedef enum _STORAGE_PROTOCOL_ATA_DATA_TYPE { 
  AtaDataTypeUnknown   = 0,
  AtaDataTypeIdentify,
  AtaDataTypeLogPage
} STORAGE_PROTOCOL_ATA_DATA_TYPE, *PSTORAGE_PROTOCOL_ATA_DATA_TYPE;
````

## Constants

<table>

<tr>
<td>AtaDataTypeIdentify</td>
<td>Identify device data type.</td>
</tr>

<tr>
<td>AtaDataTypeLogPage</td>
<td>Log page data type.</td>
</tr>

<tr>
<td>AtaDataTypeUnknown</td>
<td>Unknown data type.</td>
</tr>
</table>

## Remarks

When using <a href="..\ntddstor\ni-ntddstor-ioctl_storage_query_property.md">IOCTL_STORAGE_QUERY_PROPERTY</a> to retrieve protocol-specific information in the <a href="..\ntddstor\ns-ntddstor-_storage_protocol_data_descriptor.md">STORAGE_PROTOCOL_DATA_DESCRIPTOR</a>, configure the <a href="..\ntddstor\ns-ntddstor-_storage_property_query.md">STORAGE_PROPERTY_QUERY</a> structure as follows:

Allocate a buffer that can contains both a <a href="..\ntddstor\ns-ntddstor-_storage_property_query.md">STORAGE_PROPERTY_QUERY</a> and a <a href="..\ntddstor\ns-ntddstor-_storage_protocol_specific_data.md">STORAGE_PROTOCOL_SPECIFIC_DATA</a> structure.

Set the <b>PropertyID</b>  field to <b>StorageAdapterProtocolSpecificProperty</b> or <b>StorageDeviceProtocolSpecificProperty</b> for a controller or device/namespace request, respectively.

Set the <b>QueryType</b>  field to <b>PropertyStandardQuery</b>.

Fill the <a href="..\ntddstor\ns-ntddstor-_storage_protocol_specific_data.md">STORAGE_PROTOCOL_SPECIFIC_DATA</a> structure with the desired values. The start of the <b>STORAGE_PROTOCOL_SPECIFIC_DATA</b> is the <b>AdditionalParameters</b> field of <a href="..\ntddstor\ns-ntddstor-_storage_property_query.md">STORAGE_PROPERTY_QUERY</a>.

To specify a type of ATA protocol-specific information,  configure the <a href="..\ntddstor\ns-ntddstor-_storage_protocol_specific_data.md">STORAGE_PROTOCOL_SPECIFIC_DATA</a> structure as follows:

Set the <b>ProtocolType</b>  field to <b>ProtocolTypeAta</b>.

Set the <b>DataType</b>  field to an enumeration value defined by <b>STORAGE_PROTOCOL_ATA_DATA_TYPE</b>:<ul>
<li>Use <b>AtaDataTypeIdentify</b> to identify the ATA drive.</li>
<li>Use <b>AtaDataTypeLogPage</b> to get log pages from the ATA drive.</li>
</ul>
</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddstor.h |