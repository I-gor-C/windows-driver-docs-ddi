---
UID: NS.wudfusb.IWDFUsbTargetDeviceVtbl
title: IWDFUsbTargetDeviceVtbl
author: windows-driver-content
description: 
ms.assetid: 87b107e8-d20b-438f-807e-36fd838faf05
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFUsbTargetDeviceVtbl, IWDFUsbTargetDeviceVtbl
req.header: wudfusb.h
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

# IWDFUsbTargetDeviceVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFUsbTargetDevice *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFUsbTargetDevice *This) AddRef			
 	
### -field ULONG(* )(IWDFUsbTargetDevice *This) Release			
 	
### -field HRESULT(* )(IWDFUsbTargetDevice *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFUsbTargetDevice *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFUsbTargetDevice *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFUsbTargetDevice *This) AcquireLock			
 	
### -field void(* )(IWDFUsbTargetDevice *This) ReleaseLock			
 	
### -field void(* )(IWDFUsbTargetDevice *This,IWDFFile **ppWdfFile) GetTargetFile			
 	
### -field void(* )(IWDFUsbTargetDevice *This,IWDFFile *pFile) CancelSentRequestsForFile			
 	
### -field HRESULT(* )(IWDFUsbTargetDevice *This,IWDFIoRequest *pRequest,IWDFFile *pFile,IWDFMemory *pOutputMemory,PWDFMEMORY_OFFSET pOutputMemoryOffset,PLONGLONG DeviceOffset) FormatRequestForRead			
 	
### -field HRESULT(* )(IWDFUsbTargetDevice *This,IWDFIoRequest *pRequest,IWDFFile *pFile,IWDFMemory *pInputMemory,PWDFMEMORY_OFFSET pInputMemoryOffset,PLONGLONG DeviceOffset) FormatRequestForWrite			
 	
### -field HRESULT(* )(IWDFUsbTargetDevice *This,IWDFIoRequest *pRequest,ULONG IoctlCode,IWDFFile *pFile,IWDFMemory *pInputMemory,PWDFMEMORY_OFFSET pInputMemoryOffset,IWDFMemory *pOutputMemory,PWDFMEMORY_OFFSET pOutputMemoryOffset) FormatRequestForIoctl			
 	
### -field WINUSB_INTERFACE_HANDLE(* )(IWDFUsbTargetDevice *This) GetWinUsbHandle			
 	
### -field UCHAR(* )(IWDFUsbTargetDevice *This) GetNumInterfaces			
 	
### -field HRESULT(* )(IWDFUsbTargetDevice *This,UCHAR InterfaceIndex,IWDFUsbInterface **ppUsbInterface) RetrieveUsbInterface			
 	
### -field HRESULT(* )(IWDFUsbTargetDevice *This,IWDFIoRequest *pRequest,PWINUSB_SETUP_PACKET SetupPacket,IWDFMemory *pMemory,PWDFMEMORY_OFFSET TransferOffset) FormatRequestForControlTransfer			
 	
### -field HRESULT(* )(IWDFUsbTargetDevice *This,ULONG InformationType,ULONG *BufferLength,PVOID Buffer) RetrieveDeviceInformation			
 	
### -field HRESULT(* )(IWDFUsbTargetDevice *This,UCHAR DescriptorType,UCHAR Index,USHORT LanguageID,ULONG *BufferLength,PVOID Buffer) RetrieveDescriptor			
 	
### -field HRESULT(* )(IWDFUsbTargetDevice *This,ULONG PolicyType,ULONG *ValueLength,PVOID Value) RetrievePowerPolicy			
 	
### -field HRESULT(* )(IWDFUsbTargetDevice *This,ULONG PolicyType,ULONG ValueLength,PVOID Value) SetPowerPolicy			
 	
## -remarks

## -see-also