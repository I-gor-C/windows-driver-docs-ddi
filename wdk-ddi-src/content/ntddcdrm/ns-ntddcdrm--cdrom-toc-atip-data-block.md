---
UID: NS.ntddcdrm._CDROM_TOC_ATIP_DATA_BLOCK
title: CDROM_TOC_ATIP_DATA_BLOCK
author: windows-driver-content
description: Device control IRPs with a control code of IOCTL_CDROM_READ_TOC_EX and a format of CDROM_READ_TOC_EX_FORMAT_ATIP return their output data in a header structure of type CDROM_TOC_ATIP_DATA followed by a series of ATIP data block descriptors defined by CDROM_TOC_ATIP_DATA_BLOCK.
old-location: storage\cdrom_toc_atip_data_block.htm
ms.assetid: b98d0ba9-9c32-44ed-b6c3-db6de26a1663
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddcdrm.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CDROM_TOC_ATIP_DATA_BLOCK
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
ms.keywords: CDROM_TOC_ATIP_DATA_BLOCK, CDROM_TOC_ATIP_DATA_BLOCK, *PCDROM_TOC_ATIP_DATA_BLOCK
req.iface: 
---

# CDROM_TOC_ATIP_DATA_BLOCK structure



## -description
<p>Device control IRPs with a control code of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559367">IOCTL_CDROM_READ_TOC_EX</a> and a format of CDROM_READ_TOC_EX_FORMAT_ATIP return their output data in a header structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff551375">CDROM_TOC_ATIP_DATA</a> followed by a series of ATIP data block descriptors defined by <b>CDROM_TOC_ATIP_DATA_BLOCK</b>.</p>


## -syntax

````
typedef struct _CDROM_TOC_ATIP_DATA_BLOCK {
  UCHAR CdrwReferenceSpeed  :3;
  UCHAR Reserved3  :1;
  UCHAR WritePower  :3;
  UCHAR True1  :1;
  UCHAR Reserved4  :6;
  UCHAR UnrestrictedUse  :1;
  UCHAR Reserved5  :1;
  UCHAR A3Valid  :1;
  UCHAR A2Valid  :1;
  UCHAR A1Valid  :1;
  UCHAR DiscSubType  :3;
  UCHAR IsCdrw  :1;
  UCHAR True2  :1;
  UCHAR Reserved7;
  UCHAR LeadInMsf[3];
  UCHAR Reserved8;
  UCHAR LeadOutMsf[3];
  UCHAR Reserved9;
  UCHAR A1Values[3];
  UCHAR Reserved10;
  UCHAR A2Values[3];
  UCHAR Reserved11;
  UCHAR A3Values[3];
  UCHAR Reserved12;
} CDROM_TOC_ATIP_DATA_BLOCK, *PCDROM_TOC_ATIP_DATA_BLOCK;
````


## -struct-fields
<dl>

### -field <b>CdrwReferenceSpeed</b>

<dd>
<p>Indicates the recommended write speed for the media. Values 0x00 to 0x01 are reserved. A value of 0x02 indicates a CD-ROM speed of 4X. A value of 0x03 indicates a CD-ROM speed of 8X. Values 0x04 to 0x07 are reserved. </p>
</dd>

### -field <b>Reserved3</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>WritePower</b>

<dd>
<p>Indicates media's recommended initial laser power setting. The high order bit must be set to 1. The setting of the other bits varies between CD-R and CD-RW media. For an explanation of the values these bits can have, see the <i>SCSI Multimedia Commands - 3</i> (MMC-3) specification. </p>
</dd>

### -field <b>True1</b>

<dd>
<p>Must be set to 1. </p>
</dd>

### -field <b>Reserved4</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>UnrestrictedUse</b>

<dd>
<p>Indicates, when set to 1, that the mounted disc is defined for unrestricted use. When set to zero, indicates that the mounted disc is defined for restricted use. </p>
</dd>

### -field <b>Reserved5</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>A3Valid</b>

<dd>
<p>Indicates that bytes 16-18 (bytes 12-14 of the ATIP descriptor) are valid when set to 1. When set to zero, indicates that bytes 16-18 are invalid. </p>
</dd>

### -field <b>A2Valid</b>

<dd>
<p>Indicates that A2 values field is valid when set to 1. When set to zero, indicates that the A2 values field is invalid. </p>
</dd>

### -field <b>A1Valid</b>

<dd>
<p>Indicates that A3 values field is valid when set to 1. When set to zero, indicates that the A3 values field is invalid. </p>
</dd>

### -field <b>DiscSubType</b>

<dd>
<p>Must be set to zero. </p>
</dd>

### -field <b>IsCdrw</b>

<dd>
<p>Indicates the media is rewritable (CD-RW) when set to 1. When set to zero, indicates the media is write-once (CD-R). </p>
</dd>

### -field <b>True2</b>

<dd>
<p>Must be set to 1. </p>
</dd>

### -field <b>Reserved7</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>LeadInMsf</b>

<dd>
<p>Indicates the ATIP start time of lead-in, in terms of minutes, seconds, and frames. Valid values of the first byte are from 0x50 to 0x63. For an explanation of the values that the second and third bytes can have, see the <i>SCSI Multimedia Commands - 3</i> (MMC-3) specification. </p>
</dd>

### -field <b>Reserved8</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>LeadOutMsf</b>

<dd>
<p>Indicates the ATIP last possible start time of lead-out in terms of minutes, seconds, and frames. Valid values of the first byte are from 0x0 to 0x04F. For an explanation of the values that the second and third bytes can have, see the <i>SCSI Multimedia Commands - 3</i> (MMC-3) specification. </p>
</dd>

### -field <b>Reserved9</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>A1Values</b>

<dd>
<p>See specification <i>T10/1363-D Revision-02A</i>, by National Committee for Information Technology Standards (NCITS) For information about the permissible values for this member. </p>
</dd>

### -field <b>Reserved10</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>A2Values</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>Reserved11</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>A3Values</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>Reserved12</b>

<dd>
<p>Reserved. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559367">IOCTL_CDROM_READ_TOC_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551366">CDROM_READ_TOC_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551375">CDROM_TOC_ATIP_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20CDROM_TOC_ATIP_DATA_BLOCK structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
