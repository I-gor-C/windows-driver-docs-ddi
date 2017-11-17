---
UID: NF.wudfddi.IDriverEntry.OnDeinitialize
title: IDriverEntry::OnDeinitialize
author: windows-driver-content
description: The OnDeinitialize method performs any operations that are necessary before a system unloads a driver.
old-location: wdf\idriverentry_ondeinitialize.htm
ms.assetid: 9366029e-4f8b-4121-ad99-01a5116a7f46
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDriverEntry.OnDeinitialize
req.alt-loc: Wudfddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: IDriverEntry, OnDeinitialize, IDriverEntry::OnDeinitialize
req.iface: IDriverEntry
req.product: Windows 10 or later.
---

# IDriverEntry::OnDeinitialize method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>OnDeinitialize</b> method performs any operations that are necessary before a system unloads a driver.</p>


## -syntax

````
void OnDeinitialize(
  [in] IWDFDriver *pWdfDriver
);
````


## -parameters
<dl>

### -param <i>pWdfDriver</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558893">IWDFDriver</a> interface for the driver object that represents the driver that the system unloads.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The framework creates a new driver object for each driver that is loaded in the driver host process. When a driver is about to be unloaded from the host process, the framework calls <b>OnDeinitialize</b> to notify the driver of the departure and passes the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558893">IWDFDriver</a> interface in the call. The system unloads the driver after <b>OnDeinitialize</b> returns. </p>

<p>The framework creates a new driver object for each driver that is loaded in the driver host process. When a driver is about to be unloaded from the host process, the framework calls <b>OnDeinitialize</b> to notify the driver of the departure and passes the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558893">IWDFDriver</a> interface in the call. The system unloads the driver after <b>OnDeinitialize</b> returns. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554885">IDriverEntry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558893">IWDFDriver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IDriverEntry::OnDeinitialize method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
