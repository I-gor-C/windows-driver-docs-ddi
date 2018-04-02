---
UID: NS:winsplp._PRINTPROVIDOR
title: "_PRINTPROVIDOR"
author: windows-driver-content
description: Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated.
old-location: print\printprovidor.htm
old-project: print
ms.assetid: c030cb9d-23c0-4d0e-970f-f447e9af7528
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*LPPRINTPROVIDOR, LPPRINTPROVIDOR, LPPRINTPROVIDOR structure pointer [Print Devices], PRINTPROVIDOR, PRINTPROVIDOR structure [Print Devices], _PRINTPROVIDOR, print.printprovidor, spoolfnc_4fb8242e-e0a0-47e5-b01f-2a20932d4d84.xml, winsplp/LPPRINTPROVIDOR, winsplp/PRINTPROVIDOR"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: winsplp.h
req.include-header: Winsplp.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	winsplp.h
api_name:
-	PRINTPROVIDOR
product:
- Windows
targetos: Windows
req.typenames: PRINTPROVIDOR, *LPPRINTPROVIDOR
req.product: Windows 10 or later.
---

# _PRINTPROVIDOR structure
<div class="alert"><b>Warning</b>  <p class="note">Starting with Windows 10, the APIs which support third-party print providers are deprecated. Microsoft does not recommend any investment into third-party print providers. Additionally, on Windows 8 and newer products where the v4 print driver model is available, third-party print providers may not create or manage queues which use v4 print drivers.

</div><div> </div>The PRINTPROVIDOR structure is used as a parameter to a print provider's <a href="https://msdn.microsoft.com/library/windows/hardware/ff551614">InitializePrintProvidor</a> function. All structure member values are supplied by the provider.

## Syntax
```
typedef struct _PRINTPROVIDOR {
  BOOL( )(PWSTR pPrinterName,PHANDLE phPrinter,PPRINTER_DEFAULTS pDefault)    *fpOpenPrinter;
  BOOL( )(HANDLE hPrinter,DWORD JobId,DWORD Level,LPBYTE pJob,DWORD Command)    *fpSetJob;
  BOOL( )(HANDLE hPrinter,DWORD JobId,DWORD Level,LPBYTE pJob,DWORD cbBuf,LPDWORD pcbNeeded)    *fpGetJob;
  BOOL( )(HANDLE hPrinter,DWORD FirstJob,DWORD NoJobs,DWORD Level,LPBYTE pJob,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned)    *fpEnumJobs;
  HANDLE( )(LPWSTR pName,DWORD Level,LPBYTE pPrinter)  *fpAddPrinter;
  BOOL( )(HANDLE hPrinter)    *fpDeletePrinter;
  BOOL( )(HANDLE hPrinter,DWORD Level,LPBYTE pPrinter,DWORD Command)    *fpSetPrinter;
  BOOL( )(HANDLE hPrinter,DWORD Level,LPBYTE pPrinter,DWORD cbBuf,LPDWORD pcbNeeded)    *fpGetPrinter;
  BOOL( )(DWORD Flags,LPWSTR Name,DWORD Level,LPBYTE pPrinterEnum,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned)    *fpEnumPrinters;
  BOOL( )(LPWSTR pName,DWORD Level,LPBYTE pDriverInfo)    *fpAddPrinterDriver;
  BOOL( )(LPWSTR pName,LPWSTR pEnvironment,DWORD Level,LPBYTE pDriverInfo,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned)    *fpEnumPrinterDrivers;
  BOOL( )(HANDLE hPrinter,LPWSTR pEnvironment,DWORD Level,LPBYTE pDriverInfo,DWORD cbBuf,LPDWORD pcbNeeded)    *fpGetPrinterDriver;
  BOOL( )(LPWSTR pName,LPWSTR pEnvironment,DWORD Level,LPBYTE pDriverDirectory,DWORD cbBuf,LPDWORD pcbNeeded)    *fpGetPrinterDriverDirectory;
  BOOL( )(LPWSTR pName,LPWSTR pEnvironment,LPWSTR pDriverName)    *fpDeletePrinterDriver;
  BOOL( )(LPWSTR pName,LPWSTR pEnvironment,LPWSTR pPathName,LPWSTR pPrintProcessorName)    *fpAddPrintProcessor;
  BOOL( )(LPWSTR pName,LPWSTR pEnvironment,DWORD Level,LPBYTE pPrintProcessorInfo,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned)    *fpEnumPrintProcessors;
  BOOL( )(LPWSTR pName,LPWSTR pEnvironment,DWORD Level,LPBYTE pPrintProcessorInfo,DWORD cbBuf,LPDWORD pcbNeeded)    *fpGetPrintProcessorDirectory;
  BOOL( )(LPWSTR pName,LPWSTR pEnvironment,LPWSTR pPrintProcessorName)    *fpDeletePrintProcessor;
  BOOL( )(LPWSTR pName,LPWSTR pPrintProcessorName,DWORD Level,LPBYTE pDataypes,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned)    *fpEnumPrintProcessorDatatypes;
  DWORD( )(HANDLE hPrinter,DWORD Level,LPBYTE pDocInfo)   *fpStartDocPrinter;
  BOOL( )(HANDLE hPrinter)    *fpStartPagePrinter;
  BOOL( )(HANDLE hPrinter,LPVOID pBuf,DWORD cbBuf,LPDWORD pcWritten)    *fpWritePrinter;
  BOOL( )(HANDLE hPrinter)    *fpEndPagePrinter;
  BOOL( )(HANDLE hPrinter)    *fpAbortPrinter;
  BOOL( )(HANDLE hPrinter,LPVOID pBuf,DWORD cbBuf,LPDWORD pNoBytesRead)    *fpReadPrinter;
  BOOL( )(HANDLE hPrinter)    *fpEndDocPrinter;
  BOOL( )(HANDLE hPrinter,DWORD Level,LPBYTE pData,DWORD cbBuf,LPDWORD pcbNeeded)    *fpAddJob;
  BOOL( )(HANDLE hPrinter,DWORD JobId)    *fpScheduleJob;
  DWORD( )(HANDLE hPrinter,LPWSTR pValueName,LPDWORD pType,LPBYTE pData,DWORD nSize,LPDWORD pcbNeeded)   *fpGetPrinterData;
  DWORD( )(HANDLE hPrinter,LPWSTR pValueName,DWORD Type,LPBYTE pData,DWORD cbData)   *fpSetPrinterData;
  DWORD( )(HANDLE hPrinter,DWORD Flags)   *fpWaitForPrinterChange;
  BOOL( )(HANDLE hPrinter)    *fpClosePrinter;
  BOOL( )(HANDLE hPrinter,DWORD Level,LPBYTE pForm)    *fpAddForm;
  BOOL( )(HANDLE hPrinter,LPWSTR pFormName)    *fpDeleteForm;
  BOOL( )(HANDLE hPrinter,LPWSTR pFormName,DWORD Level,LPBYTE pForm,DWORD cbBuf,LPDWORD pcbNeeded)    *fpGetForm;
  BOOL( )(HANDLE hPrinter,LPWSTR pFormName,DWORD Level,LPBYTE pForm)    *fpSetForm;
  BOOL( )(HANDLE hPrinter,DWORD Level,LPBYTE pForm,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned)    *fpEnumForms;
  BOOL( )(LPWSTR pName,DWORD Level,LPBYTE pMonitors,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned)    *fpEnumMonitors;
  BOOL( )(LPWSTR pName,DWORD Level,LPBYTE pPorts,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned)    *fpEnumPorts;
  BOOL( )(LPWSTR pName,HWND hWnd,LPWSTR pMonitorName)    *fpAddPort;
  BOOL( )(LPWSTR pName,HWND hWnd,LPWSTR pPortName)    *fpConfigurePort;
  BOOL( )(LPWSTR pName,HWND hWnd,LPWSTR pPortName)    *fpDeletePort;
  HANDLE( )(HANDLE hPrinter,LPDEVMODEW pDevMode)  *fpCreatePrinterIC;
  BOOL( )(HANDLE hPrinterIC,LPBYTE pIn,DWORD cIn,LPBYTE pOut,DWORD cOut,DWORD ul)    *fpPlayGdiScriptOnPrinterIC;
  BOOL( )(HANDLE hPrinterIC)    *fpDeletePrinterIC;
  BOOL( )(LPWSTR pName)    *fpAddPrinterConnection;
  BOOL( )(LPWSTR pName)    *fpDeletePrinterConnection;
  DWORD( )(HANDLE hPrinter,DWORD Error,HWND hWnd,LPWSTR pText,LPWSTR pCaption,DWORD dwType)   *fpPrinterMessageBox;
  BOOL( )(LPWSTR pName,DWORD Level,LPBYTE pMonitorInfo)    *fpAddMonitor;
  BOOL( )(LPWSTR pName,LPWSTR pEnvironment,LPWSTR pMonitorName)    *fpDeleteMonitor;
  BOOL( )(HANDLE hPrinter,LPPRINTER_DEFAULTS pDefault)    *fpResetPrinter;
  BOOL( )(HANDLE hPrinter,LPWSTR pEnvironment,DWORD Level,LPBYTE pDriverInfo,DWORD cbBuf,LPDWORD pcbNeeded,DWORD dwClientMajorVersion,DWORD dwClientMinorVersion,PDWORD pdwServerMajorVersion,PDWORD pdwServerMinorVersion)    *fpGetPrinterDriverEx;
  BOOL( )(HANDLE hPrinter,DWORD fdwFlags,DWORD fdwOptions,HANDLE hNotify,PDWORD pfdwStatus,PVOID pPrinterNotifyOptions,PVOID pPrinterNotifyInit)    *fpFindFirstPrinterChangeNotification;
  BOOL( )(HANDLE hPrinter)    *fpFindClosePrinterChangeNotification;
  BOOL( )(LPWSTR pName,DWORD Level,LPBYTE lpBuffer,LPWSTR lpMonitorName)    *fpAddPortEx;
  BOOL( )(LPVOID pvReserved)    *fpShutDown;
  BOOL( )(HANDLE hPrinter,DWORD Reserved,PVOID pvReserved,PVOID pPrinterNotifyInfo)    *fpRefreshPrinterChangeNotification;
  BOOL( )(LPWSTR pPrinterName,LPHANDLE phPrinter,LPPRINTER_DEFAULTS pDefault,LPBYTE pClientInfo,DWORD Level)    *fpOpenPrinterEx;
  HANDLE( )(LPWSTR pName,DWORD Level,LPBYTE pPrinter,LPBYTE pClientInfo,DWORD ClientInfoLevel)  *fpAddPrinterEx;
  BOOL( )(LPWSTR pName,LPWSTR pPortName,DWORD Level,LPBYTE pPortInfo)    *fpSetPort;
  DWORD( )(HANDLE hPrinter,DWORD dwIndex,LPWSTR pValueName,DWORD cbValueName,LPDWORD pcbValueName,LPDWORD pType,LPBYTE pData,DWORD cbData,LPDWORD pcbData)   *fpEnumPrinterData;
  DWORD( )(HANDLE hPrinter,LPWSTR pValueName)   *fpDeletePrinterData;
  DWORD( )(LPCTSTR pszServer,LPCTSTR pszResource,PHANDLE phSpooler,LPCTSTR pszName,LPCTSTR pszAddress)   *fpClusterSplOpen;
  DWORD( )(HANDLE hSpooler)   *fpClusterSplClose;
  DWORD( )(HANDLE hSpooler)   *fpClusterSplIsAlive;
  DWORD( )(HANDLE hPrinter,LPCWSTR pKeyName,LPCWSTR pValueName,DWORD Type,LPBYTE pData,DWORD cbData)   *fpSetPrinterDataEx;
  DWORD( )(HANDLE hPrinter,LPCWSTR pKeyName,LPCWSTR pValueName,LPDWORD pType,LPBYTE pData,DWORD nSize,LPDWORD pcbNeeded)   *fpGetPrinterDataEx;
  DWORD( )(HANDLE hPrinter,LPCWSTR pKeyName,LPBYTE pEnumValues,DWORD cbEnumValues,LPDWORD pcbEnumValues,LPDWORD pnEnumValues)   *fpEnumPrinterDataEx;
  DWORD( )(HANDLE hPrinter,LPCWSTR pKeyName,LPWSTR pSubkey,DWORD cbSubkey,LPDWORD pcbSubkey)   *fpEnumPrinterKey;
  DWORD( )(HANDLE hPrinter,LPCWSTR pKeyName,LPCWSTR pValueName)   *fpDeletePrinterDataEx;
  DWORD( )(HANDLE hPrinter,LPCWSTR pKeyName)   *fpDeletePrinterKey;
  BOOL( )(HANDLE hPrinter,LARGE_INTEGER liDistanceToMove,PLARGE_INTEGER pliNewPointer,DWORD dwMoveMethod,BOOL bWrite)    *fpSeekPrinter;
  BOOL( )(LPWSTR pName,LPWSTR pEnvironment,LPWSTR pDriverName,DWORD dwDeleteFlag,DWORD dwVersionNum)    *fpDeletePrinterDriverEx;
  BOOL( )(LPCWSTR pServer,LPCWSTR pPrinterName,LPCWSTR pPrintServer,LPCWSTR pProvider)    *fpAddPerMachineConnection;
  BOOL( )(LPCWSTR pServer,LPCWSTR pPrinterName)    *fpDeletePerMachineConnection;
  BOOL( )(LPCWSTR pServer,LPBYTE pPrinterEnum,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned)    *fpEnumPerMachineConnections;
  BOOL( )(HANDLE hXcv,LPCWSTR pszDataName,PBYTE pInputData,DWORD cbInputData,PBYTE pOutputData,DWORD cbOutputData,PDWORD pcbOutputNeeded,PDWORD pdwStatus)    *fpXcvData;
  BOOL( )(LPWSTR pName,DWORD Level,LPBYTE pDriverInfo,DWORD dwFileCopyFlags)    *fpAddPrinterDriverEx;
  BOOL()(HANDLE hPrinter,LPBYTE *pBuf,DWORD cbBuf)    * fpSplReadPrinter;
  BOOL( )(LPWSTR pDriverFile)    *fpDriverUnloadComplete;
  BOOL()(HANDLE hPrinter,LPWSTR *pSpoolDir,LPHANDLE phFile,HANDLE hSpoolerProcess,HANDLE hAppProcess)    * fpGetSpoolFileInfo;
  BOOL( )(HANDLE hPrinter,DWORD cbCommit)    *fpCommitSpoolData;
  BOOL( )(HANDLE hPrinter)    *fpCloseSpoolFileHandle;
  BOOL( )(HANDLE hPrinter,LPBYTE pBuf,DWORD cbBuf,LPDWORD pcWritten,DWORD cSleep)    *fpFlushPrinter;
  DWORD()(HANDLE hPrinter,LPCWSTR pAction,PBIDI_REQUEST_CONTAINER pReqData,PBIDI_RESPONSE_CONTAINER *ppResData)   * fpSendRecvBidiData;
  BOOL( )(LPCWSTR pName,DWORD dwLevel,PVOID pInfo)    *fpAddPrinterConnection2;
  HRESULT((PCWSTR, const IID &,VOID **) * )fpGetPrintClassObject;
  HRESULT(PCWSTR, const IID *,VOID **) * )(fpGetPrintClassObject;
  HRESULT( )(HANDLE hPrinter,ULONG jobId,EPrintXPSJobOperation jobOperation,EPrintXPSJobProgress jobProgress) *fpReportJobProcessingProgress;
  VOID()(DWORD dwLevel,VOID *pfOut)    * fpEnumAndLogProvidorObjects;
  HRESULT( )(HANDLE hPrinter,LPWSTR pEnvironment,DWORD Level,LPBYTE pDriverInfo,DWORD cbBuf,LPDWORD pcbNeeded,DWORD dwClientMajorVersion,DWORD dwClientMinorVersion,PDWORD pdwServerMajorVersion,PDWORD pdwServerMinorVersion) *fpInternalGetPrinterDriver;
  HRESULT( )(LPCWSTR pcszPnpId,LPCWSTR pcszPortName,LPWSTR pszManufacturerName,DWORD cchManufacturerName,LPDWORD pcchRequiredManufacturerNameSize,LPWSTR pszModelName,DWORD cchModelName,LPDWORD pcchRequiredModelNameSize,LPDWORD pdwRank0Matches) *fpFindCompatibleDriver;
  DWORD()(HANDLE hPrinter,DWORD JobId,PCWSTR pszName,PrintPropertyValue *pValue)   * fpGetJobNamedPropertyValue;
  DWORD()(HANDLE hPrinter,DWORD JobId, const PrintNamedProperty *pProperty)   * fpSetJobNamedProperty;
  DWORD( )(HANDLE hPrinter,DWORD JobId,PCWSTR pszName)   *fpDeleteJobNamedProperty;
  DWORD(HANDLE hPrinter,DWORD JobId,DWORD *pcProperties,PrintNamedProperty **ppProperties)   * )(fpEnumJobNamedProperties;
  DWORD()(DWORD event,POWERBROADCAST_SETTING *pPowerSetting)   * fpPowerEvent;
  DWORD()(HANDLE hPrinter,HKEY *phKey)   * fpGetUserPropertyBag;
  BOOL( )()    *fpCanShutdown;
  DWORD( )(HANDLE hPrinter,PBranchOfficeJobDataContainer pJobDataContainer)   *fpLogJobInfoForBranchOffice;
} PRINTPROVIDOR, *LPPRINTPROVIDOR;
```

## Members


`fpOpenPrinter`

(Required.) Pointer to the provider's <b>OpenPrinter</b> function, which is described in the Microsoft Windows SDK documentation. However, at the provider level, this function must supply one of the DWORD return values listed in the following table.

<table>
<tr>
<th>Return value</th>
<th>Definition</th>
</tr>
<tr>
<td>ROUTER_SUCCESS</td>
<td>The provider supports the specified printer and has opened it.</td>
</tr>
<tr>
<td>ROUTER_STOP_ROUTING</td>
<td>The provider supports the specified printer, but an error occurred and the printer could not be opened. It is assumed that no other provider can support the printer. The function must call <b>SetLastError</b>.</td>
</tr>
<tr>
<td>ROUTER_UNKNOWN </td>
<td>The provider does not support the specified printer. The function must call <b>SetLastError</b> and specify ERROR_INVALID_NAME.</td>
</tr>
</table>
 

The router calls each provider until one of them returns ROUTER_SUCCESS or ROUTER_STOP_ROUTING. If the provider returns ROUTER_SUCCESS, it must also return a unique handle. (For more information, see Introduction to Print Providers.) The router first attempts to call the provider's OpenPrinterEx function. If that function is not supported, the router calls OpenPrinter.

`fpSetJob`

(Required.) Pointer to the provider's <b>SetJob</b> function (described in the Windows SDK documentation).

`fpGetJob`

(Required.) Pointer to the provider's <b>GetJob</b> function (described in the Windows SDK documentation).

`fpEnumJobs`

(Required.) Pointer to the provider's <b>EnumJobs</b> function (described in the Windows SDK documentation).

`fpAddPrinter`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>AddPrinter</b> function (described in the Windows SDK documentation).

`fpDeletePrinter`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>DeletePrinter</b> function (described in the Windows SDK documentation).

`fpSetPrinter`

(Required.) Pointer to the provider's <b>SetPrinter</b> function (described in the Windows SDK documentation).

`fpGetPrinter`

(Required.) Pointer to the provider's <b>GetPrinter</b> function (described in the Windows SDK documentation). If you are <a href="https://msdn.microsoft.com/9dbe8a00-6b5f-41ae-8ab5-218dcbe37833">writing a network print provider</a> and <b>GetPrinter</b> is returning a PRINTER_INFO_2 structure, the function should supply only the cJobs and Status structure members. The <a href="https://msdn.microsoft.com/c6f9ba42-5f0f-4919-bfac-e4cd1045de4d">local print provider</a> supplies the rest of the structure members.

`fpEnumPrinters`

(Required.) Pointer to the provider's <b>EnumPrinters</b> function (described in the Windows SDK documentation).

`fpAddPrinterDriver`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>AddPrinterDriver</b> function (described in the Windows SDK documentation). If the provider does not support the specified driver or server, it should specify ERROR_INVALID_NAME to SetLastError before returning <b>FALSE</b>.

`fpEnumPrinterDrivers`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>EnumPrinterDrivers</b> function (described in the Windows SDK documentation). If the provider does not support the specified server, it should specify ERROR_INVALID_NAME to SetLastError before returning <b>FALSE</b>.

`fpGetPrinterDriver`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>GetPrinterDriver</b> function (described in the Windows SDK documentation). The router first attempts to call the provider's <b>GetPrinterDriverEx</b> function. If that function is not supported, the router calls <b>GetPrinterDriver</b>.

`fpGetPrinterDriverDirectory`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>GetPrinterDriverDirectory</b> function (described in the Windows SDK documentation). If the provider does not support the specified server, it should specify ERROR_INVALID_NAME to <b>SetLastError</b> before returning <b>FALSE</b>.

`fpDeletePrinterDriver`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>DeletePrinterDriver</b> function (described in the Windows SDK documentation). If the provider does not support the specified server, it should specify ERROR_INVALID_NAME to <b>SetLastError</b> before returning <b>FALSE</b>.

`fpAddPrintProcessor`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>AddPrintProcessor</b> function (described in the Windows SDK documentation).

`fpEnumPrintProcessors`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>EnumPrintProcessors</b> function (described in the Windows SDK documentation).

`fpGetPrintProcessorDirectory`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>GetPrintProcessorDirectory</b> function (described in the Windows SDK documentation).

`fpDeletePrintProcessor`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>DeletePrintProcessor</b> function (described in the Windows SDK documentation).

`fpEnumPrintProcessorDatatypes`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>EnumPrintProcessorDatatypes</b> function (described in the Windows SDK documentation).

`fpStartDocPrinter`

(Required.) Pointer to the provider's <b>StartDocPrinter</b> function (described in the Windows SDK documentation).

`fpStartPagePrinter`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>StartPagePrinter</b> function (described in the Windows SDK documentation).

`fpWritePrinter`

(Required.) Pointer to the provider's <b>WritePrinter</b> function (described in the Windows SDK documentation).

`fpEndPagePrinter`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>EndPagePrinter</b> function (described in the Windows SDK documentation).

`fpAbortPrinter`

(Required.) Pointer to the provider's <b>AbortPrinter</b> function (described in the Windows SDK documentation).

`fpReadPrinter`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>ReadPrinter</b> function (described in the Windows SDK documentation).

`fpEndDocPrinter`

(Required.) Pointer to the provider's <b>EndDocPrinter</b> function (described in the Windows SDK documentation).

`fpAddJob`

(Required.) Pointer to the provider's <b>AddJob</b> function (described in the Windows SDK documentation).

`fpScheduleJob`

(Required.) Pointer to the provider's <b>ScheduleJob</b> function (described in the Windows SDK documentation).

`fpGetPrinterData`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>GetPrinterData</b> function (described in the Windows SDK documentation).

`fpSetPrinterData`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>SetPrinterData</b> function (described in the Windows SDK documentation).

`fpWaitForPrinterChange`

Obsolete. Must be <b>NULL</b>.

`fpClosePrinter`

(Required.) Pointer to the provider's <b>ClosePrinter</b> function (described in the Windows SDK documentation). If a printer change notification object has been created, then the router calls the provider's FindClosePrinterChangeNotification function (described in the Windows SDK documentation) before calling ClosePrinter.

`fpAddForm`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>AddForm</b> function (described in the Windows SDK documentation).

`fpDeleteForm`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>DeleteForm</b> function (described in the Windows SDK documentation).

`fpGetForm`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>GetForm</b> function (described in the Windows SDK documentation).

`fpSetForm`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>SetForm</b> function (described in the Windows SDK documentation).

`fpEnumForms`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>EnumForms</b> function (described in the Windows SDK documentation).

`fpEnumMonitors`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>EnumMonitors</b> function, which is described in the Windows SDK documentation. However, at the provider level this function must supply one of the DWORD return values listed in the following table.

<table>
<tr>
<th>Return value</th>
<th>Definition</th>
</tr>
<tr>
<td>ROUTER_SUCCESS</td>
<td>The provider has enumerated the monitors on the specified server.</td>
</tr>
<tr>
<td>ROUTER_STOP_ROUTING</td>
<td>The provider has enumerated the monitors on the specified server, and the router should not call other providers.</td>
</tr>
<tr>
<td>ROUTER_UNKNOWN </td>
<td>The provider does not support the specified server.</td>
</tr>
</table>

`fpEnumPorts`

<table>
<tr>
<th>Return value</th>
<th>Definition</th>
</tr>
<tr>
<td>ROUTER_SUCCESS</td>
<td>The provider has enumerated the ports on the specified server.</td>
</tr>
<tr>
<td>ROUTER_STOP_ROUTING</td>
<td>The provider has enumerated the ports on the specified server, and the router should not call other providers.</td>
</tr>
<tr>
<td>ROUTER_UNKNOWN </td>
<td>The provider does not support the specified server.</td>
</tr>
</table>

`fpAddPort`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>AddPort</b> function (described in the Windows SDK documentation). If the provider does not support the specified port, it must supply ERROR_NOT_SUPPORTED to SetLastError before returning <b>FALSE</b>.

`fpConfigurePort`

(Required.) Pointer to the provider's <b>ConfigurePort</b> function (described in the Windows SDK documentation). If the function supplies ERROR_NOT_SUPPORTED, ERROR_INVALID_NAME, or ERROR_UNKNOWN_PORT to SetLastError, the router will attempt to call another provider.

`fpDeletePort`

(Required.) Pointer to the provider's <b>DeletePort</b> function (described in the Windows SDK documentation). If the provider does not support the specified port, it must supply ERROR_NOT_SUPPORTED to SetLastError before returning <b>FALSE</b>.

`fpCreatePrinterIC`

For internal use only. Must be <b>NULL</b>.

`fpPlayGdiScriptOnPrinterIC`

For internal use only. Must be <b>NULL</b>.

`fpDeletePrinterIC`

For internal use only. Must be <b>NULL</b>.

`fpAddPrinterConnection`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>AddPrinterConnection</b> function (described in the Windows SDK documentation).

`fpDeletePrinterConnection`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>DeletePrinterConnection</b> function (described in the Windows SDK documentation).

`fpPrinterMessageBox`

Not used. Must be <b>NULL</b>.

`fpAddMonitor`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>AddMonitor</b> function (described in the Windows SDK documentation). If the provider does not support the specified monitor, it must supply ERROR_INVALID_NAME to SetLastError before returning <b>FALSE</b>.

`fpDeleteMonitor`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>DeleteMonitor</b> function (described in the Windows SDK documentation). If the provider does not support the specified monitor, it must supply ERROR_INVALID_NAME to SetLastError before returning <b>FALSE</b>.

`fpResetPrinter`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>ResetPrinter</b> function (described in the Windows SDK documentation).

`fpGetPrinterDriverEx`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>GetPrinterDriverEx</b> function (described in the Windows SDK documentation). If GetPrinterDriverEx is not supported, the router attempts to call GetPrinterDriver.

`fpFindFirstPrinterChangeNotification`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>FindFirstPrinterChangeNotification</b> function (described in the Windows SDK documentation).

`fpFindClosePrinterChangeNotification`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>FindClosePrinterChangeNotification</b> function (described in the Windows SDK documentation).

`fpAddPortEx`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>AddPortEx</b> function (described in the Windows SDK documentation). If the provider does not support the specified port, it must supply ERROR_NOT_SUPPORTED to SetLastError before returning <b>FALSE</b>.

`fpShutDown`

For internal use only. Must be <b>NULL</b>.

`fpRefreshPrinterChangeNotification`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>RefreshPrinterChangeNotification</b> function.

`fpOpenPrinterEx`

For internal use only. Must be <b>NULL</b>.

`fpAddPrinterEx`

For internal use only. Must be <b>NULL</b>.

`fpSetPort`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>SetPort</b> function (described in the Windows SDK documentation). If the function supplies ERROR_NOT_SUPPORTED, ERROR_INVALID_NAME, or ERROR_UNKNOWN_PORT to <b>SetLastError</b>, the router will attempt to call another provider.

`fpEnumPrinterData`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>EnumPrinterData</b> function (described in the Windows SDK documentation).

`fpDeletePrinterData`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>DeletePrinterData</b> function (described in the Windows SDK documentation).

`fpClusterSplOpen`

For internal use only. Must be <b>NULL</b>.

`fpClusterSplClose`

For internal use only. Must be <b>NULL</b>.

`fpClusterSplIsAlive`

For internal use only. Must be <b>NULL</b>.

`fpSetPrinterDataEx`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>SetPrinterDataEx</b> function (described in the Windows SDK documentation).

`fpGetPrinterDataEx`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>GetPrinterDataEx</b> function (described in the Windows SDK documentation).

`fpEnumPrinterDataEx`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>EnumPrinterDataEx</b> function (described in the Windows SDK documentation).

`fpEnumPrinterKey`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>EnumPrinterKey</b> function (described in the Windows SDK documentation).

`fpDeletePrinterDataEx`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>DeletePrinterDataEx</b> function (described in the Windows SDK documentation).

`fpDeletePrinterKey`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>DeletePrinterKey</b> function (described in the Windows SDK documentation).

`fpSeekPrinter`

For internal use only. Must be <b>NULL</b>.

`fpDeletePrinterDriverEx`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's DeletePrinterDriverEx function (described in the Windows SDK documentation). If the provider does not support the specified server, it should specify ERROR_INVALID_NAME to <b>SetLastError</b> before returning <b>FALSE</b>.

`fpAddPerMachineConnection`

For internal use only. Must be <b>NULL</b>.

`fpDeletePerMachineConnection`

For internal use only. Must be <b>NULL</b>.

`fpEnumPerMachineConnections`

For internal use only. Must be <b>NULL</b>.

`fpXcvData`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>XcvData</b> function.

`fpAddPrinterDriverEx`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>AddPrinterDriverEx</b> function (described in the Windows SDK documentation). If the provider does not support the specified server, it should specify ERROR_INVALID_NAME to SetLastError before returning <b>FALSE</b>.

`fpSplReadPrinter`

For internal use only. Must be <b>NULL</b>.

`fpDriverUnloadComplete`

For internal use only. Must be <b>NULL</b>.

`fpGetSpoolFileInfo`

For internal use only. Must be <b>NULL</b>.

`fpCommitSpoolData`

For internal use only. Must be <b>NULL</b>.

`fpCloseSpoolFileHandle`

For internal use only. Must be <b>NULL</b>.

`fpFlushPrinter`

For internal use only. Must be <b>NULL</b>.

`fpSendRecvBidiData`

(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>SendRecvBidiData</b> function. If this parameter is <b>NULL</b>, it means that the provider does not support bidi communication.

`fpAddPrinterConnection2`



`fpReportJobProcessingProgress`



`fpEnumAndLogProvidorObjects`



`fpInternalGetPrinterDriver`



`fpFindCompatibleDriver`



`fpGetJobNamedPropertyValue`



`fpSetJobNamedProperty`



`fpDeleteJobNamedProperty`



`fpEnumJobNamedProperties`



`fpPowerEvent`



`fpGetUserPropertyBag`



`fpCanShutdown`



`fpLogJobInfoForBranchOffice`



## Remarks
Function pointers are listed in the order they are specified within the PRINTPROVIDOR structure. To see function descriptions grouped by related capabilities, see <a href="https://msdn.microsoft.com/4fae4b69-ed4b-47b6-b6e8-41733aed51a5">Functions Defined by Print Providers</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | winsplp.h (include Winsplp.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff548837">FindFirstPrinterChangeNotification</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff551614">InitializePrintProvidor</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561930">RefreshPrinterChangeNotification</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562068">SendRecvBidiData</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff564255">XcvData</a>