---
UID: NS.storport.PWRITE_USING_TOKEN_HEADER
title: PWRITE_USING_TOKEN_HEADER
author: windows-driver-content
description: 
ms.assetid: 3a3d3578-2e65-4950-9bec-9509bac616a9
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PWRITE_USING_TOKEN_HEADER, WRITE_USING_TOKEN_HEADER, *PWRITE_USING_TOKEN_HEADER
req.header: storport.h
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

# PWRITE_USING_TOKEN_HEADER structure

## -description



## -struct-fields

### -field UCHAR [2] WriteUsingTokenDataLength			
 	
### -field UCHAR  : 1 Immediate			
 	
### -field UCHAR  : 7 Reserved1			
 	
### -field UCHAR [5] Reserved2			
 	
### -field UCHAR [8] BlockOffsetIntoToken			
 	
### -field UCHAR [BLOCK_DEVICE_TOKEN_SIZE] Token			
 	
### -field UCHAR [6] Reserved3			
 	
### -field UCHAR [2] BlockDeviceRangeDescriptorListLength			
 	
### -field UCHAR [ANYSIZE_ARRAY] BlockDeviceRangeDescriptor			
 	
## -remarks

## -see-also