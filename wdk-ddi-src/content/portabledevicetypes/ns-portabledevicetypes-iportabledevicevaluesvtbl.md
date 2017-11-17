---
UID: NS.portabledevicetypes.IPortableDeviceValuesVtbl
title: IPortableDeviceValuesVtbl
author: windows-driver-content
description: 
ms.assetid: 25f102af-69c6-4828-a643-538d06b6371f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IPortableDeviceValuesVtbl, IPortableDeviceValuesVtbl
req.header: portabledevicetypes.h
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

# IPortableDeviceValuesVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IPortableDeviceValues *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IPortableDeviceValues *This) AddRef			
 	
### -field ULONG(* )(IPortableDeviceValues *This) Release			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,DWORD *pcelt) GetCount			
 	
### -field HRESULT(* )(IPortableDeviceValues *This, const DWORD index,PROPERTYKEY *pKey,PROPVARIANT *pValue) GetAt			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key, const PROPVARIANT *pValue) SetValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,PROPVARIANT *pValue) GetValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,LPCWSTR Value) SetStringValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,LPWSTR *pValue) GetStringValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key, const ULONG Value) SetUnsignedIntegerValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,ULONG *pValue) GetUnsignedIntegerValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key, const LONG Value) SetSignedIntegerValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,LONG *pValue) GetSignedIntegerValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key, const ULONGLONG Value) SetUnsignedLargeIntegerValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,ULONGLONG *pValue) GetUnsignedLargeIntegerValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key, const LONGLONG Value) SetSignedLargeIntegerValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,LONGLONG *pValue) GetSignedLargeIntegerValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key, const FLOAT Value) SetFloatValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,FLOAT *pValue) GetFloatValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key, const HRESULT Value) SetErrorValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,HRESULT *pValue) GetErrorValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,REFPROPERTYKEY Value) SetKeyValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,PROPERTYKEY *pValue) GetKeyValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key, const BOOL Value) SetBoolValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,BOOL *pValue) GetBoolValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,IUnknown *pValue) SetIUnknownValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,IUnknown **ppValue) GetIUnknownValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,REFGUID Value) SetGuidValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,GUID *pValue) GetGuidValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,BYTE *pValue,DWORD cbValue) SetBufferValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,BYTE **ppValue,DWORD *pcbValue) GetBufferValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,IPortableDeviceValues *pValue) SetIPortableDeviceValuesValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,IPortableDeviceValues **ppValue) GetIPortableDeviceValuesValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,IPortableDevicePropVariantCollection *pValue) SetIPortableDevicePropVariantCollectionValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,IPortableDevicePropVariantCollection **ppValue) GetIPortableDevicePropVariantCollectionValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,IPortableDeviceKeyCollection *pValue) SetIPortableDeviceKeyCollectionValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,IPortableDeviceKeyCollection **ppValue) GetIPortableDeviceKeyCollectionValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,IPortableDeviceValuesCollection *pValue) SetIPortableDeviceValuesCollectionValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key,IPortableDeviceValuesCollection **ppValue) GetIPortableDeviceValuesCollectionValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,REFPROPERTYKEY key) RemoveValue			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,IPropertyStore *pStore) CopyValuesFromPropertyStore			
 	
### -field HRESULT(* )(IPortableDeviceValues *This,IPropertyStore *pStore) CopyValuesToPropertyStore			
 	
### -field HRESULT(* )(IPortableDeviceValues *This) Clear			
 	
## -remarks

## -see-also