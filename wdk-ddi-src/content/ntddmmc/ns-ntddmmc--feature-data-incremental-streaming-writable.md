---
UID: NS.ntddmmc._FEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE
title: FEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE
author: windows-driver-content
description: The FEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE structure contains information about the Incremental Streaming Writable feature.
old-location: storage\feature_data_incremental_streaming_writable.htm
old-project: storage
ms.assetid: 5e3918a4-8cc6-45b9-acb1-3a2b2088d4b9
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: FEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE, FEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE, *PFEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE
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
req.alt-api: FEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE
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

# FEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE structure



## -description
<p>The FEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE structure contains information about the Incremental Streaming Writable feature. </p>


## -syntax

````
typedef struct _FEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE {
  FEATURE_HEADER Header;
  UCHAR          DataTypeSupported[2];
  UCHAR          BufferUnderrunFree  :1;
  UCHAR          AddressModeReservation  :1;
  UCHAR          TrackRessourceInformation  :1;
  UCHAR          Reserved01  :5;
  UCHAR          NumberOfLinkSizes;
  UCHAR          LinkSize[];
} FEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE, *PFEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>Contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a> structure with header information for this feature descriptor. </p>
</dd>

### -field <b>DataTypeSupported</b>

<dd>
<p>Indicates the supported data type. See the <i>SCSI Multimedia - 4 (MMC-4)</i> specification for an explanation of the values that this member can take. <b>DataTypeSupported</b>[0] must hold the most significant byte of the number of the data type. <b>DataTypeSupported</b>[1] must hold the least significant byte of the number.</p>
</dd>

### -field <b>BufferUnderrunFree</b>

<dd>
<p>Indicates, when set to one, that the logical unit is capable of zero-loss linking.</p>
</dd>

### -field <b>AddressModeReservation</b>

<dd></dd>

### -field <b>TrackRessourceInformation</b>

<dd></dd>

### -field <b>Reserved01</b>

<dd></dd>

### -field <b>NumberOfLinkSizes</b>

<dd>
<p>Specifies the number of link sizes available for the current media. See the <i>MMC-3</i> specification for an explanation of the values that this member can take. </p>
</dd>

### -field <b>LinkSize</b>

<dd>
<p>Contains an array that indicates the number of logical blocks per link. </p>
</dd>
</dl>

## -remarks
<p>This structure holds data for the feature named "Incremental Streaming Writable" by the <i>MMC-3 </i>specification. Devices that support this feature can write data to a contiguous region, and can append data to a limited number of locations on the media. On CD media, this is known as "packet recording" and on a DVD media it is known as "incremental recording".</p>

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
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553850">FEATURE_NUMBER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20FEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
