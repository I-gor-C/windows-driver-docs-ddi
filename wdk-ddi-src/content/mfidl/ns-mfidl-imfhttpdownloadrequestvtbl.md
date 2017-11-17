---
UID: NS.mfidl.IMFHttpDownloadRequestVtbl
title: IMFHttpDownloadRequestVtbl
author: windows-driver-content
description: 
ms.assetid: deedfdfa-e367-4b55-b9cb-123501380824
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IMFHttpDownloadRequestVtbl, IMFHttpDownloadRequestVtbl
req.header: mfidl.h
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

# IMFHttpDownloadRequestVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IMFHttpDownloadRequest *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IMFHttpDownloadRequest *This) AddRef			
 	
### -field ULONG(* )(IMFHttpDownloadRequest *This) Release			
 	
### -field HRESULT(* )(IMFHttpDownloadRequest *This,LPCWSTR szHeader) AddHeader			
 	
### -field HRESULT(* )(IMFHttpDownloadRequest *This, const BYTE *pbPayload,ULONG cbPayload,IMFAsyncCallback *pCallback,IUnknown *punkState) BeginSendRequest			
 	
### -field HRESULT(* )(IMFHttpDownloadRequest *This,IMFAsyncResult *pResult) EndSendRequest			
 	
### -field HRESULT(* )(IMFHttpDownloadRequest *This,IMFAsyncCallback *pCallback,IUnknown *punkState) BeginReceiveResponse			
 	
### -field HRESULT(* )(IMFHttpDownloadRequest *This,IMFAsyncResult *pResult) EndReceiveResponse			
 	
### -field HRESULT(* )(IMFHttpDownloadRequest *This,BYTE *pb,ULONG cb,IMFAsyncCallback *pCallback,IUnknown *punkState) BeginReadPayload			
 	
### -field HRESULT(* )(IMFHttpDownloadRequest *This,IMFAsyncResult *pResult,QWORD *pqwOffset,ULONG *pcbRead) EndReadPayload			
 	
### -field HRESULT(* )(IMFHttpDownloadRequest *This,LPCWSTR szHeaderName,DWORD dwIndex,LPWSTR *ppszHeaderValue) QueryHeader			
 	
### -field HRESULT(* )(IMFHttpDownloadRequest *This,LPWSTR *ppszURL) GetURL			
 	
### -field HRESULT(* )(IMFHttpDownloadRequest *This,BOOL *pfNullSourceOrigin) HasNullSourceOrigin			
 	
### -field HRESULT(* )(IMFHttpDownloadRequest *This,QWORD *pqwStartTime,QWORD *pqwStopTime,QWORD *pqwDuration) GetTimeSeekResult			
 	
### -field HRESULT(* )(IMFHttpDownloadRequest *This,DWORD *pdwHttpStatus) GetHttpStatus			
 	
### -field HRESULT(* )(IMFHttpDownloadRequest *This,BOOL *pfAtEndOfPayload) GetAtEndOfPayload			
 	
### -field HRESULT(* )(IMFHttpDownloadRequest *This,QWORD *pqwTotalLength) GetTotalLength			
 	
### -field HRESULT(* )(IMFHttpDownloadRequest *This,QWORD *pqwRangeEnd) GetRangeEndOffset			
 	
### -field HRESULT(* )(IMFHttpDownloadRequest *This) Close			
 	
## -remarks

## -see-also