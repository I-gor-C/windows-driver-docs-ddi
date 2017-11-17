---
UID: NS.wudfddi.IWDFDevice3Vtbl
title: IWDFDevice3Vtbl
author: windows-driver-content
description: 
ms.assetid: 79d81a4e-7cc4-4428-9927-77afe0c6b11c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFDevice3Vtbl, IWDFDevice3Vtbl
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

# IWDFDevice3Vtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFDevice3 *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFDevice3 *This) AddRef			
 	
### -field ULONG(* )(IWDFDevice3 *This) Release			
 	
### -field HRESULT(* )(IWDFDevice3 *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFDevice3 *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFDevice3 *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFDevice3 *This) AcquireLock			
 	
### -field void(* )(IWDFDevice3 *This) ReleaseLock			
 	
### -field HRESULT(* )(IWDFDevice3 *This,PCWSTR pcwszServiceName,WDF_PROPERTY_STORE_RETRIEVE_FLAGS Flags,IWDFNamedPropertyStore **ppPropStore,WDF_PROPERTY_STORE_DISPOSITION *pDisposition) RetrieveDevicePropertyStore			
 	
### -field void(* )(IWDFDevice3 *This,IWDFDriver **ppWdfDriver) GetDriver			
 	
### -field HRESULT(* )(IWDFDevice3 *This,PWSTR Buffer,DWORD *pdwSizeInChars) RetrieveDeviceInstanceId			
 	
### -field void(* )(IWDFDevice3 *This,IWDFIoTarget **ppWdfIoTarget) GetDefaultIoTarget			
 	
### -field HRESULT(* )(IWDFDevice3 *This,LPCWSTR pcwszFileName,IWDFDriverCreatedFile **ppFile) CreateWdfFile			
 	
### -field void(* )(IWDFDevice3 *This,IWDFIoQueue **ppWdfIoQueue) GetDefaultIoQueue			
 	
### -field HRESULT(* )(IWDFDevice3 *This,IUnknown *pCallbackInterface,BOOL bDefaultQueue,WDF_IO_QUEUE_DISPATCH_TYPE DispatchType,BOOL bPowerManaged,BOOL bAllowZeroLengthRequests,IWDFIoQueue **ppIoQueue) CreateIoQueue			
 	
### -field HRESULT(* )(IWDFDevice3 *This,LPCGUID pDeviceInterfaceGuid,PCWSTR pReferenceString) CreateDeviceInterface			
 	
### -field HRESULT(* )(IWDFDevice3 *This,LPCGUID pDeviceInterfaceGuid,PCWSTR pReferenceString,BOOL Enable) AssignDeviceInterfaceState			
 	
### -field HRESULT(* )(IWDFDevice3 *This,PWSTR pDeviceName,DWORD *pdwDeviceNameLength) RetrieveDeviceName			
 	
### -field HRESULT(* )(IWDFDevice3 *This,REFGUID EventGuid,WDF_EVENT_TYPE EventType,BYTE *pbData,DWORD cbDataSize) PostEvent			
 	
### -field HRESULT(* )(IWDFDevice3 *This,IWDFIoQueue *pQueue,WDF_REQUEST_TYPE RequestType,BOOL Forward) ConfigureRequestDispatching			
 	
### -field void(* )(IWDFDevice3 *This,WDF_PNP_STATE State,WDF_TRI_STATE Value) SetPnpState			
 	
### -field WDF_TRI_STATE(* )(IWDFDevice3 *This,WDF_PNP_STATE State) GetPnpState			
 	
### -field void(* )(IWDFDevice3 *This) CommitPnpState			
 	
### -field HRESULT(* )(IWDFDevice3 *This,IUnknown *pCallbackInterface,IWDFObject *pParentObject,IWDFIoRequest **ppRequest) CreateRequest			
 	
### -field HRESULT(* )(IWDFDevice3 *This,PCWSTR pSymbolicLink) CreateSymbolicLink			
 	
### -field HRESULT(* )(IWDFDevice3 *This,WDF_POWER_POLICY_S0_IDLE_CAPABILITIES IdleCaps,DEVICE_POWER_STATE DxState,ULONG IdleTimeout,WDF_POWER_POLICY_S0_IDLE_USER_CONTROL UserControlOfIdleSettings,WDF_TRI_STATE Enabled) AssignS0IdleSettings			
 	
### -field HRESULT(* )(IWDFDevice3 *This,BOOL WaitForD0) StopIdle			
 	
### -field void(* )(IWDFDevice3 *This) ResumeIdle			
 	
### -field HRESULT(* )(IWDFDevice3 *This,PCWSTR pSymbolicLink,PCWSTR pReferenceString) CreateSymbolicLinkWithReferenceString			
 	
### -field HRESULT(* )(IWDFDevice3 *This,LPCGUID pDeviceInterfaceGuid,BOOL IncludeExistingInterfaces) RegisterRemoteInterfaceNotification			
 	
### -field HRESULT(* )(IWDFDevice3 *This,IWDFRemoteInterfaceInitialize *pRemoteInterfaceInit,IUnknown *pCallbackInterface,IWDFRemoteInterface **ppRemoteInterface) CreateRemoteInterface			
 	
### -field HRESULT(* )(IWDFDevice3 *This,IUnknown *pCallbackInterface,IWDFObject *pParentObject,IWDFRemoteTarget **ppRemoteTarget) CreateRemoteTarget			
 	
### -field void(* )(IWDFDevice3 *This,WDF_DEVICE_IO_TYPE *ReadWritePreference,WDF_DEVICE_IO_TYPE *IoControlPreference) GetDeviceStackIoTypePreference			
 	
### -field HRESULT(* )(IWDFDevice3 *This,DEVICE_POWER_STATE DxState,WDF_POWER_POLICY_SX_WAKE_USER_CONTROL UserControlOfWakeSettings,WDF_TRI_STATE Enabled) AssignSxWakeSettings			
 	
### -field POWER_ACTION(* )(IWDFDevice3 *This) GetSystemPowerAction			
 	
### -field HRESULT(* )(IWDFDevice3 *This,PHYSICAL_ADDRESS PhysicalAddress,SIZE_T NumberOfBytes,MEMORY_CACHING_TYPE CacheType, void **pPseudoBaseAddress) MapIoSpace			
 	
### -field void(* )(IWDFDevice3 *This, void *PseudoBaseAddress,SIZE_T NumberOfBytes) UnmapIoSpace			
 	
### -field void *(* )(IWDFDevice3 *This, void *PseudoBaseAddress) GetHardwareRegisterMappedAddress			
 	
### -field SIZE_T(* )(IWDFDevice3 *This,WDF_DEVICE_HWACCESS_TARGET_TYPE Type,WDF_DEVICE_HWACCESS_TARGET_SIZE Size, void *Address, void *Buffer,ULONG Count) ReadFromHardware			
 	
### -field void(* )(IWDFDevice3 *This,WDF_DEVICE_HWACCESS_TARGET_TYPE Type,WDF_DEVICE_HWACCESS_TARGET_SIZE Size, void *Address,SIZE_T Value, void *Buffer,ULONG Count) WriteToHardware			
 	
### -field HRESULT(* )(IWDFDevice3 *This,PWUDF_INTERRUPT_CONFIG Configuration,IWDFInterrupt **ppInterrupt) CreateInterrupt			
 	
### -field HRESULT(* )(IWDFDevice3 *This,PWUDF_WORKITEM_CONFIG pConfig,IWDFObject *pParentObject,IWDFWorkItem **ppWorkItem) CreateWorkItem			
 	
### -field HRESULT(* )(IWDFDevice3 *This,PWUDF_DEVICE_POWER_POLICY_IDLE_SETTINGS IdleSettings) AssignS0IdleSettingsEx			
 	
## -remarks

## -see-also