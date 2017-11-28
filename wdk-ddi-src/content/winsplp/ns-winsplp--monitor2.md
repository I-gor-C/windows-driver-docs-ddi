---
UID: NS.winsplp._MONITOR2
title: MONITOR2
author: windows-driver-content
description: The MONITOR2 structure contains pointers to the functions defined by print monitors.
old-location: print\monitor2.htm
old-project: print
ms.assetid: 0bfb5119-2034-4e63-9fbe-e2ff42a352d6
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: MONITOR2,
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
req.alt-api: MONITOR2
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

# MONITOR2 structure



## -description
<p>The MONITOR2 structure contains pointers to the functions defined by print monitors.</p>


## -syntax

````
typedef struct _MONITOR2 {
  DWORD cbSize;
  BOOL  (WINAPI *pfnEnumPorts)(
      HANDLE hMonitor, 
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE pPorts, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  BOOL  (WINAPI *pfnOpenPort)(
      HANDLE hMonitor, 
      LPWSTR pName, 
      PHANDLE pHandle);
  BOOL  (WINAPI *pfnOpenPortEx)(
      HANDLE hMonitor, 
      HANDLE hMonitorPort, 
      LPWSTR pPortName, 
      LPWSTR pPrinterName, 
      PHANDLE pHandle, 
      struct _MONITOR2 * pMonitor2);
  BOOL  (WINAPI *pfnStartDocPort)(
      HANDLE hPort, 
      LPWSTR pPrinterName, 
      DWORD JobId, 
      DWORD Level, 
      LPBYTE pDocInfo);
  BOOL  (WINAPI *pfnWritePort)(
      HANDLE hPort, 
      LPBYTE pBuffer, 
      DWORD cbBuf, 
      LPDWORD pcbWritten);
  BOOL  (WINAPI *pfnReadPort)(
      HANDLE hPort, 
      LPBYTE pBuffer, 
      DWORD cbBuffer, 
      LPDWORD pcbRead);
  BOOL  (WINAPI *pfnEndDocPort)(HANDLE hPort);
  BOOL  (WINAPI *pfnClosePort)(HANDLE hPort);
  BOOL  (WINAPI *pfnAddPort)(
      HANDLE hMonitor, 
      LPWSTR pName, 
      HWND hWnd, 
      LPWSTR pMonitorName);
  BOOL  (WINAPI *pfnAddPortEx)(
      HANDLE hMonitor, 
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE lpBuffer, 
      LPWSTR pMonitorName);
  BOOL  (WINAPI *pfnConfigurePort)(
      HANDLE hMonitor, 
      LPWSTR pName, 
      HWND hWnd, 
      LPWSTR pPortName);
  BOOL  (WINAPI *pfnDeletePort)(
      HANDLE hMonitor, 
      LPWSTR pName, 
      HWND hWnd, 
      LPWSTR pPortName);
  BOOL  (WINAPI *pfnGetPrinterDataFromPort)(
      HANDLE hPort, 
      DWORD ControlID, 
      LPWSTR pValueName, 
      LPWSTR lpInBuffer, 
      DWORD cbInBuffer, 
      LPWSTR lpOutBuffer, 
      DWORD cbOutBuffer, 
      LPDWORD lpcbReturned);
  BOOL  (WINAPI *pfnSetPortTimeOuts)(
      HANDLE hPort, 
      LPCOMMTIMEOUTS lpCTO, 
      DWORD reserved);
  BOOL  (WINAPI *pfnXcvOpenPort)(
      HANDLE hMonitor, 
      LPCWSTR pszObject, 
      ACCESS_MASK GrantedAccess, 
      PHANDLE phXcv);
  DWORD (WINAPI *pfnXcvDataPort)(
      HANDLE hXcv, 
      LPCWSTR pszDataName, 
      PBYTE pInputData, 
      DWORD cbInputData, 
      PBYTE pOutputData, 
      DWORD cbOutputData, 
      PDWORD pcbOutputNeeded);
  BOOL  (WINAPI *pfnXcvClosePort)(HANDLE hXcv);
  VOID  (WINAPI *pfnShutdown)(HANDLE hMonitor);
  DWORD (WINAPI *pfnSendRecvBidiDataFromPort)(
      HANDLE hPort, 
      DWORD dwAccessBit, 
      LPCWSTR pAction, 
      PBIDI_REQUEST_CONTAINER pReqData, 
      PBIDI_RESPONSE_CONTAINER* ppResData);
} MONITOR2, *PMONITOR2, *LPMONITOR2;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd>
<p>Specifies the size, in bytes, of the MONITOR2 structure.</p>
</dd>

### -field <b>pfnEnumPorts</b>

<dd>
<p>Pointer to the print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff548754">EnumPorts</a> function. (Port monitors only.)</p>
</dd>

### -field <b>pfnOpenPort</b>

<dd>
<p>Pointer to the print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff559593">OpenPort</a> function.</p>
</dd>

### -field <b>pfnOpenPortEx</b>

<dd>
<p>Pointer to the print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff559596">OpenPortEx</a> function. (Language monitors only.)</p>
</dd>

### -field <b>pfnStartDocPort</b>

<dd>
<p>Pointer to the print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff562710">StartDocPort</a> function.</p>
</dd>

### -field <b>pfnWritePort</b>

<dd>
<p>Pointer to the print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff563792">WritePort</a> function.</p>
</dd>

### -field <b>pfnReadPort</b>

<dd>
<p>Pointer to the print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff561909">ReadPort</a> function.</p>
</dd>

### -field <b>pfnEndDocPort</b>

<dd>
<p>Pointer to the print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff548742">EndDocPort</a> function.</p>
</dd>

### -field <b>pfnClosePort</b>

<dd>
<p>Pointer to the print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff545975">ClosePort</a> function.</p>
</dd>

### -field <b>pfnAddPort</b>

<dd>
<p>(Obsolete. Must be <b>NULL</b>.) Pointer to the print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff545022">AddPort</a> function.</p>
</dd>

### -field <b>pfnAddPortEx</b>

<dd>
<p>(Obsolete. Must be <b>NULL</b>.) Pointer to the print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff545025">AddPortEx</a> function. (Port monitors only.)</p>
</dd>

### -field <b>pfnConfigurePort</b>

<dd>
<p>(Obsolete. Must be <b>NULL</b>.) Pointer to the print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff546286">ConfigurePort</a> function.</p>
</dd>

### -field <b>pfnDeletePort</b>

<dd>
<p>(Obsolete. Must be <b>NULL</b>.) Pointer to the print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff547427">DeletePort</a> function.</p>
</dd>

### -field <b>pfnGetPrinterDataFromPort</b>

<dd>
<p>Pointer to the print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff550506">GetPrinterDataFromPort</a> function.</p>
</dd>

### -field <b>pfnSetPortTimeOuts</b>

<dd>
<p>Pointer to the print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff562630">SetPortTimeOuts</a> function. (Port monitors only.)</p>
</dd>

### -field <b>pfnXcvOpenPort</b>

<dd>
<p>Pointer to the print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff564259">XcvOpenPort</a> function. (Port monitors only.)</p>
</dd>

### -field <b>pfnXcvDataPort</b>

<dd>
<p>Pointer to the print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff564258">XcvDataPort</a> function. (Port monitors only.)</p>
</dd>

### -field <b>pfnXcvClosePort</b>

<dd>
<p>Pointer to the print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff564254">XcvClosePort</a> function. (Port monitors only.)</p>
</dd>

### -field <b>pfnShutdown</b>

<dd>
<p>Pointer to the print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/dn926950">Shutdown</a> function.</p>
</dd>

### -field <b>pfnSendRecvBidiDataFromPort</b>

<dd>
<p>Pointer to the print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff562071">SendRecvBidiDataFromPort</a> function.</p>
</dd>
</dl>

## -remarks
<p>Each language monitor and each port monitor server DLL must provide a MONITOR2 structure. The monitor must supply values for all structure members, and specify the structure's address as the return value for its <a href="https://msdn.microsoft.com/library/windows/hardware/ff551605">InitializePrintMonitor2</a> function.</p>

<p>If a function is not defined, its pointer must be <b>NULL</b>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551605">InitializePrintMonitor2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557541">MONITORUI</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20MONITOR2 structure%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
