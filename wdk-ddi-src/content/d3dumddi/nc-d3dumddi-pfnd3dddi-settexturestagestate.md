---
UID: NC.d3dumddi.PFND3DDDI_SETTEXTURESTAGESTATE
title: PFND3DDDI_SETTEXTURESTAGESTATE
author: windows-driver-content
description: The SetTextureStageState function updates the state of a texture at a particular stage in a multiple-texture group.
old-location: display\settexturestagestate.htm
old-project: display
ms.assetid: 56b9d7bf-1036-4ad1-a0fb-4d7154b50b27
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetTextureStageState
req.alt-loc: d3dumddi.h
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

# PFND3DDDI_SETTEXTURESTAGESTATE callback



## -description
<p>The <i>SetTextureStageState</i> function updates the state of a texture at a particular stage in a multiple-texture group.</p>


## -prototype

````
PFND3DDDI_SETTEXTURESTAGESTATE SetTextureStageState;

__checkReturn HRESULT APIENTRY SetTextureStageState(
  _In_       HANDLE                      hDevice,
  _In_ const D3DDDIARG_TEXTURESTAGESTATE *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p> A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543389">D3DDDIARG_TEXTURESTAGESTATE</a> structure that describes how to update the texture.</p>
</dd>
</dl>

## -returns
<p><i>SetTextureStageState</i> returns S_OK or an appropriate error result if the texture is not successfully updated.</p>

## -remarks
<p>The user-mode display driver is not required to store colorkey values in its private allocation structure because the Microsoft Direct3D runtime always passes the appropriate colorkeying information in calls to the driver's <i>SetTextureStageState</i> function. For example, the runtime passes the following colorkey information in the indicated members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543389">D3DDDIARG_TEXTURESTAGESTATE</a> structure that is pointed to by <i>pData</i> to perform the indicated colorkey operation: </p>

<p>D3DTSS_TEXTURECOLORKEYVAL in the <b>State</b> member and a colorkey value in the <b>Value</b> member to update the current texture's colorkey</p>

<p>D3DTSS_DISABLETEXTURECOLORKEY in the <b>State</b> member and <b>TRUE</b> in the <b>Value</b> member to disable the current texture's colorkey</p>

<p>The user-mode display driver is not required to store colorkey values in its private allocation structure because the Microsoft Direct3D runtime always passes the appropriate colorkeying information in calls to the driver's <i>SetTextureStageState</i> function. For example, the runtime passes the following colorkey information in the indicated members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543389">D3DDDIARG_TEXTURESTAGESTATE</a> structure that is pointed to by <i>pData</i> to perform the indicated colorkey operation: </p>

<p>D3DTSS_TEXTURECOLORKEYVAL in the <b>State</b> member and a colorkey value in the <b>Value</b> member to update the current texture's colorkey</p>

<p>D3DTSS_DISABLETEXTURECOLORKEY in the <b>State</b> member and <b>TRUE</b> in the <b>Value</b> member to disable the current texture's colorkey</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543389">D3DDDIARG_TEXTURESTAGESTATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544519">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETTEXTURESTAGESTATE callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
