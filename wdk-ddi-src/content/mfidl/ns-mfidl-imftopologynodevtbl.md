---
UID: NS.mfidl.IMFTopologyNodeVtbl
title: IMFTopologyNodeVtbl
author: windows-driver-content
description: 
ms.assetid: 6e123d57-fcab-476f-9a40-88deb9d64a55
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFTopologyNodeVtbl, IMFTopologyNodeVtbl
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

# IMFTopologyNodeVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFTopologyNode *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFTopologyNode *This) AddRef			
 	
### -field ULONG(* )(IMFTopologyNode *This) Release			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey,PROPVARIANT *pValue) GetItem			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey,MF_ATTRIBUTE_TYPE *pType) GetItemType			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey,REFPROPVARIANT Value,BOOL *pbResult) CompareItem			
 	
### -field HRESULT(* )(IMFTopologyNode *This,IMFAttributes *pTheirs,MF_ATTRIBUTES_MATCH_TYPE MatchType,BOOL *pbResult) Compare			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey,UINT32 *punValue) GetUINT32			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey,UINT64 *punValue) GetUINT64			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey, double *pfValue) GetDouble			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey,GUID *pguidValue) GetGUID			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey,UINT32 *pcchLength) GetStringLength			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey,LPWSTR pwszValue,UINT32 cchBufSize,UINT32 *pcchLength) GetString			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey,LPWSTR *ppwszValue,UINT32 *pcchLength) GetAllocatedString			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey,UINT32 *pcbBlobSize) GetBlobSize			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey,UINT8 *pBuf,UINT32 cbBufSize,UINT32 *pcbBlobSize) GetBlob			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey,UINT8 **ppBuf,UINT32 *pcbSize) GetAllocatedBlob			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey,REFIID riid,LPVOID *ppv) GetUnknown			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey,REFPROPVARIANT Value) SetItem			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey) DeleteItem			
 	
### -field HRESULT(* )(IMFTopologyNode *This) DeleteAllItems			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey,UINT32 unValue) SetUINT32			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey,UINT64 unValue) SetUINT64			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey, double fValue) SetDouble			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey,REFGUID guidValue) SetGUID			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey,LPCWSTR wszValue) SetString			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey, const UINT8 *pBuf,UINT32 cbBufSize) SetBlob			
 	
### -field HRESULT(* )(IMFTopologyNode *This,REFGUID guidKey,IUnknown *pUnknown) SetUnknown			
 	
### -field HRESULT(* )(IMFTopologyNode *This) LockStore			
 	
### -field HRESULT(* )(IMFTopologyNode *This) UnlockStore			
 	
### -field HRESULT(* )(IMFTopologyNode *This,UINT32 *pcItems) GetCount			
 	
### -field HRESULT(* )(IMFTopologyNode *This,UINT32 unIndex,GUID *pguidKey,PROPVARIANT *pValue) GetItemByIndex			
 	
### -field HRESULT(* )(IMFTopologyNode *This,IMFAttributes *pDest) CopyAllItems			
 	
### -field HRESULT(* )(IMFTopologyNode *This,IUnknown *pObject) SetObject			
 	
### -field HRESULT(* )(IMFTopologyNode *This,IUnknown **ppObject) GetObject			
 	
### -field HRESULT(* )(IMFTopologyNode *This,MF_TOPOLOGY_TYPE *pType) GetNodeType			
 	
### -field HRESULT(* )(IMFTopologyNode *This,TOPOID *pID) GetTopoNodeID			
 	
### -field HRESULT(* )(IMFTopologyNode *This,TOPOID ullTopoID) SetTopoNodeID			
 	
### -field HRESULT(* )(IMFTopologyNode *This,DWORD *pcInputs) GetInputCount			
 	
### -field HRESULT(* )(IMFTopologyNode *This,DWORD *pcOutputs) GetOutputCount			
 	
### -field HRESULT(* )(IMFTopologyNode *This,DWORD dwOutputIndex,IMFTopologyNode *pDownstreamNode,DWORD dwInputIndexOnDownstreamNode) ConnectOutput			
 	
### -field HRESULT(* )(IMFTopologyNode *This,DWORD dwOutputIndex) DisconnectOutput			
 	
### -field HRESULT(* )(IMFTopologyNode *This,DWORD dwInputIndex,IMFTopologyNode **ppUpstreamNode,DWORD *pdwOutputIndexOnUpstreamNode) GetInput			
 	
### -field HRESULT(* )(IMFTopologyNode *This,DWORD dwOutputIndex,IMFTopologyNode **ppDownstreamNode,DWORD *pdwInputIndexOnDownstreamNode) GetOutput			
 	
### -field HRESULT(* )(IMFTopologyNode *This,DWORD dwOutputIndex,IMFMediaType *pType) SetOutputPrefType			
 	
### -field HRESULT(* )(IMFTopologyNode *This,DWORD dwOutputIndex,IMFMediaType **ppType) GetOutputPrefType			
 	
### -field HRESULT(* )(IMFTopologyNode *This,DWORD dwInputIndex,IMFMediaType *pType) SetInputPrefType			
 	
### -field HRESULT(* )(IMFTopologyNode *This,DWORD dwInputIndex,IMFMediaType **ppType) GetInputPrefType			
 	
### -field HRESULT(* )(IMFTopologyNode *This,IMFTopologyNode *pNode) CloneFrom			
 	
## -remarks

## -see-also