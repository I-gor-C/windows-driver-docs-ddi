---
UID: NS.scsi._MODE_RIGID_GEOMETRY_PAGE
title: MODE_RIGID_GEOMETRY_PAGE
author: windows-driver-content
description: 
ms.assetid: 80c182d3-ad3e-40a2-9e23-8d827f8298cd
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MODE_RIGID_GEOMETRY_PAGE, MODE_RIGID_GEOMETRY_PAGE, *PMODE_RIGID_GEOMETRY_PAGE
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

# MODE_RIGID_GEOMETRY_PAGE structure

## -description



## -struct-fields

### -field UCHAR  : 6 PageCode			
 	
### -field UCHAR  : 1 Reserved			
 	
### -field UCHAR  : 1 PageSavable			
 	
### -field UCHAR PageLength			
 	
### -field UCHAR [3] NumberOfCylinders			
 	
### -field UCHAR NumberOfHeads			
 	
### -field UCHAR [3] StartWritePrecom			
 	
### -field UCHAR [3] StartReducedCurrent			
 	
### -field UCHAR [2] DriveStepRate			
 	
### -field UCHAR [3] LandZoneCyclinder			
 	
### -field UCHAR  : 2 RotationalPositionLock			
 	
### -field UCHAR  : 6 Reserved2			
 	
### -field UCHAR RotationOffset			
 	
### -field UCHAR Reserved3			
 	
### -field UCHAR [2] RoataionRate			
 	
### -field UCHAR [2] Reserved4			
 	
## -remarks

## -see-also