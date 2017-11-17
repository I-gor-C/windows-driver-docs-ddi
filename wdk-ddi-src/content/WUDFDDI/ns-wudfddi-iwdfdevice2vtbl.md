---
UID: NS.wudfddi.IWDFDevice2Vtbl
title: IWDFDevice2Vtbl
author: windows-driver-content
description: 
ms.assetid: 3e4a5920-6151-4fda-8dca-a34965c45c49
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFDevice2Vtbl, IWDFDevice2Vtbl
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

# IWDFDevice2Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFDevice2 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFDevice2 *This) AddRef			
 	
### -field ULONG(* )(IWDFDevice2 *This) Release			
 	
### -field HRESULT(* )(IWDFDevice2 *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFDevice2 *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFDevice2 *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFDevice2 *This) AcquireLock			
 	
### -field void(* )(IWDFDevice2 *This) ReleaseLock			
 	
### -field HRESULT(* )(IWDFDevice2 *This,PCWSTR pcwszServiceName,WDF_PROPERTY_STORE_RETRIEVE_FLAGS Flags,IWDFNamedPropertyStore **ppPropStore,WDF_PROPERTY_STORE_DISPOSITION *pDisposition) RetrieveDevicePropertyStore			
 	
### -field void(* )(IWDFDevice2 *This,IWDFDriver **ppWdfDriver) GetDriver			
 	
### -field HRESULT(* )(IWDFDevice2 *This,PWSTR Buffer,DWORD *pdwSizeInChars) RetrieveDeviceInstanceId			
 	
### -field void(* )(IWDFDevice2 *This,IWDFIoTarget **ppWdfIoTarget) GetDefaultIoTarget			
 	
### -field HRESULT(* )(IWDFDevice2 *This,LPCWSTR pcwszFileName,IWDFDriverCreatedFile **ppFile) CreateWdfFile			
 	
### -field void(* )(IWDFDevice2 *This,IWDFIoQueue **ppWdfIoQueue) GetDefaultIoQueue			
 	
### -field HRESULT(* )(IWDFDevice2 *This,IUnknown *pCallbackInterface,BOOL bDefaultQueue,WDF_IO_QUEUE_DISPATCH_TYPE DispatchType,BOOL bPowerManaged,BOOL bAllowZeroLengthRequests,IWDFIoQueue **ppIoQueue) CreateIoQueue			
 	
### -field HRESULT(* )(IWDFDevice2 *This,LPCGUID pDeviceInterfaceGuid,PCWSTR pReferenceString) CreateDeviceInterface			
 	
### -field HRESULT(* )(IWDFDevice2 *This,LPCGUID pDeviceInterfaceGuid,PCWSTR pReferenceString,BOOL Enable) AssignDeviceInterfaceState			
 	
### -field HRESULT(* )(IWDFDevice2 *This,PWSTR pDeviceName,DWORD *pdwDeviceNameLength) RetrieveDeviceName			
 	
### -field HRESULT(* )(IWDFDevice2 *This,REFGUID EventGuid,WDF_EVENT_TYPE EventType,BYTE *pbData,DWORD cbDataSize) PostEvent			
 	
### -field HRESULT(* )(IWDFDevice2 *This,IWDFIoQueue *pQueue,WDF_REQUEST_TYPE RequestType,BOOL Forward) ConfigureRequestDispatching			
 	
### -field void(* )(IWDFDevice2 *This,WDF_PNP_STATE State,WDF_TRI_STATE Value) SetPnpState			
 	
### -field WDF_TRI_STATE(* )(IWDFDevice2 *This,WDF_PNP_STATE State) GetPnpState			
 	
### -field void(* )(IWDFDevice2 *This) CommitPnpState			
 	
### -field HRESULT(* )(IWDFDevice2 *This,IUnknown *pCallbackInterface,IWDFObject *pParentObject,IWDFIoRequest **ppRequest) CreateRequest			
 	
### -field HRESULT(* )(IWDFDevice2 *This,PCWSTR pSymbolicLink) CreateSymbolicLink			
 	
### -field HRESULT(* )(IWDFDevice2 *This,WDF_POWER_POLICY_S0_IDLE_CAPABILITIES IdleCaps,DEVICE_POWER_STATE DxState,ULONG IdleTimeout,WDF_POWER_POLICY_S0_IDLE_USER_CONTROL UserControlOfIdleSettings,WDF_TRI_STATE Enabled) AssignS0IdleSettings			
 	
### -field HRESULT(* )(IWDFDevice2 *This,BOOL WaitForD0) StopIdle			
 	
### -field void(* )(IWDFDevice2 *This) ResumeIdle			
 	
### -field HRESULT(* )(IWDFDevice2 *This,PCWSTR pSymbolicLink,PCWSTR pReferenceString) CreateSymbolicLinkWithReferenceString			
 	
### -field HRESULT(* )(IWDFDevice2 *This,LPCGUID pDeviceInterfaceGuid,BOOL IncludeExistingInterfaces) RegisterRemoteInterfaceNotification			
 	
### -field HRESULT(* )(IWDFDevice2 *This,IWDFRemoteInterfaceInitialize *pRemoteInterfaceInit,IUnknown *pCallbackInterface,IWDFRemoteInterface **ppRemoteInterface) CreateRemoteInterface			
 	
### -field HRESULT(* )(IWDFDevice2 *This,IUnknown *pCallbackInterface,IWDFObject *pParentObject,IWDFRemoteTarget **ppRemoteTarget) CreateRemoteTarget			
 	
### -field void(* )(IWDFDevice2 *This,WDF_DEVICE_IO_TYPE *ReadWritePreference,WDF_DEVICE_IO_TYPE *IoControlPreference) GetDeviceStackIoTypePreference			
 	
### -field HRESULT(* )(IWDFDevice2 *This,DEVICE_POWER_STATE DxState,WDF_POWER_POLICY_SX_WAKE_USER_CONTROL UserControlOfWakeSettings,WDF_TRI_STATE Enabled) AssignSxWakeSettings			
 	
### -field POWER_ACTION(* )(IWDFDevice2 *This) GetSystemPowerAction			
 	
## -remarks

## -see-also