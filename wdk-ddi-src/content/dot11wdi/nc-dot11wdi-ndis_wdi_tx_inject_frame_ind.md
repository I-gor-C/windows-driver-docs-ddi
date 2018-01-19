---
UID : NC:dot11wdi.NDIS_WDI_TX_INJECT_FRAME_IND
title : NDIS_WDI_TX_INJECT_FRAME_IND
author : windows-driver-content
description : The NdisWdiTxInjectFrameIndication callback function allows the LE to inject frames through the regular datapath (for example, authentication/association requests/responses, Wi-Fi Direct action frames).
old-location : netvista\ndiswditxinjectframeindication.htm
old-project : netvista
ms.assetid : C384FAFF-E22D-4FA2-8B11-F6C046003C70
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
req.alt-api : NdisWdiTxInjectFrameIndication
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


# NDIS_WDI_TX_INJECT_FRAME_IND callback function
The NdisWdiTxInjectFrameIndication callback function allows the LE to inject frames through the regular datapath (for example, authentication/association requests/responses, Wi-Fi Direct action frames).

This is a callback inside <a href="..\dot11wdi\ns-dot11wdi-_ndis_wdi_data_api.md">NDIS_WDI_DATA_API</a>.

## Syntax

```
NDIS_WDI_TX_INJECT_FRAME_IND NdisWdiTxInjectFrameInd;

void NdisWdiTxInjectFrameInd(
  NDIS_HANDLE NdisMiniportDataPathHandle,
  WDI_PORT_ID PortId,
  WDI_PEER_ID PeerId,
  WDI_EXTENDED_TID ExTid,
  PNET_BUFFER_LIST pNBL,
  BOOLEAN bIsUnicast,
  BOOLEAN bUseLegacyRates,
  UINT16 Ethertype,
  WDI_EXEMPTION_ACTION_TYPE ExemptionAction
)
{...}
```

## Parameters

`NdisMiniportDataPathHandle`

The NdisMiniportDataPathHandle passed to the IHV miniport in <a href="..\dot11wdi\nc-dot11wdi-miniport_wdi_tal_txrx_initialize.md">MiniportWdiTalTxRxInitialize</a>.

`PortId`

The port ID.

`PeerId`

The peer ID. When <b>TargetPriorityQueueing</b> is true, this must be set to the wildcard value.

`ExTid`

The extended TID.

`pNBL`

Pointer to a <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> chain.

`bIsUnicast`

Specifies if the frames are to a unicast receiver address.

`bUseLegacyRates`

Specifies if legacy rates should be used to send the frames.

`Ethertype`

Specifies the Ethertype of the frames.

`ExemptionAction`

Specifies the ExemptionAction of the frames.


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
<a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="..\dot11wdi\ne-dot11wdi-_wdi_exemption_action_type.md">WDI_EXEMPTION_ACTION_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt297640">WDI_EXTENDED_TID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt297658">WDI_PEER_ID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt269099">WDI_PORT_ID</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WDI_TX_INJECT_FRAME_IND callback function%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>