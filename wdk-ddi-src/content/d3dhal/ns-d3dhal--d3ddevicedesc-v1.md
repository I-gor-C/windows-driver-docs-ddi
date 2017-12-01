---
UID: NS.d3dhal._D3DDeviceDesc_V1
title: D3DDeviceDesc_V1
author: windows-driver-content
description: Obsolete in DirectX 8.0 and later versions; see Remarks. The D3DDEVICEDESC_V1 structure describes the 3D capabilities of a device.
old-location: display\d3ddevicedesc_v1.htm
old-project: display
ms.assetid: 363e4044-e835-43e6-96ce-0fdccdd7fb52
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDeviceDesc_V1, D3DDEVICEDESC_V1, *LPD3DDEVICEDESC_V1
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dhal.h
req.include-header: D3dhal.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDEVICEDESC_V1
req.alt-loc: d3dhal.h
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

# D3DDeviceDesc_V1 structure



## -description
<p>
   Obsolete in DirectX 8.0 and later versions; see Remarks.
   </p>
<p>The D3DDEVICEDESC_V1 structure describes the 3D capabilities of a device.</p>


## -syntax

````
typedef struct _D3DDeviceDesc_V1 {
  DWORD            dwSize;
  DWORD            dwFlags;
  D3DCOLORMODEL    dcmColorModel;
  DWORD            dwDevCaps;
  D3DTRANSFORMCAPS dtcTransformCaps;
  BOOL             bClipping;
  D3DLIGHTINGCAPS  dlcLightingCaps;
  D3DPRIMCAPS      dpcLineCaps;
  D3DPRIMCAPS      dpcTriCaps;
  DWORD            dwDeviceRenderBitDepth;
  DWORD            dwDeviceZBufferBitDepth;
  DWORD            dwMaxBufferSize;
  DWORD            dwMaxVertexCount;
} D3DDEVICEDESC_V1, *LPD3DDEVICEDESC_V1;
````


## -struct-fields
<dl>

### -field <b>dwSize</b>

<dd>
<p>Specifies the size in bytes of this D3DDEVICEDESC_V1 structure.</p>
</dd>

### -field <b>dwFlags</b>

<dd>
<p>Identifies the members of this structure that contain valid data. This member can be a bitwise OR of any of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3DDD_BCLIPPING</p>
</td>
<td>
<p>The <b>bClipping</b> member contains valid data.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDD_COLORMODEL</p>
</td>
<td>
<p>The <b>dcmColorModel</b> member contains valid data.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDD_DEVCAPS</p>
</td>
<td>
<p>The <b>dwDevCaps</b> member contains valid data.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDD_DEVICERENDERBITDEPTH</p>
</td>
<td>
<p>The <b>dwDeviceRenderBitDepth</b> member contains valid data.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDD_DEVICEZBUFFERBITDEPTH</p>
</td>
<td>
<p>The <b>dwDeviceZBufferBitDepth</b> member contains valid data.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDD_LIGHTINGCAPS</p>
</td>
<td>
<p>The <b>dlcLightingCaps</b> member contains valid data.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDD_LINECAPS</p>
</td>
<td>
<p>The <b>dpcLineCaps</b> member contains valid data.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDD_MAXBUFFERSIZE</p>
</td>
<td>
<p>The <b>dwMaxBufferSize</b> member contains valid data.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDD_MAXVERTEXCOUNT</p>
</td>
<td>
<p>The <b>dwMaxVertexCount</b> member contains valid data.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDD_TRANSFORMCAPS</p>
</td>
<td>
<p>The <b>dtcTransformCaps</b> member contains valid data.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDD_TRICAPS</p>
</td>
<td>
<p>The <b>dpcTriCaps</b> member contains valid data.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dcmColorModel</b>

<dd>
<p>Specifies the device's color model. </p>
</dd>

### -field <b>dwDevCaps</b>

<dd>
<p>Identifies the capabilities of the device. This member can be a bitwise OR of any of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3DDEVCAPS_CANBLTSYSTONONLOCAL</p>
</td>
<td>
<p>The device supports a TexBlt from system memory to sublocal video memory.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDEVCAPS_CANRENDERAFTERFLIP</p>
</td>
<td>
<p>The device can queue rendering commands after a page flip. Devices must support this capability on Windows 2000 and later, meaning that the driver would always set this flag.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDEVCAPS_DRAWPRIMITIVES2</p>
</td>
<td>
<p>The device can support <a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDEVCAPS_DRAWPRIMITIVES2EX</p>
</td>
<td>
<p>The device can support Extended <a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>; i.e. a DX7-compliant driver.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDEVCAPS_DRAWPRIMTLVERTEX</p>
</td>
<td>
<p>The device can draw TLVERTEX primitives. This flag is obsolete but must be set by the driver.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDEVCAPS_EXECUTESYSTEMMEMORY</p>
</td>
<td>
<p>The device can use execute buffers from system memory. The driver must always set this bit.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDEVCAPS_EXECUTEVIDEOMEMORY</p>
</td>
<td>
<p>The device can use execute buffers from display memory. The driver must never set this bit.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDEVCAPS_FLOATTLVERTEX</p>
</td>
<td>
<p>The device accepts floating-point for posttransform vertex data. This flag is obsolete but must be set by the driver.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDEVCAPS_HWRASTERIZATION</p>
</td>
<td>
<p>The device has hardware acceleration for rasterization.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDEVCAPS_HWTRANSFORMANDLIGHT</p>
</td>
<td>
<p>The device can support transformation and lighting in hardware. D3DDEVCAPS_DRAWPRIMITIVES2EX must also be set.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDEVCAPS_SEPARATETEXTUREMEMORIES</p>
</td>
<td>
<p>
<dl>

### -field The device is texturing from separate memory pools.


### -field Setting this capability bit indicates to DirectX 8.0 and later versions of applications that they are disabled from simultaneously using multiple textures.

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>D3DDEVCAPS_SORTDECREASINGZ</p>
</td>
<td>
<p>The device needs data sorted for decreasing depth. </p>
</td>
</tr>
<tr>
<td>
<p>D3DDEVCAPS_SORTEXACT</p>
</td>
<td>
<p>The device needs data sorted exactly. </p>
</td>
</tr>
<tr>
<td>
<p>D3DDEVCAPS_SORTINCREASINGZ </p>
</td>
<td>
<p>The device needs data sorted for increasing depth. </p>
</td>
</tr>
<tr>
<td>
<p>D3DDEVCAPS_TEXTURENONLOCALVIDEOMEMORY</p>
</td>
<td>
<p>The device can texture from nonlocal video memory.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDEVCAPS_TLVERTEXSYSTEMMEMORY</p>
</td>
<td>
<p>The device can use buffers from system memory for transformed and lit vertices. This flag is obsolete but must be set by the driver.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDEVCAPS_TLVERTEXVIDEOMEMORY</p>
</td>
<td>
<p>The device can use buffers from display memory for transformed and lit vertices. This flag is obsolete and must not be set by the driver.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDEVCAPS_TEXTURESYSTEMMEMORY</p>
</td>
<td>
<p>The device can retrieve textures from system memory.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDEVCAPS_TEXTUREVIDEOMEMORY</p>
</td>
<td>
<p>The device can retrieve textures from device memory.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dtcTransformCaps</b>

<dd>
<p>Specifies a D3DTRANSFORMCAPS structure that specifies the transformation capabilities of the device. The driver must set the <b>dwCaps</b> member of that structure to zero.</p>
</dd>

### -field <b>bClipping</b>

<dd>
<p>Set to <b>TRUE</b> by the driver if the device can perform 3D clipping. </p>
</dd>

### -field <b>dlcLightingCaps</b>

<dd>
<p>Specifies the lighting capabilities of the device. This is a <a href="..\d3dcaps\ns-d3dcaps--d3dlightingcaps.md">D3DLIGHTINGCAPS</a> structure. The driver must set the <b>dwCaps</b>, <b>dwLightingModel</b>, and <b>dwNumLights</b> members of that structure to zero.</p>
</dd>

### -field <b>dpcLineCaps</b>

<dd>
<p>Specifies a <a href="..\d3dcaps\ns-d3dcaps--d3dprimcaps.md">D3DPRIMCAPS</a> structure that defines the drawing capabilities of the device for line primitives.</p>
</dd>

### -field <b>dpcTriCaps</b>

<dd>
<p>Specifies a <a href="..\d3dcaps\ns-d3dcaps--d3dprimcaps.md">D3DPRIMCAPS</a> structure that defines the drawing capabilities of the device for triangle primitives.</p>
</dd>

### -field <b>dwDeviceRenderBitDepth</b>

<dd>
<p>Specifies the device's rendering bit-depth. This member can be a bitwise OR of the following DirectDraw bit-depth constants: DDBD_8, DDBD_16, DDBD_24, or DDBD_32. </p>
</dd>

### -field <b>dwDeviceZBufferBitDepth</b>

<dd>
<p>Specifies the device's z-buffer bit-depth. This member can be a bitwise OR of the following DirectDraw bit-depth constants: DDBD_8, DDBD_16, DDBD_24, or DDBD_32.</p>
</dd>

### -field <b>dwMaxBufferSize</b>

<dd>
<p>Must be set to zero.</p>
</dd>

### -field <b>dwMaxVertexCount</b>

<dd>
<dl>

### -field <b>DirectX 7 and later versions</b>


### -field Set this member to zero because it is no longer relevant.


### -field <b>DirectX 6</b>


### -field Specifies the maximum number of vertices that the device can handle in a single call to <a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>. The runtime cannot handle more than 0xFFFE vertices; therefore, never set this member to greater than 0xFFFE.

</dl>
</dd>
</dl>

## -remarks
<p>This structure has been replaced by D3DCAPS8 (see the DirectX 8.0 SDK documentation) for DirectX 8.0 and later runtimes, but is required for legacy runtime (DirectX 7.0 and earlier) compatibility. See <a href="https://msdn.microsoft.com/a03a7cbc-95be-4251-8e3a-bef4a093f03d">Reporting DirectX 8.0 Style Direct3D Capabilities</a> for details.</p>

<p>The driver's <a href="display.drvgetdirectdrawinfo">DrvGetDirectDrawInfo</a> function returns this information in the <a href="..\d3dhal\ns-d3dhal--d3dhal-globaldriverdata.md">D3DHAL_GLOBALDRIVERDATA</a> structure that the <b>lpD3DGlobalDriverData</b> member of the <a href="display.dd_halinfo">DD_HALINFO</a> structure points to.</p>

<p>The Direct3D runtime constructs the application-level D3DDEVICEDESC7 structure (documented in the Microsoft Windows SDK documentation) from the information returned in the D3DDEVICEDESC_V1 structure and the extended capabilities queried through the driver's <a href="display.ddgetdriverinfo">DdGetDriverInfo</a> function. While some of the <b>dwDevCaps</b> flags are obsolete at the driver level, the driver must set them appropriately in order for applications to work correctly.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dhal.h (include D3dhal.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dcaps\ns-d3dcaps--d3dlightingcaps.md">D3DLIGHTINGCAPS</a>
</dt>
<dt>
<a href="..\d3dcaps\ns-d3dcaps--d3dprimcaps.md">D3DPRIMCAPS</a>
</dt>
<dt>
<a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>
</dt>
<dt>
<a href="display.ddgetdriverinfo">DdGetDriverInfo</a>
</dt>
<dt>
<a href="..\d3dhal\ns-d3dhal--d3dhal-globaldriverdata.md">D3DHAL_GLOBALDRIVERDATA</a>
</dt>
<dt>
<a href="display.dd_halinfo">DD_HALINFO</a>
</dt>
<dt>
<a href="display.drvgetdirectdrawinfo">DrvGetDirectDrawInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDEVICEDESC_V1 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
