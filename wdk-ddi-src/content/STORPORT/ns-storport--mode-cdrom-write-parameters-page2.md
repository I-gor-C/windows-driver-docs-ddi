---
UID: NS.storport._MODE_CDROM_WRITE_PARAMETERS_PAGE2
title: MODE_CDROM_WRITE_PARAMETERS_PAGE2
author: windows-driver-content
description: 
ms.assetid: 01add39b-a59e-4d8b-9016-bef5de60479c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MODE_CDROM_WRITE_PARAMETERS_PAGE2, MODE_CDROM_WRITE_PARAMETERS_PAGE2, *PMODE_CDROM_WRITE_PARAMETERS_PAGE2
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

# MODE_CDROM_WRITE_PARAMETERS_PAGE2 structure

## -description



## -struct-fields

### -field UCHAR  : 6 PageCode			
 	
### -field UCHAR  : 1 Reserved			
 	
### -field UCHAR  : 1 PageSavable			
 	
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
 	
### -field UCHAR [16] MediaCatalogNumber			
 	
### -field UCHAR [16] ISRC			
 	
### -field UCHAR [4] SubHeaderData			
 	
## -remarks

## -see-also