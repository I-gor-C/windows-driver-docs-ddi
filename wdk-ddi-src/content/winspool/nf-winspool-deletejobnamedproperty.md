---
UID: NF.winspool.DeleteJobNamedProperty
title: DeleteJobNamedProperty function
author: windows-driver-content
description: Deletes the named property for the specified print job on the specified printer.
old-location: print\deletejobnamedproperty.htm
old-project: print
ms.assetid: 14F8C0A2-0D19-446E-8C2B-530A3AEDA879
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: DeleteJobNamedProperty
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
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
req.dll: Spoolss.dll; WinSpool.drv
req.irql: 
req.product: Windows 10 or later.
---

# DeleteJobNamedProperty function



## -description
Deletes the named property for the specified print job on the specified printer.  




## -syntax

````
 WINAPI DeleteJobNamedProperty(
  _In_ HANDLE hPrinter,
  _In_ DWORD  JobId,
  _In_ PCWSTR pszName
);
````


## -parameters

### -param hPrinter [in]

A handle to the printer object of interest. Use the <a href="https://msdn.microsoft.com/8bbb46a8-2bba-4d15-a2e2-4770b52d2505">OpenPrinter</a>, <a href="gdi.openprinter2">OpenPrinter2</a>, or the <a href="gdi.addprinter">AddPrinter</a> function to retrieve a printer handle. 



### -param JobId [in]

Identifier that specifies the print job. You obtain a print job identifier by calling the <a href="gdi.addjob">AddJob</a> function or the <a href="print.oemstartdoc">StartDoc</a> function. 



### -param pszName [in]

Name of the property that will be deleted. 



## -returns
If the operation succeeds, the function returns <b>ERROR_SUCCESS.</b>


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Winspool.h (include Winspool.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>WinSpool.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>Spoolss.dll; </dt>
<dt>WinSpool.drv</dt>
</dl>
</td>
</tr>
</table>