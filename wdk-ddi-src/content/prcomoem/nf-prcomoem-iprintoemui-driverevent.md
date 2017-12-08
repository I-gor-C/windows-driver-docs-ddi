---
UID: NF.prcomoem.IPrintOemUI.DriverEvent
title: IPrintOemUI::DriverEvent
author: windows-driver-content
description: The printer driver's DrvDriverEvent function calls a user interface plug-in's IPrintOemUI::DriverEvent method for additional processing of printer driver events.
old-location: print\iprintoemui_driverevent.htm
old-project: print
ms.assetid: aacddaea-3a6f-4018-92ac-fe4aa2ddabd3
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUI, DriverEvent, IPrintOemUI::DriverEvent
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
req.alt-api: IPrintOemUI.DriverEvent
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

# IPrintOemUI::DriverEvent method



## -description
<p>The printer driver's <a href="..\winddiui\nf-winddiui-drvdriverevent.md">DrvDriverEvent</a> function calls a user interface plug-in's <code>IPrintOemUI::DriverEvent</code> method for additional processing of printer driver events.</p>


## -syntax

````
HRESULT DriverEvent(
   DWORD  dwDriverEvent,
   DWORD  dwLevel,
   LPBYTE pDriverInfo,
   LPARAM lParam
);
````


## -parameters
<dl>

### -param dwDriverEvent 

<dd>
<p>Caller-supplied bit flag indicating the event that has occurred. Valid flags are listed in the following table.</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>DRIVER_EVENT_DELETE</p>
</td>
<td>
<p>The driver is being removed.</p>
</td>
</tr>
<tr>
<td>
<p>DRIVER_EVENT_INITIALIZE</p>
</td>
<td>
<p>The driver has just been installed.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param dwLevel 

<dd>
<p>Caller-supplied value indicating the type of structure pointed to by the <i>pDriverInfo</i> parameter, as indicated in the following table.</p>
<table>
<tr>
<th><i>dwLevel</i> Value</th>
<th>Structure pointed to by <i>pDriverInfo</i></th>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>DRIVER_INFO_1</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>DRIVER_INFO_2</p>
</td>
</tr>
<tr>
<td>
<p>3</p>
</td>
<td>
<p>DRIVER_INFO_3</p>
</td>
</tr>
</table>
<p> </p>
<dl>
<dd>
<p>The DRIVER_INFO_<i>N</i> structures are described in the Microsoft Windows SDK documentation.</p>
</dd>
</dl>
</dd>

### -param pDriverInfo 

<dd>
<p>Caller-supplied pointer to a structure whose type is identified by the <i>dwLevel</i> parameter.</p>
</dd>

### -param lParam 

<dd>
<p>Caller-supplied flags. See the following Remarks section.</p>
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
<p>A user interface plug-in's <code>IPrintOemUI::DriverEvent</code> method performs the same types of operations as the <b>DrvDriverEvent</b> function that is exported by user-mode printer interface DLLs. For information about driver events and how they should be processed, see the description of the <a href="..\winddiui\nf-winddiui-drvdriverevent.md">DrvDriverEvent</a> function.</p>

<p>If you provide a user interface plug-in, the printer driver's <b>DrvDriverEvent</b> function calls the <code>IPrintOemUI::DriverEvent</code> method. The <b>DrvDriverEvent</b> function performs its own processing for the specified event, and then calls the <code>IPrintOemUI::DriverEvent</code> method to handle additional processing of the event.</p>

<p>If <code>IPrintOemUI::DriverEvent</code> methods are exported by multiple user interface plug-ins, the methods are called in the order that the plug-ins are specified for installation.</p>

<p>For more information about creating and installing user interface plug-ins, see <a href="https://msdn.microsoft.com/b7761209-1f6f-4288-af47-4ed855c2e629">Customizing Microsoft's Printer Drivers</a>.</p>

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
<a href="..\winddiui\nf-winddiui-drvdriverevent.md">DrvDriverEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemUI::DriverEvent method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
