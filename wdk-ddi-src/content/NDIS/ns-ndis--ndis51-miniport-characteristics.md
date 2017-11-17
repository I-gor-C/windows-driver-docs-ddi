---
UID: NS.ndis._NDIS51_MINIPORT_CHARACTERISTICS
title: NDIS51_MINIPORT_CHARACTERISTICS
author: windows-driver-content
description: 
ms.assetid: 81014a40-4e7e-4845-bac8-9775edd78c80
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NDIS51_MINIPORT_CHARACTERISTICS, NDIS51_MINIPORT_CHARACTERISTICS
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

# NDIS51_MINIPORT_CHARACTERISTICS structure

## -description



## -struct-fields

### -field union __unnamed_union_0c0c_103			
 	
### -field W_CANCEL_SEND_PACKETS_HANDLER CancelSendPacketsHandler			
 	
### -field W_PNP_EVENT_NOTIFY_HANDLER PnPEventNotifyHandler			
 	
### -field W_MINIPORT_SHUTDOWN_HANDLER AdapterShutdownHandler			
 	
### -field PVOID Reserved1			
 	
### -field PVOID Reserved2			
 	
### -field PVOID Reserved3			
 	
### -field PVOID Reserved4			
 	
### -field union __unnamed_union_0c0c_105			
 	
### -field union __unnamed_union_0c0c_106			
 	
### -field UCHAR MajorNdisVersion			
 	
### -field UCHAR MinorNdisVersion			
 	
### -field USHORT Filler			
 	
### -field UINT Reserved			
 	
### -field W_CHECK_FOR_HANG_HANDLER CheckForHangHandler			
 	
### -field W_DISABLE_INTERRUPT_HANDLER DisableInterruptHandler			
 	
### -field W_ENABLE_INTERRUPT_HANDLER EnableInterruptHandler			
 	
### -field W_HALT_HANDLER HaltHandler			
 	
### -field W_HANDLE_INTERRUPT_HANDLER HandleInterruptHandler			
 	
### -field W_INITIALIZE_HANDLER InitializeHandler			
 	
### -field W_ISR_HANDLER ISRHandler			
 	
### -field W_QUERY_INFORMATION_HANDLER QueryInformationHandler			
 	
### -field W_RECONFIGURE_HANDLER ReconfigureHandler			
 	
### -field W_RESET_HANDLER ResetHandler			
 	
### -field W_SET_INFORMATION_HANDLER SetInformationHandler			
 	
### -field W_RETURN_PACKET_HANDLER ReturnPacketHandler			
 	
### -field W_SEND_PACKETS_HANDLER SendPacketsHandler			
 	
### -field W_ALLOCATE_COMPLETE_HANDLER AllocateCompleteHandler			
 	
### -field W_CO_CREATE_VC_HANDLER CoCreateVcHandler			
 	
### -field W_CO_DELETE_VC_HANDLER CoDeleteVcHandler			
 	
### -field W_CO_ACTIVATE_VC_HANDLER CoActivateVcHandler			
 	
### -field W_CO_DEACTIVATE_VC_HANDLER CoDeactivateVcHandler			
 	
### -field W_CO_SEND_PACKETS_HANDLER CoSendPacketsHandler			
 	
### -field W_CO_REQUEST_HANDLER CoRequestHandler			
 	
### -field W_SEND_HANDLER SendHandler			
 	
### -field WM_SEND_HANDLER WanSendHandler			
 	
### -field W_TRANSFER_DATA_HANDLER TransferDataHandler			
 	
### -field WM_TRANSFER_DATA_HANDLER WanTransferDataHandler			
 	
### -field NDIS50_MINIPORT_CHARACTERISTICS Ndis50Chars			
 	
## -remarks

## -see-also