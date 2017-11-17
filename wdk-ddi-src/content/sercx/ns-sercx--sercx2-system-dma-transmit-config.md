---
UID: NS.sercx._SERCX2_SYSTEM_DMA_TRANSMIT_CONFIG
title: SERCX2_SYSTEM_DMA_TRANSMIT_CONFIG
author: windows-driver-content
description: 
ms.assetid: e975bf82-257f-47f2-8671-9ca8dd263182
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SERCX2_SYSTEM_DMA_TRANSMIT_CONFIG, 
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

# SERCX2_SYSTEM_DMA_TRANSMIT_CONFIG structure

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
 	
### -field PFN_SERCX2_SYSTEM_DMA_TRANSMIT_INITIALIZE_TRANSACTION EvtSerCx2SystemDmaTransmitInitializeTransaction			
 	
### -field PFN_SERCX2_SYSTEM_DMA_TRANSMIT_CLEANUP_TRANSACTION EvtSerCx2SystemDmaTransmitCleanupTransaction			
 	
### -field PFN_SERCX2_SYSTEM_DMA_TRANSMIT_CONFIGURE_DMA_CHANNEL EvtSerCx2SystemDmaTransmitConfigureDmaChannel			
 	
### -field PFN_SERCX2_SYSTEM_DMA_TRANSMIT_DRAIN_FIFO EvtSerCx2SystemDmaTransmitDrainFifo			
 	
### -field PFN_SERCX2_SYSTEM_DMA_TRANSMIT_CANCEL_DRAIN_FIFO EvtSerCx2SystemDmaTransmitCancelDrainFifo			
 	
### -field PFN_SERCX2_SYSTEM_DMA_TRANSMIT_PURGE_FIFO EvtSerCx2SystemDmaTransmitPurgeFifo			
 	
## -remarks

## -see-also