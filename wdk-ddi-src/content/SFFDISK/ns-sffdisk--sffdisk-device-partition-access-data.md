---
UID: NS.sffdisk._SFFDISK_DEVICE_PARTITION_ACCESS_DATA
title: SFFDISK_DEVICE_PARTITION_ACCESS_DATA
author: windows-driver-content
description: 
ms.assetid: 33f44c02-a935-4ae6-a709-8d333a0a2b1e
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SFFDISK_DEVICE_PARTITION_ACCESS_DATA, SFFDISK_DEVICE_PARTITION_ACCESS_DATA, *PSFFDISK_DEVICE_PARTITION_ACCESS_DATA
req.header: sffdisk.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# SFFDISK_DEVICE_PARTITION_ACCESS_DATA structure

## -description



## -struct-fields

### -field union Parameters			
 	
### -field __unnamed_union_0c62_4 __unnamed_union_0c62_4			
 	
### -field ULONG Size			
 	
### -field SFFDISK_PARTITION_ACCESS Command			
 	
### -field ULONG [2] Reserved			
 	
### -field ULONG SizeInBytes			
 	
### -field ULONG MaxReliableWriteSizeInBytes			
 	
### -field ULONG [4] Reserved			
 	
### -field SFFDISK_DEVICE_RPMB_DATA_FRAME ResultFrame			
 	
### -field SFFDISK_DEVICE_RPMB_DATA_FRAME ProgramAuthKeyFrame			
 	
### -field ULONG [4] Reserved			
 	
### -field SFFDISK_DEVICE_RPMB_DATA_FRAME ResultFrame			
 	
### -field SFFDISK_DEVICE_RPMB_DATA_FRAME QueryWriteCounterFrame			
 	
### -field ULONG CountToWrite			
 	
### -field ULONG [3] Reserved			
 	
### -field SFFDISK_DEVICE_RPMB_DATA_FRAME ResultFrame			
 	
### -field SFFDISK_DEVICE_RPMB_DATA_FRAME [1] FrameDataToWrite			
 	
### -field ULONG CountToRead			
 	
### -field ULONG [3] Reserved			
 	
### -field SFFDISK_DEVICE_RPMB_DATA_FRAME AuthenticatedReadFrame			
 	
### -field SFFDISK_DEVICE_RPMB_DATA_FRAME [1] ReturnedFrameData			
 	
### -field ULONGLONG Gpp_1_SizeInBytes			
 	
### -field ULONGLONG Gpp_2_SizeInBytes			
 	
### -field ULONGLONG Gpp_3_SizeInBytes			
 	
### -field ULONGLONG Gpp_4_SizeInBytes			
 	
### -field ULONG GppBlockSize			
 	
### -field ULONG GppPartitionId			
 	
### -field ULONG Length			
 	
### -field ULONGLONG Offset			
 	
### -field UCHAR [1024] Data			
 	
## -remarks

## -see-also