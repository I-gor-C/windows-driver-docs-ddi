---
UID: NS.wiamindr_lh.IWiaMiniDrvVtbl
title: IWiaMiniDrvVtbl
author: windows-driver-content
description: 
ms.assetid: d8c2a149-6d50-4e38-ae10-4f03c817c06f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IWiaMiniDrvVtbl, IWiaMiniDrvVtbl
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

# IWiaMiniDrvVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IWiaMiniDrv *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IWiaMiniDrv *This) AddRef			
 	
### -field ULONG(* )(IWiaMiniDrv *This) Release			
 	
### -field HRESULT(* )(IWiaMiniDrv *This,BYTE *__MIDL__IWiaMiniDrv0000,LONG __MIDL__IWiaMiniDrv0001,BSTR __MIDL__IWiaMiniDrv0002,BSTR __MIDL__IWiaMiniDrv0003,IUnknown *__MIDL__IWiaMiniDrv0004,IUnknown *__MIDL__IWiaMiniDrv0005,IWiaDrvItem **__MIDL__IWiaMiniDrv0006,IUnknown **__MIDL__IWiaMiniDrv0007,LONG *__MIDL__IWiaMiniDrv0008) drvInitializeWia			
 	
### -field HRESULT(* )(IWiaMiniDrv *This,BYTE *__MIDL__IWiaMiniDrv0009,LONG __MIDL__IWiaMiniDrv0010,PMINIDRV_TRANSFER_CONTEXT __MIDL__IWiaMiniDrv0011,LONG *__MIDL__IWiaMiniDrv0012) drvAcquireItemData			
 	
### -field HRESULT(* )(IWiaMiniDrv *This,BYTE *__MIDL__IWiaMiniDrv0013,LONG __MIDL__IWiaMiniDrv0014,LONG *__MIDL__IWiaMiniDrv0015) drvInitItemProperties			
 	
### -field HRESULT(* )(IWiaMiniDrv *This,BYTE *__MIDL__IWiaMiniDrv0016,LONG __MIDL__IWiaMiniDrv0017,ULONG __MIDL__IWiaMiniDrv0018, const PROPSPEC *__MIDL__IWiaMiniDrv0019,LONG *__MIDL__IWiaMiniDrv0020) drvValidateItemProperties			
 	
### -field HRESULT(* )(IWiaMiniDrv *This,BYTE *__MIDL__IWiaMiniDrv0021,LONG __MIDL__IWiaMiniDrv0022,PMINIDRV_TRANSFER_CONTEXT __MIDL__IWiaMiniDrv0023,LONG *__MIDL__IWiaMiniDrv0024) drvWriteItemProperties			
 	
### -field HRESULT(* )(IWiaMiniDrv *This,BYTE *__MIDL__IWiaMiniDrv0025,LONG __MIDL__IWiaMiniDrv0026,ULONG __MIDL__IWiaMiniDrv0027, const PROPSPEC *__MIDL__IWiaMiniDrv0028,LONG *__MIDL__IWiaMiniDrv0029) drvReadItemProperties			
 	
### -field HRESULT(* )(IWiaMiniDrv *This,BYTE *__MIDL__IWiaMiniDrv0030,LONG __MIDL__IWiaMiniDrv0031,LONG *__MIDL__IWiaMiniDrv0032) drvLockWiaDevice			
 	
### -field HRESULT(* )(IWiaMiniDrv *This,BYTE *__MIDL__IWiaMiniDrv0033,LONG __MIDL__IWiaMiniDrv0034,LONG *__MIDL__IWiaMiniDrv0035) drvUnLockWiaDevice			
 	
### -field HRESULT(* )(IWiaMiniDrv *This,BYTE *__MIDL__IWiaMiniDrv0036,LONG __MIDL__IWiaMiniDrv0037,LONG *__MIDL__IWiaMiniDrv0038) drvAnalyzeItem			
 	
### -field HRESULT(* )(IWiaMiniDrv *This,LONG __MIDL__IWiaMiniDrv0039,LONG __MIDL__IWiaMiniDrv0040,LPOLESTR *__MIDL__IWiaMiniDrv0041,LONG *__MIDL__IWiaMiniDrv0042) drvGetDeviceErrorStr			
 	
### -field HRESULT(* )(IWiaMiniDrv *This,BYTE *__MIDL__IWiaMiniDrv0043,LONG __MIDL__IWiaMiniDrv0044, const GUID *__MIDL__IWiaMiniDrv0045,IWiaDrvItem **__MIDL__IWiaMiniDrv0046,LONG *__MIDL__IWiaMiniDrv0047) drvDeviceCommand			
 	
### -field HRESULT(* )(IWiaMiniDrv *This,BYTE *__MIDL__IWiaMiniDrv0048,LONG __MIDL__IWiaMiniDrv0049,LONG *__MIDL__IWiaMiniDrv0050,WIA_DEV_CAP_DRV **__MIDL__IWiaMiniDrv0051,LONG *__MIDL__IWiaMiniDrv0052) drvGetCapabilities			
 	
### -field HRESULT(* )(IWiaMiniDrv *This,BYTE *__MIDL__IWiaMiniDrv0053,LONG __MIDL__IWiaMiniDrv0054,LONG *__MIDL__IWiaMiniDrv0055) drvDeleteItem			
 	
### -field HRESULT(* )(IWiaMiniDrv *This,LONG __MIDL__IWiaMiniDrv0056,BYTE *__MIDL__IWiaMiniDrv0057,LONG *__MIDL__IWiaMiniDrv0058) drvFreeDrvItemContext			
 	
### -field HRESULT(* )(IWiaMiniDrv *This,BYTE *__MIDL__IWiaMiniDrv0059,LONG __MIDL__IWiaMiniDrv0060,LONG *__MIDL__IWiaMiniDrv0061,WIA_FORMAT_INFO **__MIDL__IWiaMiniDrv0062,LONG *__MIDL__IWiaMiniDrv0063) drvGetWiaFormatInfo			
 	
### -field HRESULT(* )(IWiaMiniDrv *This, const GUID *pEventGUID,BSTR bstrDeviceID,ULONG ulReserved) drvNotifyPnpEvent			
 	
### -field HRESULT(* )(IWiaMiniDrv *This,BYTE *__MIDL__IWiaMiniDrv0064) drvUnInitializeWia			
 	
## -remarks

## -see-also