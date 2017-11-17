---
UID: NS.minitape._MODE_FLEXIBLE_DISK_PAGE
title: MODE_FLEXIBLE_DISK_PAGE
author: windows-driver-content
description: 
ms.assetid: 028db5ea-48e7-4d65-9207-831e0b451d43
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MODE_FLEXIBLE_DISK_PAGE, MODE_FLEXIBLE_DISK_PAGE, *PMODE_FLEXIBLE_DISK_PAGE
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

# MODE_FLEXIBLE_DISK_PAGE structure

## -description



## -struct-fields

### -field UCHAR  : 6 PageCode			
 	
### -field UCHAR  : 1 Reserved			
 	
### -field UCHAR  : 1 PageSavable			
 	
### -field UCHAR PageLength			
 	
### -field UCHAR [2] TransferRate			
 	
### -field UCHAR NumberOfHeads			
 	
### -field UCHAR SectorsPerTrack			
 	
### -field UCHAR [2] BytesPerSector			
 	
### -field UCHAR [2] NumberOfCylinders			
 	
### -field UCHAR [2] StartWritePrecom			
 	
### -field UCHAR [2] StartReducedCurrent			
 	
### -field UCHAR [2] StepRate			
 	
### -field UCHAR StepPluseWidth			
 	
### -field UCHAR [2] HeadSettleDelay			
 	
### -field UCHAR MotorOnDelay			
 	
### -field UCHAR MotorOffDelay			
 	
### -field UCHAR  : 5 Reserved2			
 	
### -field UCHAR  : 1 MotorOnAsserted			
 	
### -field UCHAR  : 1 StartSectorNumber			
 	
### -field UCHAR  : 1 TrueReadySignal			
 	
### -field UCHAR  : 4 StepPlusePerCyclynder			
 	
### -field UCHAR  : 4 Reserved3			
 	
### -field UCHAR WriteCompenstation			
 	
### -field UCHAR HeadLoadDelay			
 	
### -field UCHAR HeadUnloadDelay			
 	
### -field UCHAR  : 4 Pin2Usage			
 	
### -field UCHAR  : 4 Pin34Usage			
 	
### -field UCHAR  : 4 Pin1Usage			
 	
### -field UCHAR  : 4 Pin4Usage			
 	
### -field UCHAR [2] MediumRotationRate			
 	
### -field UCHAR [2] Reserved4			
 	
## -remarks

## -see-also