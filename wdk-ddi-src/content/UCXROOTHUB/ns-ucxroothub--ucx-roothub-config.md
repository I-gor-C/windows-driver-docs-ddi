---
UID: NS.ucxroothub._UCX_ROOTHUB_CONFIG
title: UCX_ROOTHUB_CONFIG
author: windows-driver-content
description: 
ms.assetid: 91092c1a-ef2f-4747-8d55-ea255c6cd297
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: UCX_ROOTHUB_CONFIG, UCX_ROOTHUB_CONFIG, *PUCX_ROOTHUB_CONFIG
req.header: ucxroothub.h
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

# UCX_ROOTHUB_CONFIG structure

## -description



## -struct-fields

### -field ULONG Size			
 	
### -field ULONG NumberOfPresentedControlUrbCallbacks			
 	
### -field PFN_UCX_ROOTHUB_CONTROL_URB EvtRootHubClearHubFeature			
 	
### -field PFN_UCX_ROOTHUB_CONTROL_URB EvtRootHubClearPortFeature			
 	
### -field PFN_UCX_ROOTHUB_CONTROL_URB EvtRootHubGetHubStatus			
 	
### -field PFN_UCX_ROOTHUB_CONTROL_URB EvtRootHubGetPortStatus			
 	
### -field PFN_UCX_ROOTHUB_CONTROL_URB EvtRootHubSetHubFeature			
 	
### -field PFN_UCX_ROOTHUB_CONTROL_URB EvtRootHubSetPortFeature			
 	
### -field PFN_UCX_ROOTHUB_CONTROL_URB EvtRootHubGetPortErrorCount			
 	
### -field PFN_UCX_ROOTHUB_CONTROL_URB EvtRootHubControlUrb			
 	
### -field PFN_UCX_ROOTHUB_INTERRUPT_TX EvtRootHubInterruptTx			
 	
### -field PFN_UCX_ROOTHUB_GET_INFO EvtRootHubGetInfo			
 	
### -field PFN_UCX_ROOTHUB_GET_20PORT_INFO EvtRootHubGet20PortInfo			
 	
### -field PFN_UCX_ROOTHUB_GET_30PORT_INFO EvtRootHubGet30PortInfo			
 	
### -field WDF_OBJECT_ATTRIBUTES WdfRequestAttributes			
 	
## -remarks

## -see-also