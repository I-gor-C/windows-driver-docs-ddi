---
UID: NF.prcomoem.IPrintOemUI.DevQueryPrintEx
title: IPrintOemUI::DevQueryPrintEx
author: windows-driver-content
description: The IPrintOemUI::DevQueryPrintEx method allows a user interface plug-in to help determine if a print job is printable.
old-location: print\iprintoemui_devqueryprintex.htm
old-project: print
ms.assetid: a1bc9be3-53ec-4506-a409-94a65d7136e1
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUI, DevQueryPrintEx, IPrintOemUI::DevQueryPrintEx
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
req.alt-api: IPrintOemUI.DevQueryPrintEx
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

# IPrintOemUI::DevQueryPrintEx method



## -description
<p>The <code>IPrintOemUI::DevQueryPrintEx</code> method allows a user interface plug-in to help determine if a print job is printable.</p>


## -syntax

````
HRESULT DevQueryPrintEx(
   POEMUIOBJ           poemuiobj,
   PDEVQUERYPRINT_INFO pDQPInfo,
   PDEVMODE            pPublicDM,
   PVOID               pOEMDM
);
````


## -parameters
<dl>

### -param <i>poemuiobj</i> 

<dd>
<p>Caller-supplied pointer to an <a href="..\printoem\ns-printoem--oemuiobj.md">OEMUIOBJ</a> structure.</p>
</dd>

### -param <i>pDQPInfo</i> 

<dd>
<p>Caller-supplied pointer to a <a href="..\winddiui\ns-winddiui--devqueryprint-info.md">DEVQUERYPRINT_INFO</a> structure.</p>
</dd>

### -param <i>pPublicDM</i> 

<dd>
<p>Caller-supplied pointer to a validated <a href="display.devmodew">DEVMODEW</a> structure.</p>
</dd>

### -param <i>pOEMDM</i> 

<dd>
<p>Caller-supplied pointer to the user interface plug-in's private DEVMODEW structure members.</p>
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
<p>A user interface plug-in's <code>IPrintOemUI::DevQueryPrintEx</code> method performs the same types of operations as the <a href="..\winddiui\nf-winddiui-devqueryprintex.md">DevQueryPrintEx</a> function that is exported by user-mode printer interface DLLs. You can use this method to enhance the functionality provided by the <b>DevQueryPrintEx</b> function. Like the <b>DevQueryPrintEx</b> function, the <code>IPrintOemUI::DevQueryPrintEx</code> method's responsibility is to determine if the print job described by the supplied DEVMODEW structure can be printed.</p>

<p>When the driver's <b>DevQueryPrintEx</b> function is called, it checks the DEVMODEW structure, along with the currently selected printer options, to determine if the job is printable. If it is not, the function returns <b>FALSE</b>. If the job appears to be printable, the function calls the <code>IPrintOemUI::DevQueryPrintEx</code> method in each user interface plug-in associated with the driver. If all <code>IPrintOemUI::DevQueryPrintEx</code> methods return S_OK, then <b>DevQueryPrintEx</b> returns <b>TRUE</b>. Thus, a job is not printable unless the <b>DevQueryPrintEx</b> function and all <code>IPrintOemUI::DevQueryPrintEx</code> methods declare it to be printable.</p>

<p>If <code>IPrintOemUI::DevQueryPrintEx</code> methods are exported by multiple user interface plug-ins, the methods are called in the order that the plug-ins are specified for installation.</p>

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
<a href="..\winddiui\nf-winddiui-devqueryprintex.md">DevQueryPrintEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemUI::DevQueryPrintEx method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
