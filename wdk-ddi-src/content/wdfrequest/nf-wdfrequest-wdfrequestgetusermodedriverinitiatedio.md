---
UID: NF.wdfrequest.WdfRequestGetUserModeDriverInitiatedIo
title: WdfRequestGetUserModeDriverInitiatedIo
author: windows-driver-content
description: The WdfRequestGetUserModeDriverInitiatedIo method determines whether an I/O request is marked as initiated by a UMDF driver.
old-location: wdf\wdfrequestgetusermodeinitiatedio.htm
old-project: wdf
ms.assetid: 3F2B060F-3818-4BBC-9BF7-7A82128274E0
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfRequestGetUserModeDriverInitiatedIo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.0
req.alt-api: WdfRequestGetUserModeDriverInitiatedIo
req.alt-loc: WUDFx02000.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: WUDFx02000.lib
req.dll: WUDFx02000.dll; TBD
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfRequestGetUserModeDriverInitiatedIo function



## -description
<p class="CCE_Message">[Applies to UMDF only]</p>
<p>The <b>WdfRequestGetUserModeDriverInitiatedIo</b> method determines whether an I/O request is marked as initiated by a UMDF driver.</p>


## -syntax

````
BOOLEAN WdfRequestGetUserModeDriverInitiatedIo(
  _In_ WDFREQUEST Request
);
````


## -parameters
<dl>

### -param Request [in]

<dd>
<p>A handle to a framework request object.</p>
</dd>
</dl>

## -returns
<p>The method returns <b>TRUE</b> if the request is marked as UMDF driver-initiated and <b>FALSE</b> if the request is not marked as UMDF driver-initiated.</p>

## -remarks
<p> This method retrieves the value of the <b>IRP_UM_DRIVER_INITIATED_IO</b> flag in the <b>Flags</b> member of the WDM <a href="..\wdm\ns-wdm--irp.md">IRP</a> structure corresponding to the I/O request.</p>

<p>For more information about using this flag, see <a href="..\wdfrequest\nf-wdfrequest-wdfrequestsetusermodedriverinitiatedio.md">WdfRequestSetUserModeDriverInitiatedIo</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum support</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfrequest.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx02000.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx02000.dll; </dt>
<dt>TBD</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfrequest\nf-wdfrequest-wdfrequestsetusermodedriverinitiatedio.md">WdfRequestSetUserModeDriverInitiatedIo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestGetUserModeDriverInitiatedIo method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
