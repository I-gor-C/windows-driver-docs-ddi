---
UID: NS.mfidl.IMFStreamDescriptorVtbl
title: IMFStreamDescriptorVtbl
author: windows-driver-content
description: 
ms.assetid: 5f8ac04d-cbfb-4f43-ac4c-4aef56a856f9
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFStreamDescriptorVtbl, IMFStreamDescriptorVtbl
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

# IMFStreamDescriptorVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFStreamDescriptor *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFStreamDescriptor *This) AddRef			
 	
### -field ULONG(* )(IMFStreamDescriptor *This) Release			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey,PROPVARIANT *pValue) GetItem			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey,MF_ATTRIBUTE_TYPE *pType) GetItemType			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey,REFPROPVARIANT Value,BOOL *pbResult) CompareItem			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,IMFAttributes *pTheirs,MF_ATTRIBUTES_MATCH_TYPE MatchType,BOOL *pbResult) Compare			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey,UINT32 *punValue) GetUINT32			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey,UINT64 *punValue) GetUINT64			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey, double *pfValue) GetDouble			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey,GUID *pguidValue) GetGUID			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey,UINT32 *pcchLength) GetStringLength			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey,LPWSTR pwszValue,UINT32 cchBufSize,UINT32 *pcchLength) GetString			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey,LPWSTR *ppwszValue,UINT32 *pcchLength) GetAllocatedString			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey,UINT32 *pcbBlobSize) GetBlobSize			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey,UINT8 *pBuf,UINT32 cbBufSize,UINT32 *pcbBlobSize) GetBlob			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey,UINT8 **ppBuf,UINT32 *pcbSize) GetAllocatedBlob			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey,REFIID riid,LPVOID *ppv) GetUnknown			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey,REFPROPVARIANT Value) SetItem			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey) DeleteItem			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This) DeleteAllItems			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey,UINT32 unValue) SetUINT32			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey,UINT64 unValue) SetUINT64			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey, double fValue) SetDouble			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey,REFGUID guidValue) SetGUID			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey,LPCWSTR wszValue) SetString			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey, const UINT8 *pBuf,UINT32 cbBufSize) SetBlob			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,REFGUID guidKey,IUnknown *pUnknown) SetUnknown			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This) LockStore			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This) UnlockStore			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,UINT32 *pcItems) GetCount			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,UINT32 unIndex,GUID *pguidKey,PROPVARIANT *pValue) GetItemByIndex			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,IMFAttributes *pDest) CopyAllItems			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,DWORD *pdwStreamIdentifier) GetStreamIdentifier			
 	
### -field HRESULT(* )(IMFStreamDescriptor *This,IMFMediaTypeHandler **ppMediaTypeHandler) GetMediaTypeHandler			
 	
## -remarks

## -see-also