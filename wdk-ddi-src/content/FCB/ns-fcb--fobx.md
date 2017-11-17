---
UID: NS.fcb._FOBX
title: FOBX
author: windows-driver-content
description: 
ms.assetid: b7f16cdf-c331-4e47-85aa-fbdbfebbc73c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: FOBX, FOBX, *PFOBX
req.header: fcb.h
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

# FOBX structure

## -description



## -struct-fields

### -field union Specific			
 	
### -field __unnamed_union_0bd5_12 __unnamed_union_0bd5_12			
 	
### -field __volatile ULONG FobxSerialNumber			
 	
### -field LIST_ENTRY FobxQLinks			
 	
### -field LIST_ENTRY ScavengerFinalizationList			
 	
### -field LIST_ENTRY ClosePendingList			
 	
### -field LARGE_INTEGER CloseTime			
 	
### -field BOOLEAN UpperFinalizationDone			
 	
### -field BOOLEAN ContainsWildCards			
 	
### -field BOOLEAN fOpenCountDecremented			
 	
### -field PRDBSS_DEVICE_OBJECT RxDeviceObject			
 	
### -field union __unnamed_union_0bd5_14			
 	
### -field LARGE_INTEGER CollectDataTime			
 	
### -field ULONG CollectDataSize			
 	
### -field THROTTLING_STATE ThrottlingState			
 	
### -field LIST_ENTRY ReadSerializationQueue			
 	
### -field LIST_ENTRY WriteSerializationQueue			
 	
### -field MRX_PIPE_HANDLE_INFORMATION PipeHandleInformation			
 	
### -field RXVBO PredictedReadOffset			
 	
### -field RXVBO PredictedWriteOffset			
 	
### -field THROTTLING_STATE LockThrottlingState			
 	
### -field LARGE_INTEGER LastLockOffset			
 	
### -field LARGE_INTEGER LastLockRange			
 	
## -remarks

## -see-also