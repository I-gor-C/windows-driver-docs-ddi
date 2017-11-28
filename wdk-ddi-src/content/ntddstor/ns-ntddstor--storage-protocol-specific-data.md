---
UID: NS.ntddstor._STORAGE_PROTOCOL_SPECIFIC_DATA
title: STORAGE_PROTOCOL_SPECIFIC_DATA
author: windows-driver-content
description: Describes protocol-specific device data, provided in the input and output buffer of an IOCTL_STORAGE_QUERY_PROPERTY request.
old-location: storage\storage_protocol_specific_data.htm
old-project: storage
ms.assetid: 74569A0A-5828-4533-8974-4DE0B4EAAAEB
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORAGE_PROTOCOL_SPECIFIC_DATA, STORAGE_PROTOCOL_SPECIFIC_DATA, *PSTORAGE_PROTOCOL_SPECIFIC_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_PROTOCOL_SPECIFIC_DATA
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

# STORAGE_PROTOCOL_SPECIFIC_DATA structure



## -description
<p>Describes  protocol-specific device data, provided in the input and output buffer of an  <a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a> request.</p>


## -syntax

````
typedef struct _STORAGE_PROTOCOL_SPECIFIC_DATA {
  STORAGE_PROTOCOL_TYPE ProtocolType;
  ULONG                 DataType;
  ULONG                 ProtocolDataRequestValue;
  ULONG                 ProtocolDataRequestSubValue;
  ULONG                 ProtocolDataOffset;
  ULONG                 ProtocolDataLength;
  ULONG                 FixedProtocolReturnData;
  ULONG                 Reserved[3];
} STORAGE_PROTOCOL_SPECIFIC_DATA, *PSTORAGE_PROTOCOL_SPECIFIC_DATA;
````


## -struct-fields
<dl>

### -field <b>ProtocolType</b>

<dd>
<p>The protocol type. Values for this member are defined in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn931818">STORAGE_PROTOCOL_TYPE</a> enumeration.</p>
</dd>

### -field <b>DataType</b>

<dd>
<p>The protocol data type. Data types are defined in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn931816">STORAGE_PROTOCOL_NVME_DATA_TYPE</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/dn931813">STORAGE_PROTOCOL_ATA_DATA_TYPE</a> enumerations.</p>
</dd>

### -field <b>ProtocolDataRequestValue</b>

<dd>
<p>The protocol data request value.</p>
</dd>

### -field <b>ProtocolDataRequestSubValue</b>

<dd>
<p>The sub value of the protocol data request.</p>
</dd>

### -field <b>ProtocolDataOffset</b>

<dd>
<p>The offset of the data buffer that is from the beginning of this structure. The typical value can be sizeof(<b>STORAGE_PROTOCOL_SPECIFIC_DATA</b>).</p>
</dd>

### -field <b>ProtocolDataLength</b>

<dd>
<p>The length of the protocol data.</p>
</dd>

### -field <b>FixedProtocolReturnData</b>

<dd>
<p>The returned data.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use.</p>
</dd>
</dl>

## -remarks
<p>When using <a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a> to retrieve protocol-specific information in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn931815">STORAGE_PROTOCOL_DATA_DESCRIPTOR</a>, configure the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566997">STORAGE_PROPERTY_QUERY</a> structure as follows:</p>

<p>Allocate a buffer that can contains both a <a href="https://msdn.microsoft.com/library/windows/hardware/ff566997">STORAGE_PROPERTY_QUERY</a> and a <b>STORAGE_PROTOCOL_SPECIFIC_DATA</b> structure.</p>

<p>Set the <b>PropertyID</b>  field to <b>StorageAdapterProtocolSpecificProperty</b> or <b>StorageDeviceProtocolSpecificProperty</b> for a controller or device/namespace request, respectively.</p>

<p>Set the <b>QueryType</b>  field to <b>PropertyStandardQuery</b>.</p>

<p>Fill the <b>STORAGE_PROTOCOL_SPECIFIC_DATA</b> structure with the desired values. The start of the <b>STORAGE_PROTOCOL_SPECIFIC_DATA</b> is the <b>AdditionalParameters</b> field of <a href="https://msdn.microsoft.com/library/windows/hardware/ff566997">STORAGE_PROPERTY_QUERY</a>.</p>

<p>To specify a type of NVMe protocol-specific information,  configure the <b>STORAGE_PROTOCOL_SPECIFIC_DATA</b> structure as follows:</p>

<p>Set the <b>ProtocolType</b>  field to <b>ProtocolTypeNVMe</b>.</p>

<p>Set the <b>DataType</b>  field to an enumeration value defined by <a href="https://msdn.microsoft.com/library/windows/hardware/dn931816">STORAGE_PROTOCOL_NVME_DATA_TYPE</a>:<ul>
<li>Use <b>NVMeDataTypeIdentify</b> to get Identify Controller data or Identify Namespace data.</li>
<li>Use <b>NVMeDataTypeLogPage</b> to get log pages (including SMART/health data).</li>
<li>Use <b>NVMeDataTypeFeature</b> to get features of the NVMe drive.</li>
</ul>
</p>

<p>To specify a type of ATA protocol-specific information,  configure the <b>STORAGE_PROTOCOL_SPECIFIC_DATA</b> structure as follows:</p>

<p>Set the <b>ProtocolType</b>  field to <b>ProtocolTypeAta</b>.</p>

<p>Set the <b>DataType</b>  field to an enumeration value defined by <a href="https://msdn.microsoft.com/library/windows/hardware/dn931813">STORAGE_PROTOCOL_ATA_DATA_TYPE</a>:<ul>
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
<dt>Ntddstor.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566997">STORAGE_PROPERTY_QUERY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566996">STORAGE_PROPERTY_ID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn931817">STORAGE_PROTOCOL_SPECIFIC_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20STORAGE_PROTOCOL_SPECIFIC_DATA structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
