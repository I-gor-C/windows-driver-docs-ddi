---
UID: NS.ntddcdrm._CDROM_TOC_FULL_TOC_DATA_BLOCK
title: CDROM_TOC_FULL_TOC_DATA_BLOCK
author: windows-driver-content
description: The CDROM_TOC_FULL_TOC_DATA_BLOCK structure contains track descriptor data used in conjunction with the data from the CDROM_TOC_FULL_TOC_DATA structure.
old-location: storage\cdrom_toc_full_toc_data_block.htm
old-project: storage
ms.assetid: 8d6d1283-b64e-4c3b-8a45-376cfe76a19d
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: CDROM_TOC_FULL_TOC_DATA_BLOCK, CDROM_TOC_FULL_TOC_DATA_BLOCK, *PCDROM_TOC_FULL_TOC_DATA_BLOCK
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
req.alt-api: CDROM_TOC_FULL_TOC_DATA_BLOCK
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

# CDROM_TOC_FULL_TOC_DATA_BLOCK structure



## -description
<p>The CDROM_TOC_FULL_TOC_DATA_BLOCK structure contains track descriptor data used in conjunction with the data from the <a href="..\ntddcdrm\ns-ntddcdrm--cdrom-toc-full-toc-data.md">CDROM_TOC_FULL_TOC_DATA</a> structure. </p>


## -syntax

````
typedef struct _CDROM_TOC_FULL_TOC_DATA_BLOCK {
  UCHAR SessionNumber;
  UCHAR Control  :4;
  UCHAR Adr  :4;
  UCHAR Reserved1;
  UCHAR Point;
  UCHAR MsfExtra[3];
  UCHAR Zero;
  UCHAR Msf[3];
} CDROM_TOC_FULL_TOC_DATA_BLOCK, *PCDROM_TOC_FULL_TOC_DATA_BLOCK;
````


## -struct-fields
<dl>

### -field SessionNumber

<dd>
<p>Contains the number of the session that the track belongs to. </p>
</dd>

### -field Control

<dd>
<p>Indicates the attributes of the track. </p>
<p></p>
<dl>

### -field AUDIO_WITH_PREEMPHASIS

<dd>
<p>Indicates two audio channels with preemphasis of 50/15 microseconds have been added. </p>
</dd>
</dl>
<p></p>
<dl>

### -field DIGITAL_COPY_PERMITTED

<dd>
<p>Indicates digital copying is allowed. </p>
</dd>
</dl>
<p></p>
<dl>

### -field AUDIO_DATA_TRACK

<dd>
<p>Indicates that the track contains nonaudio data. </p>
</dd>
</dl>
<p></p>
<dl>

### -field TWO_FOUR_CHANNEL_AUDIO

<dd>
<p>Indicates that the track contains four channels of audio data.</p>
</dd>
</dl>
</dd>

### -field Adr

<dd>
<p>Indicates the type of information encoded in the Q subchannel of the block where this table of contents entry was found.</p>
<p></p>
<dl>

### -field ADR_NO_MODE_INFORMATION

<dd>
<p>Q subchannel mode information not supplied. </p>
</dd>
</dl>
<p></p>
<dl>

### -field ADR_ENCODES_CURRENT_POSITION

<dd>
<dl>

### -field Q subchannel encodes current position data


### -field (that is, track, index, absolute address, relative address). 

</dl>
</dd>
</dl>
<p></p>
<dl>

### -field ADR_ENCODES_MEDIA_CATALOG

<dd>
<p>Q subchannel encodes media catalog number. </p>
</dd>
</dl>
<p></p>
<dl>

### -field ADR_ENCODES_ISRC 

<dd>
<p>Q subchannel encodes ISRC. </p>
</dd>
</dl>
</dd>

### -field Reserved1

<dd>
<p>Reserved. </p>
</dd>

### -field Point

<dd>
<p>Defines various types of information within the table of contents lead-in area. For information about the permissible values for this member, see specification <i>T10/1363-D Revision-02A</i>, by National Committee for Information Technology Standards (NCITS).</p>
</dd>

### -field MsfExtra

<dd>
<p>See specification <i>T10/1363-D Revision-02A</i>, by National Committee for Information Technology Standards (NCITS) For information about the permissible values for this member. </p>
</dd>

### -field Zero

<dd>
<p>Contains the value of the zero bit.</p>
</dd>

### -field Msf

<dd>
<p>Contains the minute, second, and frame. Msf[0] contains the minutes field. Msf[1] contains the seconds field, and Msf[2] contains the frames field. MSF is a format similar to logical block addressing. </p>
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
<a href="..\ntddcdrm\ni-ntddcdrm-ioctl-cdrom-read-toc-ex.md">IOCTL_CDROM_READ_TOC_EX</a>
</dt>
<dt>
<a href="..\ntddcdrm\ns-ntddcdrm--cdrom-read-toc-ex.md">CDROM_READ_TOC_EX</a>
</dt>
<dt>
<a href="..\ntddcdrm\ns-ntddcdrm--cdrom-toc-full-toc-data.md">CDROM_TOC_FULL_TOC_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20CDROM_TOC_FULL_TOC_DATA_BLOCK structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
