---
UID: NS.mfidl.IMFOutputPolicyVtbl
title: IMFOutputPolicyVtbl
author: windows-driver-content
description: 
ms.assetid: 5f00585b-a3a8-416d-b652-d73d7c5ae24b
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFOutputPolicyVtbl, IMFOutputPolicyVtbl
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

# IMFOutputPolicyVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFOutputPolicy *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFOutputPolicy *This) AddRef			
 	
### -field ULONG(* )(IMFOutputPolicy *This) Release			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey,PROPVARIANT *pValue) GetItem			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey,MF_ATTRIBUTE_TYPE *pType) GetItemType			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey,REFPROPVARIANT Value,BOOL *pbResult) CompareItem			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,IMFAttributes *pTheirs,MF_ATTRIBUTES_MATCH_TYPE MatchType,BOOL *pbResult) Compare			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey,UINT32 *punValue) GetUINT32			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey,UINT64 *punValue) GetUINT64			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey, double *pfValue) GetDouble			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey,GUID *pguidValue) GetGUID			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey,UINT32 *pcchLength) GetStringLength			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey,LPWSTR pwszValue,UINT32 cchBufSize,UINT32 *pcchLength) GetString			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey,LPWSTR *ppwszValue,UINT32 *pcchLength) GetAllocatedString			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey,UINT32 *pcbBlobSize) GetBlobSize			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey,UINT8 *pBuf,UINT32 cbBufSize,UINT32 *pcbBlobSize) GetBlob			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey,UINT8 **ppBuf,UINT32 *pcbSize) GetAllocatedBlob			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey,REFIID riid,LPVOID *ppv) GetUnknown			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey,REFPROPVARIANT Value) SetItem			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey) DeleteItem			
 	
### -field HRESULT(* )(IMFOutputPolicy *This) DeleteAllItems			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey,UINT32 unValue) SetUINT32			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey,UINT64 unValue) SetUINT64			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey, double fValue) SetDouble			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey,REFGUID guidValue) SetGUID			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey,LPCWSTR wszValue) SetString			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey, const UINT8 *pBuf,UINT32 cbBufSize) SetBlob			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,REFGUID guidKey,IUnknown *pUnknown) SetUnknown			
 	
### -field HRESULT(* )(IMFOutputPolicy *This) LockStore			
 	
### -field HRESULT(* )(IMFOutputPolicy *This) UnlockStore			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,UINT32 *pcItems) GetCount			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,UINT32 unIndex,GUID *pguidKey,PROPVARIANT *pValue) GetItemByIndex			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,IMFAttributes *pDest) CopyAllItems			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,DWORD dwAttributes,GUID guidOutputSubType,GUID *rgGuidProtectionSchemasSupported,DWORD cProtectionSchemasSupported,IMFCollection **ppRequiredProtectionSchemas) GenerateRequiredSchemas			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,GUID *pguidOriginatorID) GetOriginatorID			
 	
### -field HRESULT(* )(IMFOutputPolicy *This,DWORD *pdwMinimumGRLVersion) GetMinimumGRLVersion			
 	
## -remarks

## -see-also