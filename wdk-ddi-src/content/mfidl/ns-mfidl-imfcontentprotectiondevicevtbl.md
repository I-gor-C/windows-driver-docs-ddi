---
UID: NS.mfidl.IMFContentProtectionDeviceVtbl
title: IMFContentProtectionDeviceVtbl
author: windows-driver-content
description: 
ms.assetid: c2ea5fc7-0454-4cd2-8d7f-4ddaf0ac41b5
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFContentProtectionDeviceVtbl, IMFContentProtectionDeviceVtbl
req.header: mfidl.h
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

# IMFContentProtectionDeviceVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFContentProtectionDevice *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFContentProtectionDevice *This) AddRef			
 	
### -field ULONG(* )(IMFContentProtectionDevice *This) Release			
 	
### -field HRESULT(* )(IMFContentProtectionDevice *This,DWORD FunctionId,DWORD InputBufferByteCount, const BYTE *InputBuffer,DWORD *OutputBufferByteCount,BYTE *OutputBuffer) InvokeFunction			
 	
### -field HRESULT(* )(IMFContentProtectionDevice *This,DWORD *PrivateInputByteCount,DWORD *PrivateOutputByteCount) GetPrivateDataByteCount			
 	
## -remarks

## -see-also