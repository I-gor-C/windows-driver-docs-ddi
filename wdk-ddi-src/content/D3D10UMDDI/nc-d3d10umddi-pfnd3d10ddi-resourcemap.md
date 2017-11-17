---
UID: NC.d3d10umddi.PFND3D10DDI_RESOURCEMAP
title: PFND3D10DDI_RESOURCEMAP
author: windows-driver-content
description: The ResourceMap function maps a subresource of a resource.
old-location: display\resourcemap.htm
ms.assetid: 1310a3f8-02dd-4d35-98ad-4016e57d1eb2
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ResourceMap
req.alt-loc: d3d10umddi.h
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
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
req.iface: 
---

# PFND3D10DDI_RESOURCEMAP callback



## -description
<p>The <i>ResourceMap</i> function maps a subresource of a resource.</p>


## -prototype

````
PFND3D10DDI_RESOURCEMAP ResourceMap;

VOID APIENTRY ResourceMap(
  _In_  D3D10DDI_HDEVICE            hDevice,
  _In_  D3D10DDI_HRESOURCE          hResource,
  _In_  UINT                        Subresource,
  _In_  D3D10_DDI_MAP               DDIMap,
  _In_  UINT                        Flags,
  _Out_ D3D10DDI_MAPPED_SUBRESOURCE *pMappedSubResource
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>hResource</i> [in]

<dd>
<p> A handle to the resource to map.</p>
</dd>

### -param <i>Subresource</i> [in]

<dd>
<p> An index that indicates the subresource to map. </p>
</dd>

### -param <i>DDIMap</i> [in]

<dd>
<p> A <a href="https://msdn.microsoft.com/library/windows/hardware/ff541957">D3D10_DDI_MAP</a>-typed value that indicates the access level to map the subresource to. </p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p> A <a href="https://msdn.microsoft.com/library/windows/hardware/ff541959">D3D10_DDI_MAP_FLAG</a>-typed value that indicates how to map the subresource. </p>
</dd>

### -param <i>pMappedSubResource</i> [out]

<dd>
<p> A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541839">D3D10DDI_MAPPED_SUBRESOURCE</a> structure that receives the information about the mapped subresource.</p>
</dd>
</dl>

## -returns
<p>None</p>

<p>The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section. </p>

## -remarks
<p>The driver can call <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> to set the D3DDDIERR_DEVICEREMOVED error code.</p>

<p>Typically, immediately after the runtime receives the D3DDDIERR_DEVICEREMOVED error code, the runtime will no longer call into the user-mode display driver for much (other than for unbinding, destruction, and other cleanup operations).  </p>

<p>Typically, each call to the user-mode display driver's <i>ResourceMap</i> function is accompanied with a call to the driver's <a href="https://msdn.microsoft.com/fb2b714e-232d-40b2-88ad-ee8dcd70a057">ResourceUnmap</a> function; however, after the runtime receives the D3DDDIERR_DEVICEREMOVED error code, it will not call <i>ResourceUnmap</i>.</p>

<p>If the runtime passed the D3D10_DDI_MAP_FLAG_DONOTWAIT flag in the <i>Flags</i> parameter, the driver can call <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> to set the DXGI_DDI_ERR_WASSTILLDRAWING error code.</p>

<p>The driver can implement one pair of <i>ResourceMap</i> and <i>ResourceUnmap</i> functions that can contain <b>switch</b> statements to process various functionalities. That is, the driver can implement one <i>ResourceMap</i>-<i>ResourceUnmap</i> pair and can set the following members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a> structure to point to this implementation pair:</p>

<p><b>pfnDynamicIABufferMapDiscard</b>-<b>pfnDynamicIABufferUnmap</b></p>

<p><b>pfnDynamicIABufferMapNoOverwrite</b>-<b>pfnDynamicIABufferUnmap</b></p>

<p><b>pfnDynamicConstantBufferMapDiscard</b>-<b>pfnDynamicConstantBufferUnmap</b></p>

<p><b>pfnDynamicResourceMapDiscard</b>-<b>pfnDynamicResourceUnmap</b></p>

<p><b>pfnStagingResourceMap</b>-<b>pfnStagingResourceUnmap</b></p>

<p>However, to improve performance, the driver can implement separate map-unmap function pairs. The Microsoft Direct3D runtime calls the appropriate map-unmap function pair depending on the resource type (for example, a buffer or texture) and the type of <a href="https://msdn.microsoft.com/library/windows/hardware/ff542008">D3D10_DDI_RESOURCE_USAGE</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff541995">D3D10_DDI_RESOURCE_BIND_FLAG</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff541957">D3D10_DDI_MAP</a> values that are specified when the resource is created and mapped.</p>

<p>The following example code shows the values that are set when the Direct3D runtime calls specific map or unmap function:</p>

<p>For Windows Display Driver Model (WDDM) 1.3 and later drivers, the Microsoft Direct3D runtime supplies a restricted set of input values used by this function. For a list of all restricted values, see <a href="https://msdn.microsoft.com/F9AAE489-EC45-4EE6-875E-E084BB3054EE">Direct3D rendering performance improvements</a>.</p>

<p>The driver can call <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> to set the D3DDDIERR_DEVICEREMOVED error code.</p>

<p>Typically, immediately after the runtime receives the D3DDDIERR_DEVICEREMOVED error code, the runtime will no longer call into the user-mode display driver for much (other than for unbinding, destruction, and other cleanup operations).  </p>

<p>Typically, each call to the user-mode display driver's <i>ResourceMap</i> function is accompanied with a call to the driver's <a href="https://msdn.microsoft.com/fb2b714e-232d-40b2-88ad-ee8dcd70a057">ResourceUnmap</a> function; however, after the runtime receives the D3DDDIERR_DEVICEREMOVED error code, it will not call <i>ResourceUnmap</i>.</p>

<p>If the runtime passed the D3D10_DDI_MAP_FLAG_DONOTWAIT flag in the <i>Flags</i> parameter, the driver can call <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> to set the DXGI_DDI_ERR_WASSTILLDRAWING error code.</p>

<p>The driver can implement one pair of <i>ResourceMap</i> and <i>ResourceUnmap</i> functions that can contain <b>switch</b> statements to process various functionalities. That is, the driver can implement one <i>ResourceMap</i>-<i>ResourceUnmap</i> pair and can set the following members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a> structure to point to this implementation pair:</p>

<p><b>pfnDynamicIABufferMapDiscard</b>-<b>pfnDynamicIABufferUnmap</b></p>

<p><b>pfnDynamicIABufferMapNoOverwrite</b>-<b>pfnDynamicIABufferUnmap</b></p>

<p><b>pfnDynamicConstantBufferMapDiscard</b>-<b>pfnDynamicConstantBufferUnmap</b></p>

<p><b>pfnDynamicResourceMapDiscard</b>-<b>pfnDynamicResourceUnmap</b></p>

<p><b>pfnStagingResourceMap</b>-<b>pfnStagingResourceUnmap</b></p>

<p>However, to improve performance, the driver can implement separate map-unmap function pairs. The Microsoft Direct3D runtime calls the appropriate map-unmap function pair depending on the resource type (for example, a buffer or texture) and the type of <a href="https://msdn.microsoft.com/library/windows/hardware/ff542008">D3D10_DDI_RESOURCE_USAGE</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff541995">D3D10_DDI_RESOURCE_BIND_FLAG</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff541957">D3D10_DDI_MAP</a> values that are specified when the resource is created and mapped.</p>

<p>The following example code shows the values that are set when the Direct3D runtime calls specific map or unmap function:</p>

<p>For Windows Display Driver Model (WDDM) 1.3 and later drivers, the Microsoft Direct3D runtime supplies a restricted set of input values used by this function. For a list of all restricted values, see <a href="https://msdn.microsoft.com/F9AAE489-EC45-4EE6-875E-E084BB3054EE">Direct3D rendering performance improvements</a>.</p>

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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541957">D3D10_DDI_MAP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541959">D3D10_DDI_MAP_FLAG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541995">D3D10_DDI_RESOURCE_BIND_FLAG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542008">D3D10_DDI_RESOURCE_USAGE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541839">D3D10DDI_MAPPED_SUBRESOURCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fb2b714e-232d-40b2-88ad-ee8dcd70a057">ResourceUnmap</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D10DDI_RESOURCEMAP callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
