---
UID: NS:winsplp._MONITOR2
title: "_MONITOR2"
author: windows-driver-content
description: The MONITOR2 structure contains pointers to the functions defined by print monitors.
old-location: print\monitor2.htm
old-project: print
ms.assetid: 0bfb5119-2034-4e63-9fbe-e2ff42a352d6
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*LPMONITOR2, *PMONITOR2, LPMONITOR2, LPMONITOR2 structure pointer [Print Devices], MONITOR2, MONITOR2 structure [Print Devices], PMONITOR2, PMONITOR2 structure pointer [Print Devices], _MONITOR2, print.monitor2, spoolfnc_db4ec1e7-1368-4695-bae0-91fd5dcd8a1a.xml, winsplp/LPMONITOR2, winsplp/MONITOR2, winsplp/PMONITOR2"
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
-	MONITOR2
product:
- Windows
targetos: Windows
req.typenames: MONITOR2, *PMONITOR2, *LPMONITOR2
req.product: Windows 10 or later.
---

# _MONITOR2 structure
The MONITOR2 structure contains pointers to the functions defined by print monitors.

## Syntax
```
typedef struct _MONITOR2 {
  DWORD  cbSize;
  BOOL( )(HANDLE hMonitor,LPWSTR pName,DWORD Level,LPBYTE pPorts,DWORD cbBuf,LPDWORD pcbNeeded,LPDWORD pcReturned)  *pfnEnumPorts;
  BOOL( )(HANDLE hMonitor,LPWSTR pName,PHANDLE pHandle)  *pfnOpenPort;
  BOOL()(HANDLE hMonitor,HANDLE hMonitorPort,LPWSTR pPortName,LPWSTR pPrinterName,PHANDLE pHandle,_MONITOR2 *pMonitor2)  * pfnOpenPortEx;
  BOOL( )(HANDLE hPort,LPWSTR pPrinterName,DWORD JobId,DWORD Level,LPBYTE pDocInfo)  *pfnStartDocPort;
  BOOL( )(HANDLE hPort,LPBYTE pBuffer,DWORD cbBuf,LPDWORD pcbWritten)  *pfnWritePort;
  BOOL( )(HANDLE hPort,LPBYTE pBuffer,DWORD cbBuffer,LPDWORD pcbRead)  *pfnReadPort;
  BOOL( )(HANDLE hPort)  *pfnEndDocPort;
  BOOL( )(HANDLE hPort)  *pfnClosePort;
  BOOL( )(HANDLE hMonitor,LPWSTR pName,HWND hWnd,LPWSTR pMonitorName)  *pfnAddPort;
  BOOL( )(HANDLE hMonitor,LPWSTR pName,DWORD Level,LPBYTE lpBuffer,LPWSTR lpMonitorName)  *pfnAddPortEx;
  BOOL( )(HANDLE hMonitor,LPWSTR pName,HWND hWnd,LPWSTR pPortName)  *pfnConfigurePort;
  BOOL( )(HANDLE hMonitor,LPWSTR pName,HWND hWnd,LPWSTR pPortName)  *pfnDeletePort;
  BOOL( )(HANDLE hPort,DWORD ControlID,LPWSTR pValueName,LPWSTR lpInBuffer,DWORD cbInBuffer,LPWSTR lpOutBuffer,DWORD cbOutBuffer,LPDWORD lpcbReturned)  *pfnGetPrinterDataFromPort;
  BOOL( )(HANDLE hPort,LPCOMMTIMEOUTS lpCTO,DWORD reserved)  *pfnSetPortTimeOuts;
  BOOL( )(HANDLE hMonitor,LPCWSTR pszObject,ACCESS_MASK GrantedAccess,PHANDLE phXcv)  *pfnXcvOpenPort;
  DWORD( )(HANDLE hXcv,LPCWSTR pszDataName,PBYTE pInputData,DWORD cbInputData,PBYTE pOutputData,DWORD cbOutputData,PDWORD pcbOutputNeeded) *pfnXcvDataPort;
  BOOL( )(HANDLE hXcv)  *pfnXcvClosePort;
  VOID( )(HANDLE hMonitor)  *pfnShutdown;
  DWORD()(HANDLE hPort,DWORD dwAccessBit,LPCWSTR pAction,PBIDI_REQUEST_CONTAINER pReqData,PBIDI_RESPONSE_CONTAINER *ppResData) * pfnSendRecvBidiDataFromPort;
  DWORD()(HANDLE hMonitor,DWORD cPorts,PCWSTR *ppszPorts) * pfnNotifyUsedPorts;
  DWORD()(HANDLE hMonitor,DWORD cPorts,PCWSTR *ppszPorts) * pfnNotifyUnusedPorts;
  DWORD()(HANDLE hMonitor,DWORD event,POWERBROADCAST_SETTING *pSettings) * pfnPowerEvent;
} *LPMONITOR2, MONITOR2, *PMONITOR2;
```

## Members


`cbSize`

Specifies the size, in bytes, of the MONITOR2 structure.

`pfnEnumPorts`

A port monitor server DLL's <b>EnumPorts</b> function enumerates the ports that the port monitor supports.

`pfnOpenPort`

Pointer to the print monitor's <b>OpenPort</b> function.

`pfnOpenPortEx`

A language monitor's <code>OpenPortEx</code> function opens a printer port.

`pfnStartDocPort`

A print monitor's <code>StartDocPort</code> function performs the tasks required to start a print job on the specified port.

`pfnWritePort`

Pointer to the print monitor's <b>WritePort</b> function.

`pfnReadPort`

Pointer to the print monitor's <b>ReadPort</b> function.

`pfnEndDocPort`

A print monitor's <b>EndDocPort</b> function performs the tasks required to end a print job on the specified port.

`pfnClosePort`

Pointer to the print monitor's <b>ClosePort</b> function.

`pfnAddPort`

The <a href="https://msdn.microsoft.com/library/windows/hardware/ff545022">AddPort</a> function is obsolete and is for use only with Windows NT 4.0 and previous versions.


<a href="https://msdn.microsoft.com/library/windows/hardware/ff545022">AddPort</a> creates a port and adds it to the list of ports currently supported by the specified monitor in the spooler environment.

`pfnAddPortEx`

(Obsolete. Must be <b>NULL</b>.) Pointer to the print monitor's <b>AddPortEx</b> function. (Port monitors only.)

`pfnConfigurePort`

The <b>ConfigurePort</b> function is obsolete and is for use only with Windows NT 4.0 and previous versions. For later versions of Windows, use <b>ConfigurePortUI</b>.

<b>ConfigurePort</b> is a port management function that configures the specified port.

`pfnDeletePort`

The <b>DeletePort</b> function is obsolete and is for use only with Windows NT 4.0 and previous versions.

<b>DeletePort</b> deletes a port from the monitor's environment.

`pfnGetPrinterDataFromPort`

Pointer to the print monitor's <b>GetPrinterDataFromPort</b> function.

`pfnSetPortTimeOuts`

A port monitor server DLL's <code>SetPortTimeOuts</code> function sets port time-out values for an open port.

`pfnXcvOpenPort`

Pointer to the print monitor's <b>XcvOpenPort</b> function. (Port monitors only.)

`pfnXcvDataPort`

Pointer to the print monitor's <b>XcvDataPort</b> function. (Port monitors only.)

`pfnXcvClosePort`

Pointer to the print monitor's <b>XcvClosePort</b> function. (Port monitors only.)

`pfnShutdown`

Pointer to the print monitor's <b>Shutdown</b> function.

`pfnSendRecvBidiDataFromPort`

Pointer to the print monitor's <b>SendRecvBidiDataFromPort</b> function.

`pfnNotifyUsedPorts`



`pfnNotifyUnusedPorts`



`pfnPowerEvent`



## Remarks
Each language monitor and each port monitor server DLL must provide a MONITOR2 structure. The monitor must supply values for all structure members, and specify the structure's address as the return value for its <a href="https://msdn.microsoft.com/library/windows/hardware/ff551605">InitializePrintMonitor2</a> function.

If a function is not defined, its pointer must be <b>NULL</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | winsplp.h (include Winsplp.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff551605">InitializePrintMonitor2</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557541">MONITORUI</a>