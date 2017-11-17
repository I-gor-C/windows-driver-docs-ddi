---
UID: NS.mfidl.IMFPresentationDescriptorVtbl
title: IMFPresentationDescriptorVtbl
author: windows-driver-content
description: 
ms.assetid: 3e5dc915-8a2d-4a53-9c0e-9c88c535a9d0
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFPresentationDescriptorVtbl, IMFPresentationDescriptorVtbl
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

# IMFPresentationDescriptorVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFPresentationDescriptor *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFPresentationDescriptor *This) AddRef			
 	
### -field ULONG(* )(IMFPresentationDescriptor *This) Release			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey,PROPVARIANT *pValue) GetItem			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey,MF_ATTRIBUTE_TYPE *pType) GetItemType			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey,REFPROPVARIANT Value,BOOL *pbResult) CompareItem			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,IMFAttributes *pTheirs,MF_ATTRIBUTES_MATCH_TYPE MatchType,BOOL *pbResult) Compare			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey,UINT32 *punValue) GetUINT32			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey,UINT64 *punValue) GetUINT64			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey, double *pfValue) GetDouble			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey,GUID *pguidValue) GetGUID			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey,UINT32 *pcchLength) GetStringLength			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey,LPWSTR pwszValue,UINT32 cchBufSize,UINT32 *pcchLength) GetString			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey,LPWSTR *ppwszValue,UINT32 *pcchLength) GetAllocatedString			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey,UINT32 *pcbBlobSize) GetBlobSize			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey,UINT8 *pBuf,UINT32 cbBufSize,UINT32 *pcbBlobSize) GetBlob			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey,UINT8 **ppBuf,UINT32 *pcbSize) GetAllocatedBlob			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey,REFIID riid,LPVOID *ppv) GetUnknown			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey,REFPROPVARIANT Value) SetItem			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey) DeleteItem			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This) DeleteAllItems			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey,UINT32 unValue) SetUINT32			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey,UINT64 unValue) SetUINT64			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey, double fValue) SetDouble			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey,REFGUID guidValue) SetGUID			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey,LPCWSTR wszValue) SetString			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey, const UINT8 *pBuf,UINT32 cbBufSize) SetBlob			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,REFGUID guidKey,IUnknown *pUnknown) SetUnknown			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This) LockStore			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This) UnlockStore			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,UINT32 *pcItems) GetCount			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,UINT32 unIndex,GUID *pguidKey,PROPVARIANT *pValue) GetItemByIndex			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,IMFAttributes *pDest) CopyAllItems			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,DWORD *pdwDescriptorCount) GetStreamDescriptorCount			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,DWORD dwIndex,BOOL *pfSelected,IMFStreamDescriptor **ppDescriptor) GetStreamDescriptorByIndex			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,DWORD dwDescriptorIndex) SelectStream			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,DWORD dwDescriptorIndex) DeselectStream			
 	
### -field HRESULT(* )(IMFPresentationDescriptor *This,IMFPresentationDescriptor **ppPresentationDescriptor) Clone			
 	
## -remarks

## -see-also