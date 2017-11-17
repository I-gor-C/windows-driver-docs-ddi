---
UID: NS.storport._VPD_BLOCK_LIMITS_PAGE
title: VPD_BLOCK_LIMITS_PAGE
author: windows-driver-content
description: 
ms.assetid: 9164f154-88ba-4a22-9edc-d554b16abdfa
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: VPD_BLOCK_LIMITS_PAGE, VPD_BLOCK_LIMITS_PAGE, *PVPD_BLOCK_LIMITS_PAGE
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

# VPD_BLOCK_LIMITS_PAGE structure

## -description



## -struct-fields

### -field union __unnamed_union_0c6c_21			
 	
### -field UCHAR  : 5 DeviceType			
 	
### -field UCHAR  : 3 DeviceTypeQualifier			
 	
### -field UCHAR PageCode			
 	
### -field UCHAR [2] PageLength			
 	
### -field union __unnamed_union_0c6c_23			
 	
### -field UCHAR Reserved0			
 	
### -field UCHAR MaximumCompareAndWriteLength			
 	
### -field UCHAR [2] OptimalTransferLengthGranularity			
 	
### -field UCHAR [4] MaximumTransferLength			
 	
### -field UCHAR [4] OptimalTransferLength			
 	
### -field UCHAR [4] MaxPrefetchXDReadXDWriteTransferLength			
 	
### -field UCHAR [4] MaximumUnmapLBACount			
 	
### -field UCHAR [4] MaximumUnmapBlockDescriptorCount			
 	
### -field UCHAR [4] OptimalUnmapGranularity			
 	
### -field UCHAR [28] Reserved1			
 	
### -field UCHAR  : 7 UnmapGranularityAlignmentByte3			
 	
### -field UCHAR  : 1 UGAValid			
 	
### -field UCHAR UnmapGranularityAlignmentByte2			
 	
### -field UCHAR UnmapGranularityAlignmentByte1			
 	
### -field UCHAR UnmapGranularityAlignmentByte0			
 	
### -field UCHAR [4] UnmapGranularityAlignment			
 	
### -field UCHAR [0] Descriptors			
 	
## -remarks

## -see-also