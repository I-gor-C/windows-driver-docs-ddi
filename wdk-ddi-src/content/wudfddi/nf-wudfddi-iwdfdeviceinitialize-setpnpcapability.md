---
UID: NF.wudfddi.IWDFDeviceInitialize.SetPnpCapability
title: IWDFDeviceInitialize::SetPnpCapability method
author: windows-driver-content
description: The SetPnpCapability method sets the specified Plug and Play (PnP) capability of a device to the specified state.
old-location: wdf\iwdfdeviceinitialize_setpnpcapability.htm
old-project: wdf
ms.assetid: 82892740-12f6-469b-a65c-6905d32c0b0d
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IWDFDeviceInitialize, IWDFDeviceInitialize::SetPnpCapability, SetPnpCapability
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFDeviceInitialize.SetPnpCapability
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
req.product: Windows 10 or later.
---

# IWDFDeviceInitialize::SetPnpCapability method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>SetPnpCapability</b> method sets the specified Plug and Play (PnP) capability of a device to the specified state.



## -syntax

````
void SetPnpCapability(
  [in] WDF_PNP_CAPABILITY Capability,
  [in] WDF_TRI_STATE      Value
);
````


## -parameters

### -param Capability [in]

A <a href="wdf.wdf_pnp_capability">WDF_PNP_CAPABILITY</a>-typed value that identifies the PnP capability to set. 


### -param Value [in]

A WDF_TRI_STATE-typed value that identifies how to set the PnP capability that is specified by <i>Capability</i>. The following table shows the possible values.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<b>WdfUseDefault</b> (0)

</td>
<td>
Set the capability to the default state.

</td>
</tr>
<tr>
<td>
<b>WdfFalse</b> (1)

</td>
<td>
Do not set the capability.

</td>
</tr>
<tr>
<td>
<b>WdfTrue</b> (2)

</td>
<td>
Set the capability.

</td>
</tr>
</table>
 


## -returns
None


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
End of support

</th>
<td width="70%">
Unavailable in UMDF 2.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
1.5

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

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
<a href="..\wudfddi\nn-wudfddi-iwdfdeviceinitialize.md">IWDFDeviceInitialize</a>
</dt>
<dt>
<a href="wdf.iwdfdeviceinitialize_getpnpcapability">IWDFDeviceInitialize::GetPnpCapability</a>
</dt>
<dt>
<a href="wdf.wdf_pnp_capability">WDF_PNP_CAPABILITY</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDeviceInitialize::SetPnpCapability method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

