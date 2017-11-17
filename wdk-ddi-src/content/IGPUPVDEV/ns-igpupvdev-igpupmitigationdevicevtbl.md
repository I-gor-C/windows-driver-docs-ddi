---
UID: NS.igpupvdev.IGPUPMitigationDeviceVtbl
title: IGPUPMitigationDeviceVtbl
author: windows-driver-content
description: 
ms.assetid: a2f4cd20-4826-45e7-9687-439c9202ee6f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IGPUPMitigationDeviceVtbl, IGPUPMitigationDeviceVtbl
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

# IGPUPMitigationDeviceVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IGPUPMitigationDevice *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IGPUPMitigationDevice *This) AddRef			
 	
### -field ULONG(* )(IGPUPMitigationDevice *This) Release			
 	
### -field HRESULT(* )(IGPUPMitigationDevice *This,GUID *VmGuid,PLUID DeviceLuid,HANDLE DeviceHandle,HANDLE VmBusHandle,IUnknown *GpupServices) Initialize			
 	
### -field HRESULT(* )(IGPUPMitigationDevice *This,PLUID DeviceLuid,GPUP_POWER_DEVICE_STATE GpupPowerState) PowerTransitionComplete			
 	
### -field HRESULT(* )(IGPUPMitigationDevice *This,PLUID DeviceLuid,VGPU_BAR_SELECTOR BarIndex,ULONG64 Offset,ULONG64 Length,BYTE *ValueRead) ReadInterceptedGpup			
 	
### -field HRESULT(* )(IGPUPMitigationDevice *This,PLUID DeviceLuid,VGPU_BAR_SELECTOR BarIndex,ULONG64 Offset,ULONG64 Length, const BYTE WriteValue[]) WriteInterceptedGpup			
 	
### -field HRESULT(* )(IGPUPMitigationDevice *This,PLUID DeviceLuid,GPUP_SAVE_RESTORE_PAUSE_STATE Flags) PauseGpup			
 	
### -field HRESULT(* )(IGPUPMitigationDevice *This,PLUID DeviceLuid,GPUP_SAVE_RESTORE_PAUSE_STATE Flags) ResumeGpup			
 	
### -field HRESULT(* )(IGPUPMitigationDevice *This,PLUID DeviceLuid,GPUP_SAVE_RESTORE_PAUSE_STATE Flags,ULONG *Length,BYTE SaveBuffer[]) SaveGpupBegin			
 	
### -field HRESULT(* )(IGPUPMitigationDevice *This,PLUID DeviceLuid,GPUP_SAVE_RESTORE_PAUSE_STATE Flags,ULONG *Length,ULONG *RequestedLength,BYTE SaveBuffer[]) SaveGpupContinue			
 	
### -field HRESULT(* )(IGPUPMitigationDevice *This,PLUID DeviceLuid,GPUP_SAVE_RESTORE_PAUSE_STATE Flags,ULONG Length,ULONG Offset,ULONG TotalLength,BYTE RestoreBuffer[]) RestoreGpup			
 	
## -remarks

## -see-also