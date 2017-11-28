---
UID: NC.d3d10umddi.PFND3D11_1DDI_CREATEAUTHENTICATEDCHANNEL
title: PFND3D11_1DDI_CREATEAUTHENTICATEDCHANNEL
author: windows-driver-content
description: Creates an authenticated channel object. Implemented by a Windows Display Driver Model (WDDM) 1.2 or later user-mode display driver.
old-location: display\createauthenticatedchannel1.htm
old-project: display
ms.assetid: 90b43bc3-6569-4799-8be3-e4e60f59164f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CreateAuthenticatedChannel
req.alt-loc: D3d10umddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# PFND3D11_1DDI_CREATEAUTHENTICATEDCHANNEL callback



## -description
<p>Creates an authenticated channel object. Implemented by a Windows Display Driver Model (WDDM) 1.2 or later user-mode display driver.</p>


## -prototype

````
PFND3D11_1DDI_CREATEAUTHENTICATEDCHANNEL CreateAuthenticatedChannel;

HRESULT APIENTRY* CreateAuthenticatedChannel(
  _In_ D3D10DDI_HDEVICE                         hDevice,
  _In_ D3D11_1DDIARG_CREATEAUTHENTICATEDCHANNEL *pCreateData,
  _In_ D3D11_1DDI_HAUTHCHANNEL                  hAuthChannel,
  _In_ D3D11_1DDI_HRTAUTHCHANNEL                hRTAuthChannel
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p>A handle to the display device (graphics context).

</p>
</dd>

### -param <i>pCreateData</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406306">D3D11_1DDIARG_CREATEAUTHENTICATEDCHANNEL</a> structure. This structure specifies the attributes of the authenticated channel to be created.</p>
</dd>

### -param <i>hAuthChannel</i> [in]

<dd>
<p>A handle to the driver's private data for the authenticated channel object. For more information, see the Remarks section.</p>
</dd>

### -param <i>hRTAuthChannel</i> [in]

<dd>
<p>A handle to the authenticated channel object that the driver should use when it calls back into the Direct3D runtime.</p>
</dd>
</dl>

## -returns
<p>Returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The authenticated channel was created successfully.</p><dl>
<dt><b>D3DDDIERR_DEVICEREMOVED</b></dt>
</dl><p>The graphics adapter was removed.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>
        Memory was not available to complete the operation.</p>

<p> </p>

## -remarks
<p>The Direct3D runtime calls <i>CreateAuthenticatedChannel(D3D11_1)</i> after it has called the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451604">CalcPrivateAuthenticatedChannelSize</a> to determine the size in bytes for the private data that the driver requires for the authenticated channel object. The runtime allocates the memory for this private data for the driver. The driver uses this memory to store private data that is related to the authentication channel object.</p>

<p>When the runtime  calls <i>CreateAuthenticatedChannel(D3D11_1)</i>, it passes the handle to the private data memory in the <i>hAuthChannel</i> parameter. This handle is actually a pointer to the memory. </p>

<p>The driver must keep track of the handle to the display device that was used to create the authenticated channel. The driver should fail all subsequent calls that use this created authenticated channel, such as <a href="https://msdn.microsoft.com/library/windows/hardware/hh451691">NegotiateAuthenticatedChannelKeyExchange</a>, if the display device that is specified in those calls is different from the display device that was used to create the authenticated channel. 

</p>

<p>The Direct3D runtime calls <i>CreateAuthenticatedChannel(D3D11_1)</i> after it has called the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451604">CalcPrivateAuthenticatedChannelSize</a> to determine the size in bytes for the private data that the driver requires for the authenticated channel object. The runtime allocates the memory for this private data for the driver. The driver uses this memory to store private data that is related to the authentication channel object.</p>

<p>When the runtime  calls <i>CreateAuthenticatedChannel(D3D11_1)</i>, it passes the handle to the private data memory in the <i>hAuthChannel</i> parameter. This handle is actually a pointer to the memory. </p>

<p>The driver must keep track of the handle to the display device that was used to create the authenticated channel. The driver should fail all subsequent calls that use this created authenticated channel, such as <a href="https://msdn.microsoft.com/library/windows/hardware/hh451691">NegotiateAuthenticatedChannelKeyExchange</a>, if the display device that is specified in those calls is different from the display device that was used to create the authenticated channel. 

</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451604">CalcPrivateAuthenticatedChannelSize</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createauthenticatedchannel.md">CreateAuthenticatedChannel(D3D11_1)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451691">NegotiateAuthenticatedChannelKeyExchange</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406306">D3D11_1DDIARG_CREATEAUTHENTICATEDCHANNEL</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_CREATEAUTHENTICATEDCHANNEL callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
