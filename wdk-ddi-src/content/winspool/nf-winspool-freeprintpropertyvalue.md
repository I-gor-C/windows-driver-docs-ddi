---
UID: NF.winspool.FreePrintPropertyValue
title: FreePrintPropertyValue
author: windows-driver-content
description: Frees the value that is retrieved using GetJobNamedPropertyValue function.
old-location: print\freeprintpropertyvalue.htm
ms.assetid: 38B760D9-CB6E-45AD-A83F-3C26D1B31A30
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
req.alt-api: FreePrintPropertyValue
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
ms.keywords: FreePrintPropertyValue
req.iface: 
req.product: Windows 10 or later.
---

# FreePrintPropertyValue function



## -description
<p>Frees the value that is retrieved using <a href="https://msdn.microsoft.com/library/windows/hardware/mt299059">GetJobNamedPropertyValue</a> function. 
</p>


## -syntax

````
DWORD WINAPI FreePrintPropertyValue(
  _Inout_ PrintPropertyValue *pValue
);
````


## -parameters
<dl>

### -param <i>pValue</i> [in, out]

<dd>
<p>Pointer to <b>PrintPropertyValue</b> structure that is returned from <a href="https://msdn.microsoft.com/library/windows/hardware/mt299059">GetJobNamedPropertyValue</a>. 
</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the function returns <b>ERROR_SUCCESS</b>.  
</p>

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