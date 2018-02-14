---
UID: NC:dot11wdi.NDIS_WDI_TX_QUERY_RA_TID_STATE
title: NDIS_WDI_TX_QUERY_RA_TID_STATE
author: windows-driver-content
description: The NdisWdiTxQueryRATIDState callback function is used by the TxEngine to query the state of a RA/TID or Port queue.
old-location: netvista\ndiswditxqueryratidstate.htm
old-project: netvista
ms.assetid: 76949336-3349-4869-83C7-60D7D8A6BE24
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: netvista.ndiswditxqueryratidstate, NdisWdiTxQueryRATIDState callback function [Network Drivers Starting with Windows Vista], NdisWdiTxQueryRATIDState, NDIS_WDI_TX_QUERY_RA_TID_STATE, NDIS_WDI_TX_QUERY_RA_TID_STATE, dot11wdi/NdisWdiTxQueryRATIDState
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	dot11wdi.h
apiname:
-	NdisWdiTxQueryRATIDState
product: Windows
targetos: Windows
req.typenames: "*PSYNTH_STATS, SYNTH_STATS"
---


# NDIS_WDI_TX_QUERY_RA_TID_STATE callback function
The NdisWdiTxQueryRATIDState callback function is used by the TxEngine to query the state of a RA/TID or Port queue.

This is a callback inside <a href="..\dot11wdi\ns-dot11wdi-_ndis_wdi_data_api.md">NDIS_WDI_DATA_API</a>.

## Syntax

```
NDIS_WDI_TX_QUERY_RA_TID_STATE NdisWdiTxQueryRaTidState;

void NdisWdiTxQueryRaTidState(
  NDIS_HANDLE NdisMiniportDataPathHandle,
  WDI_PORT_ID PortId,
  WDI_PEER_ID PeerId,
  WDI_EXTENDED_TID ExTid,
  NDIS_STATUS *pWifiStatus,
  PUINT16 pQueueLength
)
{...}
```

## Parameters

`NdisMiniportDataPathHandle`

The NdisMiniportDataPathHandle passed to the IHV miniport in <a href="..\dot11wdi\nc-dot11wdi-miniport_wdi_tal_txrx_initialize.md">MiniportWdiTalTxRxInitialize</a>.

`PortId`

The port ID.

`PeerId`

The peer ID.

`ExTid`

The Extended Traffic ID (TID)

`*pWifiStatus`

Indicates the result of the query operation.  See the <i>Remarks</i> section for more information.

`pQueueLength`

The number of backlogged frames in the specified RA/TID  or Port queue.


## Return Value

This callback function does not return a value.

## Remarks

The TxMgr returns a success status if the port and peer are valid. Otherwise, it returns an error status.  In the case of a success status, the <i>QueueLength</i> is set to the number of backlogged frames in the specified RA/TID  or Port queue.

If <b>TargetPriorityQueueing</b> is true, <a href="https://msdn.microsoft.com/library/windows/hardware/mt297658">WDI_PEER_ID</a> must be set to the wildcard peer value.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Target Platform** | Windows |
| **Header** | dot11wdi.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt297658">WDI_PEER_ID</a>



<a href="..\dot11wdi\ns-dot11wdi-_ndis_wdi_data_api.md">NDIS_WDI_DATA_API</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt269099">WDI_PORT_ID</a>



<a href="..\dot11wdi\ns-dot11wdi-_wdi_txrx_target_capabilities.md">WDI_TXRX_CAPABILITIES</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt297640">WDI_EXTENDED_TID</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WDI_TX_QUERY_RA_TID_STATE callback function%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>