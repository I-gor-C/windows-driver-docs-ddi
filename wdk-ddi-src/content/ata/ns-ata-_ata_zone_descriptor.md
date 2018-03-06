---
UID: NS:ata._ATA_ZONE_DESCRIPTOR
title: "_ATA_ZONE_DESCRIPTOR"
author: windows-driver-content
description: This structure is for internal use only and should not be called from your code.
old-location: storage\ata_zone_descriptor.htm
old-project: storage
ms.assetid: 2e027ac5-7b5d-43cc-8d37-c0a3e77e68c9
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PATA_ZONE_DESCRIPTOR, ATA_ZONE_DESCRIPTOR, ATA_ZONE_DESCRIPTOR structure [Storage Devices], PATA_ZONE_DESCRIPTOR, PATA_ZONE_DESCRIPTOR structure pointer [Storage Devices], _ATA_ZONE_DESCRIPTOR, ata/ATA_ZONE_DESCRIPTOR, ata/PATA_ZONE_DESCRIPTOR, storage.ata_zone_descriptor"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ata.h
req.include-header: 
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
-	Ata.h
api_name:
-	ATA_ZONE_DESCRIPTOR
product: Windows
targetos: Windows
req.typenames: ATA_ZONE_DESCRIPTOR, *PATA_ZONE_DESCRIPTOR
---

# _ATA_ZONE_DESCRIPTOR structure
This structure is for internal use only and should not be called from your code.

## Syntax
````
typedef struct _ATA_ZONE_DESCRIPTOR {
  UCHAR     ZoneType  : 4;
  UCHAR     Reserved0  : 4;
  UCHAR     Reset  : 1;
  UCHAR     NonSeq : 1;
  UCHAR     Reserved1  : 2;
  UCHAR     ZoneCondition  : 4;
  UCHAR     Reserved2[6];
  ULONGLONG ZoneLength  : 48;
  ULONGLONG Reserved3  : 16;
  ULONGLONG ZoneStartLBA  : 48;
  ULONGLONG Reserved4  : 16;
  ULONGLONG WritePointerLBA  : 48;
  ULONGLONG Reserved5  : 16;
  UCHAR     Reserved6[32];
} ATA_ZONE_DESCRIPTOR, *PATA_ZONE_DESCRIPTOR;
````

## Members


`NonSeq`



`Reserved0`



`Reserved1`



`Reserved2`

N/A

`Reserved3`



`Reserved4`



`Reserved5`



`Reserved6`

N/A

`Reset`



`WritePointerLBA`



`ZoneCondition`



`ZoneLength`



`ZoneStartLBA`



`ZoneType`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ata.h |