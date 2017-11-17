---
UID: NS.wiamindr_lh.IWiaDrvItemVtbl
title: IWiaDrvItemVtbl
author: windows-driver-content
description: 
ms.assetid: 97684334-83b7-4aca-b9bc-580852cee7c5
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWiaDrvItemVtbl, IWiaDrvItemVtbl
req.header: wiamindr_lh.h
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

# IWiaDrvItemVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWiaDrvItem *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWiaDrvItem *This) AddRef			
 	
### -field ULONG(* )(IWiaDrvItem *This) Release			
 	
### -field HRESULT(* )(IWiaDrvItem *This,LONG *__MIDL__IWiaDrvItem0000) GetItemFlags			
 	
### -field HRESULT(* )(IWiaDrvItem *This,BYTE **__MIDL__IWiaDrvItem0001) GetDeviceSpecContext			
 	
### -field HRESULT(* )(IWiaDrvItem *This,BSTR *__MIDL__IWiaDrvItem0002) GetFullItemName			
 	
### -field HRESULT(* )(IWiaDrvItem *This,BSTR *__MIDL__IWiaDrvItem0003) GetItemName			
 	
### -field HRESULT(* )(IWiaDrvItem *This,IWiaDrvItem *__MIDL__IWiaDrvItem0004) AddItemToFolder			
 	
### -field HRESULT(* )(IWiaDrvItem *This,LONG __MIDL__IWiaDrvItem0005) UnlinkItemTree			
 	
### -field HRESULT(* )(IWiaDrvItem *This,LONG __MIDL__IWiaDrvItem0006) RemoveItemFromFolder			
 	
### -field HRESULT(* )(IWiaDrvItem *This,LONG __MIDL__IWiaDrvItem0007,BSTR __MIDL__IWiaDrvItem0008,IWiaDrvItem **__MIDL__IWiaDrvItem0009) FindItemByName			
 	
### -field HRESULT(* )(IWiaDrvItem *This,BSTR __MIDL__IWiaDrvItem0010,IWiaDrvItem **__MIDL__IWiaDrvItem0011) FindChildItemByName			
 	
### -field HRESULT(* )(IWiaDrvItem *This,IWiaDrvItem **__MIDL__IWiaDrvItem0012) GetParentItem			
 	
### -field HRESULT(* )(IWiaDrvItem *This,IWiaDrvItem **__MIDL__IWiaDrvItem0013) GetFirstChildItem			
 	
### -field HRESULT(* )(IWiaDrvItem *This,IWiaDrvItem **__MIDL__IWiaDrvItem0014) GetNextSiblingItem			
 	
### -field HRESULT(* )(IWiaDrvItem *This,BSTR *__MIDL__IWiaDrvItem0015) DumpItemData			
 	
## -remarks

## -see-also