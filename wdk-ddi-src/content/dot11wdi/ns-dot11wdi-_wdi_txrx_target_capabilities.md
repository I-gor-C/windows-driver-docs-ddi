---
UID : NS:dot11wdi._WDI_TXRX_TARGET_CAPABILITIES
title : _WDI_TXRX_TARGET_CAPABILITIES
author : windows-driver-content
description : The WDI_TXRX_CAPABILITIES structure defines the target capabilities.
old-location : netvista\wdi_txrx_capabilities.htm
old-project : netvista
ms.assetid : 7a1d3ffd-6f5e-429d-8c2f-a141f98ccad8
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _WDI_TXRX_TARGET_CAPABILITIES, WDI_TXRX_CAPABILITIES, *PWDI_TXRX_CAPABILITIES
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : dot11wdi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : WDI_TXRX_CAPABILITIES
req.alt-loc : dot11wdi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : WDI_TXRX_CAPABILITIES, *PWDI_TXRX_CAPABILITIES
---

# _WDI_TXRX_TARGET_CAPABILITIES structure
The 
   WDI_TXRX_CAPABILITIES structure defines the target capabilities.

## Syntax
````
typedef struct _WDI_TXRX_CAPABILITIES {
  WDI_INTERCONNECT_TYPE InterconnectType;
  struct {
    BOOLEAN TargetPriorityQueueing;
    UINT16  MaxMemBlocksPerFrame;
    BOOLEAN ExplicitSendCompleteFlagRequired;
    UINT8   bPad;
    UINT16  MinEffectiveSize;
    UINT16  FrameSizeGranularity;
  } TransmitCapabilities;
  struct {
    BOOLEAN RxTxForwarding;
    UINT32  MaxThroughput;
  } ReceiveCapabilities;
} WDI_TXRX_CAPABILITIES, *PWDI_TXRX_CAPABILITIES;
````

## Members

        
            `InterconnectType`

            Interconnect type of the target.
        
            `ReceiveCapabilities`

            Receive capabilities.
        
            `TransmitCapabilities`

            Transmit capabilities.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dot11wdi.h |