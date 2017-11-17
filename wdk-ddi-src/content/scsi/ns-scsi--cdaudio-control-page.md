---
UID: NS.scsi._CDAUDIO_CONTROL_PAGE
title: CDAUDIO_CONTROL_PAGE
author: windows-driver-content
description: 
ms.assetid: d32fcf95-7b31-4981-8526-27dfed380199
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: CDAUDIO_CONTROL_PAGE, CDAUDIO_CONTROL_PAGE, *PCDAUDIO_CONTROL_PAGE
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

# CDAUDIO_CONTROL_PAGE structure

## -description



## -struct-fields

### -field UCHAR  : 6 PageCode			
 	
### -field UCHAR  : 1 Reserved			
 	
### -field UCHAR  : 1 PSBit			
 	
### -field UCHAR PageLength			
 	
### -field UCHAR  : 1 Reserved2			
 	
### -field UCHAR  : 1 StopOnTrackCrossing			
 	
### -field UCHAR  : 1 Immediate			
 	
### -field UCHAR  : 5 Reserved3			
 	
### -field UCHAR [3] Reserved4			
 	
### -field UCHAR [2] Obsolete			
 	
### -field CDDA_OUTPUT_PORT [4] CDDAOutputPorts			
 	
## -remarks

## -see-also