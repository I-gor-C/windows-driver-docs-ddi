---
UID: NF.prcomoem.IPrintCoreHelper.GetOption
title: IPrintCoreHelper::GetOption
author: windows-driver-content
description: The IPrintCoreHelper::GetOption method gets a specified option for a given feature.
old-location: print\iprintcorehelper_getoption.htm
ms.assetid: 515eed09-d386-4908-9d76-4e64930af5ab
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintCoreHelper.GetOption
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
ms.keywords: IPrintCoreHelper, GetOption, IPrintCoreHelper::GetOption
req.iface: IPrintCoreHelper
req.product: Windows 10 or later.
---

# IPrintCoreHelper::GetOption method



## -description
<p>The <b>IPrintCoreHelper::GetOption</b> method gets a specified option for a given feature.</p>


## -syntax

````
HRESULT GetOption(
  [in]  const DEVMODE *pDevmode,
  [in]        DWORD   cbSize,
  [in]        PCSTR   pszFeatureRequested,
  [out]       PCSTR   *ppszOption
);
````


## -parameters
<dl>

### -param <i>pDevmode</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure. If this pointer is provided, <b>IPrintCoreHelper::GetOption</b> should use the DEVMODEW structure that is pointed to by <i>pDevmode</i> instead of the default or current DEVMODEW structure. If this method is called from the plug-in provider or from either <a href="https://msdn.microsoft.com/library/windows/hardware/ff553205">IPrintOemPS::DevMode</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff554230">IPrintOemUni::DevMode</a>, this parameter is required. In most other situations, the parameter should be <b>NULL</b>. When the core driver sets <i>pDevmode</i> to <b>NULL</b>, it modifies its internal state rather than that of the passed-in DEVMODEW structure. This is required during operations such as full UI replacement, where the DEVMODEW structure returned by a DDI, such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff548548">DrvDocumentPropertySheets</a>, is being serviced by the core driver's UI module.</p>
</dd>

### -param <i>cbSize</i> [in]

<dd>
<p>The size, in bytes, of the DEVMODEW structure that is pointed to by the <i>pDevmode</i> parameter.</p>
</dd>

### -param <i>pszFeatureRequested</i> [in]

<dd>
<p>A pointer to the ANSI string that contains the name of the feature as it appears in the GPD file.</p>
</dd>

### -param <i>ppszOption</i> [out]

<dd>
<p>A pointer to a variable that contains the address of an ANSI string. When <b>IPrintCoreHelper::GetOption</b> returns, the string should contain the keyword for the currently selected option as it appears in the configuration file. The caller should not modify this string and should not free the memory that is associated with this string.</p>
</dd>
</dl>

## -returns
<p><b>IPrintCoreHelper::GetOption</b> should return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method read the option for the specified feature.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The caller provided information that resulted in an invalid request. For example, the feature that was requested does not exist.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>The arguments were invalid. This value might mean that the feature is not supported or that too many options were requested for the feature.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>The core driver was not able to service the request because there was insufficient memory.</p><dl>
<dt><b>E_UNEXPECTED, or other return codes not listed here</b></dt>
</dl><p>The core driver seems to be in an invalid state. The caller should return a failure code.</p>

<p> </p>

## -remarks
<p><b>IPrintCoreHelper::GetOption</b> cannot be used for features that allow multiple options to be set simultaneously. </p>

<p>Feature keywords are as defined in the GPD and PPD files. In addition, the Unidrv and Pscript5 drivers support several reserved keywords for options that are stored in their private <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structures. </p>

<p>The caller should not free the string that is pointed to by <i>ppszOption</i> and should not modify the string in any way.</p>

<p><b>IPrintCoreHelper::GetOption</b> cannot be used for features that allow multiple options to be set simultaneously. </p>

<p>Feature keywords are as defined in the GPD and PPD files. In addition, the Unidrv and Pscript5 drivers support several reserved keywords for options that are stored in their private <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structures. </p>

<p>The caller should not free the string that is pointed to by <i>ppszOption</i> and should not modify the string in any way.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552963">IPrintCoreHelper::SetOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552955">IPrintCoreHelper::EnumOptions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintCoreHelper::GetOption method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
