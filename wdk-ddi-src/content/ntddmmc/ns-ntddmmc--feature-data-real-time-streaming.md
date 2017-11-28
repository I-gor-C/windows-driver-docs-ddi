---
UID: NS.ntddmmc._FEATURE_DATA_REAL_TIME_STREAMING
title: FEATURE_DATA_REAL_TIME_STREAMING
author: windows-driver-content
description: The FEATURE_DATA_REAL_TIME_STREAMING structure holds information about the Real Time Streaming feature.
old-location: storage\feature_data_real_time_streaming.htm
old-project: storage
ms.assetid: 3b1b54cc-52a5-48ce-a637-70e289c1944e
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: FEATURE_DATA_REAL_TIME_STREAMING, FEATURE_DATA_REAL_TIME_STREAMING, *PFEATURE_DATA_REAL_TIME_STREAMING
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
req.alt-api: FEATURE_DATA_REAL_TIME_STREAMING
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

# FEATURE_DATA_REAL_TIME_STREAMING structure



## -description
<p>The FEATURE_DATA_REAL_TIME_STREAMING structure holds information about the Real Time Streaming feature. </p>


## -syntax

````
typedef struct _FEATURE_DATA_REAL_TIME_STREAMING {
  FEATURE_HEADER Header;
  UCHAR          StreamRecording  :1;
  UCHAR          WriteSpeedInGetPerf  :1;
  UCHAR          WriteSpeedInMP2A  :1;
  UCHAR          SetCDSpeed  :1;
  UCHAR          ReadBufferCapacityBlock  :1;
  UCHAR          Reserved1  :3;
  UCHAR          Reserved2[3];
} FEATURE_DATA_REAL_TIME_STREAMING, *PFEATURE_DATA_REAL_TIME_STREAMING;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>Contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a> structure with header information for this feature descriptor. </p>
</dd>

### -field <b>StreamRecording</b>

<dd>
<p>Indicates, when set to 1, that the device supports the stream recording operation. When set to zero, this bit indicates that the device might not support the stream recording operation. </p>
</dd>

### -field <b>WriteSpeedInGetPerf</b>

<dd>
<p>Indicates, when set to 1, that the device supports the write speed data of the GET PERFORMANCE command and the WRC field of the SETSTREAMING command. </p>
</dd>

### -field <b>WriteSpeedInMP2A</b>

<dd>
<p>Indicates, when set to 1, that the device supports CD/DVD capabilities &amp; mechanical status mode page.</p>
</dd>

### -field <b>SetCDSpeed</b>

<dd>
<p>Indicates, when set to 1, that the device supports the SET CD SPEED command. When set to zero, it indicates that the device does not support the SET CD SPEED command.</p>
</dd>

### -field <b>ReadBufferCapacityBlock</b>

<dd>
<p>Indicates, when set to 1, that the device supports the READ BUFFERCAPACITY command.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved. </p>
</dd>
</dl>

## -remarks
<p>This structure holds data for the feature named "Real Time Streaming" by the <i>SCSI Multimedia - 4 (MMC-4)</i> specification. Devices that support this feature allow the initiator to specify the performance level of the device within certain limits allowed by the device. These devices must also indicate to the initiator whether they support stream playback operations. </p>

<p>When queried, devices supporting this feature must return the information indicated in <a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a>. No other feature-specific information is required. </p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20FEATURE_DATA_REAL_TIME_STREAMING structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
