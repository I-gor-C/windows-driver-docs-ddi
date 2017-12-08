# Dot11Wdi.h header


This header is used by Networking drivers for Windows Vista and later. For more information, see
- [Networking drivers for Windows Vista and later](../_netvista/index.md)

Dot11Wdi.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [NdisMDeregisterWdiMiniportDriver function](nf-dot11wdi-ndismderegisterwdiminiportdriver.md) | A miniport driver calls the NdisMDeregisterWdiMiniportDriver function to release resources that it allocated with a previous call to the NdisMRegisterWdiMiniportDriver function. |
| [NdisMRegisterWdiMiniportDriver function](nf-dot11wdi-ndismregisterwdiminiportdriver.md) | A miniport driver calls the NdisMRegisterWdiMiniportDriver function to register MiniportWdiXxx entry points with NDIS as the first step in initialization. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [MINIPORT_WDI_ADAPTER_HANG_DIAGNOSE callback](nc-dot11wdi-miniport-wdi-adapter-hang-diagnose.md) | The MiniportWdiAdapterHangDiagnose handler function is used to collect hardware control register states and optionally full firmware state. |
| [MINIPORT_WDI_ALLOCATE_ADAPTER callback](nc-dot11wdi-miniport-wdi-allocate-adapter.md) | The MiniportWdiAllocateAdapter handler function allocates a WDI miniport adapter. |
| [MINIPORT_WDI_CANCEL_IDLE_NOTIFICATION callback](nc-dot11wdi-miniport-wdi-cancel-idle-notification.md) | NDIS calls the MiniportWdiCancelIdleNotification handler function to notify the WDI miniport driver that NDIS has detected activity on the suspended network adapter. |
| [MINIPORT_WDI_CLOSE_ADAPTER callback](nc-dot11wdi-miniport-wdi-close-adapter.md) | The MiniportWdiCloseAdapter handler function is used by the Microsoft component to initiate the Close Task operation on the IHV driver. |
| [MINIPORT_WDI_FREE_ADAPTER callback](nc-dot11wdi-miniport-wdi-free-adapter.md) | The MiniportWdiFreeAdapter handler function requests that the IHV driver deletes its software state. |
| [MINIPORT_WDI_IDLE_NOTIFICATION callback](nc-dot11wdi-miniport-wdi-idle-notification.md) | NDIS calls the MiniportWdiIdleNotification handler function to start the NDIS selective suspend operation on an idle network adapter. Through this operation, the network adapter is suspended and transitioned to a low-power state. |
| [MINIPORT_WDI_OPEN_ADAPTER callback](nc-dot11wdi-miniport-wdi-open-adapter.md) | The MiniportWdiOpenAdapter handler function is used by the Microsoft component to initiate the Open Task operation on the IHV driver. |
| [MINIPORT_WDI_POST_ADAPTER_PAUSE callback](nc-dot11wdi-miniport-wdi-post-adapter-pause.md) | The MiniportWdiPostAdapterPause handler function is called by the Microsoft component after it finishes the data path clean up as part of the NDIS MiniportPause requirements. |
| [MINIPORT_WDI_POST_ADAPTER_RESTART callback](nc-dot11wdi-miniport-wdi-post-adapter-restart.md) | The MiniportWdiPostAdapterRestart handler function is called by the Microsoft component after it finishes restarting the data path as part of the NDIS MiniportRestart requirements. |
| [MINIPORT_WDI_RX_FLUSH callback](nc-dot11wdi-miniport-wdi-rx-flush.md) | The MiniportWdiRxFlush handler function is issued after the MiniportWdiRxStop operation is completed. Upon receiving the flush request, the target/RxEngine must discard all unindicated frames on the port/adapter before indicating RxFlushConfirm. |
| [MINIPORT_WDI_RX_GET_MPDUS callback](nc-dot11wdi-miniport-wdi-rx-get-mpdus.md) | The MiniportWdiRxGetMpdus handler function returns a NET_BUFFER_LIST chain. Each NET_BUFFER_LIST represents one MPDU. |
| [MINIPORT_WDI_RX_PPDU_RSSI callback](nc-dot11wdi-miniport-wdi-rx-ppdu-rssi.md) | The MiniportWdiRxPpduRssi handler function returns the absolute value of RSSI (in dB) for the PPDU. The RxMgr may request the RSSI only once per data indication using the PNET_BUFFER_LIST obtained from MiniportWdiRxGetMpdus. |
| [MINIPORT_WDI_RX_RESTART callback](nc-dot11wdi-miniport-wdi-rx-restart.md) | The MiniportWdiRxRestart handler function configures the RxEngine to restart indicating data traffic. This is issued following a MiniportWdiRxStop. |
| [MINIPORT_WDI_RX_RESUME callback](nc-dot11wdi-miniport-wdi-rx-resume.md) | The MiniportWdiRxResume handler function is issued by the RxMgr after it returns a pause status to a data indication. |
| [MINIPORT_WDI_RX_RETURN_FRAMES callback](nc-dot11wdi-miniport-wdi-rx-return-frames.md) | The MiniportWdiRxReturnFrames handler function returns a NET_BUFFER_LIST structure (and associated data buffers) to the TAL. |
| [MINIPORT_WDI_RX_STOP callback](nc-dot11wdi-miniport-wdi-rx-stop.md) | The MiniportWdiRxStop handler function stops RX on a given port and accepts the wildcard port ID to stop RX across the adapter. |
| [MINIPORT_WDI_RX_THROTTLE callback](nc-dot11wdi-miniport-wdi-rx-throttle.md) | The MiniportWdiRxThrottle handler function tells the TAL/target to enable mechanisms to reduce the rate of RX MSDUs. |
| [MINIPORT_WDI_TAL_TXRX_ADD_PORT callback](nc-dot11wdi-miniport-wdi-tal-txrx-add-port.md) | The MiniportWdiTalTxRxAddPort handler function notifies the datapath components of the creation of a new virtual port. |
| [MINIPORT_WDI_TAL_TXRX_DEINITIALIZE callback](nc-dot11wdi-miniport-wdi-tal-txrx-deinitialize.md) | The MiniportWdiTalTxRxDeinitialize handler function is invoked in the context of miniport halt. The functional components RXEngine and TxEngine have already been stopped and any pending data frames completed/returned. |
| [MINIPORT_WDI_TAL_TXRX_DELETE_PORT callback](nc-dot11wdi-miniport-wdi-tal-txrx-delete-port.md) | The MiniportWdiTalTxRxDeletePort handler function notifies the datapath components of the deletion of a virtual port. |
| [MINIPORT_WDI_TAL_TXRX_INITIALIZE callback](nc-dot11wdi-miniport-wdi-tal-txrx-initialize.md) | The MiniportWdiTalTxRxInitialize handler function initializes data structures in the TAL and exchanges datapath component handles between the UE and TAL. |
| [MINIPORT_WDI_TAL_TXRX_PEER_CONFIG callback](nc-dot11wdi-miniport-wdi-tal-txrx-peer-config.md) | The MiniportWdiTalTxRxPeerConfig handler function specifies the port ID, peer ID, and peer capabilities (for example, QoS capabilities). It is invoked after the peer has associated, which involves creation of the peer object in the TAL. |
| [MINIPORT_WDI_TAL_TXRX_PEER_DELETE_CONFIRM callback](nc-dot11wdi-miniport-wdi-tal-txrx-peer-delete-confirm.md) | The MiniportWdiTalTxRxPeerDeleteConfirm handler function is invoked after the completion of a PeerDeleteIndication call which did not return success. |
| [MINIPORT_WDI_TAL_TXRX_RESET_PORT callback](nc-dot11wdi-miniport-wdi-tal-txrx-reset-port.md) | The MiniportWdiTalTxRxResetPort handler function is invoked before a dot11 reset task is issued to the target. |
| [MINIPORT_WDI_TAL_TXRX_SET_PORT_OPMODE callback](nc-dot11wdi-miniport-wdi-tal-txrx-set-port-opmode.md) | The MiniportWdiTalTxRxSetPortOpMode handler function specifies the opmode used for the port so that the TxEngine and RxEngine enable the corresponding functionality. |
| [MINIPORT_WDI_TAL_TXRX_START callback](nc-dot11wdi-miniport-wdi-tal-txrx-start.md) | The MiniportWdiTalTxRxStart handler function provides TXRX configuration parameters to the TAL. |
| [MINIPORT_WDI_TAL_TXRX_STOP callback](nc-dot11wdi-miniport-wdi-tal-txrx-stop.md) | The MiniportWdiTalTxRxStop handler function stops TXRX communication between the TAL and the target. |
| [MINIPORT_WDI_TX_ABORT callback](nc-dot11wdi-miniport-wdi-tx-abort.md) | The MiniportWdiTxAbort handler function aborts outstanding TX frames for a given port or peer, which includes initiating the completion of frames owned by the TAL/target. |
| [MINIPORT_WDI_TX_DATA_SEND callback](nc-dot11wdi-miniport-wdi-tx-data-send.md) | The MiniportWdiTxDataSend handler function specifies an RA-TID or port queue to transmit from. It is issued in the context of the TX thread from the operating system, resume indication, or a work item. |
| [MINIPORT_WDI_TX_PEER_BACKLOG callback](nc-dot11wdi-miniport-wdi-tx-peer-backlog.md) | The MiniportWdiTxPeerBacklog handler function is issued when a paused peer has a change in backlog state. |
| [MINIPORT_WDI_TX_TAL_QUEUE_IN_ORDER callback](nc-dot11wdi-miniport-wdi-tx-tal-queue-in-order.md) | The MiniportWdiTxTalQueueInOrder handler function notifies the TAL target that one or more paused RA/TID queues (with WDI_TX_PAUSE_REASON_PS) is ready to transmit. |
| [MINIPORT_WDI_TX_TAL_SEND callback](nc-dot11wdi-miniport-wdi-tx-tal-send.md) | The MiniportWdiTxTalSend handler function specifies an RA-TID or port queue to transmit from. |
| [MINIPORT_WDI_TX_TAL_SEND_COMPLETE callback](nc-dot11wdi-miniport-wdi-tx-tal-send-complete.md) | The MiniportWdiTxTalSendComplete handler function returns ownership of one or more TX frame injected by the TAL back to the TxEngine. |
| [MINIPORT_WDI_TX_TARGET_DESC_DEINIT callback](nc-dot11wdi-miniport-wdi-tx-target-desc-deinit.md) | The MINIPORT_WDI_TX_TARGET_DESC_DEINIT callback function informs the TxEngine that the target TX descriptors associated with the NET_BUFFER_LIST (NBLs) in the NBL chain are no longer needed and can be freed. |
| [MINIPORT_WDI_TX_TARGET_DESC_INIT callback](nc-dot11wdi-miniport-wdi-tx-target-desc-init.md) | The MINIPORT_WDI_TX_TARGET_DESC_INIT callback function associates an opaque target TX descriptor with the NET_BUFFER_LIST (MiniportReserved[1] field) and (if applicable) populates the TX cost field (in credit units) in the WDI_FRAME_METADATA buffer of the NET_BUFFER_LIST (MiniportReserved[0]). |
| [NDIS_WDI_ALLOCATE_WDI_FRAME_METADATA callback](nc-dot11wdi-ndis-wdi-allocate-wdi-frame-metadata.md) | The NdisWdiAllocateWiFiFrameMetaData callback function allocates a frame metadata buffer. |
| [NDIS_WDI_CLOSE_ADAPTER_COMPLETE callback](nc-dot11wdi-ndis-wdi-close-adapter-complete.md) | The NdisWdiCloseAdapterComplete callback function is called by the IHV when a Close Task operation from MiniportWdiCloseAdapter has been successfully started. |
| [NDIS_WDI_FREE_WDI_FRAME_METADATA callback](nc-dot11wdi-ndis-wdi-free-wdi-frame-metadata.md) | The NdisWdiFreeWiFiFrameMetaData callback function frees a frame metadata buffer. |
| [NDIS_WDI_IDLE_NOTIFICATION_COMPLETE callback](nc-dot11wdi-ndis-wdi-idle-notification-complete.md) | Miniport drivers call NdisWdiIdleNotificationComplete callback function to complete a pending idle notification for an NDIS selective suspend operation. NDIS begins the operation when it calls the driver's MiniportWdiIdleNotification handler function. |
| [NDIS_WDI_IDLE_NOTIFICATION_CONFIRM callback](nc-dot11wdi-ndis-wdi-idle-notification-confirm.md) | Miniport drivers call NdisWdiIdleNotificationConfirm callback function to notify NDIS that the idle network adapter can safely be suspended and transitioned to a low-power state. |
| [NDIS_WDI_OPEN_ADAPTER_COMPLETE callback](nc-dot11wdi-ndis-wdi-open-adapter-complete.md) | The NdisWdiOpenAdapterComplete callback function is called by the IHV when an Open Task operation from MiniportWdiOpenAdapter has been successfully started. |
| [NDIS_WDI_PEER_CREATE_IND callback](nc-dot11wdi-ndis-wdi-peer-create-ind.md) | The NdisWdiPeerCreateIndication callback function specifies a peer ID to associate with a peer MAC address. |
| [NDIS_WDI_PEER_DELETE_IND callback](nc-dot11wdi-ndis-wdi-peer-delete-ind.md) | The NdisWdiPeerDeleteIndication callback function initiates the removal of the association of between a peer ID and a peer MAC address. |
| [NDIS_WDI_RX_FLUSH_CONFIRM callback](nc-dot11wdi-ndis-wdi-rx-flush-confirm.md) | The NdisWdiRxFlushConfirm callback function indicates completion of a MiniportWdiRxFlush request. The RxEngine must complete the discard of all RX data frames that match the flush request prior to issuing NdisWdiRxFlushConfirm. |
| [NDIS_WDI_RX_INORDER_DATA_IND callback](nc-dot11wdi-ndis-wdi-rx-inorder-data-ind.md) | The NdisWdiRxInorderDataIndication callback function informs the RxMgr that a list of specified RX frames in the correct order are present. |
| [NDIS_WDI_RX_STOP_CONFIRM callback](nc-dot11wdi-ndis-wdi-rx-stop-confirm.md) | The NdisWdiRxStopConfirm callback function indicates completion of a MiniportWdiRxStop request. |
| [NDIS_WDI_TX_ABORT_CONFIRM callback](nc-dot11wdi-ndis-wdi-tx-abort-confirm.md) | The NdisWdiTxAbortConfirm callback function indicates an asynchronous confirmation of a MiniportWdiTxAbort from WDI. |
| [NDIS_WDI_TX_DEQUEUE_IND callback](nc-dot11wdi-ndis-wdi-tx-dequeue-ind.md) | The NdisWdiTxDequeueIndication callback function is called in the context of a MiniportWdiTxDataSend or MiniportWdiTxTalSend by the IHV miniport to dequeue frames from WDI to the IHV miniport. |
| [NDIS_WDI_TX_INJECT_FRAME_IND callback](nc-dot11wdi-ndis-wdi-tx-inject-frame-ind.md) | The NdisWdiTxInjectFrameIndication callback function allows the LE to inject frames through the regular datapath (for example, authentication/association requests/responses, Wi-Fi Direct action frames). |
| [NDIS_WDI_TX_QUERY_RA_TID_STATE callback](nc-dot11wdi-ndis-wdi-tx-query-ra-tid-state.md) | The NdisWdiTxQueryRATIDState callback function is used by the TxEngine to query the state of a RA/TID or Port queue. |
| [NDIS_WDI_TX_RELEASE_FRAMES_IND callback](nc-dot11wdi-ndis-wdi-tx-release-frames-ind.md) | The NdisWdiTxReleaseFrameIndication callback function releases up to a specified number or aggregate cost of frames queued to a given peer-TID combination when transmission is paused. |
| [NDIS_WDI_TX_SEND_COMPLETE_IND callback](nc-dot11wdi-ndis-wdi-tx-send-complete-ind.md) | The NdisWdiTxSendCompleteIndication callback function specifies an array of frame IDs associated with the target's sent frames. |
| [NDIS_WDI_TX_SEND_PAUSE_IND callback](nc-dot11wdi-ndis-wdi-tx-send-pause-ind.md) | The NdisWdiTxSendPauseIndication callback function pauses transmissions on a given port to a given peer or peer-TID combination. |
| [NDIS_WDI_TX_SEND_RESTART_IND callback](nc-dot11wdi-ndis-wdi-tx-send-restart-ind.md) | The NdisWdiTxSendRestartIndication callback function resumes transmission on a given port to a given peer or peer-TID combination. |
| [NDIS_WDI_TX_TRANSFER_COMPLETE_IND callback](nc-dot11wdi-ndis-wdi-tx-transfer-complete-ind.md) | The NdisWdiTxTransferCompleteIndication callback function specifies a list of frame buffers that have been transferred to the target. Frames with different TX Status values are completed in separate indications. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS structure](ns-dot11wdi--ndis-miniport-driver-wdi-characteristics.md) | The NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS structure defines the set of handlers that a WDI miniport driver must implement. |
| [NDIS_MINIPORT_WDI_DATA_HANDLERS structure](ns-dot11wdi--ndis-miniport-wdi-data-handlers.md) | The NDIS_MINIPORT_WDI_DATA_HANDLERS structure specifies the entry points for the IHV miniport datapath handlers. |
| [NDIS_WDI_DATA_API structure](ns-dot11wdi--ndis-wdi-data-api.md) | The NDIS_WDI_DATA_API structure specifies the entry points for WDI data indications. |
| [NDIS_WDI_INIT_PARAMETERS structure](ns-dot11wdi--ndis-wdi-init-parameters.md) | The NDIS_WDI_INIT_PARAMETERS structure specifies the WDI functions provided by the operating system and called by the IHV WDI driver. |
| [TAL_TXRX_PARAMETERS structure](ns-dot11wdi--tal-txrx-parameters.md) | The TAL_TXRX_PARAMETERS structure defines the TAL TXRX parameters. |
| [WDI_FRAME_METADATA structure](ns-dot11wdi--wdi-frame-metadata.md) | The WDI_FRAME_METADATA structure defines the frame metadata. |
| [WDI_MAC_ADDRESS structure](ns-dot11wdi--wdi-mac-address.md) | The WDI_MAC_ADDRESS structure defines an IEEE media access control (MAC) address. |
| [WDI_MAC_ADDRESS structure](ns-dot11wdi--wdi-mac-address~r1.md) | The WDI_MAC_ADDRESS structure defines an IEEE media access control (MAC) address. |
| [WDI_MESSAGE_HEADER structure](ns-dot11wdi--wdi-message-header.md) | The WDI_MESSAGE_HEADER structure defines the WDI message header. All WDI command messages must start with this header. |
| [WDI_P2P_SERVICE_NAME_HASH structure](ns-dot11wdi--wdi-p2p-service-name-hash.md) | The WDI_P2P_SERVICE_NAME_HASH structure defines a hash of a WFDS Service Name. |
| [WDI_P2P_SERVICE_NAME_HASH structure](ns-dot11wdi--wdi-p2p-service-name-hash~r1.md) | The WDI_P2P_SERVICE_NAME_HASH structure defines a hash of a WFDS Service Name. |
| [WDI_RX_METADATA structure](ns-dot11wdi--wdi-rx-metadata.md) | The WDI_RX_METADATA structure defines the RX metadata. |
| [WDI_TXRX_MPDU_PN structure](ns-dot11wdi--wdi-txrx-mpdu-pn.md) | The WDI_TXRX_MPDU_PN union defines the parameters that are passed down to the TXRX component. |
| [WDI_TXRX_PARAMETERS structure](ns-dot11wdi--wdi-txrx-parameters.md) | The WDI_TXRX_PARAMETERS structure defines the parameters that are passed down to the TXRX component. |
| [WDI_TXRX_PEER_CFG structure](ns-dot11wdi--wdi-txrx-peer-cfg.md) | The WDI_TXRX_PEER_CFG structure defines peer configuration. |
| [WDI_TXRX_TARGET_CAPABILITIES structure](ns-dot11wdi--wdi-txrx-target-capabilities.md) | The WDI_TXRX_CAPABILITIES structure defines the target capabilities. |
| [WDI_TXRX_TARGET_CONFIGURATION structure](ns-dot11wdi--wdi-txrx-target-configuration.md) | The WDI_TXRX_TARGET_CONFIGURATION structure defines the target configuration. |
| [WDI_TX_COMPLETE_DATA structure](ns-dot11wdi--wdi-tx-complete-data.md) | The WDI_TX_COMPLETE_DATA structure defines TX completion data. |
| [WDI_TX_METADATA structure](ns-dot11wdi--wdi-tx-metadata.md) | The WDI_TX_METADATA structure defines the TX metadata. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [WDI_EXEMPTION_ACTION_TYPE enumeration](ne-dot11wdi--wdi-exemption-action-type.md) | The WDI_EXEMPTION_ACTION_TYPE enumeration defines the exemption types. |
| [WDI_FRAME_PAYLOAD_TYPE enumeration](ne-dot11wdi--wdi-frame-payload-type.md) | The WDI_FRAME_PAYLOAD_TYPE enumeration defines the frame payload type. |
| [WDI_INTERCONNECT_TYPE enumeration](ne-dot11wdi--wdi-interconnect-type.md) | The WDI_INTERCONNECT_TYPE enumeration defines the interconnect types. |
| [WDI_OPERATION_MODE enumeration](ne-dot11wdi--wdi-operation-mode.md) | The WDI_OPERATION_MODE enumeration defines operation modes. |
| [WDI_RX_INDICATION_LEVEL enumeration](ne-dot11wdi--wdi-rx-indication-level.md) | The WDI_RX_INDICATION_LEVEL enumeration defines the RX indication levels. |
| [WDI_RX_THROTTLE_LEVEL enumeration](ne-dot11wdi--wdi-rx-throttle-level.md) | The WDI_RX_THROTTLE_LEVEL enumeration defines the RX throttle level. The interpretation and implementation mechanisms of these throttle levels are defined by the independent hardware vendor (IHV). |
| [WDI_TXRX_PEER_QOS_CAPS enumeration](ne-dot11wdi--wdi-txrx-peer-qos-caps.md) | The WDI_TXRX_PEER_QOS_CAPS enumeration defines the Quality of Service (QoS) capabilities. |
| [WDI_TX_FRAME_STATUS enumeration](ne-dot11wdi--wdi-tx-frame-status.md) | The WDI_TX_FRAME_STATUS enumeration defines the TX frame status values. |
| [WDI_TX_PAUSE_REASON enumeration](ne-dot11wdi--wdi-tx-pause-reason.md) | The WDI_TX_PAUSE_REASON enumeration defines the reasons for a TX pause. |
| [eDiagnoseLevel enumeration](ne-dot11wdi-ediagnoselevel.md) | The eDiagnoseLevel enumeration defines the diagnosis levels for adapter hang diagnosis. |
