---
UID: NF.prcomoem.IPrintCoreUI2.EnumConstrainedOptions
title: IPrintCoreUI2::EnumConstrainedOptions
author: windows-driver-content
description: The IPrintCoreUI2::EnumConstrainedOptions method determines which options of a feature are constrained.
old-location: print\iprintcoreui2_enumconstrainedoptions.htm
old-project: print
ms.assetid: 815a20f4-9bd7-4f8d-8444-545097d1c4b3
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintCoreUI2, EnumConstrainedOptions, IPrintCoreUI2::EnumConstrainedOptions
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
req.alt-api: IPrintCoreUI2.EnumConstrainedOptions
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

# IPrintCoreUI2::EnumConstrainedOptions method



## -description
<p>The <code>IPrintCoreUI2::EnumConstrainedOptions</code> method determines which options of a feature are constrained.</p>


## -syntax

````
HRESULT EnumConstrainedOptions(
  [in]  POEMUIOBJ poemuiobj,
  [in]  DWORD     dwFlags,
  [in]  PCSTR     pszFeatureKeyword,
  [out] PSTR      pmszConstrainedOptionList,
  [in]  DWORD     cbSize,
  [out] PDWORD    pcbNeeded
);
````


## -parameters
<dl>

### -param <i>poemuiobj</i> [in]

<dd>
<p>Pointer to the current context, an <a href="..\printoem\ns-printoem--oemuiobj.md">OEMUIOBJ</a> structure.</p>
</dd>

### -param <i>dwFlags</i> [in]

<dd>
<p>Is reserved and must be set to zero.</p>
</dd>

### -param <i>pszFeatureKeyword</i> [in]

<dd>
<p>Pointer to a caller-supplied buffer containing the single feature keyword of interest to the caller.</p>
</dd>

### -param <i>pmszConstrainedOptionList</i> [out]

<dd>
<p>Pointer to a caller-supplied buffer that receives the list of option keywords, in MULTI_SZ format, for this feature. Each keyword represents an option that is constrained in the current configuration. </p>
<p>Set this parameter to <b>NULL</b> to simply query for the size (*<i>pcbNeeded</i>) of the constrained option list without having the list filled in.</p>
</dd>

### -param <i>cbSize</i> [in]

<dd>
<p>Specifies the size, in bytes, of the buffer pointed to by <i>pmszConstrainedOptionList</i>. </p>
</dd>

### -param <i>pcbNeeded</i> [out]

<dd>
<p>Pointer to a memory location that receives the actual size, in bytes, of the constrained option list.</p>
</dd>
</dl>

## -returns
<p>This method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method succeeded. The method should also return this value if none of the feature's options are constrained. In this case, the method should place one null character into the buffer pointed to by <i>pmszConstrainedOptionList</i>, and should set *<i>pcbNeeded</i> to 1.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>The value in <i>cbSize</i> was smaller than the number of bytes to be written to the output buffer (the buffer pointed to by <i>pmszConstrainedOptionList</i>).</p>

<p>The method was called with <i>pmszConstrainedOptionList</i> set to <b>NULL</b>.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>The string pointed to by <i>pszFeatureKeyword</i> was not a recognized feature.</p>

<p>The <i>poemuiobj</i> parameter pointed to an invalid context object.</p>

<p>The stickiness of the feature did not match that of the context object pointed to by <i>peomuiobj</i>. (See <a href="NULL">Replacing Driver-Supplied Property Sheet Pages</a>.)</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The method failed.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not supported.</p>

<p> </p>

## -remarks
<p>This method is supported only for Windows XP Pscript5 UI plug-ins that fully replace the core driver's standard UI pages, and is supported only during the UI plug-in's <a href="print.iprintoemui_documentpropertysheets">IPrintOemUI::DocumentPropertySheets</a> and <a href="print.iprintoemui_devicepropertysheets">IPrintOemUI::DevicePropertySheets</a> functions, and their property sheet callback routines. See <a href="NULL">Replacing Driver-Supplied Property Sheet Pages</a> for more information.</p>

<p>To reduce the need to make two calls per data access, pass the method an output buffer of a fixed size (1 KB, for example), and then check the function return value. If the method returns S_OK, the buffer already contains the data of interest. If the method returns E_OUTOFMEMORY, the value in *<i>pcbNeeded</i> is the buffer size needed to hold the data of interest. The caller should then allocate a buffer of that larger size and proceed with a second call to the method.</p>

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
<a href="print.iprintcoreui2_whyconstrained">IPrintCoreUI2::WhyConstrained</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintCoreUI2::EnumConstrainedOptions method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
