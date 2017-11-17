---
UID: NS.winsplp._SPLCLIENT_INFO_3_VISTA
title: SPLCLIENT_INFO_3_VISTA
author: windows-driver-content
description: Contains a super-set of the information in both a SPLCLIENT_INFO_1 and SPLCLIENT_INFO_2 structure. It also contains additional information needed by the provider.
old-location: print\splclient_info_3_vista.htm
ms.assetid: 076ECB20-CFAD-4A16-9B01-6936E0DD7E50
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: print
req.header: winsplp.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SPLCLIENT_INFO_3_VISTA
req.alt-loc: Winsplp.h
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
ms.keywords: SPLCLIENT_INFO_3_VISTA, SPLCLIENT_INFO_3_VISTA
req.iface: 
req.product: Windows 10 or later.
---

# SPLCLIENT_INFO_3_VISTA structure



## -description
<p>Contains a super-set of the information in both a <a href="https://msdn.microsoft.com/library/windows/hardware/ff562674">SPLCLIENT_INFO_1</a> and <b>SPLCLIENT_INFO_2</b> structure. It also contains additional information needed by the provider.</p>


## -syntax

````
typedef struct _SPLCLIENT_INFO_3_VISTA {
  UINT             cbSize;
  DWORD            dwFlags;
  DWORD            dwSize;
  PWSTR            pMachineName;
  PWSTR            pUserName;
  DWORD            dwBuildNum;
             DWORD dwMajorVersion;
  DWORD            dwMinorVersion;
  WORD             wProcessorArchitecture;
  UINT64           hSplPrinter;
} SPLCLIENT_INFO_3_VISTA;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd>
<p>Specifies the size in bytes of this structure.</p>
</dd>

### -field <b>dwFlags</b>

<dd>
<p>Specifies open printer additional flags to the provider.</p>
</dd>

### -field <b>dwSize</b>

<dd>
<p>Reserved. Used for compatibility with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562674">SPLCLIENT_INFO_1</a> structure.</p>
</dd>

### -field <b>pMachineName</b>

<dd>
<p>Specifies the client machine name.</p>
</dd>

### -field <b>pUserName</b>

<dd>
<p>Specifies the client user name.</p>
</dd>

### -field <b>dwBuildNum</b>

<dd>
<p>Specifies the client build number.</p>
</dd>

### -field <b>dwMajorVersion</b>

<dd>
<p>Specifies the major version of the client machine.</p>
</dd>

### -field <b>dwMinorVersion</b>

<dd>
<p>Specifies the minor version of the client machine.</p>
</dd>

### -field <b>wProcessorArchitecture</b>

<dd>
<p>Specifies the client machine architecture.</p>
</dd>

### -field <b>hSplPrinter</b>

<dd>
<p>Specifies the server-side handle to be used for direct calls.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winsplp.h</dt>
</dl>
</td>
</tr>
</table>