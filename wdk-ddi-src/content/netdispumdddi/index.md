---
UID: NA:netdispumdddi
---

# Netdispumdddi.h header

## -description

This header is used by Display. For more information, see
- [Display](../_display/index.md)

Netdispumdddi.h contain these programming interfaces:


## Callback functions

| Title   | Description   |
| ---- |:---- |
| [PFN_CREATE_MIRACAST_CONTEXT callback](nc-netdispumdddi-pfn_create_miracast_context.md) | Called by the operating system to create a user-mode Miracast context. |
| [PFN_DATARATE_NOTIFICATION callback](nc-netdispumdddi-pfn_datarate_notification.md) | Called by the operating system to notify the Miracast user-mode driver that the bit rate of the Miracast network link has changed. This function is registered with the operating system when the RegisterForDataRateNotifications function is called. |
| [PFN_DESTROY_MIRACAST_CONTEXT callback](nc-netdispumdddi-pfn_destroy_miracast_context.md) | Called by the operating system to destroy a user-mode Miracast context. |
| [PFN_GET_NEXT_CHUNK_DATA callback](nc-netdispumdddi-pfn_get_next_chunk_data.md) | Provides info about the next Miracast encode chunk that was reported to the Microsoft DirectX graphics kernel subsystem when the DXGK_INTERRUPT_TYPE interrupt type is DXGK_INTERRUPT_MICACAST_CHUNK_PROCESSING_COMPLETE.The data type of this function is PFN_GET_NEXT_CHUNK_DATA. |
| [PFN_HANDLE_KMD_MESSAGE callback](nc-netdispumdddi-pfn_handle_kmd_message.md) | Called by the operating system to handle the asynchronous kernel-mode message that the Miracast user-mode driver receives when the display miniport driver calls the DxgkCbMiracastSendMessage function. |
| [PFN_MIRACAST_IO_CONTROL callback](nc-netdispumdddi-pfn_miracast_io_control.md) | Called by the user-mode display driver to send the kernel-mode display miniport driver a synchronous I/O control request.The data type of this function is PFN_MIRACAST_IO_CONTROL. |
| [PFN_REGISTER_DATARATE_NOTIFICATIONS callback](nc-netdispumdddi-pfn_register_datarate_notifications.md) | Called by the user-mode driver to register with the operating system to receive network quality of service (QoS) notifications and the current network bandwidth of the Miracast connection.The data type of this function is PFN_REGISTER_DATARATE_NOTIFICATIONS. |
| [PFN_REPORT_SESSION_STATUS callback](nc-netdispumdddi-pfn_report_session_status.md) | Called by the user-mode display driver to report the status of the current Miracast connected session.The data type of this function is PFN_REPORT_SESSION_STATUS. |
| [PFN_REPORT_STATISTIC callback](nc-netdispumdddi-pfn_report_statistic.md) | Called by the user-mode display driver to report the statistics of the Miracast link to the operating system.The data type of this function is PFN_REPORT_STATISTIC. |
| [PFN_START_MIRACAST_SESSION callback](nc-netdispumdddi-pfn_start_miracast_session.md) | Called by the operating system to start a Miracast connected session. |
| [PFN_STOP_MIRACAST_SESSION callback](nc-netdispumdddi-pfn_stop_miracast_session.md) | Called by the operating system to start a Miracast connected session that had earlier been started by a call to the StartMiracastSession function. |
| [QUERY_MIRACAST_DRIVER_INTERFACE callback](nc-netdispumdddi-query_miracast_driver_interface.md) | Called by the operating system to query the Miracast user-mode driver interface, MIRACAST_DRIVER_INTERFACE. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [MIRACAST_CHUNK_DATA structure](ns-netdispumdddi-miracast_chunk_data.md) | Contains encode chunk data that is used when a user-mode driver calls the wireless display (Miracast) GetNextChunkData function. |
| [MIRACAST_CHUNK_ID structure](ns-netdispumdddi-miracast_chunk_id.md) | Stores info that identifies a wireless display (Miracast) encode chunk. |
| [MIRACAST_CHUNK_INFO structure](ns-netdispumdddi-miracast_chunk_info.md) | Contains info about a specified wireless display (Miracast) encode chunk. |
| [MIRACAST_DATARATE_STATS structure](ns-netdispumdddi-miracast_datarate_stats.md) | Contains info used in the wireless display (Miracast) pfnDataRateNotify function about the audio/video encoder bit rate and failed or retried Wi-Fi frames. |
| [MIRACAST_SESSION_INFO structure](ns-netdispumdddi-miracast_session_info.md) | Contains info on a wireless display (Miracast) connected session. |
| [MIRACAST_STATISTIC_DATA structure](ns-netdispumdddi-miracast_statistic_data.md) | Contains Miracast statistics data that the user-mode display driver reports to the operating system. |
| [MIRACAST_WFD_CONNECTION_STATS structure](ns-netdispumdddi-miracast_wfd_connection_stats.md) | Contains bit rate info on the Wi-Fi Direct connection. |
| [_MIRACAST_CALLBACKS structure](ns-netdispumdddi-_miracast_callbacks.md) | Contains pointers to wireless display (Miracast) runtime callback functions that the Miracast user-mode driver can call. |
| [_MIRACAST_DRIVER_INTERFACE structure](ns-netdispumdddi-_miracast_driver_interface.md) | Contains pointers to wireless display (Miracast) functions that are implemented by the Miracast user-mode driver. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [MIRACAST_CHUNK_TYPE enumeration](ne-netdispumdddi-miracast_chunk_type.md) | Specifies the types of wireless display (Miracast) chunk info that is to be processed. |
| [MIRACAST_PROTOCOL_EVENT enumeration](ne-netdispumdddi-miracast_protocol_event.md) | Specifies the types of wireless display (Miracast) protocol event that the user-mode display driver should report. |
| [MIRACAST_STATISTIC_TYPE enumeration](ne-netdispumdddi-miracast_statistic_type.md) | Specifies types of Miracast statistics data that the user-mode display driver generates. |
| [MIRACAST_STATUS enumeration](ne-netdispumdddi-miracast_status.md) | Specifies status types that the user-mode display driver uses to report Miracast connection status. |
