---
UID: NS.sercx._SERCX2_SYSTEM_DMA_RECEIVE_CONFIG
title: SERCX2_SYSTEM_DMA_RECEIVE_CONFIG
author: windows-driver-content
description: 
ms.assetid: b4abab66-f14e-43bc-9f5a-b0907e35dfd2
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SERCX2_SYSTEM_DMA_RECEIVE_CONFIG, 
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

# SERCX2_SYSTEM_DMA_RECEIVE_CONFIG structure

## -description



## -struct-fields

### -field ULONG Size			
 	
### -field size_t MaximumTransferLength			
 	
### -field size_t MinimumTransactionLength			
 	
### -field ULONG DmaAlignment			
 	
### -field ULONG MaximumScatterGatherFragments			
 	
### -field DMA_WIDTH DmaWidth			
 	
### -field PHYSICAL_ADDRESS DeviceAddress			
 	
### -field PCM_PARTIAL_RESOURCE_DESCRIPTOR DmaDescriptor			
 	
### -field ULONG MinimumTransferUnitOverride			
 	
### -field BOOLEAN Exclusive			
 	
### -field PFN_SERCX2_SYSTEM_DMA_RECEIVE_INITIALIZE_TRANSACTION EvtSerCx2SystemDmaReceiveInitializeTransaction			
 	
### -field PFN_SERCX2_SYSTEM_DMA_RECEIVE_CLEANUP_TRANSACTION EvtSerCx2SystemDmaReceiveCleanupTransaction			
 	
### -field PFN_SERCX2_SYSTEM_DMA_RECEIVE_CONFIGURE_DMA_CHANNEL EvtSerCx2SystemDmaReceiveConfigureDmaChannel			
 	
### -field PFN_SERCX2_SYSTEM_DMA_RECEIVE_ENABLE_NEW_DATA_NOTIFICATION EvtSerCx2SystemDmaReceiveEnableNewDataNotification			
 	
### -field PFN_SERCX2_SYSTEM_DMA_RECEIVE_CANCEL_NEW_DATA_NOTIFICATION EvtSerCx2SystemDmaReceiveCancelNewDataNotification			
 	
## -remarks

## -see-also