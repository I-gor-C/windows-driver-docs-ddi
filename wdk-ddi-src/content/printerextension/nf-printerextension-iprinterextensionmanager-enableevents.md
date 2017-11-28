---
UID: NF.printerextension.IPrinterExtensionManager.EnableEvents
title: IPrinterExtensionManager::EnableEvents
author: windows-driver-content
description: The EnableEvents method allows events to be generated for the specified printer driver until DisableEvents is called.
old-location: print\iprinterextensionmanager_enableevents.htm
old-project: print
ms.assetid: 8DF89C18-10CA-4E8B-8E2A-B373C80F7B39
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrinterExtensionManager, EnableEvents, IPrinterExtensionManager::EnableEvents
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: printerextension.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrinterExtensionManager.EnableEvents
req.alt-loc: Printerextension.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: IPrinterExtensionManager
req.product: Windows 10 or later.
---

# IPrinterExtensionManager::EnableEvents method



## -description
<p>The EnableEvents method allows events to be generated for the specified printer driver until  <a href="https://msdn.microsoft.com/library/windows/hardware/hh406703">DisableEvents</a> is called. </p>


## -syntax

````
HRESULT EnableEvents(
  [in] GUID printerDriverId
);
````


## -parameters
<dl>

### -param <i>printerDriverId</i> [in]

<dd>
<p>The GUID representing the specified driver for which to enable events. This GUID is specified in the INF file, and is also specified by the manifest file directive 'PrinterDriverID'.</p>
</dd>
</dl>

## -returns
<p>This method returns an <b>HRESULT</b> value.</p>

<p>The printer extension should call this method when it is launched so that driver events are generated for it to consume.</p>

## -remarks
<p>In the case of a driver event like, for example, Print Preferences or Printer Notifications, the app is expected to call <b>EnableEvents</b>. But if the app doesn't call <b>EnableEvents</b> within 30s, the print system assumes that a UI was  called but it's not being responsive so a standard UI is displayed instead.</p>

<p>In the case of a driver event like, for example, Print Preferences or Printer Notifications, the app is expected to call <b>EnableEvents</b>. But if the app doesn't call <b>EnableEvents</b> within 30s, the print system assumes that a UI was  called but it's not being responsive so a standard UI is displayed instead.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Printerextension.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="print.iprinterextensionmanager_interface">IPrinterExtensionManager</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterExtensionManager::EnableEvents method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
