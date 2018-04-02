---
UID: NS:dot11wdi._NDIS_WDI_DATA_API
title: "_NDIS_WDI_DATA_API"
author: windows-driver-content
description: The NDIS_WDI_DATA_API structure specifies the entry points for WDI data indications.
old-location: netvista\ndis_wdi_data_api.htm
old-project: netvista
ms.assetid: 8C26D62E-711A-4CE7-BD2B-D78B794C67FB
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PNDIS_WDI_DATA_API, NDIS_WDI_DATA_API, NDIS_WDI_DATA_API structure [Network Drivers Starting with Windows Vista], PNDIS_WDI_DATA_API, PNDIS_WDI_DATA_API structure pointer [Network Drivers Starting with Windows Vista], _NDIS_WDI_DATA_API, dot11wdi/NDIS_WDI_DATA_API, dot11wdi/PNDIS_WDI_DATA_API, netvista.ndis_wdi_data_api"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dot11wdi.h
req.include-header: Ndis.h
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	dot11wdi.h
api_name:
-	NDIS_WDI_DATA_API
product: Windows
targetos: Windows
req.typenames: NDIS_WDI_DATA_API, *PNDIS_WDI_DATA_API
---

# _NDIS_WDI_DATA_API structure
The 
  NDIS_WDI_DATA_API structure specifies the entry points for WDI data indications.

## Syntax
```
typedef struct _NDIS_WDI_DATA_API {
  NDIS_OBJECT_HEADER                                      Header;
  NDIS_WDI_TX_DEQUEUE_IND_HANDLER                         TxDequeueIndication;
  NDIS_WDI_TX_TRANSFER_COMPLETE_IND_HANDLER               TxTransferCompleteIndication;
  NDIS_WDI_TX_SEND_COMPLETE_IND_HANDLER                   TxSendCompleteIndication;
  NDIS_WDI_TX_QUERY_RA_TID_STATE_HANDLER                  TxQueryRATIDState;
  NDIS_WDI_TX_SEND_PAUSE_IND_HANDLER                      TxSendPauseIndication;
  NDIS_WDI_TX_SEND_RESTART_IND_HANDLER                    TxSendRestartIndication;
  NDIS_WDI_TX_RELEASE_FRAMES_IND_HANDLER                  TxReleaseFrameIndication;
  NDIS_WDI_TX_INJECT_FRAME_IND_HANDLER                    TxInjectFrameIndication;
  NDIS_WDI_TX_ABORT_CONFIRM_HANDLER                       TxAbortConfirm;
  NDIS_WDI_RX_INORDER_DATA_IND_HANDLER                    RxInorderDataIndication;
  NDIS_WDI_RX_STOP_CONFIRM_HANDLER                        RxStopConfirm;
  NDIS_WDI_RX_FLUSH_CONFIRM_HANDLER                       RxFlushConfirm;
  NDIS_WDI_PEER_CREATE_IND_HANDLER                        PeerCreateIndication;
  NDIS_WDI_PEER_DELETE_IND_HANDLER                        PeerDeleteIndication;
  NDIS_WDI_ALLOCATE_WDI_FRAME_METADATA_HANDLER            AllocateWiFiFrameMetaData;
  NDIS_WDI_FREE_WDI_FRAME_METADATA_HANDLER                FreeWiFiFrameMetaData;
  NDIS_WDI_TX_QUERY_SUSPECT_FRAME_COMPLETE_STATUS_HANDLER TxQuerySuspectFrameCompleteStatus;
} NDIS_WDI_DATA_API, *PNDIS_WDI_DATA_API;
```

## Members


`Header`

The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_WDI_DATA_API structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_WDI_DATA_API.
     

To indicate the version of the NDIS_WDI_DATA_API structure, set the 
     <b>Revision</b> member to the following value:





#### NDIS_OBJECT_TYPE_WDI_DATA_API_REVISION_1

Set the 
        <b>Size</b> member to NDIS_SIZEOF_WDI_DATA_API_REVISION_1.

`TxDequeueIndication`

The entry point of the <a href="https://msdn.microsoft.com/ACCB45DA-1233-4276-A0F5-466E50D9377B">NdisWdiTxDequeueIndication</a> callback function.

`TxTransferCompleteIndication`

The entry point of the <a href="https://msdn.microsoft.com/BC66C993-F571-4EB9-8163-65B038ECE754">NdisWdiTxTransferCompleteIndication</a> callback function.

`TxSendCompleteIndication`

The entry point of the <a href="https://msdn.microsoft.com/A38BA15D-FDD8-41D1-87ED-2CABC1926962">NdisWdiTxSendCompleteIndication</a> callback function.

`TxQueryRATIDState`

The entry point of the <a href="https://msdn.microsoft.com/76949336-3349-4869-83C7-60D7D8A6BE24">NdisWdiTxQueryRATIDState</a> callback function.

`TxSendPauseIndication`

The entry point of the <a href="https://msdn.microsoft.com/A8001D08-36B8-4557-A763-103BDC807CA4">NdisWdiTxSendPauseIndication</a> callback function.

`TxSendRestartIndication`

The entry point of the <a href="https://msdn.microsoft.com/40976CC1-89A4-420F-867F-99F857670DAE">NdisWdiTxSendRestartIndication</a> callback function.

`TxReleaseFrameIndication`

The entry point of the <a href="https://msdn.microsoft.com/1324D516-8AEF-4357-86EC-81F6EBDC8FB9">NdisWdiTxReleaseFrameIndication</a> callback function.

`TxInjectFrameIndication`

The entry point of the <a href="https://msdn.microsoft.com/C384FAFF-E22D-4FA2-8B11-F6C046003C70">NdisWdiTxInjectFrameIndication</a> callback function.

`TxAbortConfirm`

The entry point of the <a href="https://msdn.microsoft.com/1619BF14-DDEE-48CB-8E31-0CC17C8A4C6A">NdisWdiTxAbortConfirm</a> callback function.

`RxInorderDataIndication`

The entry point of the <a href="https://msdn.microsoft.com/F2F92DAE-6C13-4EE6-9DE7-B77F5FAFAE60">NdisWdiRxInorderDataIndication</a> callback function.

`RxStopConfirm`

The entry point of the <a href="https://msdn.microsoft.com/2022915A-2717-4098-BCD8-34130A161967">NdisWdiRxStopConfirm</a> callback function.

`RxFlushConfirm`

The entry point of the <a href="https://msdn.microsoft.com/CEED709C-F295-4633-B7C1-4719EDDC7CD4">NdisWdiRxFlushConfirm</a> callback function.

`PeerCreateIndication`

The entry point of the <a href="https://msdn.microsoft.com/58B60160-FE04-4EDE-900F-244D0F76E50D">NdisWdiPeerCreateIndication</a> callback function.

`PeerDeleteIndication`

The entry point of the <a href="https://msdn.microsoft.com/A13F2A98-BADA-43B8-A24B-0749C5558C35">NdisWdiPeerDeleteIndication</a> callback function.

`AllocateWiFiFrameMetaData`

The entry point of the <a href="https://msdn.microsoft.com/6C565DAF-3363-466F-AC4A-9DB534E581FC">NdisWdiAllocateWiFiFrameMetaData</a> callback function.

`FreeWiFiFrameMetaData`

The entry point of the <a href="https://msdn.microsoft.com/828C181F-918A-4674-B6CE-FCB9750948E0">NdisWdiFreeWiFiFrameMetaData</a> callback function.

`TxQuerySuspectFrameCompleteStatus`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | dot11wdi.h (include Ndis.h) |