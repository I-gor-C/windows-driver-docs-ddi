---
UID: NS.wudfddi.IWDFInterruptVtbl
title: IWDFInterruptVtbl
author: windows-driver-content
description: 
ms.assetid: 389f9eca-1d78-4fd6-ab1a-3365a8238b05
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFInterruptVtbl, IWDFInterruptVtbl
req.header: wudfddi.h
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

# IWDFInterruptVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFInterrupt *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFInterrupt *This) AddRef			
 	
### -field ULONG(* )(IWDFInterrupt *This) Release			
 	
### -field HRESULT(* )(IWDFInterrupt *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFInterrupt *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFInterrupt *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFInterrupt *This) AcquireLock			
 	
### -field void(* )(IWDFInterrupt *This) ReleaseLock			
 	
### -field void(* )(IWDFInterrupt *This) Enable			
 	
### -field void(* )(IWDFInterrupt *This) Disable			
 	
### -field IWDFDevice3 *(* )(IWDFInterrupt *This) GetDevice			
 	
### -field void(* )(IWDFInterrupt *This,PWDF_INTERRUPT_INFO InterruptInfo) GetInfo			
 	
### -field void(* )(IWDFInterrupt *This,WDF_INTERRUPT_POLICY Policy,WDF_INTERRUPT_PRIORITY Priority,KAFFINITY TargetProcessorSet) SetPolicy			
 	
### -field void(* )(IWDFInterrupt *This,PWDF_INTERRUPT_EXTENDED_POLICY PolicyAndGroup) SetExtendedPolicy			
 	
### -field void(* )(IWDFInterrupt *This) AcquireInterruptLock			
 	
### -field void(* )(IWDFInterrupt *This) ReleaseInterruptLock			
 	
### -field BOOLEAN(* )(IWDFInterrupt *This) QueueWorkItemForIsr			
 	
### -field BOOLEAN(* )(IWDFInterrupt *This) TryToAcquireInterruptLock			
 	
## -remarks

## -see-also