---
UID: NS.winsplp._MONITOR2
title: MONITOR2
author: windows-driver-content
description: 
ms.assetid: 63b0218b-d0f8-4cc4-b261-dba059ebca3d
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MONITOR2, 
req.header: winsplp.h
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

# MONITOR2 structure

## -description



## -struct-fields

### -field DWORD cbSize			
 	
### -field BOOL(* )(HANDLE hMonitor,LPWSTR pName,DWORD Level,LPBYTE pPorts,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned) pfnEnumPorts			
 	
### -field BOOL(* )(HANDLE hMonitor,LPWSTR pName,PHANDLE pHandle) pfnOpenPort			
 	
### -field BOOL(* )(HANDLE hMonitor,HANDLE hMonitorPort,LPWSTR pPortName,LPWSTR pPrinterName,PHANDLE pHandle,_MONITOR2 *pMonitor2) pfnOpenPortEx			
 	
### -field BOOL(* )(HANDLE hPort,LPWSTR pPrinterName,DWORD JobId,DWORD Level,LPBYTE pDocInfo) pfnStartDocPort			
 	
### -field BOOL(* )(HANDLE hPort,LPBYTE pBuffer,DWORD cbBuf,LPDWORD pcbWritten) pfnWritePort			
 	
### -field BOOL(* )(HANDLE hPort,LPBYTE pBuffer,DWORD cbBuffer,LPDWORD pcbRead) pfnReadPort			
 	
### -field BOOL(* )(HANDLE hPort) pfnEndDocPort			
 	
### -field BOOL(* )(HANDLE hPort) pfnClosePort			
 	
### -field BOOL(* )(HANDLE hMonitor,LPWSTR pName,HWND hWnd,LPWSTR pMonitorName) pfnAddPort			
 	
### -field BOOL(* )(HANDLE hMonitor,LPWSTR pName,DWORD Level,LPBYTE lpBuffer,LPWSTR lpMonitorName) pfnAddPortEx			
 	
### -field BOOL(* )(HANDLE hMonitor,LPWSTR pName,HWND hWnd,LPWSTR pPortName) pfnConfigurePort			
 	
### -field BOOL(* )(HANDLE hMonitor,LPWSTR pName,HWND hWnd,LPWSTR pPortName) pfnDeletePort			
 	
### -field BOOL(* )(HANDLE hPort,DWORD ControlID,LPWSTR pValueName,LPWSTR lpInBuffer,DWORD cbInBuffer,LPWSTR lpOutBuffer,DWORD cbOutBuffer,LPDWORD lpcbReturned) pfnGetPrinterDataFromPort			
 	
### -field BOOL(* )(HANDLE hPort,LPCOMMTIMEOUTS lpCTO,DWORD reserved) pfnSetPortTimeOuts			
 	
### -field BOOL(* )(HANDLE hMonitor,LPCWSTR pszObject,ACCESS_MASK GrantedAccess,PHANDLE phXcv) pfnXcvOpenPort			
 	
### -field DWORD(* )(HANDLE hXcv,LPCWSTR pszDataName,PBYTE pInputData,DWORD cbInputData,PBYTE pOutputData,DWORD cbOutputData,PDWORD pcbOutputNeeded) pfnXcvDataPort			
 	
### -field BOOL(* )(HANDLE hXcv) pfnXcvClosePort			
 	
### -field VOID(* )(HANDLE hMonitor) pfnShutdown			
 	
### -field DWORD(* )(HANDLE hPort,DWORD dwAccessBit,LPCWSTR pAction,PBIDI_REQUEST_CONTAINER pReqData,PBIDI_RESPONSE_CONTAINER *ppResData) pfnSendRecvBidiDataFromPort			
 	
### -field DWORD(* )(HANDLE hMonitor,DWORD cPorts,PCWSTR *ppszPorts) pfnNotifyUsedPorts			
 	
### -field DWORD(* )(HANDLE hMonitor,DWORD cPorts,PCWSTR *ppszPorts) pfnNotifyUnusedPorts			
 	
### -field DWORD(* )(HANDLE hMonitor,DWORD event,POWERBROADCAST_SETTING *pSettings) pfnPowerEvent			
 	
## -remarks

## -see-also