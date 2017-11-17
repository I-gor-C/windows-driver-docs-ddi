---
UID: NS.mfidl.IMFOutputSchemaVtbl
title: IMFOutputSchemaVtbl
author: windows-driver-content
description: 
ms.assetid: a0d27b36-d562-4cd3-99ba-82bab9992687
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFOutputSchemaVtbl, IMFOutputSchemaVtbl
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

# IMFOutputSchemaVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFOutputSchema *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFOutputSchema *This) AddRef			
 	
### -field ULONG(* )(IMFOutputSchema *This) Release			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey,PROPVARIANT *pValue) GetItem			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey,MF_ATTRIBUTE_TYPE *pType) GetItemType			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey,REFPROPVARIANT Value,BOOL *pbResult) CompareItem			
 	
### -field HRESULT(* )(IMFOutputSchema *This,IMFAttributes *pTheirs,MF_ATTRIBUTES_MATCH_TYPE MatchType,BOOL *pbResult) Compare			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey,UINT32 *punValue) GetUINT32			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey,UINT64 *punValue) GetUINT64			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey, double *pfValue) GetDouble			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey,GUID *pguidValue) GetGUID			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey,UINT32 *pcchLength) GetStringLength			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey,LPWSTR pwszValue,UINT32 cchBufSize,UINT32 *pcchLength) GetString			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey,LPWSTR *ppwszValue,UINT32 *pcchLength) GetAllocatedString			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey,UINT32 *pcbBlobSize) GetBlobSize			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey,UINT8 *pBuf,UINT32 cbBufSize,UINT32 *pcbBlobSize) GetBlob			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey,UINT8 **ppBuf,UINT32 *pcbSize) GetAllocatedBlob			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey,REFIID riid,LPVOID *ppv) GetUnknown			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey,REFPROPVARIANT Value) SetItem			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey) DeleteItem			
 	
### -field HRESULT(* )(IMFOutputSchema *This) DeleteAllItems			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey,UINT32 unValue) SetUINT32			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey,UINT64 unValue) SetUINT64			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey, double fValue) SetDouble			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey,REFGUID guidValue) SetGUID			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey,LPCWSTR wszValue) SetString			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey, const UINT8 *pBuf,UINT32 cbBufSize) SetBlob			
 	
### -field HRESULT(* )(IMFOutputSchema *This,REFGUID guidKey,IUnknown *pUnknown) SetUnknown			
 	
### -field HRESULT(* )(IMFOutputSchema *This) LockStore			
 	
### -field HRESULT(* )(IMFOutputSchema *This) UnlockStore			
 	
### -field HRESULT(* )(IMFOutputSchema *This,UINT32 *pcItems) GetCount			
 	
### -field HRESULT(* )(IMFOutputSchema *This,UINT32 unIndex,GUID *pguidKey,PROPVARIANT *pValue) GetItemByIndex			
 	
### -field HRESULT(* )(IMFOutputSchema *This,IMFAttributes *pDest) CopyAllItems			
 	
### -field HRESULT(* )(IMFOutputSchema *This,GUID *pguidSchemaType) GetSchemaType			
 	
### -field HRESULT(* )(IMFOutputSchema *This,DWORD *pdwVal) GetConfigurationData			
 	
### -field HRESULT(* )(IMFOutputSchema *This,GUID *pguidOriginatorID) GetOriginatorID			
 	
## -remarks

## -see-also