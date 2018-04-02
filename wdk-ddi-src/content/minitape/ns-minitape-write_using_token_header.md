---
UID: NS:minitape.WRITE_USING_TOKEN_HEADER
title: WRITE_USING_TOKEN_HEADER
author: windows-driver-content
description: The WRITE_USING_TOKEN_HEADER structure describes the destination data locations for an offload write data operation.
old-location: storage\write_using_token_header.htm
old-project: storage
ms.assetid: A46ED23A-7DB0-4792-B903-F748BCDAD55E
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PWRITE_USING_TOKEN_HEADER, PWRITE_USING_TOKEN_HEADER, PWRITE_USING_TOKEN_HEADER structure pointer [Storage Devices], WRITE_USING_TOKEN_HEADER, WRITE_USING_TOKEN_HEADER structure [Storage Devices], scsi/PWRITE_USING_TOKEN_HEADER, scsi/WRITE_USING_TOKEN_HEADER, storage.write_using_token_header"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: minitape.h
req.include-header: Scsi.h, Minitape.h, Storport.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
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
-	scsi.h
api_name:
-	WRITE_USING_TOKEN_HEADER
product:
- Windows
targetos: Windows
req.typenames: WRITE_USING_TOKEN_HEADER, *PWRITE_USING_TOKEN_HEADER
---

# WRITE_USING_TOKEN_HEADER structure
The <b>WRITE_USING_TOKEN_HEADER</b> structure describes the destination data locations for an offload write data operation.  The offload write data operation described by this structure is associated with a token representation of data (ROD).

## Syntax
```
typedef struct WRITE_USING_TOKEN_HEADER {
  UCHAR      WriteUsingTokenDataLength[2];
  UCHAR  : 1 Immediate;
  UCHAR  : 7 Reserved1;
  UCHAR      Reserved2[5];
  UCHAR      BlockOffsetIntoToken[8];
  UCHAR      Token[BLOCK_DEVICE_TOKEN_SIZE];
  UCHAR      Reserved3[6];
  UCHAR      BlockDeviceRangeDescriptorListLength[2];
  UCHAR      BlockDeviceRangeDescriptor[ANYSIZE_ARRAY];
} *PWRITE_USING_TOKEN_HEADER, WRITE_USING_TOKEN_HEADER;
```

## Members


`WriteUsingTokenDataLength`

The length of this structure beginning with the <i>Immediate</i> parameter and include all of the elements of the <b>BlockDeviceRangeDescriptor</b> array.

`Immediate`

If set, the status of the WRITE USING TOKEN command is returned immediately after receipt and validation of the token ROD and range descriptors. Otherwise, status is returned after all command processing is complete.

`Reserved1`

Reserved bits.

`Reserved2`

Reserved.

`BlockOffsetIntoToken`

The offset, in logical blocks,  in the ROD for <b>Token</b> indicating the start of the source data for the offload write data operation.

`Token`

A token created by a previous the POPULATE TOKEN command operation.

`Reserved3`

Reserved.

`BlockDeviceRangeDescriptorListLength`

The length, in bytes, for all  of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh967727">BLOCK_DEVICE_RANGE_DESCRIPTOR</a> structures in the <b>BlockDeviceRangeDescriptor</b> array.

`BlockDeviceRangeDescriptor`

An array of <a href="https://msdn.microsoft.com/library/windows/hardware/hh967727">BLOCK_DEVICE_RANGE_DESCRIPTOR</a> structures which describe the destination data blocks for the offload write data transfer.

## Remarks
All multibyte values are in big endian format. Prior to setting, these values must be converted from the endian format of the current platform.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 8. Available starting with Windows 8. |
| **Header** | minitape.h (include Scsi.h, Minitape.h, Storport.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh967727">BLOCK_DEVICE_RANGE_DESCRIPTOR</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh967730">POPULATE_TOKEN_HEADER</a>