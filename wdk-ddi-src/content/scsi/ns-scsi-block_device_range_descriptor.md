---
UID: NS:scsi.BLOCK_DEVICE_RANGE_DESCRIPTOR
title: BLOCK_DEVICE_RANGE_DESCRIPTOR
author: windows-driver-content
description: The BLOCK_DEVICE_RANGE_DESCRIPTOR structure describes a range of logical blocks associated with various fragments of a file for an offload copy operation.
old-location: storage\block_device_range_descriptor.htm
old-project: storage
ms.assetid: 6B262D38-8BD6-43B5-96AB-6D311B8EBA88
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PBLOCK_DEVICE_RANGE_DESCRIPTOR, BLOCK_DEVICE_RANGE_DESCRIPTOR, BLOCK_DEVICE_RANGE_DESCRIPTOR structure [Storage Devices], PBLOCK_DEVICE_RANGE_DESCRIPTOR, PBLOCK_DEVICE_RANGE_DESCRIPTOR structure pointer [Storage Devices], scsi/BLOCK_DEVICE_RANGE_DESCRIPTOR, scsi/PBLOCK_DEVICE_RANGE_DESCRIPTOR, storage.block_device_range_descriptor"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: scsi.h
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
-	BLOCK_DEVICE_RANGE_DESCRIPTOR
product: Windows
targetos: Windows
req.typenames: BLOCK_DEVICE_RANGE_DESCRIPTOR, *PBLOCK_DEVICE_RANGE_DESCRIPTOR
req.product: Windows 10 or later.
---

# BLOCK_DEVICE_RANGE_DESCRIPTOR structure
The <b>BLOCK_DEVICE_RANGE_DESCRIPTOR</b> structure describes a range of logical blocks associated with various fragments of a file for an offload copy operation.

## Syntax
````
typedef struct _BLOCK_DEVICE_RANGE_DESCRIPTOR {
  UCHAR LogicalBlockAddress[8];
  UCHAR TransferLength[4];
  UCHAR Reserved[4];
} BLOCK_DEVICE_RANGE_DESCRIPTOR, *PBLOCK_DEVICE_RANGE_DESCRIPTOR;
````

## Members


`LogicalBlockAddress`

The starting logical block address of a block range.

`TransferLength`

The length, in logical blocks, of the block range.

`Reserved`

Reserved bytes.

## Remarks
If <i>TransferLength</i> is set to 0, the range descriptor is considered valid and does not cause an error when included in a token parameter list. No operation will be performed for this descriptor.

All multibyte values are in big endian format. Prior to setting, these values must be converted from the endian format of the current platform.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 8. Available starting with Windows 8. |
| **Header** | scsi.h (include Scsi.h, Minitape.h, Storport.h) |

## See Also

<a href="..\storport\ns-storport-write_using_token_header.md">WRITE_USING_TOKEN_HEADER</a>



<a href="..\storport\ns-storport-populate_token_header.md">POPULATE_TOKEN_HEADER</a>