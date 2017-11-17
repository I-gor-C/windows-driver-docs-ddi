---
UID: NS.storport._MODE_FORMAT_PAGE
title: MODE_FORMAT_PAGE
author: windows-driver-content
description: 
ms.assetid: c8ad0d45-7131-41ca-8f07-83234bb2671e
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MODE_FORMAT_PAGE, MODE_FORMAT_PAGE, *PMODE_FORMAT_PAGE
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

# MODE_FORMAT_PAGE structure

## -description



## -struct-fields

### -field UCHAR  : 6 PageCode			
 	
### -field UCHAR  : 1 Reserved			
 	
### -field UCHAR  : 1 PageSavable			
 	
### -field UCHAR PageLength			
 	
### -field UCHAR [2] TracksPerZone			
 	
### -field UCHAR [2] AlternateSectorsPerZone			
 	
### -field UCHAR [2] AlternateTracksPerZone			
 	
### -field UCHAR [2] AlternateTracksPerLogicalUnit			
 	
### -field UCHAR [2] SectorsPerTrack			
 	
### -field UCHAR [2] BytesPerPhysicalSector			
 	
### -field UCHAR [2] Interleave			
 	
### -field UCHAR [2] TrackSkewFactor			
 	
### -field UCHAR [2] CylinderSkewFactor			
 	
### -field UCHAR  : 4 Reserved2			
 	
### -field UCHAR  : 1 SurfaceFirst			
 	
### -field UCHAR  : 1 RemovableMedia			
 	
### -field UCHAR  : 1 HardSectorFormating			
 	
### -field UCHAR  : 1 SoftSectorFormating			
 	
### -field UCHAR [3] Reserved3			
 	
## -remarks

## -see-also