---
UID: NS.ntddcdvd._DVD_DISC_CONTROL_BLOCK_WRITE_INHIBIT
title: DVD_DISC_CONTROL_BLOCK_WRITE_INHIBIT
author: windows-driver-content
description: 
ms.assetid: 2419052e-be20-4fc0-967a-e88d3c2da0be
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DVD_DISC_CONTROL_BLOCK_WRITE_INHIBIT, DVD_DISC_CONTROL_BLOCK_WRITE_INHIBIT, *PDVD_DISC_CONTROL_BLOCK_WRITE_INHIBIT
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

# DVD_DISC_CONTROL_BLOCK_WRITE_INHIBIT structure

## -description



## -struct-fields

### -field union WriteProtectActions			
 	
### -field __unnamed_union_0ae5_10 __unnamed_union_0ae5_10			
 	
### -field DVD_DISC_CONTROL_BLOCK_HEADER header			
 	
### -field UCHAR [4] UpdateCount			
 	
### -field UCHAR [16] Reserved0			
 	
### -field UCHAR [32] UpdatePassword			
 	
### -field UCHAR [32672] Reserved1			
 	
### -field UCHAR [3] ReservedDoNotUse_UseAsByteInstead_0			
 	
### -field UCHAR  : 2 WriteProtectStatus			
 	
### -field UCHAR  : 5 ReservedDoNotUse_UseAsByteInstead_1			
 	
### -field UCHAR  : 1 UpdateRequiresPassword			
 	
### -field UCHAR [4] AsByte			
 	
## -remarks

## -see-also