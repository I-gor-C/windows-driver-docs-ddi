---
UID: NC:dot11wdi.MINIPORT_WDI_RX_FLUSH
title: MINIPORT_WDI_RX_FLUSH
author: windows-driver-content
description: The MiniportWdiRxFlush handler function is issued after the MiniportWdiRxStop operation is completed. Upon receiving the flush request, the target/RxEngine must discard all unindicated frames on the port/adapter before indicating RxFlushConfirm.
old-location: netvista\miniportwdirxflush.htm
old-project: netvista
ms.assetid: 76945A84-A6DB-4753-B04E-32249359B8C6
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: MINIPORT_WDI_RX_FLUSH, MiniportWdiRxFlush, MiniportWdiRxFlush callback function [Network Drivers Starting with Windows Vista], dot11wdi/MiniportWdiRxFlush, netvista.miniportwdirxflush
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	dot11wdi.h
api_name:
-	MiniportWdiRxFlush
product: Windows
targetos: Windows
req.typenames: SYNTH_STATS, *PSYNTH_STATS
---


# MINIPORT_WDI_RX_FLUSH callback function
The 
  MiniportWdiRxFlush handler function is issued after the <a href="..\dot11wdi\nc-dot11wdi-miniport_wdi_rx_stop.md">MiniportWdiRxStop</a> operation is completed. Upon receiving the flush request, the target/RxEngine must  discard all unindicated frames on the port/adapter before indicating <a href="..\dot11wdi\nc-dot11wdi-ndis_wdi_rx_flush_confirm.md">RxFlushConfirm</a>.

This is a WDI miniport handler inside <a href="..\dot11wdi\ns-dot11wdi-_ndis_miniport_wdi_data_handlers.md">NDIS_MINIPORT_WDI_DATA_HANDLERS</a>.
<div class="alert"><b>Note</b>  You must declare the function by using the <b>MINIPORT_WDI_RX_FLUSH</b> type. For more
   information, see the following Examples section.</div><div> </div>

## Syntax

```
MINIPORT_WDI_RX_FLUSH MiniportWdiRxFlush;

void MiniportWdiRxFlush(
  TAL_TXRX_HANDLE MiniportTalTxRxContext,
  WDI_PORT_ID PortId
)
{...}
```

## Parameters

`MiniportTalTxRxContext`

TAL device handle returned by the IHV miniport in <a href="..\dot11wdi\nc-dot11wdi-miniport_wdi_tal_txrx_initialize.md">MiniportWdiTalTxRxInitialize</a>.

`PortId`

The port ID.


## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Windows |
| **Header** | dot11wdi.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt269099">WDI_PORT_ID</a>



<a href="..\dot11wdi\ns-dot11wdi-_ndis_miniport_wdi_data_handlers.md">NDIS_MINIPORT_WDI_DATA_HANDLERS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt297625">TAL_TXRX_HANDLE</a>



<a href="https://msdn.microsoft.com/EEEA7181-4A24-4F40-8A44-65EC38D1A867">WDI RX path</a>