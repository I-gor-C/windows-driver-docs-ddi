---
UID: NS.wudfusb.IWDFUsbRequestCompletionParamsVtbl
title: IWDFUsbRequestCompletionParamsVtbl
author: windows-driver-content
description: 
ms.assetid: 757ec29e-bd54-4851-bf6d-2e9338f9cf09
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWDFUsbRequestCompletionParamsVtbl, IWDFUsbRequestCompletionParamsVtbl
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

# IWDFUsbRequestCompletionParamsVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWDFUsbRequestCompletionParams *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWDFUsbRequestCompletionParams *This) AddRef			
 	
### -field ULONG(* )(IWDFUsbRequestCompletionParams *This) Release			
 	
### -field HRESULT(* )(IWDFUsbRequestCompletionParams *This) GetCompletionStatus			
 	
### -field ULONG_PTR(* )(IWDFUsbRequestCompletionParams *This) GetInformation			
 	
### -field WDF_REQUEST_TYPE(* )(IWDFUsbRequestCompletionParams *This) GetCompletedRequestType			
 	
### -field WDF_USB_REQUEST_TYPE(* )(IWDFUsbRequestCompletionParams *This) GetCompletedUsbRequestType			
 	
### -field void(* )(IWDFUsbRequestCompletionParams *This,IWDFMemory **ppMemory,ULONG *pLengthTransferred,SIZE_T *pOffset,PWINUSB_SETUP_PACKET pSetupPacket) GetDeviceControlTransferParameters			
 	
### -field void(* )(IWDFUsbRequestCompletionParams *This,IWDFMemory **ppWriteMemory,SIZE_T *pBytesWritten,SIZE_T *pWriteMemoryOffset) GetPipeWriteParameters			
 	
### -field void(* )(IWDFUsbRequestCompletionParams *This,IWDFMemory **ppReadMemory,SIZE_T *pBytesRead,SIZE_T *pReadMemoryOffset) GetPipeReadParameters			
 	
## -remarks

## -see-also