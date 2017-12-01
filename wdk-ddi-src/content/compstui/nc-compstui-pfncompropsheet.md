---
UID: NC.compstui.PFNCOMPROPSHEET
title: PFNCOMPROPSHEET
author: windows-driver-content
description: The ComPropSheet function is supplied by CPSUI and can be called by CPSUI applications (including printer interface DLLs) to build property sheet pages.
old-location: print\compropsheet.htm
old-project: print
ms.assetid: d9654346-1f28-4e02-8f6c-17e37ed09b92
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: POWERSOURCEUPDATEEX, POWERSOURCEUPDATEEX, *PPOWERSOURCEUPDATEEX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: compstui.h
req.include-header: Compstui.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ComPropSheet
req.alt-loc: compstui.h
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
---

# PFNCOMPROPSHEET callback



## -description
<p>The <i>ComPropSheet</i> function is supplied by <a href="https://msdn.microsoft.com/7af3435a-19e0-40a1-9f94-319d9d323856">CPSUI</a> and can be called by CPSUI applications (including printer interface DLLs) to build property sheet pages.</p>


## -prototype

````
PFNCOMPROPSHEET ComPropSheet;

LONG_PTR CALLBACK ComPropSheet(
  _In_ HANDLE hComPropSheet,
  _In_ UINT   Function,
  _In_ LPARAM lParam1,
  _In_ LPARAM lParam2
)
{ ... }
````


## -parameters
<dl>

### -param <i>hComPropSheet</i> [in]

<dd>
<p>Caller-supplied handle to a property sheet <a href="https://msdn.microsoft.com/b4c40c15-df16-4af0-81c8-9e70d26ba598">group parent</a>. For more information, see the following Remarks section.</p>
</dd>

### -param <i>Function</i> [in]

<dd>
<p>Caller-supplied, CPSFUNC_-prefixed <a href="print.compropsheet_function_codes">ComPropSheet function codes</a> specifying the operation to be performed by the <i>ComPropSheet</i> function.</p>
</dd>

### -param <i>lParam1</i> [in]

<dd>
<p>Caller-supplied value that depends on the <i>ComPropSheet</i> function code supplied for <i>Function</i>.</p>
</dd>

### -param <i>lParam2</i> [in]

<dd>
<p>Caller-supplied value that depends on the <i>ComPropSheet</i> function code supplied for <i>Function</i>.</p>
</dd>
</dl>

## -returns
<p>The return value depends on the <a href="print.compropsheet_function_codes">ComPropSheet function code</a> supplied for <i>Function</i>.</p>

## -remarks
<p>When CPSUI calls one of an application's <a href="..\compstui\nc-compstui-pfnpropsheetui.md">PFNPROPSHEETUI</a>-typed functions, it passes a pointer to the <i>ComPropSheet</i> function in a <a href="..\compstui\ns-compstui--propsheetui-info.md">PROPSHEETUI_INFO</a> structure. A <b>PFNPROPSHEETUI</b>-typed function can call the <i>ComPropSheet</i> function to describe property sheet pages to CPSUI.</p>

<p>A <a href="https://msdn.microsoft.com/2a8cf38f-8e27-4e08-9c0f-5d1a4cd854ac">printer interface DLL</a> can call <i>ComPropSheet</i> from within its <a href="..\winddiui\nf-winddiui-drvdocumentpropertysheets.md">DrvDocumentPropertySheets</a> function or its <a href="..\winddiui\nf-winddiui-drvdevicepropertysheets.md">DrvDevicePropertySheets</a> function.</p>

<p>
<a href="https://msdn.microsoft.com/22ac2af6-37d8-4913-95af-9c3dc8576d40">User interface plug-ins</a> for Microsoft's <a href="wdkgloss.u#wdkgloss.unidrv#wdkgloss.unidrv"><i>Unidrv</i></a> and <a href="wdkgloss.p#wdkgloss.pscript#wdkgloss.pscript"><i>Pscript</i></a> drivers can call <i>ComPropSheet</i> from within their <a href="print.iprintoemui_documentpropertysheets">IPrintOemUI::DocumentPropertySheets</a> and <a href="print.iprintoemui_devicepropertysheets">IPrintOemUI::DevicePropertySheets</a> methods.</p>

<p>The <a href="https://msdn.microsoft.com/b4c40c15-df16-4af0-81c8-9e70d26ba598">group parent</a> handle specified for the <i>hComPropSheet</i> parameter can be either of the following:</p>

<p>The handle received in the <i>hComPropSheet</i> member of a <a href="..\compstui\ns-compstui--propsheetui-info.md">PROPSHEETUI_INFO</a> structure.</p>

<p>The handle received as a result of previously calling <i>ComPropSheet</i> with a <a href="print.cpsfunc_insert_psuipage">CPSFUNC_INSERT_PSUIPAGE</a> function code, and specifying PSUIPAGEINSERT_GROUP_PARENT as the <b>Type</b> member for an <a href="..\compstui\ns-compstui--insertpsuipage-info.md">INSERTPSUIPAGE_INFO</a> structure.</p>

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
<dt>Compstui.h (include Compstui.h)</dt>
</dl>
</td>
</tr>
</table>