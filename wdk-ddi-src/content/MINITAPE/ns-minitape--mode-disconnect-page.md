---
UID: NS.minitape._MODE_DISCONNECT_PAGE
title: MODE_DISCONNECT_PAGE
author: windows-driver-content
description: 
ms.assetid: 486c2c35-f4d4-4552-aa67-ea8574504837
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MODE_DISCONNECT_PAGE, MODE_DISCONNECT_PAGE, *PMODE_DISCONNECT_PAGE
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

# MODE_DISCONNECT_PAGE structure

## -description



## -struct-fields

### -field UCHAR  : 6 PageCode			
 	
### -field UCHAR  : 1 Reserved			
 	
### -field UCHAR  : 1 PageSavable			
 	
### -field UCHAR PageLength			
 	
### -field UCHAR BufferFullRatio			
 	
### -field UCHAR BufferEmptyRatio			
 	
### -field UCHAR [2] BusInactivityLimit			
 	
### -field UCHAR [2] BusDisconnectTime			
 	
### -field UCHAR [2] BusConnectTime			
 	
### -field UCHAR [2] MaximumBurstSize			
 	
### -field UCHAR  : 2 DataTransferDisconnect			
 	
### -field UCHAR [3] Reserved2			
 	
## -remarks

## -see-also