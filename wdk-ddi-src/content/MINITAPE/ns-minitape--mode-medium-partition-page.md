---
UID: NS.minitape._MODE_MEDIUM_PARTITION_PAGE
title: MODE_MEDIUM_PARTITION_PAGE
author: windows-driver-content
description: 
ms.assetid: 5f49cfb2-8038-490c-b701-d2852f8f5d43
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MODE_MEDIUM_PARTITION_PAGE, MODE_MEDIUM_PARTITION_PAGE, *PMODE_MEDIUM_PARTITION_PAGE
req.header: minitape.h
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

# MODE_MEDIUM_PARTITION_PAGE structure

## -description



## -struct-fields

### -field UCHAR  : 6 PageCode			
 	
### -field UCHAR  : 1 Reserved1			
 	
### -field UCHAR  : 1 PSBit			
 	
### -field UCHAR PageLength			
 	
### -field UCHAR MaximumAdditionalPartitions			
 	
### -field UCHAR AdditionalPartitionDefined			
 	
### -field UCHAR  : 3 Reserved2			
 	
### -field UCHAR  : 2 PSUMBit			
 	
### -field UCHAR  : 1 IDPBit			
 	
### -field UCHAR  : 1 SDPBit			
 	
### -field UCHAR  : 1 FDPBit			
 	
### -field UCHAR MediumFormatRecognition			
 	
### -field UCHAR [2] Reserved3			
 	
### -field UCHAR [2] Partition0Size			
 	
### -field UCHAR [2] Partition1Size			
 	
## -remarks

## -see-also