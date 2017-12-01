---
UID: NE.d3dumddi._D3DDDICAPS_TYPE
title: D3DDDICAPS_TYPE
author: windows-driver-content
description: The D3DDDICAPS_TYPE enumeration type contains values that identify the type of capability information that is received from a call to the driver's GetCaps function.
old-location: display\d3dddicaps_type.htm
old-project: display
ms.assetid: 52b37309-b320-4823-8b77-8eac4235b64e
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDICAPS_TYPE
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

# D3DDDICAPS_TYPE enumeration



## -description
<p>The <b>D3DDDICAPS_TYPE</b> enumeration type contains values that identify the type of capability information that is received from a call to the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a> function.</p>


## -syntax

````
typedef enum _D3DDDICAPS_TYPE { 
  D3DDDICAPS_DDRAW                                    = 1,
  D3DDDICAPS_DDRAW_MODE_SPECIFIC                      = 2,
  D3DDDICAPS_GETFORMATCOUNT                           = 3,
  D3DDDICAPS_GETFORMATDATA                            = 4,
  D3DDDICAPS_GETMULTISAMPLEQUALITYLEVELS              = 5,
  D3DDDICAPS_GETD3DQUERYCOUNT                         = 6,
  D3DDDICAPS_GETD3DQUERYDATA                          = 7,
  D3DDDICAPS_GETD3D3CAPS                              = 8,
  D3DDDICAPS_GETD3D5CAPS                              = 9,
  D3DDDICAPS_GETD3D6CAPS                              = 10,
  D3DDDICAPS_GETD3D7CAPS                              = 11,
  D3DDDICAPS_GETD3D8CAPS                              = 12,
  D3DDDICAPS_GETD3D9CAPS                              = 13,
  D3DDDICAPS_GETDECODEGUIDCOUNT                       = 14,
  D3DDDICAPS_GETDECODEGUIDS                           = 15,
  D3DDDICAPS_GETDECODERTFORMATCOUNT                   = 16,
  D3DDDICAPS_GETDECODERTFORMATS                       = 17,
  D3DDDICAPS_GETDECODECOMPRESSEDBUFFERINFOCOUNT       = 18,
  D3DDDICAPS_GETDECODECOMPRESSEDBUFFERINFO            = 19,
  D3DDDICAPS_GETDECODECONFIGURATIONCOUNT              = 20,
  D3DDDICAPS_GETDECODECONFIGURATIONS                  = 21,
  D3DDDICAPS_GETVIDEOPROCESSORDEVICEGUIDCOUNT         = 22,
  D3DDDICAPS_GETVIDEOPROCESSORDEVICEGUIDS             = 23,
  D3DDDICAPS_GETVIDEOPROCESSORRTFORMATCOUNT           = 24,
  D3DDDICAPS_GETVIDEOPROCESSORRTFORMATS               = 25,
  D3DDDICAPS_GETVIDEOPROCESSORRTSUBSTREAMFORMATCOUNT  = 26,
  D3DDDICAPS_GETVIDEOPROCESSORRTSUBSTREAMFORMATS      = 27,
  D3DDDICAPS_GETVIDEOPROCESSORCAPS                    = 28,
  D3DDDICAPS_GETPROCAMPRANGE                          = 29,
  D3DDDICAPS_FILTERPROPERTYRANGE                      = 30,
  D3DDDICAPS_GETEXTENSIONGUIDCOUNT                    = 31,
  D3DDDICAPS_GETEXTENSIONGUIDS                        = 32,
  D3DDDICAPS_GETEXTENSIONCAPS                         = 33,
  D3DDDICAPS_GETGAMMARAMPCAPS                         = 34,
  D3DDDICAPS_CHECKOVERLAYSUPPORT                      = 35,
  D3DDDICAPS_DXVAHD_GETVPDEVCAPS                      = 36,
  D3DDDICAPS_DXVAHD_GETVPOUTPUTFORMATS                = 37,
  D3DDDICAPS_DXVAHD_GETVPINPUTFORMATS                 = 38,
  D3DDDICAPS_DXVAHD_GETVPCAPS                         = 39,
  D3DDDICAPS_DXVAHD_GETVPCUSTOMRATES                  = 40,
  D3DDDICAPS_DXVAHD_GETVPFILTERRANGE                  = 41,
  D3DDDICAPS_GETCONTENTPROTECTIONCAPS                 = 42,
  D3DDDICAPS_GETCERTIFICATESIZE                       = 43,
  D3DDDICAPS_GETCERTIFICATE                           = 44,
#if (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WIN8)
  D3DDDICAPS_GET_ARCHITECTURE_INFO                    = 45,
  D3DDDICAPS_GET_SHADER_MIN_PRECISION_SUPPORT         = 46,
  D3DDDICAPS_GET_MULTIPLANE_OVERLAY_CAPS              = 47,
  D3DDDICAPS_GET_MULTIPLANE_OVERLAY_FILTER_RANGE      = 48,
#endif 
#if (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM1_3)
  D3DDDICAPS_GET_MULTIPLANE_OVERLAY_GROUP_CAPS        = 49,
  D3DDDICAPS_GET_SIMPLE_INSTANCING_SUPPORT            = 50,
  D3DDDICAPS_GET_MARKER_CAPS                          = 51

#endif } D3DDDICAPS_TYPE;
````


## -enum-fields
<dl>

### -field <a id="D3DDDICAPS_DDRAW"></a><a id="d3dddicaps_ddraw"></a><b>D3DDDICAPS_DDRAW</b>

<dd>
<p>The driver receives a pointer to a <a href="..\d3dumddi\ns-d3dumddi--ddraw-caps.md">DDRAW_CAPS</a> structure.</p>
</dd>

### -field <a id="D3DDDICAPS_DDRAW_MODE_SPECIFIC"></a><a id="d3dddicaps_ddraw_mode_specific"></a><b>D3DDDICAPS_DDRAW_MODE_SPECIFIC</b>

<dd>
<p>The driver receives a pointer to a <a href="..\d3dumddi\ns-d3dumddi--ddraw-mode-specific-caps.md">DDRAW_MODE_SPECIFIC_CAPS</a> structure.</p>
</dd>

### -field <a id="D3DDDICAPS_GETFORMATCOUNT"></a><a id="d3dddicaps_getformatcount"></a><b>D3DDDICAPS_GETFORMATCOUNT</b>

<dd>
<p>The driver receives a pointer to the number of surface formats from the <a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a> enumeration type that the device supports. See Remarks.</p>
</dd>

### -field <a id="D3DDDICAPS_GETFORMATDATA"></a><a id="d3dddicaps_getformatdata"></a><b>D3DDDICAPS_GETFORMATDATA</b>

<dd>
<p>The driver receives a pointer to an array of <a href="..\d3dumddi\ns-d3dumddi--formatop.md">FORMATOP</a> structures for the surface formats that the device supports.</p>
</dd>

### -field <a id="D3DDDICAPS_GETMULTISAMPLEQUALITYLEVELS"></a><a id="d3dddicaps_getmultisamplequalitylevels"></a><b>D3DDDICAPS_GETMULTISAMPLEQUALITYLEVELS</b>

<dd>
<p>The driver receives a pointer to a <a href="..\d3dumddi\ns-d3dumddi--ddimultisamplequalitylevelsdata.md">DDIMULTISAMPLEQUALITYLEVELSDATA</a> structure.</p>
</dd>

### -field <a id="D3DDDICAPS_GETD3DQUERYCOUNT"></a><a id="d3dddicaps_getd3dquerycount"></a><b>D3DDDICAPS_GETD3DQUERYCOUNT</b>

<dd>
<p>The driver receives a pointer to the number of query types that the driver supports.  See Remarks.</p>
</dd>

### -field <a id="D3DDDICAPS_GETD3DQUERYDATA"></a><a id="d3dddicaps_getd3dquerydata"></a><b>D3DDDICAPS_GETD3DQUERYDATA</b>

<dd>
<p>The driver receives a pointer to an array of structures or data types for different query types, which are represented by values of the D3DDDIQUERYTYPE enumeration type. For more information about D3DDDIQUERYTYPE, see the <b>QueryType</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-createquery.md">D3DDDIARG_CREATEQUERY</a> structure.</p>
</dd>

### -field <a id="D3DDDICAPS_GETD3D3CAPS"></a><a id="d3dddicaps_getd3d3caps"></a><b>D3DDDICAPS_GETD3D3CAPS</b>

<dd>
<p>The driver receives a pointer to a <a href="..\d3dhal\ns-d3dhal--d3dhal-globaldriverdata.md">D3DHAL_GLOBALDRIVERDATA</a> structure.</p>
</dd>

### -field <a id="D3DDDICAPS_GETD3D5CAPS"></a><a id="d3dddicaps_getd3d5caps"></a><b>D3DDDICAPS_GETD3D5CAPS</b>

<dd>
<p>This value is not used.</p>
</dd>

### -field <a id="D3DDDICAPS_GETD3D6CAPS"></a><a id="d3dddicaps_getd3d6caps"></a><b>D3DDDICAPS_GETD3D6CAPS</b>

<dd>
<p>This value is not used.</p>
</dd>

### -field <a id="D3DDDICAPS_GETD3D7CAPS"></a><a id="d3dddicaps_getd3d7caps"></a><b>D3DDDICAPS_GETD3D7CAPS</b>

<dd>
<p>The driver receives a pointer to a <a href="..\d3dhal\ns-d3dhal--d3dhal-d3dextendedcaps.md">D3DHAL_D3DEXTENDEDCAPS</a> structure.</p>
</dd>

### -field <a id="D3DDDICAPS_GETD3D8CAPS"></a><a id="d3dddicaps_getd3d8caps"></a><b>D3DDDICAPS_GETD3D8CAPS</b>

<dd>
<p>The driver receives a pointer to a D3DCAPS8 structure, which is described in the DirectX 8.0 SDK documentation.</p>
</dd>

### -field <a id="D3DDDICAPS_GETD3D9CAPS"></a><a id="d3dddicaps_getd3d9caps"></a><b>D3DDDICAPS_GETD3D9CAPS</b>

<dd>
<p>The driver receives a pointer to a D3DCAPS9 structure, which is described in the DirectX 9.0 SDK documentation.</p>
</dd>

### -field <a id="D3DDDICAPS_GETDECODEGUIDCOUNT"></a><a id="d3dddicaps_getdecodeguidcount"></a><b>D3DDDICAPS_GETDECODEGUIDCOUNT</b>

<dd>
<p>The driver receives a pointer to the number of DirectX Video Acceleration (DirectX VA) decode types (that is, decode GUIDs) that the driver supports.  See Remarks.</p>
</dd>

### -field <a id="D3DDDICAPS_GETDECODEGUIDS"></a><a id="d3dddicaps_getdecodeguids"></a><b>D3DDDICAPS_GETDECODEGUIDS</b>

<dd>
<p>The driver receives a pointer to an array of DirectX VA decode types (that is, decode GUIDs) that the driver supports.</p>
</dd>

### -field <a id="D3DDDICAPS_GETDECODERTFORMATCOUNT"></a><a id="d3dddicaps_getdecodertformatcount"></a><b>D3DDDICAPS_GETDECODERTFORMATCOUNT</b>

<dd>
<p>The driver receives a pointer to the number of render target formats for a particular DirectX VA decode type (which is specified by the <b>pInfo</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a> structure that the <i>pData</i> parameter of the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a> function points to). See Remarks.</p>
</dd>

### -field <a id="D3DDDICAPS_GETDECODERTFORMATS"></a><a id="d3dddicaps_getdecodertformats"></a><b>D3DDDICAPS_GETDECODERTFORMATS</b>

<dd>
<p>The driver receives a pointer to an array of <a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a> enumeration types that represent the render target formats for a particular DirectX VA decode type (which is specified in a <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-decodeinput.md">DXVADDI_DECODEINPUT</a> structure that is pointed to by <b>pInfo</b>).</p>
</dd>

### -field <a id="D3DDDICAPS_GETDECODECOMPRESSEDBUFFERINFOCOUNT"></a><a id="d3dddicaps_getdecodecompressedbufferinfocount"></a><b>D3DDDICAPS_GETDECODECOMPRESSEDBUFFERINFOCOUNT</b>

<dd>
<p>The driver receives a pointer to the number of types of compressed buffers that are required to accelerate a particular DirectX VA video decode type (which is specified in a <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-decodeinput.md">DXVADDI_DECODEINPUT</a> structure that is pointed to by <b>pInfo</b>).  See Remarks.</p>
</dd>

### -field <a id="D3DDDICAPS_GETDECODECOMPRESSEDBUFFERINFO"></a><a id="d3dddicaps_getdecodecompressedbufferinfo"></a><b>D3DDDICAPS_GETDECODECOMPRESSEDBUFFERINFO</b>

<dd>
<p>The driver receives an array of <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-decodebufferinfo.md">DXVADDI_DECODEBUFFERINFO</a> structures that contain information about the types of compressed buffers that are required to accelerate a particular DirectX VA video decode type (which is specified in a <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-decodeinput.md">DXVADDI_DECODEINPUT</a> structure that is pointed to by <b>pInfo</b>).</p>
</dd>

### -field <a id="D3DDDICAPS_GETDECODECONFIGURATIONCOUNT"></a><a id="d3dddicaps_getdecodeconfigurationcount"></a><b>D3DDDICAPS_GETDECODECONFIGURATIONCOUNT</b>

<dd>
<p>The driver receives a pointer to the number of configurations for a particular render target format of a DirectX VA decode type (which is specified in a <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-decodeinput.md">DXVADDI_DECODEINPUT</a> structure that is pointed to by <b>pInfo</b>). See Remarks.</p>
</dd>

### -field <a id="D3DDDICAPS_GETDECODECONFIGURATIONS"></a><a id="d3dddicaps_getdecodeconfigurations"></a><b>D3DDDICAPS_GETDECODECONFIGURATIONS</b>

<dd>
<p>The driver receives a pointer to an array of <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-configpicturedecode.md">DXVADDI_CONFIGPICTUREDECODE</a> structures for the configurations for a particular render target format of a DirectX VA decode type (which is specified in a <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-decodeinput.md">DXVADDI_DECODEINPUT</a> structure that is pointed to by <b>pInfo</b>).</p>
</dd>

### -field <a id="D3DDDICAPS_GETVIDEOPROCESSORDEVICEGUIDCOUNT"></a><a id="d3dddicaps_getvideoprocessordeviceguidcount"></a><b>D3DDDICAPS_GETVIDEOPROCESSORDEVICEGUIDCOUNT</b>

<dd>
<p>The driver receives a pointer to the number of video processor device types (GUIDs) that are used to process a particular video stream (which is specified in a <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-videodesc.md">DXVADDI_VIDEODESC</a> structure that is pointed to by <b>pInfo</b>). See Remarks.</p>
</dd>

### -field <a id="D3DDDICAPS_GETVIDEOPROCESSORDEVICEGUIDS"></a><a id="d3dddicaps_getvideoprocessordeviceguids"></a><b>D3DDDICAPS_GETVIDEOPROCESSORDEVICEGUIDS</b>

<dd>
<p>The driver receives a pointer to an array of video processor device types (GUIDs) that are used to process a particular video stream (which is specified in a <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-videodesc.md">DXVADDI_VIDEODESC</a> structure that is pointed to by <b>pInfo</b>).</p>
</dd>

### -field <a id="D3DDDICAPS_GETVIDEOPROCESSORRTFORMATCOUNT"></a><a id="d3dddicaps_getvideoprocessorrtformatcount"></a><b>D3DDDICAPS_GETVIDEOPROCESSORRTFORMATCOUNT</b>

<dd>
<p>The driver receives a pointer to the number of render target formats for a particular DirectX VA video processor device type (which is pointed to by the <b>pVideoProcGuid</b> member of a <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-videoprocessorinput.md">DXVADDI_VIDEOPROCESSORINPUT</a> structure that is pointed to by <b>pInfo</b>). See Remarks.</p>
</dd>

### -field <a id="D3DDDICAPS_GETVIDEOPROCESSORRTFORMATS"></a><a id="d3dddicaps_getvideoprocessorrtformats"></a><b>D3DDDICAPS_GETVIDEOPROCESSORRTFORMATS</b>

<dd>
<p>The driver receives a pointer to an array of <a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a> enumeration types that represent the render target formats for a particular DirectX VA video processor device type (which is pointed to by the <b>pVideoProcGuid</b> member of a <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-videoprocessorinput.md">DXVADDI_VIDEOPROCESSORINPUT</a> structure that is pointed to by <b>pInfo</b>).</p>
</dd>

### -field <a id="D3DDDICAPS_GETVIDEOPROCESSORRTSUBSTREAMFORMATCOUNT"></a><a id="d3dddicaps_getvideoprocessorrtsubstreamformatcount"></a><b>D3DDDICAPS_GETVIDEOPROCESSORRTSUBSTREAMFORMATCOUNT</b>

<dd>
<p>The driver receives a pointer to the number of render target formats for a particular DirectX VA video processor substream (which is pointed to by the <b>pVideoProcGuid</b> member of a <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-videoprocessorinput.md">DXVADDI_VIDEOPROCESSORINPUT</a> structure that is pointed to by <b>pInfo</b>). See Remarks.</p>
</dd>

### -field <a id="D3DDDICAPS_GETVIDEOPROCESSORRTSUBSTREAMFORMATS"></a><a id="d3dddicaps_getvideoprocessorrtsubstreamformats"></a><b>D3DDDICAPS_GETVIDEOPROCESSORRTSUBSTREAMFORMATS</b>

<dd>
<p>The driver receives a pointer to an array of <a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a> enumeration types that represent the render target formats for a particular DirectX VA video processor substream (which is pointed to by the <b>pVideoProcGuid</b> member of a <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-videoprocessorinput.md">DXVADDI_VIDEOPROCESSORINPUT</a> structure that is pointed to by <b>pInfo</b>).</p>
</dd>

### -field <a id="D3DDDICAPS_GETVIDEOPROCESSORCAPS"></a><a id="d3dddicaps_getvideoprocessorcaps"></a><b>D3DDDICAPS_GETVIDEOPROCESSORCAPS</b>

<dd>
<p>The driver receives a pointer to a <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-videoprocessorcaps.md">DXVADDI_VIDEOPROCESSORCAPS</a> structure that contains information about the video processing capabilities on a particular video stream (which is specified in a <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-videoprocessorinput.md">DXVADDI_VIDEOPROCESSORINPUT</a> structure that is pointed to by <b>pInfo</b>).</p>
</dd>

### -field <a id="D3DDDICAPS_GETPROCAMPRANGE"></a><a id="d3dddicaps_getprocamprange"></a><b>D3DDDICAPS_GETPROCAMPRANGE</b>

<dd>
<p>The driver receives a pointer to a <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-valuerange.md">DXVADDI_VALUERANGE</a> structure that contains the range of allowed values for a particular ProcAmp control property on a particular video stream (which is specified in a <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-queryprocampinput.md">DXVADDI_QUERYPROCAMPINPUT</a> structure that is pointed to by <b>pInfo</b>).</p>
</dd>

### -field <a id="D3DDDICAPS_FILTERPROPERTYRANGE"></a><a id="d3dddicaps_filterpropertyrange"></a><b>D3DDDICAPS_FILTERPROPERTYRANGE</b>

<dd>
<p>The driver receives a pointer to a <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-valuerange.md">DXVADDI_VALUERANGE</a> structure that contains the range of allowed values for a particular filter setting on a particular video stream (which is specified in a <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-queryfilterpropertyrangeinput.md">DXVADDI_QUERYFILTERPROPERTYRANGEINPUT</a> structure that is pointed to by <b>pInfo</b>).</p>
</dd>

### -field <a id="D3DDDICAPS_GETEXTENSIONGUIDCOUNT"></a><a id="d3dddicaps_getextensionguidcount"></a><b>D3DDDICAPS_GETEXTENSIONGUIDCOUNT</b>

<dd>
<p>The driver receives a pointer to the number of extension GUIDs that are supported.  See Remarks.</p>
</dd>

### -field <a id="D3DDDICAPS_GETEXTENSIONGUIDS"></a><a id="d3dddicaps_getextensionguids"></a><b>D3DDDICAPS_GETEXTENSIONGUIDS</b>

<dd>
<p>The driver receives a pointer to an array of extension GUIDs that are supported.</p>
</dd>

### -field <a id="D3DDDICAPS_GETEXTENSIONCAPS"></a><a id="d3dddicaps_getextensioncaps"></a><b>D3DDDICAPS_GETEXTENSIONCAPS</b>

<dd>
<p>The driver receives a pointer to a private structure that contains information about a capability of an extension GUID (which is specified in a <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-queryextensioncapsinput.md">DXVADDI_QUERYEXTENSIONCAPSINPUT</a> structure that is pointed to by <b>pInfo</b>).</p>
</dd>

### -field <a id="D3DDDICAPS_GETGAMMARAMPCAPS"></a><a id="d3dddicaps_getgammarampcaps"></a><b>D3DDDICAPS_GETGAMMARAMPCAPS</b>

<dd>
<p>The driver receives a pointer to a <a href="..\d3dumddi\ns-d3dumddi--ddigammacaps.md">DDIGAMMACAPS</a> structure for the gamma-ramp capabilities that the device supports. </p>
</dd>

### -field <a id="D3DDDICAPS_CHECKOVERLAYSUPPORT"></a><a id="d3dddicaps_checkoverlaysupport"></a><b>D3DDDICAPS_CHECKOVERLAYSUPPORT</b>

<dd>
<p>The driver receives a pointer to a D3DOVERLAYCAPS structure that contains information about the capabilities of a particular overlay. The attributes of the overlay and the display mode in which the calling application wants to use the overlay are specified in a <a href="..\d3dumddi\ns-d3dumddi--ddicheckoverlaysupportinput.md">DDICHECKOVERLAYSUPPORTINPUT</a> structure that is pointed to by <b>pInfo</b>. If the driver supports the overlay, the driver sets the members of the D3DOVERLAYCAPS; otherwise, the driver fails the call to its <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a> function with either D3DDDIERR_UNSUPPORTEDOVERLAYFORMAT or D3DDDIERR_UNSUPPORTEDOVERLAY depending on whether the lack of support was based on the overlay format. D3DOVERLAYCAPS is described in the DirectXSDK documentation.</p>
<p>For more information, see <a href="https://msdn.microsoft.com/c8f1cdd6-1beb-43bd-b96c-2eea3a51321e">Overlay DDI</a>.</p>
<p> Supported starting with Windows 7.</p>
</dd>

### -field <a id="D3DDDICAPS_DXVAHD_GETVPDEVCAPS"></a><a id="d3dddicaps_dxvahd_getvpdevcaps"></a><b>D3DDDICAPS_DXVAHD_GETVPDEVCAPS</b>

<dd>
<p>The driver receives a pointer to a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-vpdevcaps.md">DXVAHDDDI_VPDEVCAPS</a> structure for the video processor capabilities that the decode device (which is specified in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-device-desc.md">DXVAHDDDI_DEVICE_DESC</a> structure that is pointed to by <b>pInfo</b>) supports.</p>
<p> Supported starting with Windows 7.</p>
</dd>

### -field <a id="D3DDDICAPS_DXVAHD_GETVPOUTPUTFORMATS"></a><a id="d3dddicaps_dxvahd_getvpoutputformats"></a><b>D3DDDICAPS_DXVAHD_GETVPOUTPUTFORMATS</b>

<dd>
<p>The driver receives an array of <a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a> enumeration types that represent the output formats for the decode device (which is specified in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-device-desc.md">DXVAHDDDI_DEVICE_DESC</a> structure that is pointed to by <b>pInfo</b>).</p>
<p> Supported starting with Windows 7.</p>
</dd>

### -field <a id="D3DDDICAPS_DXVAHD_GETVPINPUTFORMATS"></a><a id="d3dddicaps_dxvahd_getvpinputformats"></a><b>D3DDDICAPS_DXVAHD_GETVPINPUTFORMATS</b>

<dd>
<p>The driver receives an array of <a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a> enumeration types that represent the input formats for the decode device (which is specified in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-device-desc.md">DXVAHDDDI_DEVICE_DESC</a> structure that is pointed to by <b>pInfo</b>).</p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <a id="D3DDDICAPS_DXVAHD_GETVPCAPS"></a><a id="d3dddicaps_dxvahd_getvpcaps"></a><b>D3DDDICAPS_DXVAHD_GETVPCAPS</b>

<dd>
<p>The driver receives an array of <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-vpcaps.md">DXVAHDDDI_VPCAPS</a> structures for the capabilities for each video processor that the decode device (which is specified in a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-device-desc.md">DXVAHDDDI_DEVICE_DESC</a> structure that is pointed to by <b>pInfo</b>) supports.</p>
<p> Supported starting with Windows 7.</p>
</dd>

### -field <a id="D3DDDICAPS_DXVAHD_GETVPCUSTOMRATES"></a><a id="d3dddicaps_dxvahd_getvpcustomrates"></a><b>D3DDDICAPS_DXVAHD_GETVPCUSTOMRATES</b>

<dd>
<p>The driver receives an array of <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-custom-rate-data.md">DXVAHDDDI_CUSTOM_RATE_DATA</a> structures for the custom frame rates that a video processor (which is specified by a CONST_GUID that is pointed to by <b>pInfo</b>) supports.</p>
<p> Supported starting with Windows 7.</p>
</dd>

### -field <a id="D3DDDICAPS_DXVAHD_GETVPFILTERRANGE"></a><a id="d3dddicaps_dxvahd_getvpfilterrange"></a><b>D3DDDICAPS_DXVAHD_GETVPFILTERRANGE</b>

<dd>
<p>The driver receives a pointer to a <a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-filter-range-data.md">DXVAHDDDI_FILTER_RANGE_DATA</a> structure for the range that the filter (which is specified by a <a href="..\d3dumddi\ne-d3dumddi--dxvahdddi-filter.md">DXVAHDDDI_FILTER</a> enumeration value that is pointed to by <b>pInfo</b>) supports.</p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <a id="D3DDDICAPS_GETCONTENTPROTECTIONCAPS"></a><a id="d3dddicaps_getcontentprotectioncaps"></a><b>D3DDDICAPS_GETCONTENTPROTECTIONCAPS</b>

<dd>
<p>The driver receives a pointer to a D3DCONTENTPROTECTIONCAPS structure for the specific encryption and decode combination (which is specified in a <a href="..\d3dumddi\ns-d3dumddi--ddicontentprotectioncaps.md">DDICONTENTPROTECTIONCAPS</a> structure that is pointed to by <b>pInfo</b>) that the driver should use. D3DCONTENTPROTECTIONCAPS is described in the DirectXSDK documentation.</p>
<p>For more information, see <a href="https://msdn.microsoft.com/770e0fce-d3b5-4599-8165-eadf3f23f9dc">Content Protection DDI</a>.</p>
<p> Supported starting with Windows 7.</p>
</dd>

### -field <a id="D3DDDICAPS_GETCERTIFICATESIZE"></a><a id="d3dddicaps_getcertificatesize"></a><b>D3DDDICAPS_GETCERTIFICATESIZE</b>

<dd>
<p>The driver receives a pointer to a number that specifies the size, in bytes, of the driver's certificate that is used for a channel type. The runtime uses this size to allocate a buffer to hold the certificate. The runtime passes this buffer in the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a> call with D3DDDICAPS_GETCERTIFICATE set.</p>
<p> Supported starting with Windows 7.  See Remarks.</p>
</dd>

### -field <a id="D3DDDICAPS_GETCERTIFICATE"></a><a id="d3dddicaps_getcertificate"></a><b>D3DDDICAPS_GETCERTIFICATE</b>

<dd>
<p>The driver receives a pointer to the driver's certificate (which is described in a <a href="..\d3dumddi\ns-d3dumddi--ddicertificateinfo.md">DDICERTIFICATEINFO</a> structure that is pointed to by <b>pInfo</b>). The runtime passes a buffer in the <b>pData</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a> structure that the driver can fill with the certificate.</p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <a id="D3DDDICAPS_GET_ARCHITECTURE_INFO"></a><a id="d3dddicaps_get_architecture_info"></a><b>D3DDDICAPS_GET_ARCHITECTURE_INFO</b>

<dd>
<p>The driver receives a pointer to a <a href="..\d3dumddi\ns-d3dumddi-d3dddicaps-architecture-info.md">D3DDDICAPS_ARCHITECTURE_INFO</a> structure that contains information about the DirectX 11.1 adapter architecture that the device supports.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="D3DDDICAPS_GET_SHADER_MIN_PRECISION_SUPPORT"></a><a id="d3dddicaps_get_shader_min_precision_support"></a><b>D3DDDICAPS_GET_SHADER_MIN_PRECISION_SUPPORT</b>

<dd>
<p>The driver receives a pointer to a <a href="..\d3d10umddi\ns-d3d10umddi-d3d11-ddi-shader-min-precision-support-data.md">D3D11_DDI_SHADER_MIN_PRECISION_SUPPORT_DATA</a>   structure that specifies the minimum precision levels that the driver supports in shaders.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="D3DDDICAPS_GET_MULTIPLANE_OVERLAY_CAPS"></a><a id="d3dddicaps_get_multiplane_overlay_caps"></a><b>D3DDDICAPS_GET_MULTIPLANE_OVERLAY_CAPS</b>

<dd>
<p>The driver receives a pointer to a <a href="..\d3dumddi\ns-d3dumddi-d3dddi-multiplane-overlay-caps.md">D3DDDI_MULTIPLANE_OVERLAY_CAPS</a> structure that specifies basic multiplane overlay capabilities. In this case, the members of the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a> structure indicate the following:</p>
<ul>
<li>
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a>.<b>Type</b> has a value of <b>D3DDDICAPS_GET_MULTIPLANE_OVERLAY_CAPS</b>.<p>If the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a> function is called with this value for <b>Type</b> and the driver does not support multiplane overlays, the driver should return an error code.</p>
</li>
<li>
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a>.<b>pInfo</b> is a pointer of type <b>D3DDDI_VIDEO_PRESENT_SOURCE_ID</b> to the zero-based identification number of the video present source,  <b>VidPnSourceId</b>.</li>
<li>
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a>.<b>pData</b> is a pointer of type <a href="..\d3dumddi\ns-d3dumddi-d3dddi-multiplane-overlay-caps.md">D3DDDI_MULTIPLANE_OVERLAY_CAPS</a> to the capabilities structure that the driver fills out.</li>
<li>
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a>.<b>DataSize</b> is the value of <code>sizeof(D3DDDI_MULTIPLANE_OVERLAY_CAPS)</code>.</li>
</ul>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <a id="D3DDDICAPS_GET_MULTIPLANE_OVERLAY_FILTER_RANGE"></a><a id="d3dddicaps_get_multiplane_overlay_filter_range"></a><b>D3DDDICAPS_GET_MULTIPLANE_OVERLAY_FILTER_RANGE</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="D3DDDICAPS_GET_MULTIPLANE_OVERLAY_GROUP_CAPS"></a><a id="d3dddicaps_get_multiplane_overlay_group_caps"></a><b>D3DDDICAPS_GET_MULTIPLANE_OVERLAY_GROUP_CAPS</b>

<dd>
<p>The driver receives a pointer to a <a href="..\d3dumddi\ns-d3dumddi-d3dddi-multiplane-overlay-group-caps.md">D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS</a> structure  that specifies a group of overlay plane capabilities. In this case, the members of the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a> structure indicate the following:</p>
<ul>
<li>
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a>.<b>Type</b> has a value of <b>D3DDDICAPS_GET_MULTIPLANE_OVERLAY_GROUP_CAPS</b>.<p>If the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a> function is called with this value for <b>Type</b> and the driver does not support multiplane overlays, the driver should return an error code.</p>
</li>
<li>
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a>.<b>pInfo</b> is a pointer of type <a href="..\d3dumddi\ns-d3dumddi-d3dddi-multiplane-overlay-group-caps-input.md">D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS_INPUT</a> to the zero-based identification number of the video present source,  <b>VidPnSourceId</b>, and to the capability group index, <b>GroupIndex</b>.</li>
<li>
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a>.<b>pData</b> is a pointer of type <a href="..\d3dumddi\ns-d3dumddi-d3dddi-multiplane-overlay-group-caps.md">D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS</a> to the capabilities structure that the driver fills out.</li>
<li>
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a>.<b>DataSize</b> is the value of <code>sizeof(D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS)</code>.</li>
</ul>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <a id="D3DDDICAPS_GET_SIMPLE_INSTANCING_SUPPORT"></a><a id="d3dddicaps_get_simple_instancing_support"></a><b>D3DDDICAPS_GET_SIMPLE_INSTANCING_SUPPORT</b>

<dd>
<p>The driver receives a pointer to a <a href="..\d3dumddi\ns-d3dumddi-d3dddicaps-simple-instancing-support.md">D3DDDICAPS_SIMPLE_INSTANCING_SUPPORT</a> structure  that specifies simple instancing capabilities.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <a id="D3DDDICAPS_GET_MARKER_CAPS"></a><a id="d3dddicaps_get_marker_caps"></a><b>D3DDDICAPS_GET_MARKER_CAPS</b>

<dd>
<p>Supported starting with Windows 8.1.</p>
</dd>
</dl>

## -remarks
<p>For information on how to specify <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a> member values along with <b>D3DDDICAPS_TYPE</b> constant values, see Remarks of <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with  Windows Vista.</p>
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
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-ddi-shader-min-precision-support-data.md">D3D11_DDI_SHADER_MIN_PRECISION_SUPPORT_DATA</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi-d3dddi-multiplane-overlay-caps.md">D3DDDI_MULTIPLANE_OVERLAY_CAPS</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi-d3dddi-multiplane-overlay-group-caps.md">D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi-d3dddi-multiplane-overlay-group-caps-input.md">D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS_INPUT</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi-d3dddicaps-architecture-info.md">D3DDDICAPS_ARCHITECTURE_INFO</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi-d3dddicaps-simple-instancing-support.md">D3DDDICAPS_SIMPLE_INSTANCING_SUPPORT</a>
</dt>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--ddicertificateinfo.md">DDICERTIFICATEINFO</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--ddicheckoverlaysupportinput.md">DDICHECKOVERLAYSUPPORTINPUT</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--ddicontentprotectioncaps.md">DDICONTENTPROTECTIONCAPS</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--ddraw-caps.md">DDRAW_CAPS</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--ddraw-mode-specific-caps.md">DDRAW_MODE_SPECIFIC_CAPS</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-custom-rate-data.md">DXVAHDDDI_CUSTOM_RATE_DATA</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-device-desc.md">DXVAHDDDI_DEVICE_DESC</a>
</dt>
<dt>
<a href="..\d3dumddi\ne-d3dumddi--dxvahdddi-filter.md">DXVAHDDDI_FILTER</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-filter-range-data.md">DXVAHDDDI_FILTER_RANGE_DATA</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-vpcaps.md">DXVAHDDDI_VPCAPS</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvahdddi-vpdevcaps.md">DXVAHDDDI_VPDEVCAPS</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--formatop.md">FORMATOP</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICAPS_TYPE enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
