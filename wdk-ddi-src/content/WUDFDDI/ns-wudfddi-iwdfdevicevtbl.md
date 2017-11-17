---
UID: NS.wudfddi.IWDFDeviceVtbl
title: IWDFDeviceVtbl
author: windows-driver-content
description: 
ms.assetid: 965cde77-bd1c-4213-a8e6-896d09c0610f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFDeviceVtbl, IWDFDeviceVtbl
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

# IWDFDeviceVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFDevice *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFDevice *This) AddRef			
 	
### -field ULONG(* )(IWDFDevice *This) Release			
 	
### -field HRESULT(* )(IWDFDevice *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFDevice *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFDevice *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFDevice *This) AcquireLock			
 	
### -field void(* )(IWDFDevice *This) ReleaseLock			
 	
### -field HRESULT(* )(IWDFDevice *This,PCWSTR pcwszServiceName,WDF_PROPERTY_STORE_RETRIEVE_FLAGS Flags,IWDFNamedPropertyStore **ppPropStore,WDF_PROPERTY_STORE_DISPOSITION *pDisposition) RetrieveDevicePropertyStore			
 	
### -field void(* )(IWDFDevice *This,IWDFDriver **ppWdfDriver) GetDriver			
 	
### -field HRESULT(* )(IWDFDevice *This,PWSTR Buffer,DWORD *pdwSizeInChars) RetrieveDeviceInstanceId			
 	
### -field void(* )(IWDFDevice *This,IWDFIoTarget **ppWdfIoTarget) GetDefaultIoTarget			
 	
### -field HRESULT(* )(IWDFDevice *This,LPCWSTR pcwszFileName,IWDFDriverCreatedFile **ppFile) CreateWdfFile			
 	
### -field void(* )(IWDFDevice *This,IWDFIoQueue **ppWdfIoQueue) GetDefaultIoQueue			
 	
### -field HRESULT(* )(IWDFDevice *This,IUnknown *pCallbackInterface,BOOL bDefaultQueue,WDF_IO_QUEUE_DISPATCH_TYPE DispatchType,BOOL bPowerManaged,BOOL bAllowZeroLengthRequests,IWDFIoQueue **ppIoQueue) CreateIoQueue			
 	
### -field HRESULT(* )(IWDFDevice *This,LPCGUID pDeviceInterfaceGuid,PCWSTR pReferenceString) CreateDeviceInterface			
 	
### -field HRESULT(* )(IWDFDevice *This,LPCGUID pDeviceInterfaceGuid,PCWSTR pReferenceString,BOOL Enable) AssignDeviceInterfaceState			
 	
### -field HRESULT(* )(IWDFDevice *This,PWSTR pDeviceName,DWORD *pdwDeviceNameLength) RetrieveDeviceName			
 	
### -field HRESULT(* )(IWDFDevice *This,REFGUID EventGuid,WDF_EVENT_TYPE EventType,BYTE *pbData,DWORD cbDataSize) PostEvent			
 	
### -field HRESULT(* )(IWDFDevice *This,IWDFIoQueue *pQueue,WDF_REQUEST_TYPE RequestType,BOOL Forward) ConfigureRequestDispatching			
 	
### -field void(* )(IWDFDevice *This,WDF_PNP_STATE State,WDF_TRI_STATE Value) SetPnpState			
 	
### -field WDF_TRI_STATE(* )(IWDFDevice *This,WDF_PNP_STATE State) GetPnpState			
 	
### -field void(* )(IWDFDevice *This) CommitPnpState			
 	
### -field HRESULT(* )(IWDFDevice *This,IUnknown *pCallbackInterface,IWDFObject *pParentObject,IWDFIoRequest **ppRequest) CreateRequest			
 	
### -field HRESULT(* )(IWDFDevice *This,PCWSTR pSymbolicLink) CreateSymbolicLink			
 	
## -remarks

## -see-also