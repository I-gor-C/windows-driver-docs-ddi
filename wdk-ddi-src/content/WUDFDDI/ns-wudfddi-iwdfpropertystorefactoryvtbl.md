---
UID: NS.wudfddi.IWDFPropertyStoreFactoryVtbl
title: IWDFPropertyStoreFactoryVtbl
author: windows-driver-content
description: 
ms.assetid: 25ce4ce9-b208-4477-bfa9-149c1870dc61
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFPropertyStoreFactoryVtbl, IWDFPropertyStoreFactoryVtbl
req.header: wudfddi.h
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

# IWDFPropertyStoreFactoryVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFPropertyStoreFactory *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFPropertyStoreFactory *This) AddRef			
 	
### -field ULONG(* )(IWDFPropertyStoreFactory *This) Release			
 	
### -field HRESULT(* )(IWDFPropertyStoreFactory *This,PWDF_PROPERTY_STORE_ROOT RootSpecifier,WDF_PROPERTY_STORE_RETRIEVE_FLAGS Flags,REGSAM DesiredAccess,PCWSTR SubkeyPath,IWDFNamedPropertyStore2 **PropertyStore,WDF_PROPERTY_STORE_DISPOSITION *Disposition) RetrieveDevicePropertyStore			
 	
## -remarks

## -see-also