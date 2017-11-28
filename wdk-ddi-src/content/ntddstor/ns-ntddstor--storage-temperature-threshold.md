---
UID: NS.ntddstor._STORAGE_TEMPERATURE_THRESHOLD
title: STORAGE_TEMPERATURE_THRESHOLD
author: windows-driver-content
description: This structure is used to set the over or under temperature threshold of a storage device (via IOCTL_STORAGE_SET_TEMPERATURE_THRESHOLD).
old-location: storage\storage_temperature_threshold.htm
old-project: storage
ms.assetid: 19096AD2-5149-4AE1-94CD-9004ED8C24DC
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORAGE_TEMPERATURE_THRESHOLD, STORAGE_TEMPERATURE_THRESHOLD, *PSTORAGE_TEMPERATURE_THRESHOLD
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
req.alt-api: STORAGE_TEMPERATURE_THRESHOLD
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

# STORAGE_TEMPERATURE_THRESHOLD structure



## -description
<p>This structure is used to set the over or under temperature threshold of a storage device (via <a href="https://msdn.microsoft.com/library/windows/hardware/mt650982">IOCTL_STORAGE_SET_TEMPERATURE_THRESHOLD</a>).</p>


## -syntax

````
typedef struct _STORAGE_TEMPERATURE_THRESHOLD {
  ULONG   Version;
  ULONG   Size;
  USHORT  Flags;
  USHORT  Index;
  SHORT   Threshold;
  BOOLEAN OverThreshold;
  UCHAR   Reserved;
} STORAGE_TEMPERATURE_THRESHOLD, *PSTORAGE_TEMPERATURE_THRESHOLD;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of the structure.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size of this structure. This should be set to sizeof(<b>STORAGE_TEMPERATURE_THRESHOLD</b>).</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Flags set for this request. The following are valid flags.</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td><b>STORAGE_PROTOCOL_COMMAND_FLAG_ADAPTER_REQUEST</b></td>
<td>This flag indicates the request to target an adapter instead of device.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Index</b>

<dd>
<p>Identifies the instance of temperature information. Starts from 0. Index 0 may indicate a composite value.</p>
</dd>

### -field <b>Threshold</b>

<dd>
<p>A signed value that indicates the temperature of the threshold, in degrees Celsius.</p>
</dd>

### -field <b>OverThreshold</b>

<dd>
<p>Indicates if the <i>Threshold</i> specifies the over or under temperature threshold. If <b>true</b>, set the <b>OverThreshold</b> temperature value of the device; otherwise, set the <b>UnderThreshold</b> temperature value. </p>
</dd>

### -field <b>Reserved</b>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20STORAGE_TEMPERATURE_THRESHOLD structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
