---
UID: NS.ntddcdrm._SUB_Q_CHANNEL_DATA
title: SUB_Q_CHANNEL_DATA
author: windows-driver-content
description: Device control IRPs with a control code of IOCTL_CDROM_READ_Q_CHANNEL return their output data in this union.
old-location: storage\sub_q_channel_data.htm
old-project: storage
ms.assetid: d0304ac7-cb19-499c-81af-98be33312951
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SUB_Q_CHANNEL_DATA, SUB_Q_CHANNEL_DATA, *PSUB_Q_CHANNEL_DATA
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
req.alt-api: SUB_Q_CHANNEL_DATA
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

# SUB_Q_CHANNEL_DATA structure



## -description
<p>Device control IRPs with a control code of IOCTL_CDROM_READ_Q_CHANNEL return their output data in this union. </p>


## -syntax

````
typedef union _SUB_Q_CHANNEL_DATA {
  SUB_Q_CURRENT_POSITION     CurrentPosition;
  SUB_Q_MEDIA_CATALOG_NUMBER MediaCatalog;
  SUB_Q_TRACK_ISRC           TrackIsrc;
} SUB_Q_CHANNEL_DATA, *PSUB_Q_CHANNEL_DATA;
````


## -struct-fields
<dl>

### -field <b>CurrentPosition</b>

<dd>
<p>Contains position information, such as the absolute and relative addresses, in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff567596">SUB_Q_CURRENT_POSITION</a> structure. </p>
</dd>

### -field <b>MediaCatalog</b>

<dd>
<p>Contains the media catalog number in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff567600">SUB_Q_MEDIA_CATALOG_NUMBER</a>  structure.</p>
</dd>

### -field <b>TrackIsrc</b>

<dd>
<p>Contains the TrackIsrc code in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff567601">SUB_Q_TRACK_ISRC</a> structure. </p>
</dd>
</dl>

## -remarks
<p>The value of the <b>Format </b>member of the CDROM_SUB_Q_DATA_FORMAT structure that is passed as input with IOCTL_CDROM_READ_Q_CHANNEL determines which member of this union is used to return the output data. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff551371">CDROM_SUB_Q_DATA_FORMAT</a> for a detailed explanation. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559363">IOCTL_CDROM_READ_Q_CHANNEL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551371">CDROM_SUB_Q_DATA_FORMAT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567596">SUB_Q_CURRENT_POSITION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567600">SUB_Q_MEDIA_CATALOG_NUMBER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567601">SUB_Q_TRACK_ISRC</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SUB_Q_CHANNEL_DATA union%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
