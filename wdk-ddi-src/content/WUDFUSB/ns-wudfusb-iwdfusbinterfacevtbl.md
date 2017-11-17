---
UID: NS.wudfusb.IWDFUsbInterfaceVtbl
title: IWDFUsbInterfaceVtbl
author: windows-driver-content
description: 
ms.assetid: 8bdb4ec4-c948-4f51-ab19-c4af391f0f40
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFUsbInterfaceVtbl, IWDFUsbInterfaceVtbl
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

# IWDFUsbInterfaceVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFUsbInterface *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFUsbInterface *This) AddRef			
 	
### -field ULONG(* )(IWDFUsbInterface *This) Release			
 	
### -field HRESULT(* )(IWDFUsbInterface *This) DeleteWdfObject			
 	
### -field HRESULT(* )(IWDFUsbInterface *This,__drv_aliasesMem IObjectCleanup *pCleanupCallback,__drv_aliasesMem void *pContext) AssignContext			
 	
### -field HRESULT(* )(IWDFUsbInterface *This, void **ppvContext) RetrieveContext			
 	
### -field void(* )(IWDFUsbInterface *This) AcquireLock			
 	
### -field void(* )(IWDFUsbInterface *This) ReleaseLock			
 	
### -field void(* )(IWDFUsbInterface *This,PUSB_INTERFACE_DESCRIPTOR UsbAltInterfaceDescriptor) GetInterfaceDescriptor			
 	
### -field UCHAR(* )(IWDFUsbInterface *This) GetInterfaceNumber			
 	
### -field UCHAR(* )(IWDFUsbInterface *This) GetNumEndPoints			
 	
### -field UCHAR(* )(IWDFUsbInterface *This) GetConfiguredSettingIndex			
 	
### -field HRESULT(* )(IWDFUsbInterface *This,UCHAR SettingNumber) SelectSetting			
 	
### -field WINUSB_INTERFACE_HANDLE(* )(IWDFUsbInterface *This) GetWinUsbHandle			
 	
### -field HRESULT(* )(IWDFUsbInterface *This,UCHAR PipeIndex,IWDFUsbTargetPipe **ppPipe) RetrieveUsbPipeObject			
 	
## -remarks

## -see-also