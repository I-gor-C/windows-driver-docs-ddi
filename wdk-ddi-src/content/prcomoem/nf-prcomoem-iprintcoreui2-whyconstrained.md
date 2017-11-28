---
UID: NF.prcomoem.IPrintCoreUI2.WhyConstrained
title: IPrintCoreUI2::WhyConstrained
author: windows-driver-content
description: The IPrintCoreUI2::WhyConstrained method determines why the specified feature/option selection is constrained.
old-location: print\iprintcoreui2_whyconstrained.htm
old-project: print
ms.assetid: 3161620e-6155-4587-b978-599d526d792c
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintCoreUI2, WhyConstrained, IPrintCoreUI2::WhyConstrained
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
req.alt-api: IPrintCoreUI2.WhyConstrained
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

# IPrintCoreUI2::WhyConstrained method



## -description
<p>The <code>IPrintCoreUI2::WhyConstrained</code> method determines why the specified feature/option selection is constrained.</p>


## -syntax

````
HRESULT WhyConstrained(
  [in]  POEMUIOBJ poemuiobj,
  [in]  DWORD     dwFlags,
  [in]  PCSTR     pszFeatureKeyword,
  [in]  PCSTR     pszOptionKeyword,
  [out] PSTR      pmszReasonList,
  [in]  DWORD     cbSize,
  [out] PDWORD    pcbNeeded
);
````


## -parameters
<dl>

### -param <i>poemuiobj</i> [in]

<dd>
<p>Pointer to the current context, an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559571">OEMUIOBJ</a> structure.</p>
</dd>

### -param <i>dwFlags</i> [in]

<dd>
<p>Is reserved and must be set to zero.</p>
</dd>

### -param <i>pszFeatureKeyword</i> [in]

<dd>
<p>Pointer to a caller-supplied buffer containing the single feature keyword of interest to the caller.</p>
</dd>

### -param <i>pszOptionKeyword</i> [in]

<dd>
<p>Pointer to a caller-supplied buffer containing the option keyword.</p>
</dd>

### -param <i>pmszReasonList</i> [out]

<dd>
<p>Pointer to a caller-supplied buffer that receives a list of the feature/option keyword pairs that place constraints on the specified feature/option. This list is in MULTI_SZ format with each item in the list separated from the next by a null character. The list is terminated with two null characters.</p>
<p>Set this parameter to <b>NULL</b> to simply query for the size (*<i>pcbNeeded</i>) of the reason list without having the list filled in.</p>
</dd>

### -param <i>cbSize</i> [in]

<dd>
<p>Specifies the size, in bytes, of the buffer pointed to by <i>pmszReasonList</i>.</p>
</dd>

### -param <i>pcbNeeded</i> [out]

<dd>
<p>Pointer to a memory location that receives the actual size, in bytes, of the reason list.</p>
</dd>
</dl>

## -returns
<p>The method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method succeeded.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>The value in <i>cbSize</i> was smaller than the number of bytes to be written to the output buffer (the buffer pointed to by <i>pmszReasonList</i>).</p>

<p>The method was called with <i>pmszReasonList</i> set to <b>NULL</b>.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not supported.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>The <i>poemuiobj</i> parameter pointed to an invalid context object.</p>

<p>The feature keyword or option keyword was not recognized.</p>

<p>The feature stickiness (see <a href="NULL">Replacing Driver-Supplied Property Sheet Pages</a>) did not match that specified in the current context.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The method failed</p>

<p> </p>

## -remarks
<p>This method is supported only for Windows XP Pscript5 UI plug-ins that fully replace the core driver's standard UI pages, and is supported only during the UI plug-in's <a href="https://msdn.microsoft.com/library/windows/hardware/ff554173">IPrintOemUI::DocumentPropertySheets</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff554165">IPrintOemUI::DevicePropertySheets</a> functions, and their property sheet callback routines. See <a href="NULL">Replacing Driver-Supplied Property Sheet Pages</a> for more information.</p>

<p>When a user of the OEM UI attempts to select an item that is constrained, the caller can use this method to display a message explaining why the item is constrained. When this method returns, <i>pmszReasonList</i> points to a list of one or more feature/option pairs that appear in the current driver settings, but conflict with the selected feature/option keywords. If there were no conflicts, the method should return S_OK, <i>pmszReasonList</i> should be filled in with an empty ASCII string containing only a null character, and *<i>pcbNeeded</i> should be set to 1.</p>

<p>To reduce the need to make two calls per data access, pass the method an output buffer of a fixed size (1 KB, for example), and then check the function return value. If the method returns S_OK, the buffer already contains the data of interest. If the method returns E_OUTOFMEMORY, the value in *<i>pcbNeeded</i> is the buffer size needed to hold the data of interest. The caller should then allocate a buffer of that larger size and proceed with a second call to the method.</p>

<p>This method is supported only for Windows XP Pscript5 UI plug-ins that fully replace the core driver's standard UI pages, and is supported only during the UI plug-in's <a href="https://msdn.microsoft.com/library/windows/hardware/ff554173">IPrintOemUI::DocumentPropertySheets</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff554165">IPrintOemUI::DevicePropertySheets</a> functions, and their property sheet callback routines. See <a href="NULL">Replacing Driver-Supplied Property Sheet Pages</a> for more information.</p>

<p>When a user of the OEM UI attempts to select an item that is constrained, the caller can use this method to display a message explaining why the item is constrained. When this method returns, <i>pmszReasonList</i> points to a list of one or more feature/option pairs that appear in the current driver settings, but conflict with the selected feature/option keywords. If there were no conflicts, the method should return S_OK, <i>pmszReasonList</i> should be filled in with an empty ASCII string containing only a null character, and *<i>pcbNeeded</i> should be set to 1.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559571">OEMUIOBJ</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554173">IPrintOemUI::DocumentPropertySheets</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554165">IPrintOemUI::DevicePropertySheets</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553045">IPrintCoreUI2::EnumConstrainedOptions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintCoreUI2::WhyConstrained method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
