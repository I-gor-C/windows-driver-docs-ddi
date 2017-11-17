---
UID: NS.minitape._TRACK_INFORMATION
title: TRACK_INFORMATION
author: windows-driver-content
description: 
ms.assetid: 15efdb1f-9a23-4129-bcd3-dcbddcc773d7
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: TRACK_INFORMATION, TRACK_INFORMATION, *PTRACK_INFORMATION
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

# TRACK_INFORMATION structure

## -description



## -struct-fields

### -field UCHAR [2] Length			
 	
### -field UCHAR TrackNumber			
 	
### -field UCHAR SessionNumber			
 	
### -field UCHAR Reserved1			
 	
### -field UCHAR  : 4 TrackMode			
 	
### -field UCHAR  : 1 Copy			
 	
### -field UCHAR  : 1 Damage			
 	
### -field UCHAR  : 2 Reserved2			
 	
### -field UCHAR  : 4 DataMode			
 	
### -field UCHAR  : 1 FP			
 	
### -field UCHAR  : 1 Packet			
 	
### -field UCHAR  : 1 Blank			
 	
### -field UCHAR  : 1 RT			
 	
### -field UCHAR  : 1 NWA_V			
 	
### -field UCHAR  : 7 Reserved3			
 	
### -field UCHAR [4] TrackStartAddress			
 	
### -field UCHAR [4] NextWritableAddress			
 	
### -field UCHAR [4] FreeBlocks			
 	
### -field UCHAR [4] FixedPacketSize			
 	
## -remarks

## -see-also