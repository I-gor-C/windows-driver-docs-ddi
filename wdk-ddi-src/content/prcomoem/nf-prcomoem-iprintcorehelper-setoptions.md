---
UID: NF.prcomoem.IPrintCoreHelper.SetOptions
title: IPrintCoreHelper::SetOptions
author: windows-driver-content
description: The IPrintCoreHelper::SetOptions method sets multiple feature-option pairs at the same time.
old-location: print\iprintcorehelper_setoptions.htm
old-project: print
ms.assetid: 0441558c-db3d-46d1-a251-a32e98098e9e
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintCoreHelper, SetOptions, IPrintCoreHelper::SetOptions
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
req.alt-api: IPrintCoreHelper.SetOptions
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
req.iface: IPrintCoreHelper
req.product: Windows 10 or later.
---

# IPrintCoreHelper::SetOptions method



## -description
<p>The <b>IPrintCoreHelper::SetOptions</b> method sets multiple feature-option pairs at the same time.</p>


## -syntax

````
STDMETHOD  SetOptions(
  [in, optional] PDEVMODE                   pDevmode,
  [in]           DWORD                      cbSize,
  [in]           BOOL                       bResolveConflicts,
  [in]           CONST PRINT_FEATURE_OPTION pFOPairs[],
  [in]           DWORD                      cPairs,
  [out]          PDWORD                     pcPairsWritten,
  [out]          PDWORD                     pdwResult
);
````


## -parameters
<dl>

### -param pDevmode [in, optional]

<dd>
<p>A pointer to a <a href="display.devmodew">DEVMODEW</a> structure. If this pointer is provided, <b>IPrintCoreHelper::SetOptions</b> should use the DEVMODEW structure that is pointed to by <i>pDevmode</i> instead of the default or current DEVMODEW structure. If this method is called from the plug-in provider or from either <a href="print.iprintoemps_devmode">IPrintOemPS::DevMode</a> or <a href="print.iprintoemuni_devmode">IPrintOemUni::DevMode</a>, this parameter is required. In most other situations, the parameter should be <b>NULL</b>. When the core driver sets <i>pDevmode</i> to <b>NULL</b>, it modifies its internal state rather than that of the passed-in DEVMODEW structure. This is required during operations such as full UI replacement, where the DEVMODEW structure returned by a DDI, such as <a href="..\winddiui\nf-winddiui-drvdocumentpropertysheets.md">DrvDocumentPropertySheets</a>, is being serviced by the core driver's UI module.</p>
</dd>

### -param cbSize [in]

<dd>
<p>The size, in bytes, of the DEVMODEW structure that is pointed to by the <i>pDevmode</i> parameter. </p>
</dd>

### -param bResolveConflicts [in]

<dd>
<p>A Boolean value that indicates whether <b>IPrintCoreHelper::SetOptions</b> should resolve conflicts that arise from one or more constraints specified in the GPD or PPD view of the configuration file, as well as constraints for functionality implemented by Unidrv or Pscript or the print processor. If <b>TRUE</b>, this method should attempt to resolve the conflict. If <b>FALSE</b>, this method should not attempt to resolve conflicts. For more information, see the Remarks section.</p>
</dd>

### -param pFOPairs[] [in]

<dd>
<p>An array of <a href="..\prcomoem\ns-prcomoem--print-feature-option.md">PRINT_FEATURE_OPTION</a> elements, where each element contains a feature-option pair. Each feature-option pair lists a feature and the option to select for that feature. All settings are applied sequentially. Duplicates are not disallowed, but settings that appear later in the array (that is, at a higher index) override those that appear earlier in the array. </p>
</dd>

### -param cPairs [in]

<dd>
<p>The number of feature-option pairs that are pointed to by the <i>pFOPairs</i> parameter. </p>
</dd>

### -param pcPairsWritten [out]

<dd>
<p>A pointer to a variable that receives the number of feature-option pairs that were successfully saved before <b>IPrintCoreHelper::SetOptions</b> returned or failed. If this method returns successfully, *<i>pcPairsWritten</i> will have the same value as <i>cPairs</i>. If the method fails, *<i>pcPairsWritten</i> can have any value from zero through the value of <i>cPairs</i>. This parameter is optional and can be <b>NULL</b>.</p>
</dd>

### -param pdwResult [out]

<dd>
<p>A pointer to a variable that receives the status of the conflict resolution. The status can be one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>SETOPTIONS_RESULT_NO_CONFLICT</p>
</td>
<td>
<p>No constraint that was specified in the GPD or PPD view of the configuration file was violated, relative to the new setting.</p>
</td>
</tr>
<tr>
<td>
<p>SETOPTIONS_RESULT_CONFLICT_RESOLVED</p>
</td>
<td>
<p>At least one constraint that was specified in the GPD or PPD view of the configuration file was violated, and the caller requested that the method should resolve conflicts. This value results in changed settings with conflicts resolved.</p>
</td>
</tr>
<tr>
<td>
<p>SETOPTIONS_RESULT_CONFLICT_NOT_RESOLVED</p>
</td>
<td>
<p>At least one constraint that was specified in the GPD or PPD view of the configuration file was violated, and the caller requested that the method should not resolve conflicts. The settings do not change, and conflicts remain.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>IPrintCoreHelper::SetOptions</b> should return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>One or more of the arguments is invalid, or the feature was not supported.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>Memory for the result array could not be allocated.</p>

<p> </p>

<p>For other failures, the method should return a standard COM error code.</p>

## -remarks
<p><b>IPrintCoreHelper::SetOptions</b> can be used to change multiple settings simultaneously and to resolve constraints after all of the selected options have been set. Changes to options are applied sequentially, starting from the beginning of the <i>pFOPairs</i> array, so if the same feature appears twice in this array, only the last option for the feature will be selected. Changes to options are not committed (that is, saved to the registry) unless the <i>bResolveConflicts</i> parameter is <b>TRUE</b>.</p>

<p>For most scenarios, the <i>bResolveConflicts</i> parameter should be set to <b>TRUE</b>. Set this parameter to <b>FALSE</b> if you want to prompt the user to resolve conflicts.</p>

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
<a href="print.iprintcorehelper_getoption">IPrintCoreHelper::GetOption</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintCoreHelper::SetOptions method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
