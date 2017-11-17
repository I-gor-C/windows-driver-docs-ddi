---
UID: NS.mfidl.IMFTopologyVtbl
title: IMFTopologyVtbl
author: windows-driver-content
description: 
ms.assetid: 8538ad6f-c16d-4cc7-be1f-9d075b7388d2
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFTopologyVtbl, IMFTopologyVtbl
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

# IMFTopologyVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFTopology *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFTopology *This) AddRef			
 	
### -field ULONG(* )(IMFTopology *This) Release			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey,PROPVARIANT *pValue) GetItem			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey,MF_ATTRIBUTE_TYPE *pType) GetItemType			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey,REFPROPVARIANT Value,BOOL *pbResult) CompareItem			
 	
### -field HRESULT(* )(IMFTopology *This,IMFAttributes *pTheirs,MF_ATTRIBUTES_MATCH_TYPE MatchType,BOOL *pbResult) Compare			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey,UINT32 *punValue) GetUINT32			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey,UINT64 *punValue) GetUINT64			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey, double *pfValue) GetDouble			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey,GUID *pguidValue) GetGUID			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey,UINT32 *pcchLength) GetStringLength			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey,LPWSTR pwszValue,UINT32 cchBufSize,UINT32 *pcchLength) GetString			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey,LPWSTR *ppwszValue,UINT32 *pcchLength) GetAllocatedString			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey,UINT32 *pcbBlobSize) GetBlobSize			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey,UINT8 *pBuf,UINT32 cbBufSize,UINT32 *pcbBlobSize) GetBlob			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey,UINT8 **ppBuf,UINT32 *pcbSize) GetAllocatedBlob			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey,REFIID riid,LPVOID *ppv) GetUnknown			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey,REFPROPVARIANT Value) SetItem			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey) DeleteItem			
 	
### -field HRESULT(* )(IMFTopology *This) DeleteAllItems			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey,UINT32 unValue) SetUINT32			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey,UINT64 unValue) SetUINT64			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey, double fValue) SetDouble			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey,REFGUID guidValue) SetGUID			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey,LPCWSTR wszValue) SetString			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey, const UINT8 *pBuf,UINT32 cbBufSize) SetBlob			
 	
### -field HRESULT(* )(IMFTopology *This,REFGUID guidKey,IUnknown *pUnknown) SetUnknown			
 	
### -field HRESULT(* )(IMFTopology *This) LockStore			
 	
### -field HRESULT(* )(IMFTopology *This) UnlockStore			
 	
### -field HRESULT(* )(IMFTopology *This,UINT32 *pcItems) GetCount			
 	
### -field HRESULT(* )(IMFTopology *This,UINT32 unIndex,GUID *pguidKey,PROPVARIANT *pValue) GetItemByIndex			
 	
### -field HRESULT(* )(IMFTopology *This,IMFAttributes *pDest) CopyAllItems			
 	
### -field HRESULT(* )(IMFTopology *This,TOPOID *pID) GetTopologyID			
 	
### -field HRESULT(* )(IMFTopology *This,IMFTopologyNode *pNode) AddNode			
 	
### -field HRESULT(* )(IMFTopology *This,IMFTopologyNode *pNode) RemoveNode			
 	
### -field HRESULT(* )(IMFTopology *This,WORD *pwNodes) GetNodeCount			
 	
### -field HRESULT(* )(IMFTopology *This,WORD wIndex,IMFTopologyNode **ppNode) GetNode			
 	
### -field HRESULT(* )(IMFTopology *This) Clear			
 	
### -field HRESULT(* )(IMFTopology *This,IMFTopology *pTopology) CloneFrom			
 	
### -field HRESULT(* )(IMFTopology *This,TOPOID qwTopoNodeID,IMFTopologyNode **ppNode) GetNodeByID			
 	
### -field HRESULT(* )(IMFTopology *This,IMFCollection **ppCollection) GetSourceNodeCollection			
 	
### -field HRESULT(* )(IMFTopology *This,IMFCollection **ppCollection) GetOutputNodeCollection			
 	
## -remarks

## -see-also