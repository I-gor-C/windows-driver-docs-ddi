---
UID: NS.minitape._MODE_CDROM_WRITE_PARAMETERS_PAGE
title: MODE_CDROM_WRITE_PARAMETERS_PAGE
author: windows-driver-content
description: 
ms.assetid: 7de42f2a-a0f9-45da-9168-756f437fa912
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MODE_CDROM_WRITE_PARAMETERS_PAGE, MODE_CDROM_WRITE_PARAMETERS_PAGE, *PMODE_CDROM_WRITE_PARAMETERS_PAGE
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

# MODE_CDROM_WRITE_PARAMETERS_PAGE structure

## -description



## -struct-fields

### -field UCHAR PageLength			
 	
### -field UCHAR  : 4 WriteType			
 	
### -field UCHAR  : 1 TestWrite			
 	
### -field UCHAR  : 1 LinkSizeValid			
 	
### -field UCHAR  : 1 BufferUnderrunFreeEnabled			
 	
### -field UCHAR  : 1 Reserved2			
 	
### -field UCHAR  : 4 TrackMode			
 	
### -field UCHAR  : 1 Copy			
 	
### -field UCHAR  : 1 FixedPacket			
 	
### -field UCHAR  : 2 MultiSession			
 	
### -field UCHAR  : 4 DataBlockType			
 	
### -field UCHAR  : 4 Reserved3			
 	
### -field UCHAR LinkSize			
 	
### -field UCHAR Reserved4			
 	
### -field UCHAR  : 6 HostApplicationCode			
 	
### -field UCHAR  : 2 Reserved5			
 	
### -field UCHAR SessionFormat			
 	
### -field UCHAR Reserved6			
 	
### -field UCHAR [4] PacketSize			
 	
### -field UCHAR [2] AudioPauseLength			
 	
### -field UCHAR  : 7 Reserved7			
 	
### -field UCHAR  : 1 MediaCatalogNumberValid			
 	
### -field UCHAR [13] MediaCatalogNumber			
 	
### -field UCHAR MediaCatalogNumberZero			
 	
### -field UCHAR MediaCatalogNumberAFrame			
 	
### -field UCHAR  : 7 Reserved8			
 	
### -field UCHAR  : 1 ISRCValid			
 	
### -field UCHAR [2] ISRCCountry			
 	
### -field UCHAR [3] ISRCOwner			
 	
### -field UCHAR [2] ISRCRecordingYear			
 	
### -field UCHAR [5] ISRCSerialNumber			
 	
### -field UCHAR ISRCZero			
 	
### -field UCHAR ISRCAFrame			
 	
### -field UCHAR ISRCReserved			
 	
### -field UCHAR [4] SubHeaderData			
 	
## -remarks

## -see-also