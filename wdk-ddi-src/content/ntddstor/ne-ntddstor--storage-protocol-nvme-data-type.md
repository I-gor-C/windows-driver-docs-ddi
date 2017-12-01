---
UID: NE.ntddstor._STORAGE_PROTOCOL_NVME_DATA_TYPE
title: STORAGE_PROTOCOL_NVME_DATA_TYPE
author: windows-driver-content
description: Describes the type of NVMe protocol-specific data that's to be queried during an IOCTL_STORAGE_QUERY_PROPERTY request.
old-location: storage\storage_protocol_nvme_data_type.htm
old-project: storage
ms.assetid: 02DB004B-F5B9-4CA2-9CA8-9C7BFB9BA5CD
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SERIALPERF_STATS, SERIALPERF_STATS, *PSERIALPERF_STATS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_PROTOCOL_NVME_DATA_TYPE
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

# STORAGE_PROTOCOL_NVME_DATA_TYPE enumeration



## -description
<p>Describes  the type of NVMe protocol-specific data that's to be queried during an <a href="..\ntddstor\ni-ntddstor-ioctl-storage-query-property.md">IOCTL_STORAGE_QUERY_PROPERTY</a> request.</p>


## -syntax

````
typedef enum _STORAGE_PROTOCOL_NVME_DATA_TYPE { 
  NVMeDataTypeUnknown   = 0,
  NVMeDataTypeIdentify,
  NVMeDataTypeLogPage,
  NVMeDataTypeFeature
} STORAGE_PROTOCOL_NVME_DATA_TYPE, *PSTORAGE_PROTOCOL_NVME_DATA_TYPE;
````


## -enum-fields
<dl>

### -field <a id="NVMeDataTypeUnknown"></a><a id="nvmedatatypeunknown"></a><a id="NVMEDATATYPEUNKNOWN"></a><b>NVMeDataTypeUnknown</b>

<dd>
<p>Unknown data type.</p>
</dd>

### -field <a id="NVMeDataTypeIdentify"></a><a id="nvmedatatypeidentify"></a><a id="NVMEDATATYPEIDENTIFY"></a><b>NVMeDataTypeIdentify</b>

<dd>
<p>Identify data type. This can be either Identify Controller data or Identify Namespace data. When this type of data is being queried, the ProtocolDataRequestValue field of <a href="..\ntddstor\ns-ntddstor--storage-protocol-specific-data.md">STORAGE_PROTOCOL_SPECIFIC_DATA</a> will have a value of <b>NVME_IDENTIFY_CNS_CONTROLLER</b> for adapter or <b>NVME_IDENTIFY_CNS_SPECIFIC_NAMESPACE</b> for namespace. If the ProtocolDataRequestValue is <b>NVME_IDENTIFY_CNS_SPECIFIC_NAMESPACE</b>, the ProtocolDataRequestSubValue field from the <b>STORAGE_PROTOCOL_SPECIFIC_DATA</b> structure will have a value of the namespace ID.</p>
</dd>

### -field <a id="NVMeDataTypeLogPage"></a><a id="nvmedatatypelogpage"></a><a id="NVMEDATATYPELOGPAGE"></a><b>NVMeDataTypeLogPage</b>

<dd>
<p>Log page data type.</p>
</dd>

### -field <a id="NVMeDataTypeFeature"></a><a id="nvmedatatypefeature"></a><a id="NVMEDATATYPEFEATURE"></a><b>NVMeDataTypeFeature</b>

<dd>
<p>Feature data type.</p>
</dd>
</dl>

## -remarks
<p>When using <a href="..\ntddstor\ni-ntddstor-ioctl-storage-query-property.md">IOCTL_STORAGE_QUERY_PROPERTY</a> to retrieve protocol-specific information in the <a href="..\ntddstor\ns-ntddstor--storage-protocol-data-descriptor.md">STORAGE_PROTOCOL_DATA_DESCRIPTOR</a>, configure the <a href="..\ntddstor\ns-ntddstor--storage-property-query.md">STORAGE_PROPERTY_QUERY</a> structure as follows:</p>

<p>Allocate a buffer that can contains both a <a href="..\ntddstor\ns-ntddstor--storage-property-query.md">STORAGE_PROPERTY_QUERY</a> and a <a href="..\ntddstor\ns-ntddstor--storage-protocol-specific-data.md">STORAGE_PROTOCOL_SPECIFIC_DATA</a> structure.</p>

<p>Set the <b>PropertyID</b>  field to <b>StorageAdapterProtocolSpecificProperty</b> or <b>StorageDeviceProtocolSpecificProperty</b> for a controller or device/namespace request, respectively.</p>

<p>Set the <b>QueryType</b>  field to <b>PropertyStandardQuery</b>.</p>

<p>Fill the <a href="..\ntddstor\ns-ntddstor--storage-protocol-specific-data.md">STORAGE_PROTOCOL_SPECIFIC_DATA</a> structure with the desired values. The start of the <b>STORAGE_PROTOCOL_SPECIFIC_DATA</b> is the <b>AdditionalParameters</b> field of <a href="..\ntddstor\ns-ntddstor--storage-property-query.md">STORAGE_PROPERTY_QUERY</a>.</p>

<p>To specify a type of NVMe protocol-specific information,  configure the <a href="..\ntddstor\ns-ntddstor--storage-protocol-specific-data.md">STORAGE_PROTOCOL_SPECIFIC_DATA</a> structure as follows:</p>

<p>Set the <b>ProtocolType</b>  field to <b>ProtocolTypeNVMe</b>.</p>

<p>Set the <b>DataType</b>  field to an enumeration value defined by <b>STORAGE_PROTOCOL_NVME_DATA_TYPE</b>:<ul>
<li>Use <b>NVMeDataTypeIdentify</b> to get Identify Controller data or Identify Namespace data.</li>
<li>Use <b>NVMeDataTypeLogPage</b> to get log pages (including SMART/health data).</li>
<li>Use <b>NVMeDataTypeFeature</b> to get features of the NVMe drive.</li>
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
<dt>Ntddstor.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddstor\ni-ntddstor-ioctl-storage-query-property.md">IOCTL_STORAGE_QUERY_PROPERTY</a>
</dt>
<dt>
<a href="..\ntddstor\ns-ntddstor--storage-property-query.md">STORAGE_PROPERTY_QUERY</a>
</dt>
<dt>
<a href="storage.storage_property_id">STORAGE_PROPERTY_ID</a>
</dt>
<dt>
<a href="..\ntddstor\ns-ntddstor--storage-protocol-specific-data.md">STORAGE_PROTOCOL_SPECIFIC_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20STORAGE_PROTOCOL_NVME_DATA_TYPE enumeration%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
