---
UID : NC:d3dumddi.PFND3DDDI_CREATEAUTHENTICATEDCHANNEL
title : PFND3DDDI_CREATEAUTHENTICATEDCHANNEL
author : windows-driver-content
description : The CreateAuthenticatedChannel function creates a channel that the Microsoft Direct3D runtime and the driver can use to set and query protections.
old-location : display\createauthenticatedchannel.htm
old-project : display
ms.assetid : 0a565bff-fc6f-41c1-a6fd-3a82dd0d7889
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXGK_PTE, DXGK_PTE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3dumddi.h
req.include-header : D3dumddi.h
req.target-type : Desktop
req.target-min-winverclnt : CreateAuthenticatedChannel is supported beginning with the Windows 7 operating system.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : CreateAuthenticatedChannel
req.alt-loc : d3dumddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : DXGK_PTE
---


# PFND3DDDI_CREATEAUTHENTICATEDCHANNEL callback function
The <b>CreateAuthenticatedChannel</b> function creates a channel that the Microsoft Direct3D runtime and the driver can use to set and query protections.

## Syntax

```
PFND3DDDI_CREATEAUTHENTICATEDCHANNEL Pfnd3dddiCreateauthenticatedchannel;

HRESULT Pfnd3dddiCreateauthenticatedchannel(
  HANDLE hDevice,
  D3DDDIARG_CREATEAUTHENTICATEDCHANNEL *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`




## Return Value

<b>CreateAuthenticatedChannel</b> returns one of the following values:
<dl>
<dt><b>S_OK</b></dt>
</dl>The channel is successfully created.
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_createauthenticatedchannel.md">CreateAuthenticatedChannel</a> could not allocate the required memory for it to complete.
<dl>
<dt><b>D3DDDIERR_NOTAVAILABLE</b></dt>
</dl>The driver does not support the channel type that is specified in the <b>ChannelType</b> member of the <a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_createauthenicatedchannel.md">D3DDDIARG_CREATEAUTHENTICATEDCHANNEL</a> structure that the <i>pData</i> parameter points to.

## Remarks

The runtime passes the handle to the authenticated channel that the driver returns in the <b>ChannelType</b> member of the <a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_createauthenicatedchannel.md">D3DDDIARG_CREATEAUTHENTICATEDCHANNEL</a> structure in all subsequent calls that require the handle. 

The driver must keep track of the display device (<i>hDevice</i>) that was used to create the authenticated channel. The driver should fail all subsequent calls that use this created authenticated channel (for example, the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_authenticatedchannelkeyexchange.md">AuthenticatedChannelKeyExchange</a> function) if the display device that is specified in those calls is different from the display device that was used to create the authenticated channel.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dumddi.h (include D3dumddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_createauthenicatedchannel.md">D3DDDIARG_CREATEAUTHENTICATEDCHANNEL</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_CREATEAUTHENTICATEDCHANNEL callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>