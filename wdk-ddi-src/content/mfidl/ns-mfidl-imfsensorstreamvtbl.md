---
UID: NS.mfidl.IMFSensorStreamVtbl
title: IMFSensorStreamVtbl
author: windows-driver-content
description: 
ms.assetid: ac584866-05eb-40ef-bc4d-d9ea4d09e949
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFSensorStreamVtbl, IMFSensorStreamVtbl
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

# IMFSensorStreamVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFSensorStream *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFSensorStream *This) AddRef			
 	
### -field ULONG(* )(IMFSensorStream *This) Release			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey,PROPVARIANT *pValue) GetItem			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey,MF_ATTRIBUTE_TYPE *pType) GetItemType			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey,REFPROPVARIANT Value,BOOL *pbResult) CompareItem			
 	
### -field HRESULT(* )(IMFSensorStream *This,IMFAttributes *pTheirs,MF_ATTRIBUTES_MATCH_TYPE MatchType,BOOL *pbResult) Compare			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey,UINT32 *punValue) GetUINT32			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey,UINT64 *punValue) GetUINT64			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey, double *pfValue) GetDouble			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey,GUID *pguidValue) GetGUID			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey,UINT32 *pcchLength) GetStringLength			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey,LPWSTR pwszValue,UINT32 cchBufSize,UINT32 *pcchLength) GetString			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey,LPWSTR *ppwszValue,UINT32 *pcchLength) GetAllocatedString			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey,UINT32 *pcbBlobSize) GetBlobSize			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey,UINT8 *pBuf,UINT32 cbBufSize,UINT32 *pcbBlobSize) GetBlob			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey,UINT8 **ppBuf,UINT32 *pcbSize) GetAllocatedBlob			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey,REFIID riid,LPVOID *ppv) GetUnknown			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey,REFPROPVARIANT Value) SetItem			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey) DeleteItem			
 	
### -field HRESULT(* )(IMFSensorStream *This) DeleteAllItems			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey,UINT32 unValue) SetUINT32			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey,UINT64 unValue) SetUINT64			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey, double fValue) SetDouble			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey,REFGUID guidValue) SetGUID			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey,LPCWSTR wszValue) SetString			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey, const UINT8 *pBuf,UINT32 cbBufSize) SetBlob			
 	
### -field HRESULT(* )(IMFSensorStream *This,REFGUID guidKey,IUnknown *pUnknown) SetUnknown			
 	
### -field HRESULT(* )(IMFSensorStream *This) LockStore			
 	
### -field HRESULT(* )(IMFSensorStream *This) UnlockStore			
 	
### -field HRESULT(* )(IMFSensorStream *This,UINT32 *pcItems) GetCount			
 	
### -field HRESULT(* )(IMFSensorStream *This,UINT32 unIndex,GUID *pguidKey,PROPVARIANT *pValue) GetItemByIndex			
 	
### -field HRESULT(* )(IMFSensorStream *This,IMFAttributes *pDest) CopyAllItems			
 	
### -field HRESULT(* )(IMFSensorStream *This,DWORD *pdwCount) GetMediaTypeCount			
 	
### -field HRESULT(* )(IMFSensorStream *This,DWORD dwIndex,IMFMediaType **ppMediaType) GetMediaType			
 	
### -field HRESULT(* )(IMFSensorStream *This,IMFSensorStream **ppStream) CloneSensorStream			
 	
## -remarks

## -see-also