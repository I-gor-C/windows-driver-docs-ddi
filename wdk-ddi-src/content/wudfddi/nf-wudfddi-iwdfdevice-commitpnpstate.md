---
UID: NF.wudfddi.IWDFDevice.CommitPnpState
title: IWDFDevice::CommitPnpState
author: windows-driver-content
description: The CommitPnpState method commits the state of the Plug and Play (PnP) property (that is, turns on, turns off, or sets to the default state) that the IWDFDevice::SetPnpState method set.
old-location: wdf\iwdfdevice_commitpnpstate.htm
old-project: wdf
ms.assetid: 650ad98a-81e5-4ec8-b276-a5dc79366652
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFDevice, CommitPnpState, IWDFDevice::CommitPnpState
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFDevice.CommitPnpState
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
req.iface: IWDFDevice
req.product: Windows 10 or later.
---

# IWDFDevice::CommitPnpState method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>CommitPnpState</b> method commits the state of the Plug and Play (PnP) property (that is, turns on, turns off, or sets to the default state) that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558892">IWDFDevice::SetPnpState</a> method set.</p>


## -syntax

````
void CommitPnpState();
````


## -parameters


## -returns
<p>None</p>

<p>None</p>

<p>None</p>

## -remarks
<p>The values of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561434">WDF_PNP_STATE</a> enumeration identify the state of PnP for the device.</p>

<p>For a code example of how to use the <b>CommitPnpState</b> method, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558892">IWDFDevice::SetPnpState</a>.</p>

<p>The values of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561434">WDF_PNP_STATE</a> enumeration identify the state of PnP for the device.</p>

<p>For a code example of how to use the <b>CommitPnpState</b> method, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558892">IWDFDevice::SetPnpState</a>.</p>

<p>The values of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561434">WDF_PNP_STATE</a> enumeration identify the state of PnP for the device.</p>

<p>For a code example of how to use the <b>CommitPnpState</b> method, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558892">IWDFDevice::SetPnpState</a>.</p>

<p>The values of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561434">WDF_PNP_STATE</a> enumeration identify the state of PnP for the device.</p>

<p>For a code example of how to use the <b>CommitPnpState</b> method, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558892">IWDFDevice::SetPnpState</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556917">IWDFDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558892">IWDFDevice::SetPnpState</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561434">WDF_PNP_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDevice::CommitPnpState method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
