---
UID: NF.wudfusb.IWDFUsbTargetPipe.Reset
title: IWDFUsbTargetPipe::Reset
author: windows-driver-content
description: The Reset method resets the data toggle and clears the stall condition on a USB pipe.
old-location: wdf\iwdfusbtargetpipe_reset.htm
old-project: wdf
ms.assetid: 8d42dd60-a032-4486-87e0-2204e833035b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IWDFUsbTargetPipe, Reset, IWDFUsbTargetPipe::Reset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfusb.h
req.include-header: Wudfusb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFUsbTargetPipe.Reset
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: 
req.iface: IWDFUsbTargetPipe
req.product: Windows 10 or later.
---

# IWDFUsbTargetPipe::Reset method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>Reset</b> method resets the data toggle and clears the stall condition on a USB pipe.</p>


## -syntax

````
HRESULT  Reset();
````


## -parameters


## -returns
<p><b>Reset</b> returns one of the following values:</p><dl>
<dt><b>S_OK </b></dt>
</dl><p>
<a href="wdf.iwdfusbtargetpipe_reset">Reset</a> successfully reset the data toggle and cleared the stall condition. </p><dl>
<dt><b>E_OUTOFMEMORY </b></dt>
</dl><p>
<a href="wdf.iwdfusbtargetpipe_reset">Reset</a> encountered an allocation failure.</p><dl>
<dt><b>An error code that is defined in Winerror.h</b></dt>
</dl><p>This value corresponds to the error code that the WinUsb API returned.</p>

<p> </p>

<p><b>Reset</b> returns one of the following values:</p><dl>
<dt><b>S_OK </b></dt>
</dl><p>
<a href="wdf.iwdfusbtargetpipe_reset">Reset</a> successfully reset the data toggle and cleared the stall condition. </p><dl>
<dt><b>E_OUTOFMEMORY </b></dt>
</dl><p>
<a href="wdf.iwdfusbtargetpipe_reset">Reset</a> encountered an allocation failure.</p><dl>
<dt><b>An error code that is defined in Winerror.h</b></dt>
</dl><p>This value corresponds to the error code that the WinUsb API returned.</p>

<p> </p>

<p><b>Reset</b> returns one of the following values:</p><dl>
<dt><b>S_OK </b></dt>
</dl><p>
<a href="wdf.iwdfusbtargetpipe_reset">Reset</a> successfully reset the data toggle and cleared the stall condition. </p><dl>
<dt><b>E_OUTOFMEMORY </b></dt>
</dl><p>
<a href="wdf.iwdfusbtargetpipe_reset">Reset</a> encountered an allocation failure.</p><dl>
<dt><b>An error code that is defined in Winerror.h</b></dt>
</dl><p>This value corresponds to the error code that the WinUsb API returned.</p>

<p> </p>

## -remarks
<p>The <b>Reset</b> method generates a UMDF request and synchronously sends the request to the I/O target.</p>

<p>For more information about how <b>Reset</b> works, see the <a href="buses.winusb_resetpipe">WinUsb_ResetPipe</a> function.</p>

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
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.5</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfusb.h (include Wudfusb.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wudfusb\nn-wudfusb-iwdfusbtargetpipe.md">IWDFUsbTargetPipe</a>
</dt>
<dt>
<a href="buses.winusb_resetpipe">WinUsb_ResetPipe</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFUsbTargetPipe::Reset method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
