---
UID: NS.winsplp._PRINTPROVIDOR
title: PRINTPROVIDOR
author: windows-driver-content
description: 
ms.assetid: 16823b72-3911-4888-9777-9f521d1c8690
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PRINTPROVIDOR, 
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

# PRINTPROVIDOR structure

## -description



## -struct-fields

### -field BOOL(* )(PWSTR pPrinterName,PHANDLE phPrinter,PPRINTER_DEFAULTS pDefault) fpOpenPrinter			
 	
### -field BOOL(* )(HANDLE hPrinter,DWORD JobId,DWORD Level,LPBYTE pJob,DWORD Command) fpSetJob			
 	
### -field BOOL(* )(HANDLE hPrinter,DWORD JobId,DWORD Level,LPBYTE pJob,DWORD cbBuf,LPDWORD pcbNeeded) fpGetJob			
 	
### -field BOOL(* )(HANDLE hPrinter,DWORD FirstJob,DWORD NoJobs,DWORD Level,LPBYTE pJob,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned) fpEnumJobs			
 	
### -field HANDLE(* )(LPWSTR pName,DWORD Level,LPBYTE pPrinter) fpAddPrinter			
 	
### -field BOOL(* )(HANDLE hPrinter) fpDeletePrinter			
 	
### -field BOOL(* )(HANDLE hPrinter,DWORD Level,LPBYTE pPrinter,DWORD Command) fpSetPrinter			
 	
### -field BOOL(* )(HANDLE hPrinter,DWORD Level,LPBYTE pPrinter,DWORD cbBuf,LPDWORD pcbNeeded) fpGetPrinter			
 	
### -field BOOL(* )(DWORD Flags,LPWSTR Name,DWORD Level,LPBYTE pPrinterEnum,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned) fpEnumPrinters			
 	
### -field BOOL(* )(LPWSTR pName,DWORD Level,LPBYTE pDriverInfo) fpAddPrinterDriver			
 	
### -field BOOL(* )(LPWSTR pName,LPWSTR pEnvironment,DWORD Level,LPBYTE pDriverInfo,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned) fpEnumPrinterDrivers			
 	
### -field BOOL(* )(HANDLE hPrinter,LPWSTR pEnvironment,DWORD Level,LPBYTE pDriverInfo,DWORD cbBuf,LPDWORD pcbNeeded) fpGetPrinterDriver			
 	
### -field BOOL(* )(LPWSTR pName,LPWSTR pEnvironment,DWORD Level,LPBYTE pDriverDirectory,DWORD cbBuf,LPDWORD pcbNeeded) fpGetPrinterDriverDirectory			
 	
### -field BOOL(* )(LPWSTR pName,LPWSTR pEnvironment,LPWSTR pDriverName) fpDeletePrinterDriver			
 	
### -field BOOL(* )(LPWSTR pName,LPWSTR pEnvironment,LPWSTR pPathName,LPWSTR pPrintProcessorName) fpAddPrintProcessor			
 	
### -field BOOL(* )(LPWSTR pName,LPWSTR pEnvironment,DWORD Level,LPBYTE pPrintProcessorInfo,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned) fpEnumPrintProcessors			
 	
### -field BOOL(* )(LPWSTR pName,LPWSTR pEnvironment,DWORD Level,LPBYTE pPrintProcessorInfo,DWORD cbBuf,LPDWORD pcbNeeded) fpGetPrintProcessorDirectory			
 	
### -field BOOL(* )(LPWSTR pName,LPWSTR pEnvironment,LPWSTR pPrintProcessorName) fpDeletePrintProcessor			
 	
### -field BOOL(* )(LPWSTR pName,LPWSTR pPrintProcessorName,DWORD Level,LPBYTE pDataypes,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned) fpEnumPrintProcessorDatatypes			
 	
### -field DWORD(* )(HANDLE hPrinter,DWORD Level,LPBYTE pDocInfo) fpStartDocPrinter			
 	
### -field BOOL(* )(HANDLE hPrinter) fpStartPagePrinter			
 	
### -field BOOL(* )(HANDLE hPrinter,LPVOID pBuf,DWORD cbBuf,LPDWORD pcWritten) fpWritePrinter			
 	
### -field BOOL(* )(HANDLE hPrinter) fpEndPagePrinter			
 	
### -field BOOL(* )(HANDLE hPrinter) fpAbortPrinter			
 	
### -field BOOL(* )(HANDLE hPrinter,LPVOID pBuf,DWORD cbBuf,LPDWORD pNoBytesRead) fpReadPrinter			
 	
### -field BOOL(* )(HANDLE hPrinter) fpEndDocPrinter			
 	
### -field BOOL(* )(HANDLE hPrinter,DWORD Level,LPBYTE pData,DWORD cbBuf,LPDWORD pcbNeeded) fpAddJob			
 	
### -field BOOL(* )(HANDLE hPrinter,DWORD JobId) fpScheduleJob			
 	
### -field DWORD(* )(HANDLE hPrinter,LPWSTR pValueName,LPDWORD pType,LPBYTE pData,DWORD nSize,LPDWORD pcbNeeded) fpGetPrinterData			
 	
### -field DWORD(* )(HANDLE hPrinter,LPWSTR pValueName,DWORD Type,LPBYTE pData,DWORD cbData) fpSetPrinterData			
 	
### -field DWORD(* )(HANDLE hPrinter,DWORD Flags) fpWaitForPrinterChange			
 	
### -field BOOL(* )(HANDLE hPrinter) fpClosePrinter			
 	
### -field BOOL(* )(HANDLE hPrinter,DWORD Level,LPBYTE pForm) fpAddForm			
 	
### -field BOOL(* )(HANDLE hPrinter,LPWSTR pFormName) fpDeleteForm			
 	
### -field BOOL(* )(HANDLE hPrinter,LPWSTR pFormName,DWORD Level,LPBYTE pForm,DWORD cbBuf,LPDWORD pcbNeeded) fpGetForm			
 	
### -field BOOL(* )(HANDLE hPrinter,LPWSTR pFormName,DWORD Level,LPBYTE pForm) fpSetForm			
 	
### -field BOOL(* )(HANDLE hPrinter,DWORD Level,LPBYTE pForm,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned) fpEnumForms			
 	
### -field BOOL(* )(LPWSTR pName,DWORD Level,LPBYTE pMonitors,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned) fpEnumMonitors			
 	
### -field BOOL(* )(LPWSTR pName,DWORD Level,LPBYTE pPorts,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned) fpEnumPorts			
 	
### -field BOOL(* )(LPWSTR pName,HWND hWnd,LPWSTR pMonitorName) fpAddPort			
 	
### -field BOOL(* )(LPWSTR pName,HWND hWnd,LPWSTR pPortName) fpConfigurePort			
 	
### -field BOOL(* )(LPWSTR pName,HWND hWnd,LPWSTR pPortName) fpDeletePort			
 	
### -field HANDLE(* )(HANDLE hPrinter,LPDEVMODEW pDevMode) fpCreatePrinterIC			
 	
### -field BOOL(* )(HANDLE hPrinterIC,LPBYTE pIn,DWORD cIn,LPBYTE pOut,DWORD cOut,DWORD ul) fpPlayGdiScriptOnPrinterIC			
 	
### -field BOOL(* )(HANDLE hPrinterIC) fpDeletePrinterIC			
 	
### -field BOOL(* )(LPWSTR pName) fpAddPrinterConnection			
 	
### -field BOOL(* )(LPWSTR pName) fpDeletePrinterConnection			
 	
### -field DWORD(* )(HANDLE hPrinter,DWORD Error,HWND hWnd,LPWSTR pText,LPWSTR pCaption,DWORD dwType) fpPrinterMessageBox			
 	
### -field BOOL(* )(LPWSTR pName,DWORD Level,LPBYTE pMonitorInfo) fpAddMonitor			
 	
### -field BOOL(* )(LPWSTR pName,LPWSTR pEnvironment,LPWSTR pMonitorName) fpDeleteMonitor			
 	
### -field BOOL(* )(HANDLE hPrinter,LPPRINTER_DEFAULTS pDefault) fpResetPrinter			
 	
### -field BOOL(* )(HANDLE hPrinter,LPWSTR pEnvironment,DWORD Level,LPBYTE pDriverInfo,DWORD cbBuf,LPDWORD pcbNeeded,DWORD dwClientMajorVersion,DWORD dwClientMinorVersion,PDWORD pdwServerMajorVersion,PDWORD pdwServerMinorVersion) fpGetPrinterDriverEx			
 	
### -field BOOL(* )(HANDLE hPrinter,DWORD fdwFlags,DWORD fdwOptions,HANDLE hNotify,PDWORD pfdwStatus,PVOID pPrinterNotifyOptions,PVOID pPrinterNotifyInit) fpFindFirstPrinterChangeNotification			
 	
### -field BOOL(* )(HANDLE hPrinter) fpFindClosePrinterChangeNotification			
 	
### -field BOOL(* )(LPWSTR pName,DWORD Level,LPBYTE lpBuffer,LPWSTR lpMonitorName) fpAddPortEx			
 	
### -field BOOL(* )(LPVOID pvReserved) fpShutDown			
 	
### -field BOOL(* )(HANDLE hPrinter,DWORD Reserved,PVOID pvReserved,PVOID pPrinterNotifyInfo) fpRefreshPrinterChangeNotification			
 	
### -field BOOL(* )(LPWSTR pPrinterName,LPHANDLE phPrinter,LPPRINTER_DEFAULTS pDefault,LPBYTE pClientInfo,DWORD Level) fpOpenPrinterEx			
 	
### -field HANDLE(* )(LPWSTR pName,DWORD Level,LPBYTE pPrinter,LPBYTE pClientInfo,DWORD ClientInfoLevel) fpAddPrinterEx			
 	
### -field BOOL(* )(LPWSTR pName,LPWSTR pPortName,DWORD Level,LPBYTE pPortInfo) fpSetPort			
 	
### -field DWORD(* )(HANDLE hPrinter,DWORD dwIndex,LPWSTR pValueName,DWORD cbValueName,LPDWORD pcbValueName,LPDWORD pType,LPBYTE pData,DWORD cbData,LPDWORD pcbData) fpEnumPrinterData			
 	
### -field DWORD(* )(HANDLE hPrinter,LPWSTR pValueName) fpDeletePrinterData			
 	
### -field DWORD(* )(LPCTSTR pszServer,LPCTSTR pszResource,PHANDLE phSpooler,LPCTSTR pszName,LPCTSTR pszAddress) fpClusterSplOpen			
 	
### -field DWORD(* )(HANDLE hSpooler) fpClusterSplClose			
 	
### -field DWORD(* )(HANDLE hSpooler) fpClusterSplIsAlive			
 	
### -field DWORD(* )(HANDLE hPrinter,LPCWSTR pKeyName,LPCWSTR pValueName,DWORD Type,LPBYTE pData,DWORD cbData) fpSetPrinterDataEx			
 	
### -field DWORD(* )(HANDLE hPrinter,LPCWSTR pKeyName,LPCWSTR pValueName,LPDWORD pType,LPBYTE pData,DWORD nSize,LPDWORD pcbNeeded) fpGetPrinterDataEx			
 	
### -field DWORD(* )(HANDLE hPrinter,LPCWSTR pKeyName,LPBYTE pEnumValues,DWORD cbEnumValues,LPDWORD pcbEnumValues,LPDWORD pnEnumValues) fpEnumPrinterDataEx			
 	
### -field DWORD(* )(HANDLE hPrinter,LPCWSTR pKeyName,LPWSTR pSubkey,DWORD cbSubkey,LPDWORD pcbSubkey) fpEnumPrinterKey			
 	
### -field DWORD(* )(HANDLE hPrinter,LPCWSTR pKeyName,LPCWSTR pValueName) fpDeletePrinterDataEx			
 	
### -field DWORD(* )(HANDLE hPrinter,LPCWSTR pKeyName) fpDeletePrinterKey			
 	
### -field BOOL(* )(HANDLE hPrinter,LARGE_INTEGER liDistanceToMove,PLARGE_INTEGER pliNewPointer,DWORD dwMoveMethod,BOOL bWrite) fpSeekPrinter			
 	
### -field BOOL(* )(LPWSTR pName,LPWSTR pEnvironment,LPWSTR pDriverName,DWORD dwDeleteFlag,DWORD dwVersionNum) fpDeletePrinterDriverEx			
 	
### -field BOOL(* )(LPCWSTR pServer,LPCWSTR pPrinterName,LPCWSTR pPrintServer,LPCWSTR pProvider) fpAddPerMachineConnection			
 	
### -field BOOL(* )(LPCWSTR pServer,LPCWSTR pPrinterName) fpDeletePerMachineConnection			
 	
### -field BOOL(* )(LPCWSTR pServer,LPBYTE pPrinterEnum,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned) fpEnumPerMachineConnections			
 	
### -field BOOL(* )(HANDLE hXcv,LPCWSTR pszDataName,PBYTE pInputData,DWORD cbInputData,PBYTE pOutputData,DWORD cbOutputData,PDWORD pcbOutputNeeded,PDWORD pdwStatus) fpXcvData			
 	
### -field BOOL(* )(LPWSTR pName,DWORD Level,LPBYTE pDriverInfo,DWORD dwFileCopyFlags) fpAddPrinterDriverEx			
 	
### -field BOOL(* )(HANDLE hPrinter,LPBYTE *pBuf,DWORD cbBuf) fpSplReadPrinter			
 	
### -field BOOL(* )(LPWSTR pDriverFile) fpDriverUnloadComplete			
 	
### -field BOOL(* )(HANDLE hPrinter,LPWSTR *pSpoolDir,LPHANDLE phFile,HANDLE hSpoolerProcess,HANDLE hAppProcess) fpGetSpoolFileInfo			
 	
### -field BOOL(* )(HANDLE hPrinter,DWORD cbCommit) fpCommitSpoolData			
 	
### -field BOOL(* )(HANDLE hPrinter) fpCloseSpoolFileHandle			
 	
### -field BOOL(* )(HANDLE hPrinter,LPBYTE pBuf,DWORD cbBuf,LPDWORD pcWritten,DWORD cSleep) fpFlushPrinter			
 	
### -field DWORD(* )(HANDLE hPrinter,LPCWSTR pAction,PBIDI_REQUEST_CONTAINER pReqData,PBIDI_RESPONSE_CONTAINER *ppResData) fpSendRecvBidiData			
 	
### -field BOOL(* )(LPCWSTR pName,DWORD dwLevel,PVOID pInfo) fpAddPrinterConnection2			
 	
### -field HRESULT(* )(PCWSTR, const IID &,VOID **) fpGetPrintClassObject			
 	
### -field HRESULT(* )(PCWSTR, const IID *,VOID **) fpGetPrintClassObject			
 	
### -field HRESULT(* )(HANDLE hPrinter,ULONG jobId,EPrintXPSJobOperation jobOperation,EPrintXPSJobProgress jobProgress) fpReportJobProcessingProgress			
 	
### -field VOID(* )(DWORD dwLevel,VOID *pfOut) fpEnumAndLogProvidorObjects			
 	
### -field HRESULT(* )(HANDLE hPrinter,LPWSTR pEnvironment,DWORD Level,LPBYTE pDriverInfo,DWORD cbBuf,LPDWORD pcbNeeded,DWORD dwClientMajorVersion,DWORD dwClientMinorVersion,PDWORD pdwServerMajorVersion,PDWORD pdwServerMinorVersion) fpInternalGetPrinterDriver			
 	
### -field HRESULT(* )(LPCWSTR pcszPnpId,LPCWSTR pcszPortName,LPWSTR pszManufacturerName,DWORD cchManufacturerName,LPDWORD pcchRequiredManufacturerNameSize,LPWSTR pszModelName,DWORD cchModelName,LPDWORD pcchRequiredModelNameSize,LPDWORD pdwRank0Matches) fpFindCompatibleDriver			
 	
### -field DWORD(* )(HANDLE hPrinter,DWORD JobId,PCWSTR pszName,PrintPropertyValue *pValue) fpGetJobNamedPropertyValue			
 	
### -field DWORD(* )(HANDLE hPrinter,DWORD JobId, const PrintNamedProperty *pProperty) fpSetJobNamedProperty			
 	
### -field DWORD(* )(HANDLE hPrinter,DWORD JobId,PCWSTR pszName) fpDeleteJobNamedProperty			
 	
### -field DWORD(* )(HANDLE hPrinter,DWORD JobId,DWORD *pcProperties,PrintNamedProperty **ppProperties) fpEnumJobNamedProperties			
 	
### -field DWORD(* )(DWORD event,POWERBROADCAST_SETTING *pPowerSetting) fpPowerEvent			
 	
### -field DWORD(* )(HANDLE hPrinter,HKEY *phKey) fpGetUserPropertyBag			
 	
### -field BOOL(* )() fpCanShutdown			
 	
### -field DWORD(* )(HANDLE hPrinter,PBranchOfficeJobDataContainer pJobDataContainer) fpLogJobInfoForBranchOffice			
 	
## -remarks

## -see-also