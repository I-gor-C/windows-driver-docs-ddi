---
UID: NS.ntddmmc._FEATURE_DATA_FIRMWARE_DATE
title: FEATURE_DATA_FIRMWARE_DATE
author: windows-driver-content
description: The FEATURE_DATA_FIRMWARE_DATE structure holds the date information associated with the Firmware Information feature.
old-location: storage\feature_data_firmware_date.htm
old-project: storage
ms.assetid: 1f6c6a37-9510-47bc-b507-b3fd7477b432
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: FEATURE_DATA_FIRMWARE_DATE, FEATURE_DATA_FIRMWARE_DATE, *PFEATURE_DATA_FIRMWARE_DATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddmmc.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FEATURE_DATA_FIRMWARE_DATE
req.alt-loc: ntddmmc.h
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

# FEATURE_DATA_FIRMWARE_DATE structure



## -description
<p>The FEATURE_DATA_FIRMWARE_DATE structure holds the date information associated with the Firmware Information feature. </p>


## -syntax

````
typedef struct _FEATURE_DATA_FIRMWARE_DATE {
  FEATURE_HEADER Header;
  UCHAR          Year[4];
  UCHAR          Month[2];
  UCHAR          Day[2];
  UCHAR          Hour[2];
  UCHAR          Minute[2];
  UCHAR          Seconds[2];
  UCHAR          Reserved[2];
} FEATURE_DATA_FIRMWARE_DATE, *PFEATURE_DATA_FIRMWARE_DATE;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>Contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a> structure with header information for this feature descriptor. </p>
</dd>

### -field <b>Year</b>

<dd>
<p>Contains the two low order decimal digits represented as ASCII characters that indicate the year. For example, if the year is 2013, the <b>Year</b> member will contain characters "33" (a hexadecimal value of 0x3133). </p>
</dd>

### -field <b>Month</b>

<dd>
<p>Contains two decimal digits represented as ASCII characters that indicate the month. For example, if the month is August, the <b>Month</b> member will contain characters "08" (a hexadecimal value of 0x3038). </p>
</dd>

### -field <b>Day</b>

<dd>
<p>Contains two decimal digits represented as ASCII characters that indicate the day. For example, if the day is August 12, the <b>Day</b> member will contain characters "12" (a hexadecimal value of 0x3132). </p>
</dd>

### -field <b>Hour</b>

<dd>
<p>Contains two decimal digits represented as ASCII characters that indicate the hour. For example, if the time 1:20:43 PM, the <b>Hour</b> member will contain the characters "13" (hexadecimal value of 0x3133). </p>
</dd>

### -field <b>Minute</b>

<dd>
<p>Contains two decimal digits represented as ASCII characters that indicates the minute of the hour. For example, if the time 1:20:43 PM, the <b>Minute</b> member will contain the characters "20" (hexadecimal value of 0x3230). </p>
</dd>

### -field <b>Seconds</b>

<dd>
<p>Contains two decimal digits represented as ASCII characters that indicates the minute of the hour. For example, if the time 1:20:43 PM, the <b>Seconds</b> member will contain the characters "43" (hexadecimal value of 0x3433). </p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>

## -remarks
<p>The structure holds the date information associated with the feature named "Firmware Information" by the <i>SCSI Multimedia - 4</i> (<i>MMC-4</i>) specification. Devices that support this feature can be queried for the date and Greenwich Mean Time (GMT) of the creation of the firmware revision currently loaded on the device. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddmmc.h (include Ntddcdrm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20FEATURE_DATA_FIRMWARE_DATE structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
