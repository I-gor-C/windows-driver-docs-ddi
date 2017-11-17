---
UID: NS.ntddcdvd._DVD_DISC_CONTROL_BLOCK_HEADER
title: DVD_DISC_CONTROL_BLOCK_HEADER
author: windows-driver-content
description: 
ms.assetid: 5aa2f8c6-bf3c-4bc6-90e8-bd66e9de8c0b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DVD_DISC_CONTROL_BLOCK_HEADER, DVD_DISC_CONTROL_BLOCK_HEADER, *PDVD_DISC_CONTROL_BLOCK_HEADER
req.header: ntddcdvd.h
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

# DVD_DISC_CONTROL_BLOCK_HEADER structure

## -description



## -struct-fields

### -field union ProhibitedActions			
 	
### -field __unnamed_union_0ae5_8 __unnamed_union_0ae5_8			
 	
### -field UCHAR [4] ContentDescriptor			
 	
### -field UCHAR [32] VendorId			
 	
### -field UCHAR [3] ReservedDoNotUse_UseAsByteInstead_0			
 	
### -field UCHAR  : 1 RecordingWithinTheUserDataArea			
 	
### -field UCHAR  : 1 ReadingDiscControlBlocks			
 	
### -field UCHAR  : 1 FormattingTheMedium			
 	
### -field UCHAR  : 1 ModificationOfThisDiscControlBlock			
 	
### -field UCHAR  : 4 ReservedDoNotUse_UseAsByteInstead_1			
 	
### -field UCHAR [4] AsByte			
 	
## -remarks

## -see-also