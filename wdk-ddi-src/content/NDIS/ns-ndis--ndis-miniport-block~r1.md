---
UID: NS.ndis._NDIS_MINIPORT_BLOCK~r1
title: NDIS_MINIPORT_BLOCK
author: windows-driver-content
description: 
ms.assetid: b48bf9ef-01fd-4be7-aac9-9880f4a60376
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NDIS_MINIPORT_BLOCK, 
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

# NDIS_MINIPORT_BLOCK structure

## -description



## -struct-fields

### -field NDIS_OBJECT_HEADER Header			
 	
### -field PNDIS_MINIPORT_BLOCK NextMiniport			
 	
### -field PNDIS_MINIPORT_BLOCK BaseMiniport			
 	
### -field NDIS_HANDLE MiniportAdapterContext			
 	
### -field UNICODE_STRING Reserved4			
 	
### -field PVOID Reserved10			
 	
### -field NDIS_HANDLE OpenQueue			
 	
### -field REFERENCE ShortRef			
 	
### -field NDIS_HANDLE Reserved12			
 	
### -field UCHAR Padding1			
 	
### -field UCHAR LockAcquired			
 	
### -field UCHAR PmodeOpens			
 	
### -field UCHAR Reserved23			
 	
### -field KSPIN_LOCK Lock			
 	
### -field PNDIS_REQUEST Reserved25			
 	
### -field PVOID Interrupt			
 	
### -field ULONG Flags			
 	
### -field ULONG PnPFlags			
 	
### -field LIST_ENTRY PacketList			
 	
### -field PNDIS_PACKET FirstPendingPacket			
 	
### -field PNDIS_PACKET ReturnPacketsQueue			
 	
### -field ULONG RequestBuffer			
 	
### -field PVOID Reserved26			
 	
### -field PNDIS_MINIPORT_BLOCK PrimaryMiniport			
 	
### -field PVOID Reserved11			
 	
### -field PVOID BusDataContext			
 	
### -field ULONG Reserved3			
 	
### -field PCM_RESOURCE_LIST Resources			
 	
### -field NDIS_TIMER WakeUpDpcTimer			
 	
### -field UNICODE_STRING Reserved20			
 	
### -field UNICODE_STRING SymbolicLinkName			
 	
### -field ULONG CheckForHangSeconds			
 	
### -field ULONG Reserved5			
 	
### -field NDIS_STATUS ResetStatus			
 	
### -field NDIS_HANDLE ResetOpen			
 	
### -field FILTERDBS FilterDbs			
 	
### -field FILTER_PACKET_INDICATION_HANDLER PacketIndicateHandler			
 	
### -field NDIS_M_SEND_COMPLETE_HANDLER SendCompleteHandler			
 	
### -field NDIS_M_SEND_RESOURCES_HANDLER SendResourcesHandler			
 	
### -field NDIS_M_RESET_COMPLETE_HANDLER ResetCompleteHandler			
 	
### -field NDIS_MEDIUM MediaType			
 	
### -field ULONG BusNumber			
 	
### -field NDIS_INTERFACE_TYPE BusType			
 	
### -field NDIS_INTERFACE_TYPE AdapterType			
 	
### -field PDEVICE_OBJECT Reserved6			
 	
### -field PDEVICE_OBJECT Reserved7			
 	
### -field PDEVICE_OBJECT Reserved8			
 	
### -field PVOID MiniportSGDmaBlock			
 	
### -field PNDIS_AF_LIST CallMgrAfList			
 	
### -field PVOID MiniportThread			
 	
### -field PVOID SetInfoBuf			
 	
### -field USHORT SetInfoBufLen			
 	
### -field USHORT MaxSendPackets			
 	
### -field NDIS_STATUS FakeStatus			
 	
### -field PVOID Reserved24			
 	
### -field PUNICODE_STRING Reserved9			
 	
### -field PVOID Reserved21			
 	
### -field UINT MacOptions			
 	
### -field PNDIS_REQUEST PendingRequest			
 	
### -field UINT MaximumLongAddresses			
 	
### -field UINT Reserved27			
 	
### -field UINT CurrentLookahead			
 	
### -field UINT MaximumLookahead			
 	
### -field ULONG_PTR Reserved1			
 	
### -field W_DISABLE_INTERRUPT_HANDLER DisableInterruptHandler			
 	
### -field W_ENABLE_INTERRUPT_HANDLER EnableInterruptHandler			
 	
### -field W_SEND_PACKETS_HANDLER SendPacketsHandler			
 	
### -field NDIS_M_START_SENDS DeferredSendHandler			
 	
### -field ETH_RCV_INDICATE_HANDLER EthRxIndicateHandler			
 	
### -field TR_RCV_INDICATE_HANDLER TrRxIndicateHandler			
 	
### -field PVOID Reserved2			
 	
### -field ETH_RCV_COMPLETE_HANDLER EthRxCompleteHandler			
 	
### -field TR_RCV_COMPLETE_HANDLER TrRxCompleteHandler			
 	
### -field PVOID Reserved22			
 	
### -field NDIS_M_STATUS_HANDLER StatusHandler			
 	
### -field NDIS_M_STS_COMPLETE_HANDLER StatusCompleteHandler			
 	
### -field NDIS_M_TD_COMPLETE_HANDLER TDCompleteHandler			
 	
### -field NDIS_M_REQ_COMPLETE_HANDLER QueryCompleteHandler			
 	
### -field NDIS_M_REQ_COMPLETE_HANDLER SetCompleteHandler			
 	
### -field NDIS_WM_SEND_COMPLETE_HANDLER WanSendCompleteHandler			
 	
### -field WAN_RCV_HANDLER WanRcvHandler			
 	
### -field WAN_RCV_COMPLETE_HANDLER WanRcvCompleteHandler			
 	
## -remarks

## -see-also