---
UID: NS.ntddstor._STORAGE_TEMPERATURE_DATA_DESCRIPTOR
title: STORAGE_TEMPERATURE_DATA_DESCRIPTOR
author: windows-driver-content
description: This structure is used in conjunction with IOCTL_STORAGE_QUERY_PROPERTY to return temperature data from a storage device or adapter.
old-location: storage\storage_temperature_data_descriptor.htm
old-project: storage
ms.assetid: A6041B10-0296-4A96-B65C-C35B8DCB2B5D
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORAGE_TEMPERATURE_DATA_DESCRIPTOR, STORAGE_TEMPERATURE_DATA_DESCRIPTOR, *PSTORAGE_TEMPERATURE_DATA_DESCRIPTOR
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
req.alt-api: STORAGE_TEMPERATURE_DATA_DESCRIPTOR
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

# STORAGE_TEMPERATURE_DATA_DESCRIPTOR structure



## -description
<p>This structure is used in conjunction with <a href="..\ntddstor\ni-ntddstor-ioctl-storage-query-property.md">IOCTL_STORAGE_QUERY_PROPERTY</a> to return temperature data from a storage device or adapter. </p>


## -syntax

````
typedef struct _STORAGE_TEMPERATURE_DATA_DESCRIPTOR {
  ULONG                    Version;
  ULONG                    Size;
  SHORT                    CriticalTemperature;
  SHORT                    WarningTemperature;
  USHORT                   InfoCount;
  UCHAR                    Reserved0[2];
  ULONG                    Reserved1[2];
  STORAGE_TEMPERATURE_INFO TemperatureInfo[ANYSIZE_ARRAY];
} STORAGE_TEMPERATURE_DATA_DESCRIPTOR, *PSTORAGE_TEMPERATURE_DATA_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field Version

<dd>
<p>Contains the size of this structure, in bytes. The value of this member will change as members are added to the structure.</p>
</dd>

### -field Size

<dd>
<p>Specifies the total size of the data returned, in bytes. This may include data that follows this structure.</p>
</dd>

### -field CriticalTemperature

<dd>
<p>Indicates the minimum temperature in degrees Celsius that may prevent normal operation. Exceeding this temperature may result in possible data loss, automatic device shutdown, extreme performance throttling, or permanent damage.      </p>
</dd>

### -field WarningTemperature

<dd>
<p>Indicates the maximum temperature in degrees Celsius at which the device is capable of operating continuously without degrading operation or reliability.    </p>
</dd>

### -field InfoCount

<dd>
<p>Specifies the number of <a href="..\ntddstor\ns-ntddstor--storage-temperature-info.md">STORAGE_TEMPERATURE_INFO</a> structures reported in <b>TemperatureInfo</b>. More than one set of temperature data may be returned when there are multiple sensors in the drive.</p>
</dd>

### -field Reserved0

<dd>
<p>Reserved for future use.</p>
</dd>

### -field Reserved1

<dd>
<p>Reserved for future use.</p>
</dd>

### -field TemperatureInfo[ANYSIZE_ARRAY]

<dd>
<p>Device temperature data, of type <a href="..\ntddstor\ns-ntddstor--storage-temperature-info.md">STORAGE_TEMPERATURE_INFO</a>.</p>
</dd>
</dl>

## -remarks


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
<a href="..\ntddstor\ns-ntddstor--storage-temperature-info.md">STORAGE_TEMPERATURE_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20STORAGE_TEMPERATURE_DATA_DESCRIPTOR structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
