---
UID : NC:dot11wdi.NDIS_WDI_RX_FLUSH_CONFIRM
title : NDIS_WDI_RX_FLUSH_CONFIRM
author : windows-driver-content
description : The NdisWdiRxFlushConfirm callback function indicates completion of a MiniportWdiRxFlush request. The RxEngine must complete the discard of all RX data frames that match the flush request prior to issuing NdisWdiRxFlushConfirm.
old-location : netvista\ndiswdirxflushconfirm.htm
old-project : netvista
ms.assetid : CEED709C-F295-4633-B7C1-4719EDDC7CD4
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _SYNTH_STATS, SYNTH_STATS, *PSYNTH_STATS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : dot11wdi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : NdisWdiRxFlushConfirm
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
req.irql : 
req.typenames : SYNTH_STATS, *PSYNTH_STATS
---


# NDIS_WDI_RX_FLUSH_CONFIRM callback function
The NdisWdiRxFlushConfirm callback function indicates completion of a <a href="..\dot11wdi\nc-dot11wdi-miniport_wdi_rx_flush.md">MiniportWdiRxFlush</a> request. The RxEngine must complete the discard of all RX data frames that match the flush request prior to issuing <i>NdisWdiRxFlushConfirm</i>.

This is a callback inside <a href="..\dot11wdi\ns-dot11wdi-_ndis_wdi_data_api.md">NDIS_WDI_DATA_API</a>.

## Syntax

```
NDIS_WDI_RX_FLUSH_CONFIRM NdisWdiRxFlushConfirm;

void NdisWdiRxFlushConfirm(
  NDIS_HANDLE NdisMiniportDataPathHandle
)
{...}
```

## Parameters

`NdisMiniportDataPathHandle`

The NdisMiniportDataPathHandle passed to the IHV miniport in <a href="..\dot11wdi\nc-dot11wdi-miniport_wdi_tal_txrx_initialize.md">MiniportWdiTalTxRxInitialize</a>.


## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dot11wdi.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\dot11wdi\ns-dot11wdi-_ndis_wdi_data_api.md">NDIS_WDI_DATA_API</a>
</dt>
<dt>
<a href="..\dot11wdi\nc-dot11wdi-miniport_wdi_rx_flush.md">MiniportWdiRxFlush</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/EEEA7181-4A24-4F40-8A44-65EC38D1A867">WDI RX path</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WDI_RX_FLUSH_CONFIRM callback function%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>