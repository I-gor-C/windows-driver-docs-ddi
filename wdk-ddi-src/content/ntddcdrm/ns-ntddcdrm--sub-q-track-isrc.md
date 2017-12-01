---
UID: NS.ntddcdrm._SUB_Q_TRACK_ISRC
title: SUB_Q_TRACK_ISRC
author: windows-driver-content
description: The SUB_Q_TRACK_ISC contains position information and is used in conjunction with the SUB_Q_CHANNEL_DATA structure.
old-location: storage\sub_q_track_isrc.htm
old-project: storage
ms.assetid: 0439bd46-b009-435d-aab7-efca48a17cb7
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SUB_Q_TRACK_ISRC, SUB_Q_TRACK_ISRC, *PSUB_Q_TRACK_ISRC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddcdrm.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SUB_Q_TRACK_ISRC
req.alt-loc: ntddcdrm.h
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

# SUB_Q_TRACK_ISRC structure



## -description
<p>The SUB_Q_TRACK_ISC contains position information and is used in conjunction with the <a href="..\ntddcdrm\ns-ntddcdrm--sub-q-channel-data.md">SUB_Q_CHANNEL_DATA</a> structure. </p>


## -syntax

````
typedef struct _SUB_Q_TRACK_ISRC {
  SUB_Q_HEADER Header;
  UCHAR        FormatCode;
  UCHAR        Reserved0;
  UCHAR        Track;
  UCHAR        Reserved1;
  UCHAR        Reserved2  :7;
  UCHAR        Tcval  :1;
  UCHAR        TrackIsrc[15];
} SUB_Q_TRACK_ISRC, *PSUB_Q_TRACK_ISRC;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>Indicates, among other things, the length of the Q subchannel data that was retrieved. See <a href="..\ntddcdrm\ns-ntddcdrm--sub-q-header.md">SUB_Q_HEADER</a> for further details. </p>
</dd>

### -field <b>FormatCode</b>

<dd>
<p>Should have a value of IOCTL_CDROM_TRACK_ISRC. </p>
</dd>

### -field <b>Reserved0</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>Track</b>

<dd>
<p>Contains the number for the track for which the ISRC value was requested. </p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>Tcval</b>

<dd>
<p>Indicates that ISRC data was detected, if set to 1. Otherwise, if set to zero, indicates that <b>TrackIsrc</b> is invalid. </p>
</dd>

### -field <b>TrackIsrc</b>

<dd>
<p>Contains an array that holds the tracking ISRC data. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddcdrm.h (include Ntddcdrm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddcdrm\ni-ntddcdrm-ioctl-cdrom-read-q-channel.md">IOCTL_CDROM_READ_Q_CHANNEL</a>
</dt>
<dt>
<a href="..\ntddcdrm\ns-ntddcdrm--cdrom-sub-q-data-format.md">CDROM_SUB_Q_DATA_FORMAT</a>
</dt>
<dt>
<a href="..\ntddcdrm\ns-ntddcdrm--sub-q-channel-data.md">SUB_Q_CHANNEL_DATA</a>
</dt>
<dt>
<a href="..\ntddcdrm\ns-ntddcdrm--sub-q-header.md">SUB_Q_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SUB_Q_TRACK_ISRC structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
