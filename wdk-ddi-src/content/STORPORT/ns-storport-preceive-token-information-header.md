---
UID: NS.storport.PRECEIVE_TOKEN_INFORMATION_HEADER
title: PRECEIVE_TOKEN_INFORMATION_HEADER
author: windows-driver-content
description: 
ms.assetid: b54168cc-7189-4e10-9c8d-f050bd09f0b7
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PRECEIVE_TOKEN_INFORMATION_HEADER, RECEIVE_TOKEN_INFORMATION_HEADER, *PRECEIVE_TOKEN_INFORMATION_HEADER
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

# PRECEIVE_TOKEN_INFORMATION_HEADER structure

## -description



## -struct-fields

### -field UCHAR [4] AvailableData			
 	
### -field UCHAR  : 5 ResponseToServiceAction			
 	
### -field UCHAR  : 3 Reserved1			
 	
### -field UCHAR  : 7 OperationStatus			
 	
### -field UCHAR  : 1 Reserved2			
 	
### -field UCHAR [2] OperationCounter			
 	
### -field UCHAR [4] EstimatedStatusUpdateDelay			
 	
### -field UCHAR CompletionStatus			
 	
### -field UCHAR SenseDataFieldLength			
 	
### -field UCHAR SenseDataLength			
 	
### -field UCHAR TransferCountUnits			
 	
### -field UCHAR [8] TransferCount			
 	
### -field UCHAR [2] SegmentsProcessed			
 	
### -field UCHAR [6] Reserved3			
 	
### -field UCHAR [ANYSIZE_ARRAY] SenseData			
 	
## -remarks

## -see-also