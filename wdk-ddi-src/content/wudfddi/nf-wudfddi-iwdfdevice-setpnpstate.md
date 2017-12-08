---
UID: NF.wudfddi.IWDFDevice.SetPnpState
title: IWDFDevice::SetPnpState
author: windows-driver-content
description: The SetPnpState method turns on or off (or sets to the default state) the specified Plug and Play (PnP) property of a device.
old-location: wdf\iwdfdevice_setpnpstate.htm
old-project: wdf
ms.assetid: 3bd88ecd-7c7c-4ee9-8eb8-bc5653bd4ed0
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IWDFDevice, SetPnpState, IWDFDevice::SetPnpState
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
req.alt-api: IWDFDevice.SetPnpState
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

# IWDFDevice::SetPnpState method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>SetPnpState</b> method turns on or off (or sets to the default state) the specified Plug and Play (PnP) property of a device.</p>


## -syntax

````
void SetPnpState(
  [in] WDF_PNP_STATE State,
  [in] WDF_TRI_STATE Value
);
````


## -parameters
<dl>

### -param State [in]

<dd>
<p>A <a href="..\wudfddi_types\ne-wudfddi-types--wdf-pnp-state.md">WDF_PNP_STATE</a>-typed value that identifies the PnP property to set.</p>
</dd>

### -param Value [in]

<dd>
<p>A WDF_TRI_STATE-typed value that identifies how to set the PnP property that <i>State</i> specifies. The following table shows the possible values for <i>Value</i>.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>WdfUseDefault</b> (0)</p>
</td>
<td>
<p>Set the PnP property to the default state.</p>
</td>
</tr>
<tr>
<td>
<p><b>WdfFalse</b> (1)</p>
</td>
<td>
<p>Turn off the PnP property.</p>
</td>
</tr>
<tr>
<td>
<p><b>WdfTrue</b> (2)</p>
</td>
<td>
<p>Turn on the PnP property.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Before the state of the PnP property that <b>SetPnpState</b> set can take effect, the driver must call the <a href="wdf.iwdfdevice_commitpnpstate">IWDFDevice::CommitPnpState</a> method.</p>

<p>The following code example shows how to indicate that a device failed as the result of a request.</p>

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
<a href="..\wudfddi\nn-wudfddi-iwdfdevice.md">IWDFDevice</a>
</dt>
<dt>
<a href="wdf.iwdfdevice_commitpnpstate">IWDFDevice::CommitPnpState</a>
</dt>
<dt>
<a href="wdf.iwdfdevice_getpnpstate">IWDFDevice::GetPnpState</a>
</dt>
<dt>
<a href="..\wudfddi_types\ne-wudfddi-types--wdf-pnp-state.md">WDF_PNP_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDevice::SetPnpState method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
