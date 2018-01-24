---
UID : NS:bthddi._CHANNEL_CONFIG_PARAMETERS_ENHANCED
title : _CHANNEL_CONFIG_PARAMETERS_ENHANCED
author : windows-driver-content
description : The CHANNEL_CONFIG_PARAMETERS_ENHANCED structure describes configuration parameters for inbound and outbound directions of an L2CAP channel.
old-location : bltooth\channel_config_parameters_enhanced.htm
old-project : bltooth
ms.assetid : 4C28FD6E-A1DD-4887-95B0-6028ECA18204
ms.author : windowsdriverdev
ms.date : 12/21/2017
ms.keywords : _CHANNEL_CONFIG_PARAMETERS_ENHANCED, *PCHANNEL_CONFIG_PARAMETERS_ENHANCED, CHANNEL_CONFIG_PARAMETERS_ENHANCED
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : bthddi.h
req.include-header : Bthddi.h
req.target-type : Windows
req.target-min-winverclnt : Supported in Windows 8 and later versions of Windows
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : CHANNEL_CONFIG_PARAMETERS_ENHANCED
req.alt-loc : Bthddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : Developers should code this function to operate at either IRQL = DISPATCH_LEVEL (if the callback   function does not access paged memory), or IRQL = PASSIVE_LEVEL (if the callback function must access   paged memory)
req.typenames : "*PCHANNEL_CONFIG_PARAMETERS_ENHANCED, CHANNEL_CONFIG_PARAMETERS_ENHANCED"
---

# _CHANNEL_CONFIG_PARAMETERS_ENHANCED structure
The CHANNEL_CONFIG_PARAMETERS_ENHANCED structure describes configuration parameters for inbound and outbound directions of an L2CAP channel.

## Syntax
````
typedef struct _CHANNEL_CONFIG_PARAMETERS_ENHANCED {
  ULONG                                 Flags;
  CO_MTU                                Mtu;
  CO_FLUSHTO                            FlushTO;
  ULONG                                 NumExtraOptions;
  PL2CAP_CONFIG_OPTION                  ExtraOptions;
  L2CAP_FLOWSPEC                        Flow;
  L2CAP_RETRANSMISSION_AND_FLOW_CONTROL RetransmissionAndFlow;
  CO_FCS                                Fcs;
  L2CAP_EXTENDED_FLOW_SPEC              ExtendedFlowSpec;
  CO_EXTENDED_WINDOW_SIZE               ExtendedWindowSize;
} CHANNEL_CONFIG_PARAMETERS_ENHANCED, *PCHANNEL_CONFIG_PARAMETERS_ENHANCED;
````

## Members

        
            `ExtendedFlowSpec`

            Extended flow specification for the L2CAP channel. This member is reserved. Do not use.
        
            `ExtendedWindowSize`

            Extended window size. This member is reserved. Do not use.
        
            `ExtraOptions`

            Array of extra options
        
            `Fcs`

            Frame check sequence
        
            `Flags`

            Combination of CFG_XXX flags.
        
            `Flow`

            QOS for the direction
        
            `FlushTO`

            Flush timeout for the direction
        
            `Mtu`

            MTU for the direction.
        
            `NumExtraOptions`

            Number of elements in the ExtraOptions array
        
            `RetransmissionAndFlow`

            Retransmission and flow for the direction


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | bthddi.h (include Bthddi.h) |