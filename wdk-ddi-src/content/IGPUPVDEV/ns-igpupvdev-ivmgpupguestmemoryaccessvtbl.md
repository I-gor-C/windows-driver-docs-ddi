---
UID: NS.igpupvdev.IVmGPUPGuestMemoryAccessVtbl
title: IVmGPUPGuestMemoryAccessVtbl
author: windows-driver-content
description: 
ms.assetid: 45e3b96f-d53f-44c5-9cad-898a6d3e480f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IVmGPUPGuestMemoryAccessVtbl, IVmGPUPGuestMemoryAccessVtbl
req.header: igpupvdev.h
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

# IVmGPUPGuestMemoryAccessVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IVmGPUPGuestMemoryAccess *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IVmGPUPGuestMemoryAccess *This) AddRef			
 	
### -field ULONG(* )(IVmGPUPGuestMemoryAccess *This) Release			
 	
### -field HRESULT(* )(IVmGPUPGuestMemoryAccess *This,UINT64 StartGpaAddress,UINT64 ByteCount,BOOL WriteProtected,PVOID *MapAddress,IUnknown **Aperture) CreateRamApertureFromByteRange			
 	
### -field HRESULT(* )(IVmGPUPGuestMemoryAccess *This,GUEST_PHYSICAL_ADDRESS StartAddress,UINT64 ByteCount,BYTE ClientBuffer[]) ReadRamBytes			
 	
### -field HRESULT(* )(IVmGPUPGuestMemoryAccess *This,GUEST_PHYSICAL_ADDRESS StartAddress,UINT64 ByteCount, const BYTE ClientBuffer[]) WriteRamBytes			
 	
## -remarks

## -see-also