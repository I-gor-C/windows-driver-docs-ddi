---
UID: NS:ntddcdrm._CDROM_TOC_ATIP_DATA_BLOCK
title: "_CDROM_TOC_ATIP_DATA_BLOCK"
author: windows-driver-content
description: Device control IRPs with a control code of IOCTL_CDROM_READ_TOC_EX and a format of CDROM_READ_TOC_EX_FORMAT_ATIP return their output data in a header structure of type CDROM_TOC_ATIP_DATA followed by a series of ATIP data block descriptors defined by CDROM_TOC_ATIP_DATA_BLOCK.
old-location: storage\cdrom_toc_atip_data_block.htm
old-project: storage
ms.assetid: b98d0ba9-9c32-44ed-b6c3-db6de26a1663
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PCDROM_TOC_ATIP_DATA_BLOCK, CDROM_TOC_ATIP_DATA_BLOCK, CDROM_TOC_ATIP_DATA_BLOCK structure [Storage Devices], PCDROM_TOC_ATIP_DATA_BLOCK, PCDROM_TOC_ATIP_DATA_BLOCK structure pointer [Storage Devices], _CDROM_TOC_ATIP_DATA_BLOCK, ntddcdrm/CDROM_TOC_ATIP_DATA_BLOCK, ntddcdrm/PCDROM_TOC_ATIP_DATA_BLOCK, storage.cdrom_toc_atip_data_block, structs-CD-ROM_8c2f3446-c864-450a-a873-9e1d29b1e052.xml"
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddcdrm.h
api_name:
-	CDROM_TOC_ATIP_DATA_BLOCK
product:
- Windows
targetos: Windows
req.typenames: CDROM_TOC_ATIP_DATA_BLOCK, *PCDROM_TOC_ATIP_DATA_BLOCK
---

# _CDROM_TOC_ATIP_DATA_BLOCK structure
Device control IRPs with a control code of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559367">IOCTL_CDROM_READ_TOC_EX</a> and a format of CDROM_READ_TOC_EX_FORMAT_ATIP return their output data in a header structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff551375">CDROM_TOC_ATIP_DATA</a> followed by a series of ATIP data block descriptors defined by <b>CDROM_TOC_ATIP_DATA_BLOCK</b>.

## Syntax
```
typedef struct _CDROM_TOC_ATIP_DATA_BLOCK {
  UCHAR  : 3 CdrwReferenceSpeed;
  UCHAR  : 1 Reserved3;
  UCHAR  : 3 WritePower;
  UCHAR  : 1 True1;
  UCHAR  : 6 Reserved4;
  UCHAR  : 1 UnrestrictedUse;
  UCHAR  : 1 Reserved5;
  UCHAR  : 1 A3Valid;
  UCHAR  : 1 A2Valid;
  UCHAR  : 1 A1Valid;
  UCHAR  : 3 DiscSubType;
  UCHAR  : 1 IsCdrw;
  UCHAR  : 1 True2;
  UCHAR      Reserved7;
  UCHAR      LeadInMsf[3];
  UCHAR      Reserved8;
  UCHAR      LeadOutMsf[3];
  UCHAR      Reserved9;
  UCHAR      A1Values[3];
  UCHAR      Reserved10;
  UCHAR      A2Values[3];
  UCHAR      Reserved11;
  UCHAR      A3Values[3];
  UCHAR      Reserved12;
} CDROM_TOC_ATIP_DATA_BLOCK, *PCDROM_TOC_ATIP_DATA_BLOCK;
```

## Members


`CdrwReferenceSpeed`

Indicates the recommended write speed for the media. Values 0x00 to 0x01 are reserved. A value of 0x02 indicates a CD-ROM speed of 4X. A value of 0x03 indicates a CD-ROM speed of 8X. Values 0x04 to 0x07 are reserved.

`Reserved3`

Reserved.

`WritePower`

Indicates media's recommended initial laser power setting. The high order bit must be set to 1. The setting of the other bits varies between CD-R and CD-RW media. For an explanation of the values these bits can have, see the <i>SCSI Multimedia Commands - 3</i> (MMC-3) specification.

`True1`

Must be set to 1.

`Reserved4`

Reserved.

`UnrestrictedUse`

Indicates, when set to 1, that the mounted disc is defined for unrestricted use. When set to zero, indicates that the mounted disc is defined for restricted use.

`Reserved5`

Reserved.

`A3Valid`

Indicates that bytes 16-18 (bytes 12-14 of the ATIP descriptor) are valid when set to 1. When set to zero, indicates that bytes 16-18 are invalid.

`A2Valid`

Indicates that A2 values field is valid when set to 1. When set to zero, indicates that the A2 values field is invalid.

`A1Valid`

Indicates that A3 values field is valid when set to 1. When set to zero, indicates that the A3 values field is invalid.

`DiscSubType`

Must be set to zero.

`IsCdrw`

Indicates the media is rewritable (CD-RW) when set to 1. When set to zero, indicates the media is write-once (CD-R).

`True2`

Must be set to 1.

`Reserved7`

Reserved.

`LeadInMsf`

Indicates the ATIP start time of lead-in, in terms of minutes, seconds, and frames. Valid values of the first byte are from 0x50 to 0x63. For an explanation of the values that the second and third bytes can have, see the <i>SCSI Multimedia Commands - 3</i> (MMC-3) specification.

`Reserved8`

Reserved.

`LeadOutMsf`

Indicates the ATIP last possible start time of lead-out in terms of minutes, seconds, and frames. Valid values of the first byte are from 0x0 to 0x04F. For an explanation of the values that the second and third bytes can have, see the <i>SCSI Multimedia Commands - 3</i> (MMC-3) specification.

`Reserved9`

Reserved.

`A1Values`

See specification <i>T10/1363-D Revision-02A</i>, by National Committee for Information Technology Standards (NCITS) For information about the permissible values for this member.

`Reserved10`

Reserved.

`A2Values`

Reserved.

`Reserved11`

Reserved.

`A3Values`

Reserved.

`Reserved12`

Reserved.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddcdrm.h (include Ntddcdrm.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff551366">CDROM_READ_TOC_EX</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff551375">CDROM_TOC_ATIP_DATA</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559367">IOCTL_CDROM_READ_TOC_EX</a>