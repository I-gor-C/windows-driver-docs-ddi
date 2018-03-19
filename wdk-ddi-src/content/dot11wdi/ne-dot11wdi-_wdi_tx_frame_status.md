---
UID: NE:dot11wdi._WDI_TX_FRAME_STATUS
title: "_WDI_TX_FRAME_STATUS"
author: windows-driver-content
description: The WDI_TX_FRAME_STATUS enumeration defines the TX frame status values.
old-location: netvista\wdi_tx_frame_status.htm
old-project: netvista
ms.assetid: 6ea8a7ac-96dc-4337-884f-d30fbee1f760
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: WDI_TX_FRAME_STATUS, WDI_TX_FRAME_STATUS enumeration [Network Drivers Starting with Windows Vista], WDI_TxFrameStatus_Discard, WDI_TxFrameStatus_NoAck, WDI_TxFrameStatus_Ok, WDI_TxFrameStatus_SendCancelled, WDI_TxFrameStatus_SendPostponed, WDI_TxFrameStatus_TransferCancelled, WDI_TxFrameStatus_TransferFailed, _WDI_TX_FRAME_STATUS, dot11wdi/WDI_TX_FRAME_STATUS, dot11wdi/WDI_TxFrameStatus_Discard, dot11wdi/WDI_TxFrameStatus_NoAck, dot11wdi/WDI_TxFrameStatus_Ok, dot11wdi/WDI_TxFrameStatus_SendCancelled, dot11wdi/WDI_TxFrameStatus_SendPostponed, dot11wdi/WDI_TxFrameStatus_TransferCancelled, dot11wdi/WDI_TxFrameStatus_TransferFailed, netvista.wdi_tx_frame_status, netvista.wifi_tx_frame_status
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
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
-	HeaderDef
api_location:
-	dot11wdi.h
api_name:
-	WDI_TX_FRAME_STATUS
product: Windows
targetos: Windows
req.typenames: WDI_TX_FRAME_STATUS
---

# _WDI_TX_FRAME_STATUS Enumeration
The WDI_TX_FRAME_STATUS enumeration defines the TX frame status values.

## Syntax
````
typedef enum _WDI_TX_FRAME_STATUS { 
  WDI_TxFrameStatus_Ok                 = 0,
  WDI_TxFrameStatus_Discard            = 1,
  WDI_TxFrameStatus_NoAck              = 2,
  WDI_TxFrameStatus_TransferCancelled  = 3,
  WDI_TxFrameStatus_SendCancelled      = 4,
  WDI_TxFrameStatus_SendPostponed      = 5,
  WDI_TxFrameStatus_TransferFailed     = 128
} WDI_TX_FRAME_STATUS;
````

## Constants

<table>
            
                <tr>
                    <td>WDI_TxFrameStatus_Ok</td>
                    <td>Frame transmitted without errors.</td>
                </tr>
            
                <tr>
                    <td>WDI_TxFrameStatus_Discard</td>
                    <td>The frame was discarded to make room for higher priority frames.</td>
                </tr>
            
                <tr>
                    <td>WDI_TxFrameStatus_NoAck</td>
                    <td>Transmission failed after exhausting the maximum number of retries.</td>
                </tr>
            
                <tr>
                    <td>WDI_TxFrameStatus_TransferCancelled</td>
                    <td>TX stop requested.</td>
                </tr>
            
                <tr>
                    <td>WDI_TxFrameStatus_SendCancelled</td>
                    <td>TX stop requested.</td>
                </tr>
            
                <tr>
                    <td>WDI_TxFrameStatus_SendPostponed</td>
                    <td>The frame could not be transmitted at this time (for example, the peer is in PS). The frame should be transferred at a suitable time, when the corresponding TX queue is unpaused. This status is not allowed for targets that have <b>TargetPriorityQueueing</b> set to TRUE.</td>
                </tr>
            
                <tr>
                    <td>WDI_TxFrameStatus_TransferFailed</td>
                    <td>The transfer failed.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | dot11wdi.h |

## See Also

<a href="..\dot11wdi\ns-dot11wdi-_wdi_txrx_target_capabilities.md">WDI_TXRX_CAPABILITIES</a>