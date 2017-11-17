---
UID: NS.ndis._NDIS50_PROTOCOL_CHARACTERISTICS
title: NDIS50_PROTOCOL_CHARACTERISTICS
author: windows-driver-content
description: 
ms.assetid: 9a9481e3-dead-4a46-b496-5cf76c19f9d0
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NDIS50_PROTOCOL_CHARACTERISTICS, NDIS50_PROTOCOL_CHARACTERISTICS
req.header: ndis.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# NDIS50_PROTOCOL_CHARACTERISTICS structure

## -description



## -struct-fields

### -field union __unnamed_union_0c0c_94			
 	
### -field PVOID [4] ReservedHandlers			
 	
### -field CO_SEND_COMPLETE_HANDLER CoSendCompleteHandler			
 	
### -field CO_STATUS_HANDLER CoStatusHandler			
 	
### -field CO_RECEIVE_PACKET_HANDLER CoReceivePacketHandler			
 	
### -field CO_AF_REGISTER_NOTIFY_HANDLER CoAfRegisterNotifyHandler			
 	
### -field union __unnamed_union_0c0c_96			
 	
### -field union __unnamed_union_0c0c_97			
 	
### -field union __unnamed_union_0c0c_98			
 	
### -field union __unnamed_union_0c0c_99			
 	
### -field UCHAR MajorNdisVersion			
 	
### -field UCHAR MinorNdisVersion			
 	
### -field USHORT Filler			
 	
### -field OPEN_ADAPTER_COMPLETE_HANDLER OpenAdapterCompleteHandler			
 	
### -field CLOSE_ADAPTER_COMPLETE_HANDLER CloseAdapterCompleteHandler			
 	
### -field RESET_COMPLETE_HANDLER ResetCompleteHandler			
 	
### -field REQUEST_COMPLETE_HANDLER RequestCompleteHandler			
 	
### -field RECEIVE_COMPLETE_HANDLER ReceiveCompleteHandler			
 	
### -field STATUS_HANDLER StatusHandler			
 	
### -field STATUS_COMPLETE_HANDLER StatusCompleteHandler			
 	
### -field NDIS_STRING Name			
 	
### -field RECEIVE_PACKET_HANDLER ReceivePacketHandler			
 	
### -field BIND_HANDLER BindAdapterHandler			
 	
### -field UNBIND_HANDLER UnbindAdapterHandler			
 	
### -field PNP_EVENT_HANDLER PnPEventHandler			
 	
### -field UNLOAD_PROTOCOL_HANDLER UnloadHandler			
 	
### -field UINT Reserved			
 	
### -field UINT Flags			
 	
### -field SEND_COMPLETE_HANDLER SendCompleteHandler			
 	
### -field WAN_SEND_COMPLETE_HANDLER WanSendCompleteHandler			
 	
### -field TRANSFER_DATA_COMPLETE_HANDLER TransferDataCompleteHandler			
 	
### -field WAN_TRANSFER_DATA_COMPLETE_HANDLER WanTransferDataCompleteHandler			
 	
### -field RECEIVE_HANDLER ReceiveHandler			
 	
### -field WAN_RECEIVE_HANDLER WanReceiveHandler			
 	
### -field NDIS40_PROTOCOL_CHARACTERISTICS Ndis40Chars			
 	
## -remarks

## -see-also