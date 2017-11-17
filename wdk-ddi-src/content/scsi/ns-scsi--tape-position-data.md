---
UID: NS.scsi._TAPE_POSITION_DATA
title: TAPE_POSITION_DATA
author: windows-driver-content
description: 
ms.assetid: 3ee79392-0395-49c4-b62c-fb9a6cf2592f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: TAPE_POSITION_DATA, TAPE_POSITION_DATA, *PTAPE_POSITION_DATA
req.header: scsi.h
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

# TAPE_POSITION_DATA structure

## -description



## -struct-fields

### -field UCHAR  : 2 Reserved1			
 	
### -field UCHAR  : 1 BlockPositionUnsupported			
 	
### -field UCHAR  : 3 Reserved2			
 	
### -field UCHAR  : 1 EndOfPartition			
 	
### -field UCHAR  : 1 BeginningOfPartition			
 	
### -field UCHAR PartitionNumber			
 	
### -field USHORT Reserved3			
 	
### -field UCHAR [4] FirstBlock			
 	
### -field UCHAR [4] LastBlock			
 	
### -field UCHAR Reserved4			
 	
### -field UCHAR [3] NumberOfBlocks			
 	
### -field UCHAR [4] NumberOfBytes			
 	
## -remarks

## -see-also