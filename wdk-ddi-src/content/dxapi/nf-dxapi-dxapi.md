---
UID: NF.dxapi.DxApi
title: DxApi function
author: windows-driver-content
description: The DxApi function accepts commands from the hardware decoder's video capture driver to access the DxApi interface functions that are implemented in a video miniport driver.
old-location: display\dxapi.htm
old-project: display
ms.assetid: c4b38376-b54f-4fbb-b305-5951a1ea76a1
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: DxApi
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dxapi.h
req.include-header: Ddkmapi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxApi
req.alt-loc: Dxapi.lib,Dxapi.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Dxapi.lib
req.dll: 
req.irql: 
---

# DxApi function



## -description
The <b>DxApi</b> function accepts commands from the hardware decoder's video capture driver to access the <a href="display.dxapi_functions">DxApi interface functions</a> that are implemented in a <a href="https://msdn.microsoft.com/3a540bfe-f340-4f12-acee-323b97683074">video miniport driver</a>.


## -syntax

````
DWORD DxApi(
   DWORD  dwFunctionNum,
   LPVOID lpvInBuffer,
   DWORD  cbInBuffer,
   LPVOID lpvOutBuffer,
   DWORD  cbOutBuffer
);
````


## -parameters

### -param dwFunctionNum 

Indicates the behavior of the <b>DxApi</b> function (function identifier). See the Remarks section for the list of function identifiers.

### -param lpvInBuffer 

Points to the input buffer.

### -param cbInBuffer 

Indicates the size in bytes of the input buffer.

### -param lpvOutBuffer 

Points to the output buffer.

### -param cbOutBuffer 

Indicates the size in bytes of the output buffer.

## -returns
<b>DxApi</b> returns the number of bytes actually written to the output buffer.

## -remarks
<b>DxApi</b> accepts a function identifier (<i>dwFunctionNum</i>), an input buffer (<i>lpvInBuffer</i>) and its size (<i>cbInBuffer</i>), and an output buffer (<i>lpvOutBuffer</i>) and its size (<i>cbOutBuffer</i>). The behavior of the function and the size and format of the input and output buffers depend on the specified function identifier. The return value is the number of actual bytes written into the output buffer.

The following function identifiers are defined for the <b>DxApi</b> function in the <i>ddkmapi.h</i> header file: 


<a href="display.dd_dxapi_addvpcapturebuffer">DD_DXAPI_ADDVPCAPTUREBUFFER</a>



<a href="display.dd_dxapi_closehandle">DD_DXAPI_CLOSEHANDLE</a>



<a href="display.dd_dxapi_flip_overlay">DD_DXAPI_FLIP_OVERLAY</a>



<a href="display.dd_dxapi_flip_vp">DD_DXAPI_FLIP_VP</a>



<a href="display.dd_dxapi_flushvpcapturebuffers">DD_DXAPI_FLUSHVPCAPTUREBUFFERS</a>



<a href="display.dd_dxapi_get_current_vp_autoflip_surface">DD_DXAPI_GET_CURRENT_VP_AUTOFLIP_SURFACE</a>



<a href="display.dd_dxapi_get_last_vp_autoflip_surface">DD_DXAPI_GET_LAST_VP_AUTOFLIP_SURFACE</a>



<a href="display.dd_dxapi_get_polarity">DD_DXAPI_GET_POLARITY</a>



<a href="display.dd_dxapi_get_surface_state">DD_DXAPI_GET_SURFACE_STATE</a>



<a href="display.dd_dxapi_get_vp_field_number">DD_DXAPI_GET_VP_FIELD_NUMBER</a>



<a href="display.dd_dxapi_getkernelcaps">DD_DXAPI_GETKERNELCAPS</a>



<a href="display.dd_dxapi_getversionnumber">DD_DXAPI_GETVERSIONNUMBER</a>



<a href="display.dd_dxapi_lock">DD_DXAPI_LOCK</a>



<a href="display.dd_dxapi_opendirectdraw">DD_DXAPI_OPENDIRECTDRAW</a>



<a href="display.dd_dxapi_opensurface">DD_DXAPI_OPENSURFACE</a>



<a href="display.dd_dxapi_openvideoport">DD_DXAPI_OPENVIDEOPORT</a>



<a href="display.dd_dxapi_openvpcapturedevice">DD_DXAPI_OPENVPCAPTUREDEVICE</a>



<a href="display.dd_dxapi_register_callback">DD_DXAPI_REGISTER_CALLBACK</a>



<a href="display.dd_dxapi_set_surface_state">DD_DXAPI_SET_SURFACE_STATE</a>



<a href="display.dd_dxapi_set_vp_field_number">DD_DXAPI_SET_VP_FIELD_NUMBER</a>



<a href="display.dd_dxapi_set_vp_skip_field">DD_DXAPI_SET_VP_SKIP_FIELD</a>



<a href="display.dd_dxapi_unregister_callback">DD_DXAPI_UNREGISTER_CALLBACK</a>


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
Header
</th>
<td width="70%">
<dl>
<dt>Dxapi.h (include Ddkmapi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Dxapi.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dd_dxapi_addvpcapturebuffer">DD_DXAPI_ADDVPCAPTUREBUFFER</a>
</dt>
<dt>
<a href="display.dd_dxapi_closehandle">DD_DXAPI_CLOSEHANDLE</a>
</dt>
<dt>
<a href="display.dd_dxapi_flip_overlay">DD_DXAPI_FLIP_OVERLAY</a>
</dt>
<dt>
<a href="display.dd_dxapi_flip_vp">DD_DXAPI_FLIP_VP</a>
</dt>
<dt>
<a href="display.dd_dxapi_flushvpcapturebuffers">DD_DXAPI_FLUSHVPCAPTUREBUFFERS</a>
</dt>
<dt>
<a href="display.dd_dxapi_get_current_vp_autoflip_surface">DD_DXAPI_GET_CURRENT_VP_AUTOFLIP_SURFACE</a>
</dt>
<dt>
<a href="display.dd_dxapi_get_last_vp_autoflip_surface">DD_DXAPI_GET_LAST_VP_AUTOFLIP_SURFACE</a>
</dt>
<dt>
<a href="display.dd_dxapi_get_polarity">DD_DXAPI_GET_POLARITY</a>
</dt>
<dt>
<a href="display.dd_dxapi_get_surface_state">DD_DXAPI_GET_SURFACE_STATE</a>
</dt>
<dt>
<a href="display.dd_dxapi_get_vp_field_number">DD_DXAPI_GET_VP_FIELD_NUMBER</a>
</dt>
<dt>
<a href="display.dd_dxapi_getkernelcaps">DD_DXAPI_GETKERNELCAPS</a>
</dt>
<dt>
<a href="display.dd_dxapi_getversionnumber">DD_DXAPI_GETVERSIONNUMBER</a>
</dt>
<dt>
<a href="display.dd_dxapi_lock">DD_DXAPI_LOCK</a>
</dt>
<dt>
<a href="display.dd_dxapi_opendirectdraw">DD_DXAPI_OPENDIRECTDRAW</a>
</dt>
<dt>
<a href="display.dd_dxapi_opensurface">DD_DXAPI_OPENSURFACE</a>
</dt>
<dt>
<a href="display.dd_dxapi_openvideoport">DD_DXAPI_OPENVIDEOPORT</a>
</dt>
<dt>
<a href="display.dd_dxapi_openvpcapturedevice">DD_DXAPI_OPENVPCAPTUREDEVICE</a>
</dt>
<dt>
<a href="display.dd_dxapi_register_callback">DD_DXAPI_REGISTER_CALLBACK</a>
</dt>
<dt>
<a href="display.dd_dxapi_set_surface_state">DD_DXAPI_SET_SURFACE_STATE</a>
</dt>
<dt>
<a href="display.dd_dxapi_set_vp_field_number">DD_DXAPI_SET_VP_FIELD_NUMBER</a>
</dt>
<dt>
<a href="display.dd_dxapi_set_vp_skip_field">DD_DXAPI_SET_VP_SKIP_FIELD</a>
</dt>
<dt>
<a href="display.dd_dxapi_unregister_callback">DD_DXAPI_UNREGISTER_CALLBACK</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DxApi function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
