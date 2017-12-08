---
UID: NF.prcomoem.IPrintCoreUI2.SetOptions
title: IPrintCoreUI2::SetOptions
author: windows-driver-content
description: The IPrintCoreUI2::SetOptions method sets the driver's feature settings.
old-location: print\iprintcoreui2_setoptions.htm
old-project: print
ms.assetid: b608e331-6b13-4b27-8bb1-00a7c2fef281
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintCoreUI2, SetOptions, IPrintCoreUI2::SetOptions
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
req.alt-api: IPrintCoreUI2.SetOptions
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

# IPrintCoreUI2::SetOptions method



## -description
<p>The <code>IPrintCoreUI2::SetOptions</code> method sets the driver's feature settings.</p>


## -syntax

````
HRESULT SetOptions(
  [in]  POEMUIOBJ poemuiobj,
  [in]  DWORD     dwFlags,
  [in]  PCSTR     pmszFeatureOptionBuf,
  [in]  DWORD     cbIn,
  [out] PDWORD    pdwResult
);
````


## -parameters
<dl>

### -param poemuiobj [in]

<dd>
<p>Pointer to the current context, an <a href="..\printoem\ns-printoem--oemuiobj.md">OEMUIOBJ</a> structure.</p>
</dd>

### -param dwFlags [in]

<dd>
<p>Specifies whether the core driver is to resolve conflicts. This parameter must be set to one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>SETOPTIONS_FLAG_KEEP_CONFLICT</p>
</td>
<td>
<p>Ask core driver to not resolve any conflict that arises.</p>
</td>
</tr>
<tr>
<td>
<p>SETOPTIONS_FLAG_RESOLVE_CONFLICT</p>
</td>
<td>
<p>Ask core driver to resolve any conflict that arises.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param pmszFeatureOptionBuf [in]

<dd>
<p>Pointer to a caller-supplied buffer containing a list of feature/option keyword pairs in MULTI_SZ format. Each item in this list is separated from the next by a null character, and the list is terminated with two null characters.</p>
</dd>

### -param cbIn [in]

<dd>
<p>Specifies the size, in bytes, of the buffer pointed to by <i>pmszFeatureOptionBuf</i>. This size includes the last MULTI_SZ null character.</p>
</dd>

### -param pdwResult [out]

<dd>
<p>Pointer to a memory location that receives one of the following values. These constants are defined in printoem.h.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>SETOPTIONS_RESULT_CONFLICT_REMAINED</p>
</td>
<td>
<p>The core driver found conflicts, but has left them unresolved.</p>
</td>
</tr>
<tr>
<td>
<p>SETOPTIONS_RESULT_CONFLICT_RESOLVED</p>
</td>
<td>
<p>The core driver found and resolved all conflicts.</p>
</td>
</tr>
<tr>
<td>
<p>SETOPTIONS_RESULT_NO_CONFLICT</p>
</td>
<td>
<p>The core driver did not find any conflict.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>The method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method succeeded.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not supported.</p>

<p>A structure of the type specified by <i>dwLevel</i> is not supported.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>The value in <i>dwFlags</i> was incorrect.</p>

<p>The input buffer (pointed to by <i>pmszFeatureOptionBuf</i>) was not in MULTI_SZ format.</p>

<p>The <i>poemuiobj</i> parameter pointed to an invalid context object.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The method failed</p>

<p> </p>

## -remarks
<p>This method is supported only for Windows XP Pscript5 plug-ins, not for Unidrv plug-ins.</p>

<p>This method is called to set the driver's feature settings using a list of feature/option keyword pairs. The caller can access the resultant feature settings using the <a href="print.iprintcoreui2_getoptions">IPrintCoreUI2::GetOptions</a> method. </p>

<p>If this method returns any value other than S_OK, then it did not make any change in the driver's feature settings.</p>

<p>The <i>pmszFeatureOptionBuf</i> input buffer must be constructed in the same way as the output buffer of the <b>IPrintCoreUI2::GetOptions</b> method. That is, the feature/option keyword pairs must be in MULTI_SZ format, and each item in the list is separated from the next by a null character. A pair of null characters terminates the list.</p>

<p>If the input buffer contains a feature keyword or its option keyword that is not recognized, or the feature is recognized but not supported in the current sticky mode (see <a href="https://msdn.microsoft.com/b7f79841-f82c-4a60-9c2f-58772a65a5eb">Replacing Driver-Supplied Property Sheet Pages</a>), then the feature/option pair is ignored, and the current option for that feature continues to be in effect.</p>

<p>This method is supported only for UI plug-ins that fully replace the core driver's standard UI pages, and is supported only during the UI plug-in's <a href="print.iprintoemui_documentpropertysheets">IPrintOemUI::DocumentPropertySheets</a> and <a href="print.iprintoemui_devicepropertysheets">IPrintOemUI::DevicePropertySheets</a> functions, and their property sheet callback routines.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/c8b5c235-0b74-47c8-b6ba-eba810a8467b">Using GetOptions and SetOptions</a>.</p>

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
<a href="..\printoem\ns-printoem--oemuiobj.md">OEMUIOBJ</a>
</dt>
<dt>
<a href="print.iprintoemui_documentpropertysheets">IPrintOemUI::DocumentPropertySheets</a>
</dt>
<dt>
<a href="print.iprintoemui_devicepropertysheets">IPrintOemUI::DevicePropertySheets</a>
</dt>
<dt>
<a href="print.iprintcoreui2_getoptions">IPrintCoreUI2::GetOptions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintCoreUI2::SetOptions method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
