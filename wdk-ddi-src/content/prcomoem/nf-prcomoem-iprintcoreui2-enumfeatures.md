---
UID: NF.prcomoem.IPrintCoreUI2.EnumFeatures
title: IPrintCoreUI2::EnumFeatures
author: windows-driver-content
description: The IPrintCoreUI2::EnumFeatures method enumerates a printer's available features.
old-location: print\iprintcoreui2_enumfeatures.htm
old-project: print
ms.assetid: e5c16b6d-555d-4360-b781-4d22be81ab56
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintCoreUI2, EnumFeatures, IPrintCoreUI2::EnumFeatures
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
req.alt-api: IPrintCoreUI2.EnumFeatures
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

# IPrintCoreUI2::EnumFeatures method



## -description
<p>The <code>IPrintCoreUI2::EnumFeatures</code> method enumerates a printer's available features.</p>


## -syntax

````
HRESULT EnumFeatures(
  [in]  POEMUIOBJ poemuiobj,
  [in]  DWORD     dwFlags,
  [out] PSTR      pmszFeatureList,
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

### -param <i>pmszFeatureList</i> [out]

<dd>
<p>Pointer to a caller-supplied buffer that receives a null-delimited list of feature keywords in MULTI_SZ format. The list is terminated with two null characters.</p>
<p>Set this parameter to <b>NULL</b> to simply query for the size (*<i>pcbNeeded</i>) of the feature list without having the list filled in.</p>
</dd>

### -param <i>cbSize</i> [in]

<dd>
<p>Specifies the size, in bytes, of the buffer pointed to by <i>pmszFeatureList</i>.</p>
</dd>

### -param <i>pcbNeeded</i> [out]

<dd>
<p>Pointer to a memory location that receives the actual size, in bytes, of the feature list.</p>
</dd>
</dl>

## -returns
<p>This method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method succeeded.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>The value in <i>cbSize</i> was smaller than the number of bytes to be written to the output buffer (the buffer pointed to by <i>pmszFeatureList</i>).</p>

<p>The method was called with <i>pmszFeatureList</i> set to <b>NULL</b>.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>The <i>poemuiobj</i> parameter pointed to an invalid context object.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The method failed</p>

<p> </p>

## -remarks
<p>This method is supported only for Windows XP Pscript5 plug-ins, not for Unidrv plug-ins. </p>

<p><a href="wdkgloss.p#wdkgloss.printer-sticky#wdkgloss.printer-sticky"><i>printer-sticky</i></a> features (see <a href="NULL">Replacing Driver-Supplied Property Sheet Pages</a>), such as those that determine installable memory and the presence of optional accessories, are included in the feature keyword list, which appears in the output buffer pointed to by <i>pmszFeatureList</i> when the method returns. For Pscript5, such features have the <b>OpenGroupType</b> feature attribute set to "InstallableOptions". </p>

<p>To reduce the need to make two calls per data access, pass the method an output buffer of a fixed size (1 KB, for example), and then check the function return value. If the method returns S_OK, the buffer already contains the data of interest. If the method returns E_OUTOFMEMORY, the value in *<i>pcbNeeded</i> is the buffer size needed to hold the data of interest. The caller should then allocate a buffer of that larger size and proceed with a second call to the method.</p>

<p>For more information, see <a href="NULL">Using EnumFeatures</a>.</p>

<p>This method is supported only for Windows XP Pscript5 plug-ins, not for Unidrv plug-ins. </p>

<p><a href="wdkgloss.p#wdkgloss.printer-sticky#wdkgloss.printer-sticky"><i>printer-sticky</i></a> features (see <a href="NULL">Replacing Driver-Supplied Property Sheet Pages</a>), such as those that determine installable memory and the presence of optional accessories, are included in the feature keyword list, which appears in the output buffer pointed to by <i>pmszFeatureList</i> when the method returns. For Pscript5, such features have the <b>OpenGroupType</b> feature attribute set to "InstallableOptions". </p>

<p>To reduce the need to make two calls per data access, pass the method an output buffer of a fixed size (1 KB, for example), and then check the function return value. If the method returns S_OK, the buffer already contains the data of interest. If the method returns E_OUTOFMEMORY, the value in *<i>pcbNeeded</i> is the buffer size needed to hold the data of interest. The caller should then allocate a buffer of that larger size and proceed with a second call to the method.</p>

<p>For more information, see <a href="NULL">Using EnumFeatures</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553052">IPrintCoreUI2::EnumOptions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintCoreUI2::EnumFeatures method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
