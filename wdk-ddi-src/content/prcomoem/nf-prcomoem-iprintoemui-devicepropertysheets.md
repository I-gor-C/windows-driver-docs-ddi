---
UID: NF.prcomoem.IPrintOemUI.DevicePropertySheets
title: IPrintOemUI::DevicePropertySheets
author: windows-driver-content
description: The IPrintOemUI::DevicePropertySheets method allows a user interface plug-in to append a new page to a printer device's printer property sheet.
old-location: print\iprintoemui_devicepropertysheets.htm
ms.assetid: 7d782f53-2409-416d-a3be-dad932c440a1
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
req.alt-api: IPrintOemUI.DevicePropertySheets
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
ms.keywords: IPrintOemUI, DevicePropertySheets, IPrintOemUI::DevicePropertySheets
req.iface: IPrintOemUI
req.product: Windows 10 or later.
---

# IPrintOemUI::DevicePropertySheets method



## -description
<p>The <code>IPrintOemUI::DevicePropertySheets</code> method allows a user interface plug-in to append a new page to a printer device's printer property sheet.</p>


## -syntax

````
HRESULT DevicePropertySheets(
   PPROPSHEETUI_INFO pPSUIInfo,
   LPARAM            lParam
);
````


## -parameters
<dl>

### -param <i>pPSUIInfo</i> 

<dd>
<p>Caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561767">PROPSHEETUI_INFO</a> structure.</p>
</dd>

### -param <i>lParam</i> 

<dd>
<p>Caller-supplied value that depends on the reason value in <i>pPSUIInfo</i>--&gt;<b>Reason</b>. The reason value can be one of the following constants, which are defined in compstui.h. For more information about these constants, see the Remarks section and <i>lParam</i> parameter description in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559812">PFNPROPSHEETUI</a> function type.</p>
<p>PROPSHEETUI_REASON_DESTROY</p>
<p>PROPSHEETUI_REASON_GET_ICON</p>
<p>PROPSHEETUI_REASON_GET_INFO_HEADER</p>
<p>PROPSHEETUI_REASON_INIT</p>
<p>PROPSHEETUI_REASON_SET_RESULT</p>
</dd>
</dl>

## -returns
<p>The return value depends on the contents of PROPSHEETUI_INFO structure's <b>Reason</b> member. For more information, see the description of <a href="https://msdn.microsoft.com/library/windows/hardware/ff548542">DrvDevicePropertySheets</a>.</p>

## -remarks
<p>A user interface plug-in's <code>IPrintOemUI::DevicePropertySheets</code> method performs the same types of operations as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548542">DrvDevicePropertySheets</a> function that is exported by user-mode printer interface DLLs. Both functions have the same input parameters.</p>

<p>If you provide a user interface plug-in, the <code>IPrintOemUI::DevicePropertySheets</code> method is called after the driver's <b>DrvDevicePropertySheets</b> function is called.</p>

<p>When <code>IPrintOemUI::DevicePropertySheets</code> is called, the <b>lParamInit</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561767">PROPSHEETUI_INFO</a> structure contains the address of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559576">OEMUIPSPARAM</a> structure.</p>

<p>If you implement this method, you typically also supply a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564313">_CPSUICALLBACK</a>-typed callback function to handle user modifications. This callback function must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff553115">IPrintOemDriverUI::DrvUpdateUISetting</a> to inform the driver when the value associated with a user interface setting has been modified, if the value is stored in the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure (instead of the plug-in's private DEVMODEW members) or in registry keys.</p>

<p>If <code>IPrintOemUI::DevicePropertySheets</code> methods are exported by multiple user interface plug-ins, the methods are called in the order that the plug-ins are specified for installation.</p>

<p>If one user interface plug-in supports several printer models, and if you only want the new page to be displayed for some of those models, the <code>IPrintOemUI::DevicePropertySheets</code> method should just provide a success return value, without actually adding the page, for the models not requiring the page.</p>

<p>For more information about creating and installing user interface plug-ins, see <a href="NULL">Customizing Microsoft's Printer Drivers</a>.</p>

<p>A user interface plug-in's <code>IPrintOemUI::DevicePropertySheets</code> method performs the same types of operations as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548542">DrvDevicePropertySheets</a> function that is exported by user-mode printer interface DLLs. Both functions have the same input parameters.</p>

<p>If you provide a user interface plug-in, the <code>IPrintOemUI::DevicePropertySheets</code> method is called after the driver's <b>DrvDevicePropertySheets</b> function is called.</p>

<p>When <code>IPrintOemUI::DevicePropertySheets</code> is called, the <b>lParamInit</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561767">PROPSHEETUI_INFO</a> structure contains the address of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559576">OEMUIPSPARAM</a> structure.</p>

<p>If you implement this method, you typically also supply a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564313">_CPSUICALLBACK</a>-typed callback function to handle user modifications. This callback function must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff553115">IPrintOemDriverUI::DrvUpdateUISetting</a> to inform the driver when the value associated with a user interface setting has been modified, if the value is stored in the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure (instead of the plug-in's private DEVMODEW members) or in registry keys.</p>

<p>If <code>IPrintOemUI::DevicePropertySheets</code> methods are exported by multiple user interface plug-ins, the methods are called in the order that the plug-ins are specified for installation.</p>

<p>If one user interface plug-in supports several printer models, and if you only want the new page to be displayed for some of those models, the <code>IPrintOemUI::DevicePropertySheets</code> method should just provide a success return value, without actually adding the page, for the models not requiring the page.</p>

<p>For more information about creating and installing user interface plug-ins, see <a href="NULL">Customizing Microsoft's Printer Drivers</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548542">DrvDevicePropertySheets</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554173">IPrintOemUI::DocumentPropertySheets</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559812">PFNPROPSHEETUI</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemUI::DevicePropertySheets method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
