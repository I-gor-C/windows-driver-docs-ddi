---
UID: NS.spbcx._SPB_CONTROLLER_CONFIG
title: SPB_CONTROLLER_CONFIG
author: windows-driver-content
description: 
ms.assetid: 2696bfbd-4e0d-4ad6-9fd1-79ebf6084c3b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SPB_CONTROLLER_CONFIG, 
req.header: spbcx.h
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

# SPB_CONTROLLER_CONFIG structure

## -description



## -struct-fields

### -field ULONG Size			
 	
### -field WDF_IO_QUEUE_DISPATCH_TYPE ControllerDispatchType			
 	
### -field WDF_TRI_STATE PowerManaged			
 	
### -field PFN_SPB_TARGET_CONNECT EvtSpbTargetConnect			
 	
### -field PFN_SPB_TARGET_DISCONNECT EvtSpbTargetDisconnect			
 	
### -field PFN_SPB_CONTROLLER_LOCK EvtSpbControllerLock			
 	
### -field PFN_SPB_CONTROLLER_UNLOCK EvtSpbControllerUnlock			
 	
### -field PFN_SPB_CONTROLLER_READ EvtSpbIoRead			
 	
### -field PFN_SPB_CONTROLLER_WRITE EvtSpbIoWrite			
 	
### -field PFN_SPB_CONTROLLER_SEQUENCE EvtSpbIoSequence			
 	
## -remarks

## -see-also