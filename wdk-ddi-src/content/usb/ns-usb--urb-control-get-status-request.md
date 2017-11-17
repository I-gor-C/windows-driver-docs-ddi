---
UID: NS.usb._URB_CONTROL_GET_STATUS_REQUEST
title: URB_CONTROL_GET_STATUS_REQUEST
author: windows-driver-content
description: 
ms.assetid: 9866fce7-4188-473f-ab93-d31141a29da2
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: URB_CONTROL_GET_STATUS_REQUEST, 
req.header: usb.h
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

# URB_CONTROL_GET_STATUS_REQUEST structure

## -description



## -struct-fields

### -field struct Hdr			
 	
### -field _URB_HEADER _URB_HEADER			
 	
### -field struct _URB			
 	
### -field _URB * UrbLink			
 	
### -field struct hca			
 	
### -field _URB_HCD_AREA _URB_HCD_AREA			
 	
### -field PVOID Reserved			
 	
### -field ULONG Reserved0			
 	
### -field ULONG TransferBufferLength			
 	
### -field PVOID TransferBuffer			
 	
### -field PMDL TransferBufferMDL			
 	
### -field UCHAR [4] Reserved1			
 	
### -field USHORT Index			
 	
### -field USHORT Reserved2			
 	
## -remarks

## -see-also