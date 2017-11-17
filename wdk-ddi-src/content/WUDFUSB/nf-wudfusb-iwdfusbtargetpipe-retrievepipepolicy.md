---
UID: NF.wudfusb.IWDFUsbTargetPipe.RetrievePipePolicy
title: IWDFUsbTargetPipe::RetrievePipePolicy
author: windows-driver-content
description: The RetrievePipePolicy method retrieves a WinUsb pipe policy.
old-location: wdf\iwdfusbtargetpipe_retrievepipepolicy.htm
ms.assetid: 578f7633-307e-4cda-b8fe-ae73a095976f
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfusb.h
req.include-header: Wudfusb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFUsbTargetPipe.RetrievePipePolicy
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
ms.keywords: IWDFUsbTargetPipe, RetrievePipePolicy, IWDFUsbTargetPipe::RetrievePipePolicy
req.iface: IWDFUsbTargetPipe
req.product: Windows 10 or later.
---

# IWDFUsbTargetPipe::RetrievePipePolicy method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>RetrievePipePolicy</b> method retrieves a WinUsb pipe policy.</p>


## -syntax

````
HRESULT RetrievePipePolicy(
  [in]      ULONG PolicyType,
  [in, out] ULONG *ValueLength,
  [out]     PVOID Value
);
````


## -parameters
<dl>

### -param <i>PolicyType</i> [in]

<dd>
<p>The type of WinUsb pipe policy that the UMDF driver requests.</p>
</dd>

### -param <i>ValueLength</i> [in, out]

<dd>
<p>A pointer to a variable that, on input, contains the size, in bytes, of the buffer that <b>RetrievePipePolicy</b> supplies for <i>Value</i>. On output, this parameter contains the size that <b>RetrievePipePolicy</b> requires for <i>Value</i>.</p>
</dd>

### -param <i>Value</i> [out]

<dd>
<p>A pointer that receives the buffer that contains the WinUsb pipe policy.</p>
</dd>
</dl>

## -returns
<p><b>RetrievePipePolicy</b> returns one of the following values: </p><dl>
<dt><b>S_OK </b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/578f7633-307e-4cda-b8fe-ae73a095976f">RetrievePipePolicy</a> successfully retrieved the WinUsb pipe policy. </p><dl>
<dt><b>E_OUTOFMEMORY </b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/578f7633-307e-4cda-b8fe-ae73a095976f">RetrievePipePolicy</a> encountered an allocation failure.</p><dl>
<dt><b>An error code that is defined in Winerror.h</b></dt>
</dl><p>This value corresponds to the error code that the WinUsb API returned.</p>

<p> </p>

## -remarks
<p>Pipe policy controls the behavior of the USB pipe (for example, time-outs, handling short packets, and so on).</p>

<p>For more information about valid policy types that a UMDF driver can pass for the <i>PolicyType</i> parameter and values that the framework returns, see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540266">WinUsb_GetPipePolicy</a> function.</p>

<p>For information about the behavior of the pipe policies, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff728833">WinUSB Functions for Pipe Policy Modification</a>.</p>

<p>The <b>RetrievePipePolicy</b> method generates a UMDF request and synchronously sends the request to the I/O target.</p>

<p>Pipe policy controls the behavior of the USB pipe (for example, time-outs, handling short packets, and so on).</p>

<p>For more information about valid policy types that a UMDF driver can pass for the <i>PolicyType</i> parameter and values that the framework returns, see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540266">WinUsb_GetPipePolicy</a> function.</p>

<p>For information about the behavior of the pipe policies, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff728833">WinUSB Functions for Pipe Policy Modification</a>.</p>

<p>The <b>RetrievePipePolicy</b> method generates a UMDF request and synchronously sends the request to the I/O target.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560391">IWDFUsbTargetPipe</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540266">WinUsb_GetPipePolicy</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560421">IWDFUsbTargetPipe::SetPipePolicy</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFUsbTargetPipe::RetrievePipePolicy method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
