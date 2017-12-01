---
UID: NF.prcomoem.IPrintCoreUI2.QuerySimulationSupport
title: IPrintCoreUI2::QuerySimulationSupport
author: windows-driver-content
description: The IPrintCoreUI2::QuerySimulationSupport method retrieves a spooler simulation capability structure, which indicates the kinds of simulation the spooler supports.
old-location: print\iprintcoreui2_querysimulationsupport.htm
old-project: print
ms.assetid: 0136df19-9491-47ea-9a8f-c9a932646686
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintCoreUI2, QuerySimulationSupport, IPrintCoreUI2::QuerySimulationSupport
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintCoreUI2.QuerySimulationSupport
req.alt-loc: prcomoem.h
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
req.iface: IPrintCoreUI2
req.product: Windows 10 or later.
---

# IPrintCoreUI2::QuerySimulationSupport method



## -description
<p>The <code>IPrintCoreUI2::QuerySimulationSupport</code> method retrieves a spooler simulation capability structure, which indicates the kinds of simulation the spooler supports.</p>


## -syntax

````
HRESULT QuerySimulationSupport(
  [in]  HANDLE hPrinter,
  [in]  DWORD  dwLevel,
  [out] PBYTE  pCaps,
  [in]  DWORD  cbSize,
  [out] PDWORD pcbNeeded
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> [in]

<dd>
<p>Specifies a handle to the printer.</p>
</dd>

### -param <i>dwLevel</i> [in]

<dd>
<p>Specifies the spooler simulation capability structure returned in the buffer pointed to by <i>pCaps</i>. Currently, only level 1 of spooler simulation support is provided.</p>
<table>
<tr>
<th>Value</th>
<th>Spooler Simulation Support Structure</th>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>
<a href="..\printoem\ns-printoem--simulate-caps-1.md">SIMULATE_CAPS_1</a> (defined in printoem.h)</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>pCaps</i> [out]

<dd>
<p>Pointer to the output buffer, which contains a structure of the type indicated by the value in the <i>dwLevel</i> parameter.</p>
</dd>

### -param <i>cbSize</i> [in]

<dd>
<p>Specifies the size, in bytes, of the output buffer, which is pointed to by <i>pCaps</i>.</p>
</dd>

### -param <i>pcbNeeded</i> [out]

<dd>
<p>Specifies the size, in bytes, of the memory needed to store a structure of the type indicated by <i>dwLevel</i>.</p>
</dd>
</dl>

## -returns
<p>The method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method succeeded.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>The value in <i>cbSize</i> was smaller than the number of bytes to be written to the output buffer (the buffer pointed to by <i>pCaps</i>).</p>

<p>The method was called with <i>pCaps</i> set to <b>NULL</b>.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not supported.</p>

<p>A structure of the type specified by <i>dwLevel</i> is not supported.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The method failed</p>

<p> </p>

## -remarks
<p>This method is supported only for Windows XP Pscript5 plug-ins, not for Unidrv plug-ins.</p>

<p>The <code>IPrintCoreUI2::QuerySimulationSupport</code> method stores a spooler simulation capability structure in the buffer pointed to by <i>pCaps</i>. This structure specifies the level of spooler support for "N-up" printing, reverse printing, the maximum number of pages that can be printed, collation, and others.</p>

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
<dt>Prcomoem.h (include Prcomoem.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\printoem\ns-printoem--simulate-caps-1.md">SIMULATE_CAPS_1</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintCoreUI2::QuerySimulationSupport method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
