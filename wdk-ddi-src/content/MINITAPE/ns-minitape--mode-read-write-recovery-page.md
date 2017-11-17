---
UID: NS.minitape._MODE_READ_WRITE_RECOVERY_PAGE
title: MODE_READ_WRITE_RECOVERY_PAGE
author: windows-driver-content
description: 
ms.assetid: a74d3803-33de-457f-b253-6ac1d5fe5f33
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MODE_READ_WRITE_RECOVERY_PAGE, MODE_READ_WRITE_RECOVERY_PAGE, *PMODE_READ_WRITE_RECOVERY_PAGE
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

# MODE_READ_WRITE_RECOVERY_PAGE structure

## -description



## -struct-fields

### -field UCHAR  : 6 PageCode			
 	
### -field UCHAR  : 1 Reserved1			
 	
### -field UCHAR  : 1 PSBit			
 	
### -field UCHAR PageLength			
 	
### -field UCHAR  : 1 DCRBit			
 	
### -field UCHAR  : 1 DTEBit			
 	
### -field UCHAR  : 1 PERBit			
 	
### -field UCHAR  : 1 EERBit			
 	
### -field UCHAR  : 1 RCBit			
 	
### -field UCHAR  : 1 TBBit			
 	
### -field UCHAR  : 1 ARRE			
 	
### -field UCHAR  : 1 AWRE			
 	
### -field UCHAR ReadRetryCount			
 	
### -field UCHAR [4] Reserved4			
 	
### -field UCHAR WriteRetryCount			
 	
### -field UCHAR [3] Reserved5			
 	
## -remarks

## -see-also