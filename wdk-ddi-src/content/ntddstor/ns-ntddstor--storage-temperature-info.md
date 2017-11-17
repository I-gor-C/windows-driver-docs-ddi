---
UID: NS.ntddstor._STORAGE_TEMPERATURE_INFO
title: STORAGE_TEMPERATURE_INFO
author: windows-driver-content
description: Describes device temperature data. Returned as part of STORAGE_TEMPERATURE_DATA_DESCRIPTOR when querying for temperature data with an IOCTL_STORAGE_QUERY_PROPERTY request.
old-location: storage\storage_temperature_info.htm
ms.assetid: 1B7C68BF-78AE-4427-B5DC-E388CB5FAC0C
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_TEMPERATURE_INFO
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
ms.keywords: STORAGE_TEMPERATURE_INFO, STORAGE_TEMPERATURE_INFO, *PSTORAGE_TEMPERATURE_INFO
req.iface: 
---

# STORAGE_TEMPERATURE_INFO structure



## -description
<p>Describes  device temperature data. Returned as part of <a href="https://msdn.microsoft.com/library/windows/hardware/mt651017">STORAGE_TEMPERATURE_DATA_DESCRIPTOR</a> when querying for temperature data with an <a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a> request. </p>


## -syntax

````
typedef struct _STORAGE_TEMPERATURE_INFO {
  WORD    Index;
  SHORT   Temperature;
  SHORT   OverThreshold;
  SHORT   UnderThreshold;
  BOOLEAN OverThresholdChangable;
  BOOLEAN UnderThresholdChangable;
  BOOLEAN EventGenerated;
  UCHAR   Reserved0;
  ULONG   Reserved1;
} STORAGE_TEMPERATURE_INFO, *PSTORAGE_TEMPERATURE_INFO;
````


## -struct-fields
<dl>

### -field <b>Index</b>

<dd>
<p>Identifies the instance of temperature information. Starts from 0. Index 0 may indicate a composite value.      </p>
</dd>

### -field <b>Temperature</b>

<dd>
<p>A signed value that indicates the current temperature, in degrees Celsius. </p>
</dd>

### -field <b>OverThreshold</b>

<dd>
<p>A signed value that specifies the maximum temperature within the desired threshold, in degrees Celsius.</p>
</dd>

### -field <b>UnderThreshold</b>

<dd>
<p>A signed value that specifies the minimum temperature within the desired threshold, in degrees Celsius.</p>
</dd>

### -field <b>OverThresholdChangable</b>

<dd>
<p>Indicates if <i>OverThreshold</i> can be changed by using <a href="https://msdn.microsoft.com/library/windows/hardware/mt650982">IOCTL_STORAGE_SET_TEMPERATURE_THRESHOLD</a>.</p>
</dd>

### -field <b>UnderThresholdChangable</b>

<dd>
<p>Indicates if <i>UnderThreshold</i> can be changed by using <a href="https://msdn.microsoft.com/library/windows/hardware/mt650982">IOCTL_STORAGE_SET_TEMPERATURE_THRESHOLD</a>.</p>
</dd>

### -field <b>EventGenerated</b>

<dd>
<p>Indicates if a notification will be generated when the current temperature crosses a threshold.</p>
</dd>

### -field <b>Reserved0</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved for future use.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566997">STORAGE_PROPERTY_QUERY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566996">STORAGE_PROPERTY_ID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt651018">STORAGE_TEMPERATURE_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20STORAGE_TEMPERATURE_INFO structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
