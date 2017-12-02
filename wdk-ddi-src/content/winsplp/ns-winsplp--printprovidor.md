---
UID: NS.winsplp._PRINTPROVIDOR
title: PRINTPROVIDOR
author: windows-driver-content
description: Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated.
old-location: print\printprovidor.htm
old-project: print
ms.assetid: c030cb9d-23c0-4d0e-970f-f447e9af7528
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: PRINTPROVIDOR,
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
req.alt-api: PRINTPROVIDOR
req.alt-loc: winsplp.h
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
req.iface: 
req.product: Windows 10 or later.
---

# PRINTPROVIDOR structure



## -description

## -syntax

````
typedef struct _PRINTPROVIDOR {
  BOOL   (*fpOpenPrinter)(
      PWSTR pPrinterName, 
      PHANDLE phPrinter, 
      PPRINTER_DEFAULTS pDefault);
  BOOL   (*fpSetJob)(
      HANDLE hPrinter, 
      DWORD JobId, 
      DWORD Level, 
      LPBYTE pJob, 
      DWORD Command);
  BOOL   (*fpGetJob)(
      HANDLE hPrinter, 
      DWORD JobId, 
      DWORD Level, 
      LPBYTE pJob, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded);
  BOOL   (*fpEnumJobs)(
      HANDLE hPrinter, 
      DWORD FirstJob, 
      DWORD NoJobs, 
      DWORD Level, 
      LPBYTE pJob, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  HANDLE (*fpAddPrinter)(
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE pPrinter);
  BOOL   (*fpDeletePrinter)(HANDLE hPrinter);
  BOOL   (*fpSetPrinter)(
      HANDLE hPrinter, 
      DWORD Level, 
      LPBYTE pPrinter, 
      DWORD Command);
  BOOL   (*fpGetPrinter)(
      HANDLE hPrinter, 
      DWORD Level, 
      LPBYTE pPrinter, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded);
  BOOL   (*fpEnumPrinters)(
      DWORD Flags, 
      LPWSTR Name, 
      DWORD Level, 
      LPBYTE pPrinterEnum, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  BOOL   (*fpAddPrinterDriver)(
      LPWSTR Name, 
      DWORD Level, 
      LPBYTE pDriverInfo);
  BOOL   (*fpEnumPrinterDrivers)(
      LPWSTR pName, 
      LPWSTR pEnvironment, 
      DWORD Level, 
      LPBYTE pDriverInfo, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  BOOL   (*fpGetPrinterDriver)(
      HANDLE hPrinter, 
      LPWSTR pEnvironment, 
      DWORD Level, 
      LPBYTE pDriverInfo, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded);
  BOOL   (*fpGetPrinterDriverDirectory)(
      LPWSTR pName, 
      LPWSTR pEnvironment, 
      DWORD Level, 
      LPBYTE pDriverDirectory, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded);
  BOOL   (*fpDeletePrinterDriver)(
      LPWSTR pName, 
      LPWSTR pEnvironment, 
      LPWSTR pDriverName);
  BOOL   (*fpAddPrintProcessor)(
      LPWSTR pName, 
      LPWSTR pEnvironment, 
      LPWSTR pPathName, 
      LPWSTR pPrintProcessorName);
  BOOL   (*fpEnumPrintProcessors)(
      LPWSTR pName, 
      LPWSTR pEnvironment, 
      DWORD Level, 
      LPBYTE pPrintProcessorInfo, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  BOOL   (*fpGetPrintProcessorDirectory)(
      LPWSTR pName, 
      LPWSTR pEnvironment, 
      DWORD Level, 
      LPBYTE pPrintProcessorInfo, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded);
  BOOL   (*fpDeletePrintProcessor)(
      LPWSTR pName, 
      LPWSTR pEnvironment, 
      LPWSTR pPrintProcessorName);
  BOOL   (*fpEnumPrintProcessorDatatypes)(
      LPWSTR pName, 
      LPWSTR pPrintProcessorName, 
      DWORD Level, 
      LPBYTE pDataypes, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  DWORD  (*fpStartDocPrinter)(
      HANDLE hPrinter, 
      DWORD Level, 
      LPBYTE pDocInfo);
  BOOL   (*fpStartPagePrinter)(HANDLE hPrinter);
  BOOL   (*fpWritePrinter)(
      HANDLE hPrinter, 
      LPVOID pBuf, 
      DWORD cbBuf, 
      LPDWORD pcWritten);
  BOOL   (*fpEndPagePrinter)(HANDLE hPrinter);
  BOOL   (*fpAbortPrinter)(HANDLE hPrinter);
  BOOL   (*fpReadPrinter)(
      HANDLE hPrinter, 
      LPVOID pBuf, 
      DWORD cbBuf, 
      LPDWORD pNoBytesRead);
  BOOL   (*fpEndDocPrinter)(HANDLE hPrinter);
  BOOL   (*fpAddJob)(
      HANDLE hPrinter, 
      DWORD Level, 
      LPBYTE pData, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded);
  BOOL   (*fpScheduleJob)(
      HANDLE hPrinter, 
      DWORD JobId);
  DWORD  (*fpGetPrinterData)(
      HANDLE hPrinter, 
      LPWSTR pValueName, 
      LPDWORD pType, 
      LPBYTE pData, 
      DWORD nSize, 
      LPDWORD pcbNeeded);
  DWORD  (*fpSetPrinterData)(
      HANDLE hPrinter, 
      LPWSTR pValueName, 
      DWORD Type, 
      LPBYTE pData, 
      DWORD cbData);
  DWORD  (*fpWaitForPrinterChange)(
      HANDLE hPrinter, 
      DWORD Flags);
  BOOL   (*fpClosePrinter)(HANDLE hPrinter);
  BOOL   (*fpAddForm)(
      HANDLE hPrinter, 
      DWORD Level, 
      LPBYTE pForm);
  BOOL   (*fpDeleteForm)(
      HANDLE hPrinter, 
      LPWSTR pFormName);
  BOOL   (*fpGetForm)(
      HANDLE hPrinter, 
      LPWSTR pFormName, 
      DWORD Level, 
      LPBYTE pForm, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded);
  BOOL   (*fpSetForm)(
      HANDLE hPrinter, 
      LPWSTR pFormName, 
      DWORD Level, 
      LPBYTE pForm);
  BOOL   (*fpEnumForms)(
      HANDLE hPrinter, 
      DWORD Level, 
      LPBYTE pForm, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  BOOL   (*fpEnumMonitors)(
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE pMonitors, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  BOOL   (*fpEnumPorts)(
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE pPorts, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  BOOL   (*fpAddPort)(
      LPWSTR pName, 
      HWND hWnd, 
      LPWSTR pMonitorName);
  BOOL   (*fpConfigurePort)(
      LPWSTR pName, 
      HWND hWnd, 
      LPWSTR pPortName);
  BOOL   (*fpDeletePort)(
      LPWSTR pName, 
      HWND hWnd, 
      LPWSTR pPortName);
  HANDLE (*fpCreatePrinterIC)(
      HANDLE hPrinter, 
      LPDEVMODEW pDevMode);
  BOOL   (*fpPlayGdiScriptOnPrinterIC)(
      HANDLE hPrinterIC, 
      LPBYTE pIn, 
      DWORD cIn, 
      LPBYTE pOut, 
      DWORD cOut, 
      DWORD ul);
  BOOL   (*fpDeletePrinterIC)(HANDLE hPrinterIC);
  BOOL   (*fpAddPrinterConnection)(LPWSTR pName);
  BOOL   (*fpDeletePrinterConnection)(LPWSTR pName);
  DWORD  (*fpPrinterMessageBox)(
      HANDLE hPrinter, 
      DWORD Error, 
      HWND hWnd, 
      LPWSTR pText, 
      LPWSTR pCaption, 
      DWORD dwType);
  BOOL   (*fpAddMonitor)(
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE pMonitorInfo);
  BOOL   (*fpDeleteMonitor)(
      LPWSTR pName, 
      LPWSTR pEnvironment, 
      LPWSTR pMonitorName);
  BOOL   (*fpResetPrinter)(
      HANDLE hPrinter, 
      LPPRINTER_DEFAULTS pDefault);
  BOOL   (*fpGetPrinterDriverEx)(
      HANDLE hPrinter, 
      LPWSTR pEnvironment, 
      DWORD Level, 
      LPBYTE pDriverInfo, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      DWORD dwClientMajorVersion, 
      DWORD dwClientMinorVersion, 
      PDWORD pdwServerMajorVersion, 
      PDWORD pdwServerMinorVersion);
  BOOL   (*fpFindFirstPrinterChangeNotification)(
      HANDLE hPrinter, 
      DWORD fdwFlags, 
      DWORD fdwOptions, 
      HANDLE hNotify, 
      PDWORD pfdwStatus, 
      PVOID pPrinterNotifyOptions, 
      PVOID pPrinterNotifyInit);
  BOOL   (*fpFindClosePrinterChangeNotification)(HANDLE hPrinter);
  BOOL   (*fpAddPortEx)(
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE lpBuffer, 
      LPWSTR lpMonitorName);
  BOOL   (*fpShutDown)(LPVOID pvReserved);
  BOOL   (*fpRefreshPrinterChangeNotification)(
      HANDLE hPrinter, 
      DWORD Reserved, 
      PVOID pvReserved, 
      PVOID pPrinterNotifyInfo);
  BOOL   (*fpOpenPrinterEx)(
      LPWSTR pPrinterName, 
      LPHANDLE phPrinter, 
      LPPRINTER_DEFAULTS pDefault, 
      LPBYTE pClientInfo, 
      DWORD Level);
  HANDLE (*fpAddPrinterEx)(
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE pPrinter, 
      LPBYTE pClientInfo, 
      DWORD ClientInfoLevel);
  BOOL   (*fpSetPort)(
      LPWSTR pName, 
      LPWSTR pPortName, 
      DWORD Level, 
      LPBYTE pPortInfo);
  DWORD  (*fpEnumPrinterData)(
      HANDLE hPrinter, 
      DWORD dwIndex, 
      LPWSTR pValueName, 
      DWORD cbValueName, 
      LPDWORD pcbValueName, 
      LPDWORD pType, 
      LPBYTE pData, 
      DWORD cbData, 
      LPDWORD pcbData);
  DWORD  (*fpDeletePrinterData)(
      HANDLE hPrinter, 
      LPWSTR pValueName);
  DWORD  (*fpClusterSplOpen)(
      LPCTSTR pszServer, 
      LPCTSTR pszResource, 
      PHANDLE phSpooler, 
      LPCTSTR pszName, 
      LPCTSTR pszAddress);
  DWORD  (*fpClusterSplClose)(HANDLE hSpooler);
  DWORD  (*fpClusterSplIsAlive)(HANDLE hSpooler);
  DWORD  (*fpSetPrinterDataEx)(
      HANDLE hPrinter, 
      LPCWSTR pKeyName, 
      LPCWSTR pValueName, 
      DWORD Type, 
      LPBYTE pData, 
      DWORD cbData);
  DWORD  (*fpGetPrinterDataEx)(
      HANDLE hPrinter, 
      LPCWSTR pKeyName, 
      LPCWSTR pValueName, 
      LPDWORD pType, 
      LPBYTE pData, 
      DWORD nSize, 
      LPDWORD pcbNeeded);
  DWORD  (*fpEnumPrinterDataEx)(
      HANDLE hPrinter, 
      LPCWSTR pKeyName, 
      LPBYTE pEnumValues, 
      DWORD cbEnumValues, 
      LPDWORD pcbEnumValues, 
      LPDWORD pnEnumValues);
  DWORD  (*fpEnumPrinterKey)(
      HANDLE hPrinter, 
      LPCWSTR pKeyName, 
      LPWSTR pSubkey, 
      DWORD cbSubkey, 
      LPDWORD pcbSubkey);
  DWORD  (*fpDeletePrinterDataEx)(
      HANDLE hPrinter, 
      LPCWSTR pKeyName, 
      LPCWSTR pValueName);
  DWORD  (*fpDeletePrinterKey)(
      HANDLE hPrinter, 
      LPCWSTR pKeyName);
  BOOL   (*fpSeekPrinter)(
      HANDLE hPrinter, 
      LARGE_INTEGER liDistanceToMove, 
      PLARGE_INTEGER pliNewPointer, 
      DWORD dwMoveMethod, 
      BOOL bWrite);
  BOOL   (*fpDeletePrinterDriverEx)(
      LPWSTR pName, 
      LPWSTR pEnvironment, 
      LPWSTR pDriverName, 
      DWORD dwDeleteFlag, 
      DWORD dwVersionNum);
  BOOL   (*fpAddPerMachineConnection)(
      LPCWSTR pServer, 
      LPCWSTR pPrinterName, 
      LPCWSTR pPrintServer, 
      LPCWSTR pProvider);
  void   (*fpDeletePerMachineConnection)(
      LPCWSTR pServer, 
      LPCWSTR pPrinterName);
  BOOL   (*fpEnumPerMachineConnections)(
      LPCWSTR pServer, 
      LPBYTE pPrinterEnum, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  BOOL   (*fpXcvData)(
      HANDLE hXcv, 
      LPCWSTR pszDataName, 
      PBYTE pInputData, 
      DWORD cbInputData, 
      PBYTE pOutputData, 
      DWORD cbOutputData, 
      PDWORD pcbOutputNeeded, 
      PDWORD pdwStatus);
  BOOL   (*fpAddPrinterDriverEx)(
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE pDriverInfo, 
      DWORD dwFileCopyFlags);
  BOOL   (*fpSplReadPrinter)(
      HANDLE hPrinter, 
      LPBYTE* pBuf, 
      DWORD cbBuf);
  BOOL   (*fpDriverUnloadComplete)(LPWSTR pDriverFile);
  BOOL   (*fpGetSpoolFileInfo)(
      HANDLE hPrinter, 
      LPWSTR* pSpoolDir, 
      LPHANDLE phFile, 
      HANDLE hSpoolerProcess, 
      HANDLE hAppProcess);
  BOOL   (*fpCommitSpoolData)(
      HANDLE hPrinter, 
      DWORD cbCommit);
  BOOL   (*fpCloseSpoolFileHandle)(HANDLE hPrinter);
  BOOL   (*fpFlushPrinter)(
      HANDLE hPrinter, 
      LPBYTE pBuf, 
      DWORD cbBuf, 
      LPDWORD pcWritten, 
      DWORD cSleep);
  DWORD  (*fpSendRecvBidiData)(
      HANDLE hPrinter, 
      LPCWSTR pAction, 
      PBIDI_REQUEST_CONTAINER pReqData, 
      PBIDI_RESPONSE_CONTAINER* ppResData);
} PRINTPROVIDOR, *LPPRINTPROVIDOR;
````


## -struct-fields
<dl>

### -field fpOpenPrinter

<dd>
<p>(Required.) Pointer to the provider's <b>OpenPrinter</b> function, which is described in the Microsoft Windows SDK documentation. However, at the provider level, this function must supply one of the DWORD return values listed in the following table.</p>
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
<p> </p>
<p>The router calls each provider until one of them returns ROUTER_SUCCESS or ROUTER_STOP_ROUTING. If the provider returns ROUTER_SUCCESS, it must also return a unique handle. (For more information, see Introduction to Print Providers.) The router first attempts to call the provider's OpenPrinterEx function. If that function is not supported, the router calls OpenPrinter.</p>
</dd>

### -field fpSetJob

<dd>
<p>(Required.) Pointer to the provider's <b>SetJob</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpGetJob

<dd>
<p>(Required.) Pointer to the provider's <b>GetJob</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpEnumJobs

<dd>
<p>(Required.) Pointer to the provider's <b>EnumJobs</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpAddPrinter

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>AddPrinter</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpDeletePrinter

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>DeletePrinter</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpSetPrinter

<dd>
<p>(Required.) Pointer to the provider's <b>SetPrinter</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpGetPrinter

<dd>
<p>(Required.) Pointer to the provider's <b>GetPrinter</b> function (described in the Windows SDK documentation). If you are <a href="https://msdn.microsoft.com/9dbe8a00-6b5f-41ae-8ab5-218dcbe37833">writing a network print provider</a> and <b>GetPrinter</b> is returning a PRINTER_INFO_2 structure, the function should supply only the cJobs and Status structure members. The <a href="https://msdn.microsoft.com/c6f9ba42-5f0f-4919-bfac-e4cd1045de4d">local print provider</a> supplies the rest of the structure members.</p>
</dd>

### -field fpEnumPrinters

<dd>
<p>(Required.) Pointer to the provider's <b>EnumPrinters</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpAddPrinterDriver

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>AddPrinterDriver</b> function (described in the Windows SDK documentation). If the provider does not support the specified driver or server, it should specify ERROR_INVALID_NAME to SetLastError before returning <b>FALSE</b>.</p>
</dd>

### -field fpEnumPrinterDrivers

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>EnumPrinterDrivers</b> function (described in the Windows SDK documentation). If the provider does not support the specified server, it should specify ERROR_INVALID_NAME to SetLastError before returning <b>FALSE</b>.</p>
</dd>

### -field fpGetPrinterDriver

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>GetPrinterDriver</b> function (described in the Windows SDK documentation). The router first attempts to call the provider's <b>GetPrinterDriverEx</b> function. If that function is not supported, the router calls <b>GetPrinterDriver</b>.</p>
</dd>

### -field fpGetPrinterDriverDirectory

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>GetPrinterDriverDirectory</b> function (described in the Windows SDK documentation). If the provider does not support the specified server, it should specify ERROR_INVALID_NAME to <b>SetLastError</b> before returning <b>FALSE</b>.</p>
</dd>

### -field fpDeletePrinterDriver

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>DeletePrinterDriver</b> function (described in the Windows SDK documentation). If the provider does not support the specified server, it should specify ERROR_INVALID_NAME to <b>SetLastError</b> before returning <b>FALSE</b>.</p>
</dd>

### -field fpAddPrintProcessor

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>AddPrintProcessor</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpEnumPrintProcessors

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>EnumPrintProcessors</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpGetPrintProcessorDirectory

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>GetPrintProcessorDirectory</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpDeletePrintProcessor

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>DeletePrintProcessor</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpEnumPrintProcessorDatatypes

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>EnumPrintProcessorDatatypes</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpStartDocPrinter

<dd>
<p>(Required.) Pointer to the provider's <b>StartDocPrinter</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpStartPagePrinter

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>StartPagePrinter</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpWritePrinter

<dd>
<p>(Required.) Pointer to the provider's <b>WritePrinter</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpEndPagePrinter

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>EndPagePrinter</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpAbortPrinter

<dd>
<p>(Required.) Pointer to the provider's <b>AbortPrinter</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpReadPrinter

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>ReadPrinter</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpEndDocPrinter

<dd>
<p>(Required.) Pointer to the provider's <b>EndDocPrinter</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpAddJob

<dd>
<p>(Required.) Pointer to the provider's <b>AddJob</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpScheduleJob

<dd>
<p>(Required.) Pointer to the provider's <b>ScheduleJob</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpGetPrinterData

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>GetPrinterData</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpSetPrinterData

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>SetPrinterData</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpWaitForPrinterChange

<dd>
<p>Obsolete. Must be <b>NULL</b>.</p>
</dd>

### -field fpClosePrinter

<dd>
<p>(Required.) Pointer to the provider's <b>ClosePrinter</b> function (described in the Windows SDK documentation). If a printer change notification object has been created, then the router calls the provider's FindClosePrinterChangeNotification function (described in the Windows SDK documentation) before calling ClosePrinter.</p>
</dd>

### -field fpAddForm

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>AddForm</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpDeleteForm

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>DeleteForm</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpGetForm

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>GetForm</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpSetForm

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>SetForm</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpEnumForms

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>EnumForms</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpEnumMonitors

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>EnumMonitors</b> function, which is described in the Windows SDK documentation. However, at the provider level this function must supply one of the DWORD return values listed in the following table.</p>
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
<p> </p>
</dd>

### -field fpEnumPorts

<dd>
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
<p> </p>
</dd>

### -field fpAddPort

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>AddPort</b> function (described in the Windows SDK documentation). If the provider does not support the specified port, it must supply ERROR_NOT_SUPPORTED to SetLastError before returning <b>FALSE</b>.</p>
</dd>

### -field fpConfigurePort

<dd>
<p>(Required.) Pointer to the provider's <b>ConfigurePort</b> function (described in the Windows SDK documentation). If the function supplies ERROR_NOT_SUPPORTED, ERROR_INVALID_NAME, or ERROR_UNKNOWN_PORT to SetLastError, the router will attempt to call another provider.</p>
</dd>

### -field fpDeletePort

<dd>
<p>(Required.) Pointer to the provider's <b>DeletePort</b> function (described in the Windows SDK documentation). If the provider does not support the specified port, it must supply ERROR_NOT_SUPPORTED to SetLastError before returning <b>FALSE</b>.</p>
</dd>

### -field fpCreatePrinterIC

<dd>
<p>For internal use only. Must be <b>NULL</b>.</p>
</dd>

### -field fpPlayGdiScriptOnPrinterIC

<dd>
<p>For internal use only. Must be <b>NULL</b>.</p>
</dd>

### -field fpDeletePrinterIC

<dd>
<p>For internal use only. Must be <b>NULL</b>.</p>
</dd>

### -field fpAddPrinterConnection

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>AddPrinterConnection</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpDeletePrinterConnection

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>DeletePrinterConnection</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpPrinterMessageBox

<dd>
<p>Not used. Must be <b>NULL</b>.</p>
</dd>

### -field fpAddMonitor

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>AddMonitor</b> function (described in the Windows SDK documentation). If the provider does not support the specified monitor, it must supply ERROR_INVALID_NAME to SetLastError before returning <b>FALSE</b>.</p>
</dd>

### -field fpDeleteMonitor

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>DeleteMonitor</b> function (described in the Windows SDK documentation). If the provider does not support the specified monitor, it must supply ERROR_INVALID_NAME to SetLastError before returning <b>FALSE</b>.</p>
</dd>

### -field fpResetPrinter

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>ResetPrinter</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpGetPrinterDriverEx

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>GetPrinterDriverEx</b> function (described in the Windows SDK documentation). If GetPrinterDriverEx is not supported, the router attempts to call GetPrinterDriver.</p>
</dd>

### -field fpFindFirstPrinterChangeNotification

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <a href="..\winspool\nf-winspool-findfirstprinterchangenotification.md">FindFirstPrinterChangeNotification</a> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpFindClosePrinterChangeNotification

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>FindClosePrinterChangeNotification</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpAddPortEx

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>AddPortEx</b> function (described in the Windows SDK documentation). If the provider does not support the specified port, it must supply ERROR_NOT_SUPPORTED to SetLastError before returning <b>FALSE</b>.</p>
</dd>

### -field fpShutDown

<dd>
<p>For internal use only. Must be <b>NULL</b>.</p>
</dd>

### -field fpRefreshPrinterChangeNotification

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <a href="print.refreshprinterchangenotification">RefreshPrinterChangeNotification</a> function.</p>
</dd>

### -field fpOpenPrinterEx

<dd>
<p>For internal use only. Must be <b>NULL</b>.</p>
</dd>

### -field fpAddPrinterEx

<dd>
<p>For internal use only. Must be <b>NULL</b>.</p>
</dd>

### -field fpSetPort

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>SetPort</b> function (described in the Windows SDK documentation). If the function supplies ERROR_NOT_SUPPORTED, ERROR_INVALID_NAME, or ERROR_UNKNOWN_PORT to <b>SetLastError</b>, the router will attempt to call another provider.</p>
</dd>

### -field fpEnumPrinterData

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>EnumPrinterData</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpDeletePrinterData

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>DeletePrinterData</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpClusterSplOpen

<dd>
<p>For internal use only. Must be <b>NULL</b>.</p>
</dd>

### -field fpClusterSplClose

<dd>
<p>For internal use only. Must be <b>NULL</b>.</p>
</dd>

### -field fpClusterSplIsAlive

<dd>
<p>For internal use only. Must be <b>NULL</b>.</p>
</dd>

### -field fpSetPrinterDataEx

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>SetPrinterDataEx</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpGetPrinterDataEx

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>GetPrinterDataEx</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpEnumPrinterDataEx

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>EnumPrinterDataEx</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpEnumPrinterKey

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>EnumPrinterKey</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpDeletePrinterDataEx

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>DeletePrinterDataEx</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpDeletePrinterKey

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>DeletePrinterKey</b> function (described in the Windows SDK documentation).</p>
</dd>

### -field fpSeekPrinter

<dd>
<p>For internal use only. Must be <b>NULL</b>.</p>
</dd>

### -field fpDeletePrinterDriverEx

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's DeletePrinterDriverEx function (described in the Windows SDK documentation). If the provider does not support the specified server, it should specify ERROR_INVALID_NAME to <b>SetLastError</b> before returning <b>FALSE</b>.</p>
</dd>

### -field fpAddPerMachineConnection

<dd>
<p>For internal use only. Must be <b>NULL</b>.</p>
</dd>

### -field fpDeletePerMachineConnection

<dd>
<p>For internal use only. Must be <b>NULL</b>.</p>
</dd>

### -field fpEnumPerMachineConnections

<dd>
<p>For internal use only. Must be <b>NULL</b>.</p>
</dd>

### -field fpXcvData

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <a href="print.xcvdata">XcvData</a> function.</p>
</dd>

### -field fpAddPrinterDriverEx

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>AddPrinterDriverEx</b> function (described in the Windows SDK documentation). If the provider does not support the specified server, it should specify ERROR_INVALID_NAME to SetLastError before returning <b>FALSE</b>.</p>
</dd>

### -field fpSplReadPrinter

<dd>
<p>For internal use only. Must be <b>NULL</b>.</p>
</dd>

### -field fpDriverUnloadComplete

<dd>
<p>For internal use only. Must be <b>NULL</b>.</p>
</dd>

### -field fpGetSpoolFileInfo

<dd>
<p>For internal use only. Must be <b>NULL</b>.</p>
</dd>

### -field fpCommitSpoolData

<dd>
<p>For internal use only. Must be <b>NULL</b>.</p>
</dd>

### -field fpCloseSpoolFileHandle

<dd>
<p>For internal use only. Must be <b>NULL</b>.</p>
</dd>

### -field fpFlushPrinter

<dd>
<p>For internal use only. Must be <b>NULL</b>.</p>
</dd>

### -field fpSendRecvBidiData

<dd>
<p>(Optional. Can be <b>NULL</b>.) Pointer to the provider's <b>SendRecvBidiData</b> function. If this parameter is <b>NULL</b>, it means that the provider does not support bidi communication.</p>
</dd>
</dl>

## -remarks
<p>Function pointers are listed in the order they are specified within the PRINTPROVIDOR structure. To see function descriptions grouped by related capabilities, see <a href="https://msdn.microsoft.com/4fae4b69-ed4b-47b6-b6e8-41733aed51a5">Functions Defined by Print Providers</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winsplp.h (include Winsplp.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\winsplp\nf-winsplp-initializeprintprovidor.md">InitializePrintProvidor</a>
</dt>
<dt>
<a href="..\winspool\nf-winspool-findfirstprinterchangenotification.md">FindFirstPrinterChangeNotification</a>
</dt>
<dt>
<a href="print.refreshprinterchangenotification">RefreshPrinterChangeNotification</a>
</dt>
<dt>
<a href="print.xcvdata">XcvData</a>
</dt>
<dt>
<a href="print.sendrecvbididata">SendRecvBidiData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20PRINTPROVIDOR structure%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
