---
UID: NS.sercx._SERCX_CONFIG
title: SERCX_CONFIG
author: windows-driver-content
description: 
ms.assetid: ecb4df14-b7d4-4a27-8d5c-c3dee4d0f094
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SERCX_CONFIG, 
req.header: sercx.h
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

# SERCX_CONFIG structure

## -description



## -struct-fields

### -field ULONG Size			
 	
### -field WDF_TRI_STATE PowerManaged			
 	
### -field PFN_SERCX_FILEOPEN EvtSerCxFileOpen			
 	
### -field PFN_SERCX_FILECLOSE EvtSerCxFileClose			
 	
### -field PFN_SERCX_FILECLEANUP EvtSerCxFileCleanup			
 	
### -field PFN_SERCX_TRANSMIT EvtSerCxTransmit			
 	
### -field PFN_SERCX_RECEIVE EvtSerCxReceive			
 	
### -field PFN_SERCX_WAITMASK EvtSerCxWaitmask			
 	
### -field PFN_SERCX_PURGE EvtSerCxPurge			
 	
### -field PFN_SERCX_CONTROL EvtSerCxControl			
 	
### -field PFN_SERCX_APPLY_CONFIG EvtSerCxApplyConfig			
 	
### -field PFN_SERCX_TRANSMIT_CANCEL EvtSerCxTransmitCancel			
 	
### -field PFN_SERCX_RECEIVE_CANCEL EvtSerCxReceiveCancel			
 	
## -remarks

## -see-also