---
UID: NS.usb._URB_ISOCH_TRANSFER
title: URB_ISOCH_TRANSFER
author: windows-driver-content
description: 
ms.assetid: 279683c8-b2a9-4cb6-a924-6bc9d40083f8
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: URB_ISOCH_TRANSFER, 
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

# URB_ISOCH_TRANSFER structure

## -description



## -struct-fields

### -field struct Hdr			
 	
### -field _URB_HEADER _URB_HEADER			
 	
### -field struct _URB			
 	
### -field _URB * UrbLink			
 	
### -field struct hca			
 	
### -field _URB_HCD_AREA _URB_HCD_AREA			
 	
### -field USBD_PIPE_HANDLE PipeHandle			
 	
### -field ULONG TransferFlags			
 	
### -field ULONG TransferBufferLength			
 	
### -field PVOID TransferBuffer			
 	
### -field PMDL TransferBufferMDL			
 	
### -field ULONG StartFrame			
 	
### -field ULONG NumberOfPackets			
 	
### -field ULONG ErrorCount			
 	
### -field USBD_ISO_PACKET_DESCRIPTOR [1] IsoPacket			
 	
## -remarks

## -see-also