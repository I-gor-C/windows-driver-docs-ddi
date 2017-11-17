---
UID: NS.winsplp._MONITORREG
title: MONITORREG
author: windows-driver-content
description: The MONITORREG structure supplies print monitors with the address of registry functions to use instead of Win32 registry API functions.
old-location: print\monitorreg.htm
ms.assetid: 57c146bc-574f-4137-89bb-e891e005de05
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: print
req.header: winsplp.h
req.include-header: Winsplp.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MONITORREG
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
ms.keywords: MONITORREG, MONITORREG, *PMONITORREG
req.iface: 
req.product: Windows 10 or later.
---

# MONITORREG structure



## -description
<p>The MONITORREG structure supplies print monitors with the address of registry functions to use instead of Win32 registry API functions.</p>


## -syntax

````
typedef struct _MONITORREG {
  DWORD cbSize;
  LONG  (WINAPI *fpCreateKey)(
      HKEYMONITOR hcKey, 
      LPCTSTR pszSubKey, 
      DWORD dwOptions, 
      REGSAM samDesired, 
      PSECURITY_ATTRIBUTES pSecurityAttributes, 
      HKEYMONITOR phckResult, 
      PDWORD pdwDisposition, 
      HANDLE hSpooler);
  LONG  (WINAPI *fpOpenKey)(
      HKEYMONITOR hcKey, 
      LPCTSTR pszSubKey, 
      REGSAM samDesired, 
      HKEYMONITOR phkResult, 
      HANDLE hSpooler);
  LONG  (WINAPI *fpCloseKey)(
      HKEYMONITOR hcKey, 
      HANDLE hSpooler);
  LONG  (WINAPI *fpDeleteKey)(
      HKEYMONITOR hcKey, 
      LPCTSTR pszSubKey, 
      HANDLE hSpooler);
  LONG  (WINAPI *fpEnumKey)(
      HKEYMONITOR hcKey, 
      DWORD dwIndex, 
      LPTSTR pszName, 
      PDWORD pcchName, 
      PFILETIME pftLastWriteTime, 
      HANDLE hSpooler);
  LONG  (WINAPI *fpQueryInfoKey)(
      HKEYMONITOR hcKey, 
      PDWORD pcSubKeys, 
      PDWORD pcbKey, 
      PDWORD pcValues, 
      PDWORD pcbValue, 
      PDWORD pcbData, 
      PDWORD pcbSecurityDescriptor, 
      PFILETIME pftLastWriteTime, 
      HANDLE hSpooler);
  LONG  (WINAPI *fpSetValue)(
      HKEYMONITOR hcKey, 
      LPCTSTR pszValue, 
      DWORD dwType, 
      const BYTE* pData, 
      DWORD cbData, 
      HANDLE hSpooler);
  LONG  (WINAPI *fpDeleteValue)(
      HKEYMONITOR hcKey, 
      LPCTSTR pszValue, 
      HANDLE hSpooler);
  LONG  (WINAPI *fpEnumValue)(
      HKEYMONITOR hcKey, 
      DWORD dwIndex, 
      LPTSTR pszValue, 
      PDWORD pcbValue, 
      PDWORD pTyp, 
      PBYTE pcbData, 
      PDWORD pcbData, 
      HANDLE hSpooler);
  LONG  (WINAPI *fpQueryValue)(
      HKEYMONITOR hcKey, 
      LPCTSTR pszValue, 
      PDWORD pType, 
      PBYTE pData, 
      PDWORD pcbData, 
      HANDLE hSpooler);
} MONITORREG, *PMONITORREG;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd>
<p>Size, in bytes, of the MONITORREG structure.</p>
</dd>

### -field <b>fpCreateKey</b>

<dd></dd>

### -field <b>fpOpenKey</b>

<dd></dd>

### -field <b>fpCloseKey</b>

<dd></dd>

### -field <b>fpDeleteKey</b>

<dd></dd>

### -field <b>fpEnumKey</b>

<dd></dd>

### -field <b>fpQueryInfoKey</b>

<dd></dd>

### -field <b>fpSetValue</b>

<dd></dd>

### -field <b>fpDeleteValue</b>

<dd></dd>

### -field <b>fpEnumValue</b>

<dd></dd>

### -field <b>fpQueryValue</b>

<dd></dd>
</dl>

## -remarks
<p>The MONITORREG structure's address is supplied in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff557535">MONITORINIT</a> structure, which is passed to a print monitor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff551605">InitializePrintMonitor2</a> function.</p>

<p>When <a href="NULL">storing port configuration information</a>, print monitors must not explicitly call either the Win32 registry API or the cluster registry API. Instead, they must call equivalent spooler registry functions. The MONITORREG structure supplies the addresses of these functions. The following table lists each spooler registry function and its equivalent cluster registry function.</p>

<p><b>CreateKey</b></p>

<p><b>ClusterRegCreateKey</b></p>

<p><b>OpenKey</b></p>

<p><b>ClusterRegOpenKey</b></p>

<p><b>CloseKey</b></p>

<p><b>ClusterRegCloseKey</b></p>

<p><b>DeleteKey</b></p>

<p><b>ClusterRegDeleteKey</b></p>

<p><b>EnumKey</b></p>

<p><b>ClusterRegEnumKey</b></p>

<p><b>QueryInfoKey</b></p>

<p><b>ClusterRegQueryInfoKey</b></p>

<p><b>SetValue</b></p>

<p><b>ClusterRegSetValue</b></p>

<p><b>DeleteValue</b></p>

<p><b>ClusterRegDeleteValue</b></p>

<p><b>EnumValue</b></p>

<p><b>ClusterRegEnumValue</b></p>

<p><b>QueryValue</b></p>

<p><b>ClusterRegQueryValue</b></p>

<p> </p>

<p>Input and output parameters for these spooler functions match the parameters of the equivalent cluster registry functions (described in the Microsoft Windows SDK documentation), with the following exceptions:</p>

<p>Each spooler registry function requires an <i>hSpooler</i> input parameter. This is the spooler handle received in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557535">MONITORINIT</a> structure.</p>

<p>The spooler registry functions use HANDLE and PHANDLE parameter types instead of the HKEY and PHKEY types used by the cluster registry functions. Monitors receive the handle of the root registry location in the <b>hckRegistryRoot</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557535">MONITORINIT</a> structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557535">MONITORINIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551605">InitializePrintMonitor2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20MONITORREG structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
