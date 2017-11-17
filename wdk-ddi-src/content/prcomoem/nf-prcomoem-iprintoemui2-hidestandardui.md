---
UID: NF.prcomoem.IPrintOemUI2.HideStandardUI
title: IPrintOemUI2::HideStandardUI
author: windows-driver-content
description: The IPrintOemUI2::HideStandardUI method allows a user interface plug-in to specify whether the standard property sheets should be displayed or hidden.
old-location: print\iprintoemui2_hidestandardui.htm
ms.assetid: 144618d0-0d77-487c-a074-8bd9f6030de2
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
req.alt-api: IPrintOemUI2.HideStandardUI
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
ms.keywords: IPrintOemUI2, HideStandardUI, IPrintOemUI2::HideStandardUI
req.iface: IPrintOemUI2
req.product: Windows 10 or later.
---

# IPrintOemUI2::HideStandardUI method



## -description
<p>The <code>IPrintOemUI2::HideStandardUI</code> method allows a user interface plug-in to specify whether the standard property sheets should be displayed or hidden. Beginning with Microsoft Windows XP, this method can be implemented by a Pscript5 user interface plug-in. Beginning with Windows Vista, this method can be implemented by a Unidrv user interface plug-in.</p>


## -syntax

````
HRESULT HideStandardUI(
   DWORD dwMode
);
````


## -parameters
<dl>

### -param <i>dwMode</i> 

<dd>
<p>Specifies which type of property sheet UI -- document property sheet or device property sheet -- to hide. This parameter should be set to one of the following constants, which are defined in printoem.h:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>OEMCUIP_DOCPROP</p>
</td>
<td>
<p>Hide standard document property sheet UI.</p>
</td>
</tr>
<tr>
<td>
<p>OEMCUIP_PRNPROP</p>
</td>
<td>
<p>Hide standard device property sheet UI.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>On success, this method should return S_OK. Otherwise, it should return E_NOTIMPL. See Remarks for additional information.</p>

## -remarks
<p>This method is supported in Windows Vista for Pscript 5 and Unidrv plug-ins, and in Windows XP only for Pscript5 plug-ins.</p>

<p>Within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548548">DrvDocumentPropertySheets</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548542">DrvDevicePropertySheets</a> DDIs when pPSUIInfo--&gt;Reason is set to PROPSHEETUI_REASON_INIT, the driver calls the <code>IPrintOemUI2::HideStandardUI</code> method to ask the UI plug-in about user interface requests. This method can respond in any of four ways: </p>

<p>Hide standard document property sheet UI.</p>

<p>Hide standard device property sheet UI.</p>

<p>Hide all standard property sheet UI.</p>

<p>Do not hide any standard property sheet UI.</p>

<p>The following table summarizes how the <code>IPrintOemUI2::HideStandardUI</code> method would respond in each of these situations.</p>

<p>Hide standard document property sheet UI. The plug-in implements its own document property sheet UI.</p>

<p>If <i>dwMode</i> == OEMCUIP_DOCPROP, return S_OK; otherwise return E_NOTIMPL.</p>

<p>Hide standard device property sheet UI. The plug-in implements its own device property sheet UI.</p>

<p>If <i>dwMode</i> == OEMCUIP_PRNPROP, return S_OK; otherwise return E_NOTIMPL.</p>

<p>Hide all standard property sheet UI. The plug-in implements its own document property sheet and device property sheet UI.</p>

<p>Return S_OK, regardless of the value of <i>dwMode</i>.</p>

<p>Display all standard property sheet UI.</p>

<p>Return E_NOTIMPL, regardless of the value of <i>dwMode</i>.</p>

<p> </p>

<p>If the <code>IPrintOemUI2::HideStandardUI</code> method indicates to the driver that all standard property sheets should be hidden, the driver omits calls to compstui.dll (see <a href="NULL">Pscript Components</a>) to add the standard property sheets. A UI plug-in must implement at least one custom property sheet UI if <code>IPrintOemUI2::HideStandardUI</code> returns S_OK.</p>

<p>When the printer has multiple UI plug-ins installed, the driver calls UI plug-ins in the order they were installed, until one of them returns S_OK, or until all of the UI plug-ins have been called and none of them returned S_OK. The former case indicates to the driver that the standard property sheet UI should be hidden. The latter case indicates to the driver that the standard property sheet UI should be displayed.</p>

<p>This method is supported in Windows Vista for Pscript 5 and Unidrv plug-ins, and in Windows XP only for Pscript5 plug-ins.</p>

<p>Within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548548">DrvDocumentPropertySheets</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548542">DrvDevicePropertySheets</a> DDIs when pPSUIInfo--&gt;Reason is set to PROPSHEETUI_REASON_INIT, the driver calls the <code>IPrintOemUI2::HideStandardUI</code> method to ask the UI plug-in about user interface requests. This method can respond in any of four ways: </p>

<p>Hide standard document property sheet UI.</p>

<p>Hide standard device property sheet UI.</p>

<p>Hide all standard property sheet UI.</p>

<p>Do not hide any standard property sheet UI.</p>

<p>The following table summarizes how the <code>IPrintOemUI2::HideStandardUI</code> method would respond in each of these situations.</p>

<p>Hide standard document property sheet UI. The plug-in implements its own document property sheet UI.</p>

<p>If <i>dwMode</i> == OEMCUIP_DOCPROP, return S_OK; otherwise return E_NOTIMPL.</p>

<p>Hide standard device property sheet UI. The plug-in implements its own device property sheet UI.</p>

<p>If <i>dwMode</i> == OEMCUIP_PRNPROP, return S_OK; otherwise return E_NOTIMPL.</p>

<p>Hide all standard property sheet UI. The plug-in implements its own document property sheet and device property sheet UI.</p>

<p>Return S_OK, regardless of the value of <i>dwMode</i>.</p>

<p>Display all standard property sheet UI.</p>

<p>Return E_NOTIMPL, regardless of the value of <i>dwMode</i>.</p>

<p> </p>

<p>If the <code>IPrintOemUI2::HideStandardUI</code> method indicates to the driver that all standard property sheets should be hidden, the driver omits calls to compstui.dll (see <a href="NULL">Pscript Components</a>) to add the standard property sheets. A UI plug-in must implement at least one custom property sheet UI if <code>IPrintOemUI2::HideStandardUI</code> returns S_OK.</p>

<p>When the printer has multiple UI plug-ins installed, the driver calls UI plug-ins in the order they were installed, until one of them returns S_OK, or until all of the UI plug-ins have been called and none of them returned S_OK. The former case indicates to the driver that the standard property sheet UI should be hidden. The latter case indicates to the driver that the standard property sheet UI should be displayed.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548548">DrvDocumentPropertySheets</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548542">DrvDevicePropertySheets</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemUI2::HideStandardUI method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
