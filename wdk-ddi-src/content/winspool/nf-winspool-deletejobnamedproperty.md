---
UID: NF.winspool.DeleteJobNamedProperty
title: DeleteJobNamedProperty
author: windows-driver-content
description: Deletes the named property for the specified print job on the specified printer.
old-location: print\deletejobnamedproperty.htm
ms.assetid: 14F8C0A2-0D19-446E-8C2B-530A3AEDA879
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: winspool.h
req.include-header: Winspool.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DeleteJobNamedProperty
req.alt-loc: spoolss.dll,WinSpool.drv
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: WinSpool.lib
req.dll: Spoolss.dll; 
WinSpool.drv
req.irql: 
ms.keywords: DeleteJobNamedProperty
req.iface: 
req.product: Windows 10 or later.
---

# DeleteJobNamedProperty function



## -description
<p>Deletes the named property for the specified print job on the specified printer.  
</p>


## -syntax

````
 WINAPI DeleteJobNamedProperty(
  _In_ HANDLE hPrinter,
  _In_ DWORD  JobId,
  _In_ PCWSTR pszName
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> [in]

<dd>
<p>A handle to the printer object of interest. Use the <a href="NULL">OpenPrinter</a>, <a href="gdi.openprinter2">OpenPrinter2</a>, or the <a href="gdi.addprinter">AddPrinter</a> function to retrieve a printer handle. 
</p>
</dd>

### -param <i>JobId</i> [in]

<dd>
<p>Identifier that specifies the print job. You obtain a print job identifier by calling the <a href="gdi.addjob">AddJob</a> function or the <a href="https://msdn.microsoft.com/67580632-ff9a-4d29-8e4e-c21f04aa4b47">StartDoc</a> function. 
</p>
</dd>

### -param <i>pszName</i> [in]

<dd>
<p>Name of the property that will be deleted. 
</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the function returns <b>ERROR_SUCCESS.</b></p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winspool.h (include Winspool.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>WinSpool.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Spoolss.dll; </dt>
<dt>WinSpool.drv</dt>
</dl>
</td>
</tr>
</table>