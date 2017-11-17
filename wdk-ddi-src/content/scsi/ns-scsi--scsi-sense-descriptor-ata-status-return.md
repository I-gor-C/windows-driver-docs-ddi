---
UID: NS.scsi._SCSI_SENSE_DESCRIPTOR_ATA_STATUS_RETURN
title: SCSI_SENSE_DESCRIPTOR_ATA_STATUS_RETURN
author: windows-driver-content
description: 
ms.assetid: ac1677e4-0153-4977-8fe8-3b6de98c66ff
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SCSI_SENSE_DESCRIPTOR_ATA_STATUS_RETURN, SCSI_SENSE_DESCRIPTOR_ATA_STATUS_RETURN, *PSCSI_SENSE_DESCRIPTOR_ATA_STATUS_RETURN
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

# SCSI_SENSE_DESCRIPTOR_ATA_STATUS_RETURN structure

## -description



## -struct-fields

### -field SCSI_SENSE_DESCRIPTOR_HEADER Header			
 	
### -field UCHAR  : 1 Extend			
 	
### -field UCHAR  : 7 Reserved1			
 	
### -field UCHAR Error			
 	
### -field UCHAR SectorCount15_8			
 	
### -field UCHAR SectorCount7_0			
 	
### -field UCHAR LbaLow15_8			
 	
### -field UCHAR LbaLow7_0			
 	
### -field UCHAR LbaMid15_8			
 	
### -field UCHAR LbaMid7_0			
 	
### -field UCHAR LbaHigh15_8			
 	
### -field UCHAR LbaHigh7_0			
 	
### -field UCHAR Device			
 	
### -field UCHAR Status			
 	
## -remarks

## -see-also