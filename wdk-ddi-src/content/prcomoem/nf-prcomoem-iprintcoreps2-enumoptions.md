---
UID: NF.prcomoem.IPrintCorePS2.EnumOptions
title: IPrintCorePS2::EnumOptions
author: windows-driver-content
description: The IPrintCorePS2::EnumOptions method enumerates the available options of a specific feature.
old-location: print\iprintcoreps2_enumoptions.htm
old-project: print
ms.assetid: 2a861450-0bc5-432b-bf5d-9a9761c22ea1
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintCorePS2, EnumOptions, IPrintCorePS2::EnumOptions
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
req.alt-api: IPrintCorePS2.EnumOptions
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
req.iface: IPrintCorePS2
req.product: Windows 10 or later.
---

# IPrintCorePS2::EnumOptions method



## -description
<p>The <code>IPrintCorePS2::EnumOptions</code> method enumerates the available options of a specific feature.</p>


## -syntax

````
HRESULT EnumOptions(
  [in]  PDEVOBJ pdevobj,
  [in]  DWORD   dwFlags,
  [in]  PCSTR   pszFeatureKeyword,
  [out] PSTR    pmszOptionList,
  [in]  DWORD   cbSize,
  [out] PDWORD  pcbNeeded
);
````


## -parameters
<dl>

### -param <i>pdevobj</i> [in]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547573">DEVOBJ</a> structure.</p>
</dd>

### -param <i>dwFlags</i> [in]

<dd>
<p>Is reserved and must be set to zero.</p>
</dd>

### -param <i>pszFeatureKeyword</i> [in]

<dd>
<p>Pointer to a caller-supplied buffer containing an ASCII string, specifying a feature keyword whose options are requested.</p>
</dd>

### -param <i>pmszOptionList</i> [out]

<dd>
<p>Pointer to a caller-supplied buffer that receives a null-delimited list, in MULTI_SZ format, containing the option keywords for the feature keyword pointed to by <i>pszFeatureKeyword</i>. This list is terminated with two null characters. </p>
<p>Set this parameter to <b>NULL</b> to simply query for the size (*<i>pcbNeeded</i>) of the option list without having the list filled in.</p>
</dd>

### -param <i>cbSize</i> [in]

<dd>
<p>Specifies the size, in bytes, of the buffer pointed to by <i>pmszOptionList</i>.</p>
</dd>

### -param <i>pcbNeeded</i> [out]

<dd>
<p>Pointer to a memory location that receives the actual size, in bytes, of the requested data.</p>
</dd>
</dl>

## -returns
<p>This method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method succeeded.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>The value in <i>cbSize</i> was smaller than the number of bytes to be written to the output buffer (the buffer pointed to by <i>pmszOptionList</i>).</p>

<p>The method was called with <i>pmszOptionList</i> set to <b>NULL</b>.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>The string pointed to by <i>pszFeatureKeyword</i> is not a recognized feature.</p>

<p>The <i>pdevobj</i> parameter pointed to an invalid driver context object.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>(Pscript only)</p>

<p>The Pscript5 driver feature is not supported under the current configuration.</p>

<p>The Pscript5 driver feature is supported under the current configuration, but the Pscript5 driver feature's options are not enumerable.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The method failed.</p>

<p> </p>

## -remarks
<p>To reduce the need to make two calls per data access, pass the method an output buffer of a fixed size (1 KB, for example), and then check the function return value. If the method returns S_OK, the buffer already contains the data of interest. If the method returns E_OUTOFMEMORY, the value in *<i>pcbNeeded</i> is the buffer size needed to hold the data of interest. The caller should then allocate a buffer of that larger size and proceed with a second call to the method.</p>

<p>This method is supported for any Pscript5 render plug-in.</p>

<p>For more information, see <a href="NULL">Using EnumOptions</a>.</p>

<p>To reduce the need to make two calls per data access, pass the method an output buffer of a fixed size (1 KB, for example), and then check the function return value. If the method returns S_OK, the buffer already contains the data of interest. If the method returns E_OUTOFMEMORY, the value in *<i>pcbNeeded</i> is the buffer size needed to hold the data of interest. The caller should then allocate a buffer of that larger size and proceed with a second call to the method.</p>

<p>This method is supported for any Pscript5 render plug-in.</p>

<p>For more information, see <a href="NULL">Using EnumOptions</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547573">DEVOBJ</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552990">IPrintCorePS2::EnumFeatures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintCorePS2::EnumOptions method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
