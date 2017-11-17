---
UID: NS.scsi._MODE_INFO_EXCEPTIONS
title: MODE_INFO_EXCEPTIONS
author: windows-driver-content
description: 
ms.assetid: 505a9856-5b1a-4f2e-a1ff-9cc2e1ab6e42
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MODE_INFO_EXCEPTIONS, MODE_INFO_EXCEPTIONS, *PMODE_INFO_EXCEPTIONS
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

# MODE_INFO_EXCEPTIONS structure

## -description



## -struct-fields

### -field union __unnamed_union_0af3_37			
 	
### -field UCHAR  : 6 PageCode			
 	
### -field UCHAR  : 1 Reserved1			
 	
### -field UCHAR  : 1 PSBit			
 	
### -field UCHAR PageLength			
 	
### -field UCHAR  : 4 ReportMethod			
 	
### -field UCHAR  : 4 Reserved4			
 	
### -field UCHAR [4] IntervalTimer			
 	
### -field UCHAR [4] ReportCount			
 	
### -field UCHAR  : 1 LogErr			
 	
### -field UCHAR  : 1 Reserved2			
 	
### -field UCHAR  : 1 Test			
 	
### -field UCHAR  : 1 Dexcpt			
 	
### -field UCHAR  : 3 Reserved3			
 	
### -field UCHAR  : 1 Perf			
 	
### -field UCHAR Flags			
 	
## -remarks

## -see-also