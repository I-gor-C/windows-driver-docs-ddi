---
UID: NF.printerextension.IPrinterExtensionManager.DisableEvents
title: IPrinterExtensionManager::DisableEvents
author: windows-driver-content
description: Disallows events to be generated.
old-location: print\iprinterextensionmanager_disableevents.htm
old-project: print
ms.assetid: 3F4C444E-8DFC-478A-B3A9-D9E7D97CF3C4
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrinterExtensionManager, DisableEvents, IPrinterExtensionManager::DisableEvents
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
req.alt-api: IPrinterExtensionManager.DisableEvents
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

# IPrinterExtensionManager::DisableEvents method



## -description
<p>Disallows events to be generated.</p>


## -syntax

````
HRESULT DisableEvents(
    Void
);
````


## -parameters
<dl>

### -param Void 

<dd>
<p>This method has no parameters.</p>
</dd>
</dl>

## -returns
<p>This method returns an <b>HRESULT</b> value.</p>

## -remarks


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
<a href="print.iprinterextensionmanager_enableevents">EnableEvents</a>
</dt>
<dt>
<a href="print.iprinterextensionmanager_interface">IPrinterExtensionManager</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterExtensionManager::DisableEvents method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
