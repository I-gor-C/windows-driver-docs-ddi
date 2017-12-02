---
UID: NF.prcomoem.IPrintOemUI.UpdateExternalFonts
title: IPrintOemUI::UpdateExternalFonts
author: windows-driver-content
description: The IPrintOemUI::UpdateExternalFonts method allows a user interface plug-in to update a printer's Unidrv Font Format Files (.uff file).
old-location: print\iprintoemui_updateexternalfonts.htm
old-project: print
ms.assetid: 5c501305-fa5f-4466-9a9a-83f072d904b3
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUI, UpdateExternalFonts, IPrintOemUI::UpdateExternalFonts
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
req.alt-api: IPrintOemUI.UpdateExternalFonts
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
req.iface: IPrintOemUI
req.product: Windows 10 or later.
---

# IPrintOemUI::UpdateExternalFonts method



## -description
<p>The <code>IPrintOemUI::UpdateExternalFonts</code> method allows a user interface plug-in to update a printer's <a href="print.customized_font_management#ddk_unidrv_font_format_files_gg#ddk_unidrv_font_format_files_gg">Unidrv Font Format Files</a> (.uff file).</p>


## -syntax

````
HRESULT UpdateExternalFonts(
   HANDLE hPrinter,
   HANDLE hHeap,
   PWSTR  pwstrCartridges
);
````


## -parameters
<dl>

### -param hPrinter 

<dd>
<p>Caller-supplied printer handle.</p>
</dd>

### -param hHeap 

<dd>
<p>Caller-supplied handle to heap memory the method can use for local storage.</p>
</dd>

### -param pwstrCartridges 

<dd>
<p>Caller-supplied pointer to an array of strings representing the names of all cartridges currently installed on the printer.</p>
</dd>
</dl>

## -returns
<p>The method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not implemented.</p>

<p> </p>

## -remarks
<p>A user interface plug-in must implement the <code>IPrintOemUI::UpdateExternalFonts</code> method if the plug-in is replacing Unidrv's default font installer. For more information, see <a href="https://msdn.microsoft.com/d753368d-b1c8-454e-a02b-131dc778e723">Customized Font Installers for Unidrv</a>.</p>

<p>The <code>IPrintOemUI::UpdateExternalFonts</code> method's purpose is to examine the list of installed cartridges (supplied by <i>pwstrCartridges</i>) and ensure that the .uff file specified by the "ExternalFontFile" registry value contains font descriptions for only the cartridge fonts contained in the installed cartridges. (This .uff file can also contain descriptions of <a href="wdkgloss.p#wdkgloss.pcl#wdkgloss.pcl"><i>PCL</i></a>-downloadable soft fonts.)</p>

<p>Descriptions of cartridge fonts can be copied from the .uff file specified by the "ExtFontCartFile" registry value. For more information, see <a href="print.customized_font_management#ddk_unidrv_font_format_files_gg#ddk_unidrv_font_format_files_gg">Unidrv Font Format Files</a>.</p>

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
<a href="print.iprintoemui_fontinstallerdlgproc">IPrintOemUI::FontInstallerDlgProc</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemUI::UpdateExternalFonts method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
