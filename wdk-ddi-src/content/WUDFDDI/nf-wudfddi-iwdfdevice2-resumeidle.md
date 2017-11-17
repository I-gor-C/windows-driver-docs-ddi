---
UID: NF.wudfddi.IWDFDevice2.ResumeIdle
title: IWDFDevice2::ResumeIdle
author: windows-driver-content
description: The ResumeIdle method informs the framework that the device is not in use and can be placed in a device low-power state if it remains idle.
old-location: wdf\iwdfdevice2_resumeidle.htm
ms.assetid: e821f738-3712-49c2-9026-ff6ddc0381a6
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFDevice2.ResumeIdle
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
req.irql: <= DISPATCH_LEVEL
ms.keywords: IWDFDevice2, ResumeIdle, IWDFDevice2::ResumeIdle
req.iface: IWDFDevice2
req.product: Windows 10 or later.
---

# IWDFDevice2::ResumeIdle method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>ResumeIdle</b> method informs the framework that the device is not in use and can be placed in a device low-power state if it remains idle.</p>


## -syntax

````
void ResumeIdle();
````


## -parameters


## -returns
<p>None.</p>

<p>None.</p>

<p>None.</p>

## -remarks
<p>Every call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff556948">IWDFDevice2::StopIdle</a> must eventually be followed by a call to <b>ResumeIdle</b>, or else the device will never return to a low-power state if it again becomes idle.</p>

<p>For more information about <a href="https://msdn.microsoft.com/1a4907c9-8e3b-4fb6-a7d4-89985e470e48">StopIdle</a> and <b>ResumeIdle</b>, see <a href="wdf.supporting_idle_power_down_in_umdf_drivers">Supporting Idle Power-Down in UMDF-based Drivers</a>.</p>

<p>The following code example obtains the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556918">IWDFDevice2</a> interface and then calls <b>ResumeIdle</b>. </p>

<p>Every call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff556948">IWDFDevice2::StopIdle</a> must eventually be followed by a call to <b>ResumeIdle</b>, or else the device will never return to a low-power state if it again becomes idle.</p>

<p>For more information about <a href="https://msdn.microsoft.com/1a4907c9-8e3b-4fb6-a7d4-89985e470e48">StopIdle</a> and <b>ResumeIdle</b>, see <a href="wdf.supporting_idle_power_down_in_umdf_drivers">Supporting Idle Power-Down in UMDF-based Drivers</a>.</p>

<p>The following code example obtains the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556918">IWDFDevice2</a> interface and then calls <b>ResumeIdle</b>. </p>

<p>Every call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff556948">IWDFDevice2::StopIdle</a> must eventually be followed by a call to <b>ResumeIdle</b>, or else the device will never return to a low-power state if it again becomes idle.</p>

<p>For more information about <a href="https://msdn.microsoft.com/1a4907c9-8e3b-4fb6-a7d4-89985e470e48">StopIdle</a> and <b>ResumeIdle</b>, see <a href="wdf.supporting_idle_power_down_in_umdf_drivers">Supporting Idle Power-Down in UMDF-based Drivers</a>.</p>

<p>The following code example obtains the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556918">IWDFDevice2</a> interface and then calls <b>ResumeIdle</b>. </p>

<p>Every call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff556948">IWDFDevice2::StopIdle</a> must eventually be followed by a call to <b>ResumeIdle</b>, or else the device will never return to a low-power state if it again becomes idle.</p>

<p>For more information about <a href="https://msdn.microsoft.com/1a4907c9-8e3b-4fb6-a7d4-89985e470e48">StopIdle</a> and <b>ResumeIdle</b>, see <a href="wdf.supporting_idle_power_down_in_umdf_drivers">Supporting Idle Power-Down in UMDF-based Drivers</a>.</p>

<p>The following code example obtains the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556918">IWDFDevice2</a> interface and then calls <b>ResumeIdle</b>. </p>

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
<p>1.9</p>
</td>
</tr>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556918">IWDFDevice2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556948">IWDFDevice2::StopIdle</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDevice2::ResumeIdle method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
