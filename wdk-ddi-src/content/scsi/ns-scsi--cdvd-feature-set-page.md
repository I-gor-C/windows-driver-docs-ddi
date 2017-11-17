---
UID: NS.scsi._CDVD_FEATURE_SET_PAGE
title: CDVD_FEATURE_SET_PAGE
author: windows-driver-content
description: 
ms.assetid: d6385716-8930-49d4-9c7d-ac47f665229c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: CDVD_FEATURE_SET_PAGE, CDVD_FEATURE_SET_PAGE, *PCDVD_FEATURE_SET_PAGE
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

# CDVD_FEATURE_SET_PAGE structure

## -description



## -struct-fields

### -field UCHAR  : 6 PageCode			
 	
### -field UCHAR  : 1 Reserved			
 	
### -field UCHAR  : 1 PSBit			
 	
### -field UCHAR PageLength			
 	
### -field UCHAR [2] CDAudio			
 	
### -field UCHAR [2] EmbeddedChanger			
 	
### -field UCHAR [2] PacketSMART			
 	
### -field UCHAR [2] PersistantPrevent			
 	
### -field UCHAR [2] EventStatusNotification			
 	
### -field UCHAR [2] DigitalOutput			
 	
### -field UCHAR [2] CDSequentialRecordable			
 	
### -field UCHAR [2] DVDSequentialRecordable			
 	
### -field UCHAR [2] RandomRecordable			
 	
### -field UCHAR [2] KeyExchange			
 	
### -field UCHAR [2] Reserved2			
 	
## -remarks

## -see-also