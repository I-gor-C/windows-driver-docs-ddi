---
UID: NS.ntifs._ENCRYPTED_DATA_INFO
title: ENCRYPTED_DATA_INFO
author: windows-driver-content
description: 
ms.assetid: f055602b-03dd-40dc-bfdf-2ced391477c5
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: ENCRYPTED_DATA_INFO, ENCRYPTED_DATA_INFO, *PENCRYPTED_DATA_INFO
req.header: ntifs.h
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

# ENCRYPTED_DATA_INFO structure

## -description



## -struct-fields

### -field ULONGLONG StartingFileOffset			
 	
### -field ULONG OutputBufferOffset			
 	
### -field ULONG BytesWithinFileSize			
 	
### -field ULONG BytesWithinValidDataLength			
 	
### -field USHORT CompressionFormat			
 	
### -field UCHAR DataUnitShift			
 	
### -field UCHAR ChunkShift			
 	
### -field UCHAR ClusterShift			
 	
### -field UCHAR EncryptionFormat			
 	
### -field USHORT NumberOfDataBlocks			
 	
### -field ULONG [ANYSIZE_ARRAY] DataBlockSize			
 	
## -remarks

## -see-also