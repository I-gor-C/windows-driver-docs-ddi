---
UID: NF.prcomoem.IPrintCoreHelperUni.GetOption
title: IPrintCoreHelperUni::GetOption
author: windows-driver-content
description: The IPrintCoreHelperUni::GetOption method gets a specified option for a given feature.
old-location: print\iprintcorehelperuni_getoption.htm
old-project: print
ms.assetid: 0850ba08-089a-4715-bee4-a44a95e6dee6
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintCoreHelperUni, GetOption, IPrintCoreHelperUni::GetOption
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
req.alt-api: IPrintCoreHelperUni.GetOption
req.alt-loc: Prcomoem.h
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
req.iface: IPrintCoreHelperUni
req.product: Windows 10 or later.
---

# IPrintCoreHelperUni::GetOption method



## -description
<p>The <code>IPrintCoreHelperUni::GetOption</code> method gets a specified option for a given feature.</p>


## -syntax

````
STDMETHOD GetOption(
  [in, optional] CONST DEVMODE *pDevmode,
  [in]           DWORD         cbSize,
  [in]           PCSTR         pszFeatureRequested,
  [out]          PCSTR         *ppszOption
);
````


## -parameters
<dl>

### -param pDevmode [in, optional]

<dd>
<p>A pointer to a <a href="display.devmodew">DEVMODEW</a> structure. If this pointer is provided, <code>IPrintCoreHelperUni::GetOption</code> should use the DEVMODEW structure that is pointed to by <i>pDevmode</i> instead of the default or current DEVMODEW structure. If this method is called from the plug-in provider or from <a href="print.iprintoemuni_devmode">IPrintOemUni::DevMode</a>, this parameter is required. In most other situations, the parameter should be <b>NULL</b>. When the core driver sets <i>pDevmode</i> to <b>NULL</b>, it modifies its internal state rather than that of the passed-in DEVMODEW structure. This is required during operations such as full UI replacement, where the DEVMODEW structure returned by a DDI, such as <a href="..\winddiui\nf-winddiui-drvdocumentpropertysheets.md">DrvDocumentPropertySheets</a>, is being serviced by the core driver's UI module.</p>
</dd>

### -param cbSize [in]

<dd>
<p>The size, in bytes, of the DEVMODEW structure that is pointed to by the <i>pDevmode</i> parameter.</p>
</dd>

### -param pszFeatureRequested [in]

<dd>
<p>A pointer to the ANSI string that contains the name of the feature as it appears in the GPD file.</p>
</dd>

### -param ppszOption [out]

<dd>
<p>A pointer to a variable that contains the address of an ANSI string. When <code>IPrintCoreHelperUni::GetOption</code> returns, the string should contain the keyword for the currently selected option as it appears in the configuration file. The caller should not modify this string and should not free the memory that is associated with this string.</p>
</dd>
</dl>

## -returns
<p><code>IPrintCoreHelperUni::GetOption</code> should return one of the following values.</p><dl>
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
<p><code>IPrintCoreHelperUni::GetOption</code> cannot be used for features that allow multiple options to be set simultaneously. </p>

<p>Feature keywords are as defined in the GPD file. In addition, the Unidrv driver supports several reserved keywords for options that are stored in its private <a href="display.devmodew">DEVMODEW</a> structure. For the list of Unidrv features, see <a href="https://msdn.microsoft.com/eb2cbe3c-b516-4db3-92ad-5eafd7181624">Keyword Mapping</a>.</p>

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
<a href="print.iprintcorehelperuni_setoptions">IPrintCoreHelperUni::SetOptions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintCoreHelperUni::GetOption method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
