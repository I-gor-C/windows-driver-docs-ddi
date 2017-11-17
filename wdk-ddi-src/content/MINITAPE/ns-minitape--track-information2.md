---
UID: NS.minitape._TRACK_INFORMATION2
title: TRACK_INFORMATION2
author: windows-driver-content
description: 
ms.assetid: abeabd03-2cc1-4dd7-aa06-5d9e77db4560
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: TRACK_INFORMATION2, TRACK_INFORMATION2, *PTRACK_INFORMATION2
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

# TRACK_INFORMATION2 structure

## -description



## -struct-fields

### -field UCHAR [2] Length			
 	
### -field UCHAR TrackNumberLsb			
 	
### -field UCHAR SessionNumberLsb			
 	
### -field UCHAR Reserved4			
 	
### -field UCHAR  : 4 TrackMode			
 	
### -field UCHAR  : 1 Copy			
 	
### -field UCHAR  : 1 Damage			
 	
### -field UCHAR  : 2 Reserved5			
 	
### -field UCHAR  : 4 DataMode			
 	
### -field UCHAR  : 1 FixedPacket			
 	
### -field UCHAR  : 1 Packet			
 	
### -field UCHAR  : 1 Blank			
 	
### -field UCHAR  : 1 ReservedTrack			
 	
### -field UCHAR  : 1 NWA_V			
 	
### -field UCHAR  : 1 LRA_V			
 	
### -field UCHAR  : 6 Reserved6			
 	
### -field UCHAR [4] TrackStartAddress			
 	
### -field UCHAR [4] NextWritableAddress			
 	
### -field UCHAR [4] FreeBlocks			
 	
### -field UCHAR [4] FixedPacketSize			
 	
### -field UCHAR [4] TrackSize			
 	
### -field UCHAR [4] LastRecordedAddress			
 	
### -field UCHAR TrackNumberMsb			
 	
### -field UCHAR SessionNumberMsb			
 	
### -field UCHAR [2] Reserved7			
 	
## -remarks

## -see-also