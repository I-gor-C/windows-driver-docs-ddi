---
UID: NS.ata._GP_LOG_NCQ_COMMAND_ERROR
title: GP_LOG_NCQ_COMMAND_ERROR
author: windows-driver-content
description: 
ms.assetid: e6fb2fef-f2a8-428d-898f-b180b72c2050
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: GP_LOG_NCQ_COMMAND_ERROR, GP_LOG_NCQ_COMMAND_ERROR, *PGP_LOG_NCQ_COMMAND_ERROR
req.header: ata.h
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

# GP_LOG_NCQ_COMMAND_ERROR structure

## -description



## -struct-fields

### -field UCHAR  : 5 NcqTag			
 	
### -field UCHAR  : 1 Reserved0			
 	
### -field UCHAR  : 1 UNL			
 	
### -field UCHAR  : 1 NonQueuedCmd			
 	
### -field UCHAR Reserved1			
 	
### -field UCHAR Status			
 	
### -field UCHAR Error			
 	
### -field UCHAR LBA7_0			
 	
### -field UCHAR LBA15_8			
 	
### -field UCHAR LBA23_16			
 	
### -field UCHAR Device			
 	
### -field UCHAR LBA31_24			
 	
### -field UCHAR LBA39_32			
 	
### -field UCHAR LBA47_40			
 	
### -field UCHAR Reserved2			
 	
### -field UCHAR Count7_0			
 	
### -field UCHAR Count15_8			
 	
### -field UCHAR SenseKey			
 	
### -field UCHAR ASC			
 	
### -field UCHAR ASCQ			
 	
### -field UCHAR [239] Reserved3			
 	
### -field UCHAR [255] Vendor			
 	
### -field UCHAR Checksum			
 	
## -remarks

## -see-also